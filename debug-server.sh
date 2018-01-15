#!/usr/bin/env bash
# standalone dev server
. venv/bin/activate

export FLASK_DEBUG=1
export FLASK_APP=src/conc-server.py
export WERKZEUG_DEBUG_PIN=off

flask run --host=0.0.0.0 &
