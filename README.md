# 🌊 Jal Drishti: AI-Driven Flood Intelligence & Mission Control

[![Vercel Deployment](https://img.shields.io/badge/Vercel-Deployed-black?logo=vercel)](https://jaldhristhi-mission-control-nhiqggvew.vercel.app)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/ItzHimanshu007/JALDHRISHTI_V.2.git)

**Jal Drishti** (Water Vision) is a state-of-the-art Mission Control Dashboard engineered for high-fidelity flood simulation, real-time risk assessment, and tactical resource deployment. Designed for disaster management professionals, it translates complex hydrological data into actionable field intelligence.

---

## 🚀 Advanced Intelligence Features

### 1. 🧠 Flood Risk Intelligence (AI Analysis)
Move beyond simple monitoring. Our AI engine performs real-time terrain analysis to predict flood impact zones based on multi-criteria modeling:
- **Terrain Stability Analysis**: Real-time evaluation of elevation, slope, and land-use saturation.
- **Dynamic Risk Gridding**: Visualizes danger zones from 'Low' to 'Extreme' based on rainfall intensity.
- **Automated Reporting**: Generates deep-scan tactical summaries with a single click.

### 2. 🗺️ Intelligent Population Heatmap
Our predictive population modeling isn't just a random cluster. It uses **Geographic Building Analysis** to:
- Focus density on **actual building centers** and residential hubs.
- Automatically **avoid riverbeds, floodplains, and unpopulated plains**.
- Link population vulnerability directly to current simulation risk levels.

### 3. 🛡️ Risk-Aware Tactical Rescue Routing
The dashboard features a professional A* pathfinding system designed for emergency extraction:
- **Danger Avoidance**: Routes are strictly prohibited from crossing 'Extreme' risk zones (>70% flood risk).
- **Multi-Destination Ranking**: Simultaneously calculates paths to 5 safe havens per village (Hospitals, Shelters, High Ground) and ranks them by safety and distance.
- **Smoothed Pathing**: Uses Catmull-Rom splines for realistic vehicle/personnel transit visualization.

### 4. 🎯 Linked Resource Optimization
A MISSION-LINKED heuristic engine for resource distribution:
- **Prioritized Allocation**: Distributes limited resources (Boats, Ambulances, Personnel) with 80% bias towards 'Extreme' danger zones.
- **Simulation Interlock**: Optimization only runs when active risk is detected (Rainfall > 0mm).
- **Control & Abort**: Real-time management with a dedicated "Stop Optimization" interrupt.

---

## 🛠️ Technology Ecosystem

- **Engine**: vanilla JavaScript (ES6+) with optimized A* pathfinding and Catmull-Rom spline logic.
- **Mapping**: **MapLibre GL JS** with AWS Terrarium 3D terrain rendering.
- **Visuals**: **Chart.js** for precinct forecasting; CSS3 Glassmorphism for a premium HUD feel.
- **Deployment**: Dual-stack deployment on **GitHub** (Source) and **Vercel** (Live Dashboard).

---

## 📂 System Architecture

```bash
jaldrishti/
├── dashboard/              # Mission Control Frontend
│   ├── index.html          # Entry Point & HUD Layout
│   ├── js/                 # Core Intelligence (pathfinding, optimization)
│   ├── css/                # Professional Mission Control Styling
│   └── data/               # Spatial GeoJSON & Hydrological Data
├── src/                    # Backend Intelligence Core
│   ├── resource_allocator.py # Heuristic Allocation Logic
│   └── rescue_path.py      # Pathfinding Algorithms
└── vercel.json             # Deployment Configuration
```

---

## ⚡ Quick Start

1. **Local Development**:
   ```bash
   python3 -m http.server 8001
   ```
   Navigate to `http://localhost:8001/dashboard`.

2. **Live Production**:
   Access the stable build at [jaldhristhi-mission-control.vercel.app](https://jaldhristhi-mission-control-nhiqggvew.vercel.app).

---

## 📍 Coverage Areas
- **Meppadi (Kerala)**: High-altitude terrain stabilization.
- **Darbhanga (Bihar)**: Riverine flood basin management.
- **Dhemaji (Assam)**: Extreme precipitation response planning.

---

*Developed as a professional disaster management solution for Jal Drishti.*
