#! /usr/bin/env bash

python -m uvicorn \
  --host 0.0.0.0 \
  --port 3000 \
  --reload \
  fastapi_playground.main:app \
  --log-config logging.yaml
