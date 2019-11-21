#!/usr/bin/env bash
set -uex
pushd .

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "script_dir is ${script_dir}"

pushd "${script_dir}/../pandoc_resume"
make IN_DIR="${script_dir}/../markdown"
popd

function finish {
  popd
}
trap finish EXIT