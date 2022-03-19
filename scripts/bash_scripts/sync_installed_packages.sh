#!/bin/bash

cd ~/linux_environment/
if [[ 'git status --porcelain' ]]; then
   git add -A 
   git commit -m "Daily update 1"
   git push origin main > text.txt
fi
