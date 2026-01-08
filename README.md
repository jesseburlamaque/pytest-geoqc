# pytest-geoqc

[![pytest](https://img.shields.io/badge/pytest-passing-brightgreen?logo=pytest&logoColor=white)]
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Geospatial data quality validation (GeoQC) with pytest + Natural Earth dataset.

## Project Structure

pytest-geoqc/
├── src/pytest_geoqc/core.py     # QC logic
├── tests/test_core.py           # pytest tests
├── data/                        # Natural Earth shapefiles
├── scripts/                     # verify_data.py
├── pyproject.toml               # pytest config
└── requirements.txt

## Features

- ✅ CRS EPSG:4326 validated
- ✅ Real feature count (250+ countries, 280+ lakes)
- ✅ 99%+ valid geometries
- ✅ Real Natural Earth 10m data





