#!/bin/bash

set -o errexit
set -o verbose

# Set environment variables from file.
set -a
source aws.env
set -o verbose

tox -e lint,docs,doctests,linkcheck,pytest,clean,build
tox -e publish -- --repository pypi

set +o verbose
set +a
