#!/bin/bash
cd ..
rm -R ./bbackup
pwd
git clone https://github.com/Zep314/bbackup.git
cd ./bbackup
pwd
python3 -m venv .venv
pip install -r ./requirements.txt
chmod +x ./make.sh
chmod +x ./start.sh
