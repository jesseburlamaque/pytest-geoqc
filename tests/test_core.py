import pytest
from pytest_geoqc.core import get_countries_validation, get_lakes_validation

@pytest.fixture
def countries_result():
    return get_countries_validation()

@pytest.fixture
def lakes_result():
    return get_lakes_validation()

def test_countries_crs(countries_result):
    assert countries_result["crs"] == "EPSG:4326"

def test_countries_n_features(countries_result):
    assert countries_result["n_features"] >= 250  # Esperado ~258

def test_countries_geoms_valid(countries_result):
    assert countries_result["n_valid_geoms"] == countries_result["n_features"]
    assert countries_result["n_null_geoms"] == 0

def test_lakes_crs(lakes_result):
    assert lakes_result["crs"] == "EPSG:4326"

def test_lakes_n_features(lakes_result):
    assert lakes_result["n_features"] >= 280  # Esperado ~286

def test_lakes_geoms_valid(lakes_result):
    assert lakes_result["n_valid_geoms"] == lakes_result["n_features"]
    assert lakes_result["n_null_geoms"] == 0
