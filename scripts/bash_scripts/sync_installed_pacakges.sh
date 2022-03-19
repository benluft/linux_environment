#!/bin/bash

cd ~/linux_environment/
if [[ 'git status --porcelain' ]]; then
   /usr/bin/git add -A 
   /usr/bin/git commit -am "Daily update"
   /usr/bin/git push -u origin main
fi
