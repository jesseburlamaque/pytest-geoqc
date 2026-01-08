from pathlib import Path
import geopandas as gpd
from typing import Dict, Any

DATA_DIR = Path("data")

def validate_shapefile(shp_path: Path) -> Dict[str, Any]:
    """Valida shapefile: CRS, features, geometrias válidas."""
    if not shp_path.exists():
        raise FileNotFoundError(f"Shapefile não encontrado: {shp_path}")
    
    gdf = gpd.read_file(shp_path)
    
    result = {
        "crs": str(gdf.crs) if gdf.crs else None,
        "n_features": len(gdf),
        "n_valid_geoms": len(gdf[gdf.geometry.is_valid]),
        "n_null_geoms": gdf.geometry.isna().sum(),
        "expected_crs": "EPSG:4326"
    }
    
    return result

def get_countries_validation() -> Dict[str, Any]:
    """Validação específica para países Natural Earth."""
    shp = DATA_DIR / "ne_10m_admin_0_countries" / "ne_10m_admin_0_countries.shp"
    return validate_shapefile(shp)

def get_lakes_validation() -> Dict[str, Any]:
    """Validação específica para lagos Natural Earth."""
    shp = DATA_DIR / "ne_10m_lakes" / "ne_10m_lakes.shp"
    return validate_shapefile(shp)
