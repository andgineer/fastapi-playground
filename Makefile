#!make

run:
	python -m uvicorn \
	--host 0.0.0.0 \
	--port 8000 \
	--reload \
	fastapi_playground.main:app \
	--log-config logging.yaml

