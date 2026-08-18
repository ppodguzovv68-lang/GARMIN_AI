from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Garmin AI")

INDEX_HTML = """<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Garmin AI</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 640px; margin: 40px auto; padding: 0 16px; color: #222; }
    .card { border: 1px solid #ddd; border-radius: 8px; padding: 16px 20px; margin-top: 16px; }
    .ok { color: #1a7f37; font-weight: 600; }
  </style>
</head>
<body>
  <h1>Garmin AI</h1>
  <p>Локальный анализ тренировок Garmin.</p>
  <div class="card">
    <p>Статус приложения: <span class="ok">работает</span></p>
    <p>API: <code>GET /api/health</code></p>
  </div>
</body>
</html>"""


@app.get("/", response_class=HTMLResponse)
def index():
    return INDEX_HTML


@app.get("/api/health")
def health():
    return {"status": "ok"}
