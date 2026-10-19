# Python Flask site

A small Flask site with Home and About pages.

## Setup

Requires Python 3.10 or newer.

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

```powershell
python app.py
```

Open <http://127.0.0.1:5000> in your browser. The development server uses Flask's debug mode; do not expose it to an untrusted network or use it as a production server.

## Routes

- `/` — Home
- `/about` — About
