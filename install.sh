#!/usr/bin/env bash
if ! command -v python3 &> /dev/null ; then
    echo 2>&1 "I can't go on. Can't find python3 on path."
    exit 1
fi
python3 -m venv ./venv
. venv/bin/activate
pip install -r requirements.txt
echo "Likely next step: source ./venv/bin/activate"
