#!/bin/bash
cd ..
rm -R ./bbackup
pwd
git clone https://github.com/Zep314/bbackup.git
cd ./bbackup
pwd
chmod +x ./make.sh
chmod +x ./start.sh
python3 -m venv .venv
source ./.venv/bin/activate
pip3 install --break-system-packages -r ./requirements.txt
deactivate
