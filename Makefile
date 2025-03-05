#!make

.HELP: help  ## Upgrade dependencies
reqs:
	mamba update --all
	mamba env export > environment.yml.tmp && grep -v 'prefix:' environment.yml.tmp > environment.yml && rm environment.yml.tmp

.HELP: help  ## Run the server
run:
	python -m uvicorn \
	--host 0.0.0.0 \
	--port 8000 \
	--reload \
	fastapi_playground.main:app \
	--log-config logging.yaml

.HELP: help  ## Run sql model
sqlmodel:
	DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/foo python -m uvicorn \
	--host 0.0.0.0 \
	--port 8000 \
	--reload \
	fastapi_playground.sqlmodel.main:app \
	--log-config logging.yaml

.HELP: help  ## Display this message
help:
	@grep -E \
		'^.HELP: .*?## .*$$' $(MAKEFILE_LIST) | \
		sort | \
		awk 'BEGIN {FS = ".HELP: |## "}; {printf "\033[36m%-19s\033[0m %s\n", $$2, $$3}'
