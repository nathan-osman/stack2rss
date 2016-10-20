#!/bin/sh

virtualenv=$(dirname "$BASH_SOURCE")/virtualenv
if test -d $virtualenv; then
    . $virtualenv/bin/activate
else
    echo virtualenv does not exist: $virtualenv >&2
    echo Create it with: virtualenv --distribute $virtualenv >&2
    echo Better yet, run ./scripts/setup.sh >&2
fi
