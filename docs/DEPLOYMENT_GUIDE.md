# Deployment Guide

## Quick Deploy (Vercel)

The dashboard is a static frontend, deployable directly to Vercel:

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

The `vercel.json` routes all traffic to `/dashboard/`.

---

## Local Development

### Backend API

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start API server
uvicorn src.api_server:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend Dashboard

```bash
# Option 1: Python HTTP server
python3 -m http.server 8001

# Option 2: Node.js serve
npx -y serve dashboard -p 8001
```

Navigate to `http://localhost:8001/dashboard`.

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `API_HOST` | `0.0.0.0` | API bind address |
| `API_PORT` | `8000` | API port |
| `LOG_LEVEL` | `INFO` | Logging level |

Copy `.env.example` to `.env` and customize as needed.

---

## Production Checklist

- [ ] Set `LOG_LEVEL=WARNING` in production
- [ ] Enable HTTPS via reverse proxy (nginx/Caddy)
- [ ] Configure CORS origins for your domain
- [ ] Set up monitoring and alerting
- [ ] Run `make validate-data` to verify data integrity
