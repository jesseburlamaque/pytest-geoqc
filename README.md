# pytest-geoqc

[![pytest](https://img.shields.io/badge/pytest-passing-brightgreen?logo=pytest&logoColor=white)] 
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Geospatial data quality validation (GeoQC) with pytest + Natural Earth dataset.

This repository demonstrates Test-Driven Development (TDD) applied to geospatial data quality validation (GeoQC), using pytest as the primary framework.

```text
1. Expectations -> 2. Write test -> 3. Code passes -> 4. Refactor -> 5. Commit
    ↓                       ↓                    ↓                ↓              ↓
"CRS=EPSG:4326"         -> test_crs()        validate_shapefile()  pytest -v      git commit
"250+ features"         -> test_features()   get_countries()       6/6 pass       GitHub 
"99% geom OK"           -> test_geoms()      is_valid_geometry     Coverage 100%
```

## Validações

```python
# 1. Correct CRS (WGS84 standard)
assert result["crs"] == "EPSG:4326"  # Base for global analyses

# 2. Complete global coverage
assert result["n_features"] >= 250   # 193 UN + 65 territories = 258

# 3. Geometric quality (Shapely)
assert (valid_geoms / total) > 0.99  # Realistic tolerance for Natural Earth
assert null_geoms == 0               # No empty geometries
```

## Project Structure


```text
pytest-geoqc/
src/pytest_geoqc/core.py     # QC logic
├── tests/test_core.py           # pytest tests
├── data/                        # Natural Earth shapefiles
├── scripts/                     # verify_data.py
├── pyproject.toml               # pytest config
└── requirements.txt
```

## Features

- ✅ CRS EPSG:4326 validated
- ✅ Real feature count (250+ countries, 280+ lakes)
- ✅ 99%+ valid geometries
- ✅ Real Natural Earth 10m data





