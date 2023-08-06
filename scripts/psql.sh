#! /usr/bin/env bash
echo
echo connecting to postgresql running in docker container (docker-compose up -d)
echo uses password from ~/.pgpass
echo
psql -h 127.0.0.1 --user postgres foo
