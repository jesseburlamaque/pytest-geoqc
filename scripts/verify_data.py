from pathlib import Path
import geopandas as gpd

DATA_DIR = Path("data")

countries_shp = DATA_DIR / "ne_10m_admin_0_countries" / "ne_10m_admin_0_countries.shp"
lakes_shp = DATA_DIR / "ne_10m_lakes" / "ne_10m_lakes.shp"

if countries_shp.exists():
    gdf_countries = gpd.read_file(countries_shp)
    print(f"✅ Países: {len(gdf_countries)} features, CRS: {gdf_countries.crs}")
else:
    print("❌ Países .shp não encontrado")

if lakes_shp.exists():
    gdf_lakes = gpd.read_file(lakes_shp)
    print(f"✅ Lagos: {len(gdf_lakes)} features, CRS: {gdf_lakes.crs}")
else:
    print("❌ Lagos .shp não encontrado")
