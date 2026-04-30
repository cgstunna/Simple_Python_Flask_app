# Flask CI/CD Demo

Simple Flask app with:
- Python tests in GitHub Actions
- Docker image build after tests pass
- SSH deployment job for a remote server

## Local run

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

## Local tests

```bash
pytest -q
```

## Intentional test failure

In GitHub Actions, run the workflow manually and set `break_test=true`.
This sets `BREAK_TEST=true` and makes one test fail on purpose.

## Required GitHub Secrets for deploy

- `SSH_HOST`: server IP or domain
- `SSH_USER`: SSH username
- `SSH_PRIVATE_KEY`: private key text for that user
- `DEPLOY_PATH`: folder on server where this repo is checked out
