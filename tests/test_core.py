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

def test_countries_geoms_mostly_valid(countries_result):
    """99%+ geometrias válidas aceitável para Natural Earth."""
    valid_ratio = countries_result["n_valid_geoms"] / countries_result["n_features"]
    assert valid_ratio > 0.99
    assert countries_result["n_null_geoms"] == 0

def test_lakes_crs(lakes_result):
    assert lakes_result["crs"] == "EPSG:4326"

def test_lakes_n_features(lakes_result):
    assert lakes_result["n_features"] >= 280  # Esperado ~286

def test_lakes_geoms_mostly_valid(lakes_result):
    """99%+ geometrias válidas aceitável para Natural Earth."""
    valid_ratio = lakes_result["n_valid_geoms"] / lakes_result["n_features"]
    assert valid_ratio > 0.99
    assert lakes_result["n_null_geoms"] == 0

