#!/usr/bin/env bash

set -e

if [[ "${TRAVIS_PYTHON_VERSION}" == "3.5"* ]]; then
  tox -e "py{27,34,35}-dj{10,11}, py{34,35}-dj20"

elif [[ "${TRAVIS_PYTHON_VERSION}" == "3.6"* ]]; then
  tox -e "py36-dj{10,11,20}"

else
  echo "Unsupported Python version. Exiting"
  exit 1

fi
