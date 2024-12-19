#!/bin/bash
cd ..
rm -R ./bbackup
git clone https://github.com/Zep314/bbackup.git
python3 -m venv .venv
pip install -r ./requirements.txt
