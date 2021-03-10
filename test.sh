#!/usr/bin/env bash

count=$(curl localhost:9098/payload -H "Content-type: application/json" -s -d '{"credit": "4111111111111111"}' | grep -c "tok_sat")
exit_code=$((count ^ 1))
exit $exit_code