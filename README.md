# Report_Jin — README

Quick steps to run and test the project locally and in Docker.

## Prerequisites
- macOS
- Python 3.8+
- virtualenv / venv
- Docker

## Test locally
1. Export your FRED API token in the current shell:
   ```bash
   export FRED_API_TOKEN="your_token_here"
   ```
2. Create and activate a virtual environment and install deps:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Navigate to the project root:
   ```bash
   cd /Users/isaac/Repositories/Projects/Report_Jin
   ```
4. Run the app:
   ```bash
   python3 -m app.main
   ```

## Test in Docker (recommended: pass token at runtime)
1. Ensure the env var is set locally:
   ```bash
   export FRED_API_TOKEN="your_token_here"
   ```
2. Build and run the image, passing the token into the container:
   ```bash
   docker build --build-arg FRED_API_TOKEN="$FRED_API_TOKEN" -t report_jin:latest .
   docker run --rm -e FRED_API_TOKEN="$FRED_API_TOKEN" report_jin:latest
   ```

Notes and tips
- Passing the build-arg alone does not make the value available at runtime unless the Dockerfile maps ARG -> ENV.
- To verify the token inside a short-lived container:
  ```bash
  docker run --rm -e FRED_API_TOKEN="$FRED_API_TOKEN" python:3.10-slim python -c 'import os; print("FRED_API_TOKEN:", bool(os.environ.get("FRED_API_TOKEN")))'
  ```
- Alternative: use an env file:
  ```bash
  echo "FRED_API_TOKEN=$FRED_API_TOKEN" > .env
  docker run --env-file .env --rm report_jin:latest
  ```
- Add runtime checks in the app to raise a clear error if FRED_API_TOKEN is missing (recommended).