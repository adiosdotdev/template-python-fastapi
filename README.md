# Python FastAPI Template

Production-oriented FastAPI starter for Adios.

## Deploy

```sh
adios up
```

## Configuration

* **Runtime:** `python@3.13`
* **Build:** Installs dependencies from `requirements.txt`
* **Start:** Runs Uvicorn and binds to `${PORT:-8080}`

## Notes

* The ASGI app entrypoint is `main:app`
* Worker count can be adjusted with `UVICORN_WORKERS`
