#!/usr/bin/env bash

if [ -n "$DEBUG" ]; then
	set -x
fi

set -o errexit
set -o nounset
set -o pipefail

DIR=$(cd $(dirname "${BASH_SOURCE}") && pwd -P)

POETRY_HOME="${POETRY_HOME:=${HOME}/.poetry}"
echo "[metrics] Run spotifier PEP 8 checks."
"$POETRY_HOME"/bin/poetry run flake8 --select=E,W,I --max-line-length 80 --import-order-style pep8 --exclude .git,__pycache__,.eggs,*.egg,.pytest_cache,spotifier/version.py,spotifier/__init__.py --tee --output-file=pep8_violations.txt --statistics --count spotifier
echo "[metrics] Run spotifier PEP 257 checks."
"$POETRY_HOME"/bin/poetry run flake8 --select=D --ignore D301 --tee --output-file=pep257_violations.txt --statistics --count spotifier
echo "[metrics] Run spotifier code complexity checks."
"$POETRY_HOME"/bin/poetry run flake8 --select=C901 --tee --output-file=code_complexity.txt --count spotifier
echo "[metrics] Run spotifier open TODO checks."
"$POETRY_HOME"/bin/poetry run flake8 --select=T --tee --output-file=todo_occurence.txt --statistics --count spotifier tests
