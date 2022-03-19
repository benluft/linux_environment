#!/bin/bash


if [ -z "$SSH_AUTH_SOCK" ]
then
    export SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
fi

cd ~/linux_environment

if [[ 'git status --porcelain' ]]; then
   git add -A 
   git commit -m "Daily update $(date +%F)"
   git push
fi

