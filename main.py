from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Hello from Adios</title>
  <style>
    body { margin: 0; min-height: 100vh; display: grid; place-items: center; font-family: Arial, sans-serif; color: #f8fafc; background: #020617; }
    main { width: min(680px, calc(100% - 48px)); }
    p.kicker { color: #67e8f9; font-weight: 700; letter-spacing: .24em; text-transform: uppercase; }
    h1 { margin: 16px 0; font-size: clamp(3rem, 9vw, 5.5rem); line-height: 1; }
    p { color: #cbd5e1; font-size: 1.125rem; line-height: 1.7; }
    nav { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 32px; }
    a { border: 1px solid rgba(255,255,255,.18); border-radius: 8px; color: #f8fafc; padding: 12px 16px; text-decoration: none; }
    a.primary { background: #67e8f9; color: #020617; border-color: #67e8f9; font-weight: 700; }
  </style>
</head>
<body>
  <main>
    <p class="kicker">Adios starter</p>
    <h1>Hello from Adios</h1>
    <p>This FastAPI template is ready to build, ship, and run on Adios.</p>
    <nav aria-label="Adios links">
      <a class="primary" href="https://app.adios.dev/signup">Deploy on Adios</a>
      <a href="https://www.adios.dev/docs/quickstart">Read the quickstart</a>
    </nav>
  </main>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def home():
    return HTML


@app.get("/healthz")
def healthz():
    return {"ok": True}
