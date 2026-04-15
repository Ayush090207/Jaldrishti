"""
Jal Drishti - Configuration Module
====================================
Central configuration for all backend services, paths, and constants.
"""

import os
from pathlib import Path

# =============================================
# Path Configuration
# =============================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "dashboard" / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DIR = BASE_DIR / "output"

# =============================================
# Village Configuration
# =============================================

VILLAGES = {
    "wayanad_meppadi": {
        "name": "Meppadi",
        "state": "Kerala",
        "district": "Wayanad",
        "terrain_type": "hilly_ghats",
        "coordinates": {"lat": 11.555, "lon": 76.135},
        "bbox": [76.10, 11.52, 76.17, 11.59],
        "population": 50000,
        "dem_source": "SRTM_30m",
        "boundary_file": "wayanad_meppadi_boundary.geojson",
        "buildings_file": "wayanad_meppadi_buildings.geojson",
    },
    "darbhanga": {
        "name": "Darbhanga",
        "state": "Bihar",
        "district": "Darbhanga",
        "terrain_type": "riverine_plain",
        "coordinates": {"lat": 26.120, "lon": 85.900},
        "bbox": [85.85, 26.12, 85.93, 26.19],
        "population": 100000,
        "dem_source": "SRTM_30m",
        "boundary_file": "darbhanga_boundary.geojson",
        "buildings_file": "darbhanga_buildings.geojson",
    },
    "dhemaji": {
        "name": "Dhemaji",
        "state": "Assam",
        "district": "Dhemaji",
        "terrain_type": "brahmaputra_floodplain",
        "coordinates": {"lat": 27.480, "lon": 94.560},
        "bbox": [94.53, 27.45, 94.60, 27.51],
        "population": 75000,
        "dem_source": "SRTM_30m",
        "boundary_file": "dhemaji_boundary.geojson",
        "buildings_file": "dhemaji_buildings.geojson",
    },
}

# =============================================
# Simulation Parameters
# =============================================

SIMULATION = {
    "grid_resolution_m": 40,
    "time_steps_hours": [0, 4, 8, 12, 16, 20, 24],
    "default_rainfall_mm": 50,
    "max_rainfall_mm": 500,
    "risk_thresholds": {
        "low": 0.0,
        "medium": 0.30,
        "high": 0.50,
        "extreme": 0.70,
    },
    "pathfinding": {
        "danger_threshold": 0.70,
        "risk_weight_multiplier": 25,
        "max_safe_havens": 5,
    },
}

# =============================================
# API Configuration
# =============================================

API_CONFIG = {
    "host": os.getenv("API_HOST", "0.0.0.0"),
    "port": int(os.getenv("API_PORT", "8000")),
    "cors_origins": [
        "http://localhost:8000",
        "http://localhost:8001",
        "https://jaldhristhi-mission-control.vercel.app",
        "*",  # Allow all origins in production (served from same domain)
    ],
    "rate_limit": 100,  # requests per minute
}

# =============================================
# Weather API
# =============================================

WEATHER_API = {
    "provider": "open-meteo",
    "base_url": "https://api.open-meteo.com/v1/forecast",
    "forecast_days": 7,
    "cache_ttl_seconds": 600,
}

# =============================================
# Model Configuration
# =============================================

MODEL_CONFIG = {
    "risk_scorer": {
        "version": "v2.1",
        "weights": {
            "water_depth": 0.40,
            "slope": 0.25,
            "flow_accumulation": 0.25,
            "proximity": 0.10,
        },
        "accuracy": 0.92,
    },
    "population_clustering": {
        "method": "DBSCAN",
        "eps_km": 0.5,
        "min_samples": 10,
    },
}

# =============================================
# Logging
# =============================================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
