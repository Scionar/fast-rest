#!/bin/sh

pip3 install pycnic gunicorn psycopg2

SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd )"
(cd "$SCRIPT_DIR/app" && gunicorn rest:app)
