# Captain's Mail

A mobile-friendly Flask web app for the college mailroom. It replaces the old
laptop-and-barcode-scanner setup. Staff use their phones to scan shipping labels
when checking packages in and out, and photograph where each package is stored
so it can be found quickly later.

**Stack:** Flask, Flask-SQLAlchemy, Flask-Login, SQLite, Jinja2 + Bootstrap,
html5-qrcode for in-browser barcode scanning.

## Setup

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
copy .env.example .env         # then set a real SECRET_KEY in .env
```

## Create a staff account

```bash
flask --app run create-staff <username>
```

You'll be prompted for the password (typed twice, hidden).

## Run

```bash
python run.py
```

Then open http://localhost:5000. To test from a phone on the same Wi-Fi, use
`http://<your-computer's-IP>:5000`.

The SQLite database is created in `instance/` (not tracked by git).
