#!/bin/bash

set -o errexit
set -o verbose

targets=(src)

# Trim trailing whitespace over project.
find . -not -path '.git' -iname '*.py' -iname '*.md'

isort --jobs 4 --profile black "${targets[@]}"

autoflake --recursive \
          --in-place \
          --remove-unused-variables \
          --remove-all-unused-imports "${targets[@]}"

autopep8 --jobs 4 \
         --recursive \
         --in-place -a -a "${targets[@]}"

black --config .black.toml "${targets[@]}"
