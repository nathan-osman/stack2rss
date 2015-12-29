#!/bin/sh

cd $(dirname "$0")
. ./virtualenv.sh

export PYTHONPATH=.
python "$@"
