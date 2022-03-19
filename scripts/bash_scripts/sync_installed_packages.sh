#!/bin/bash

if [[ 'git status --porcelain' ]]; then
   git -C ~/linux_environment/ add -A 
   git -C ~/linux_environment/ commit -m "Daily update 1"
   git -C ~/linux_environment/ push origin main > text.txt
fi
