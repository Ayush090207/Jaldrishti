"""
Pytest Fixtures for Jal Drishti Test Suite
"""

import pytest
import numpy as np
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@pytest.fixture
def sample_villages():
    """Sample village configuration data."""
    return {
        "wayanad_meppadi": {
            "terrain_type": "hilly_ghats",
            "bbox": (76.10, 11.52, 76.17, 11.59),
            "population": 50000,
            "coordinates": {"lat": 11.555, "lon": 76.135},
        },
        "darbhanga": {
            "terrain_type": "riverine_plain",
            "bbox": (85.85, 26.12, 85.93, 26.19),
            "population": 100000,
            "coordinates": {"lat": 26.120, "lon": 85.900},
        },
        "dhemaji": {
            "terrain_type": "brahmaputra_floodplain",
            "bbox": (94.53, 27.45, 94.60, 27.51),
            "population": 75000,
            "coordinates": {"lat": 27.480, "lon": 94.560},
        },
    }


@pytest.fixture
def sample_dem():
    """Generate a 20x20 synthetic DEM for testing."""
    dem = np.zeros((20, 20))
    for i in range(20):
        for j in range(20):
            dem[i, j] = 100 + np.sin(i * 0.3) * 20 + np.cos(j * 0.4) * 15
    return dem


@pytest.fixture
def sample_clusters():
    """Sample population cluster data."""
    return [
        {"cluster_id": "C01", "lat": 11.553, "lng": 76.132, "population": 4200},
        {"cluster_id": "C02", "lat": 11.560, "lng": 76.140, "population": 3800},
        {"cluster_id": "C03", "lat": 11.545, "lng": 76.125, "population": 1800},
    ]


@pytest.fixture
def sample_rescue_centers():
    """Sample rescue center coordinate tuples."""
    return [
        (11.565, 76.145),
        (11.550, 76.130),
    ]


@pytest.fixture
def data_dir():
    """Path to the test data directory."""
    return Path(__file__).resolve().parent.parent / "dashboard" / "data"
