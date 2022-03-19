#!/bin/bash

cd ~/linux_environment/
if [[ 'git status --porcelain' ]]; then
   git add -A 
   git commit -am "Daily update 1"
   git push origin main
fi
