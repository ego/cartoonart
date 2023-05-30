#!/bin/bash

set -o errexit
set -o verbose


pip-compile --upgrade dev-requirements.in
pip-compile --upgrade requirements.in
pip-sync dev-requirements.txt requirements.txt
