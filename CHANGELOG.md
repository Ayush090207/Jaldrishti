# Changelog

All notable changes to Jal Drishti are documented here.

## [2.0.0] - 2024-07-15

### Added
- 🗺️ **3D Terrain Rendering** with AWS Terrarium elevation tiles
- 🧠 **Multi-criteria AI Risk Scoring** (water depth 40%, slope 25%, flow accumulation 25%, proximity 10%)
- 🛡️ **Risk-Aware A* Rescue Routing** with Catmull-Rom spline smoothing
- 🎯 **Mission-Linked Resource Optimization** with simulation interlock
- 🌡️ **Live Weather Integration** via Open-Meteo API with 7-day forecast
- 📊 **Precinct Forecasting Charts** with Chart.js (monthly risk, short-term precipitation)
- 🏘️ **Intelligent Population Heatmap** using building centroid analysis
- 📄 **Tactical Report Generation** with downloadable text reports
- 🌊 **Terrain-Specific Flood Algorithms** for hilly, riverine, and floodplain terrains
- 🚁 **Drone Intelligence** page for future aerial integration
- 📖 **Interactive Methodology** documentation page

### Changed
- Upgraded MapLibre GL JS for high-performance WebGL rendering
- Switched from Mapbox to Esri World Imagery for satellite tiles
- Replaced OpenWeatherMap with Open-Meteo (no API key required)
- Professional dark-mode HUD with glassmorphism styling

### Coverage Areas
- **Meppadi** (Wayanad, Kerala) — Western Ghats hilly terrain
- **Darbhanga** (Bihar) — Gangetic riverine plain
- **Dhemaji** (Assam) — Brahmaputra floodplain

## [1.0.0] - 2024-03-01

### Added
- Initial dashboard with basic flood visualization
- Single village support (Wayanad)
- Simple risk overlay
- Basic population heatmap
