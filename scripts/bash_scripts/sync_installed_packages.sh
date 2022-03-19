#!/bin/bash


if [ -z "$SSH_AUTH_SOCK" ]
then
    export SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
fi

cd ~/linux_environment

# Always pull just in case changed somewhere else
git pull

if [[ 'git status --porcelain ./setup/module_installs/*.txt' ]]; then
   git add ./setup/module_installs
   git commit -m "Daily update module installs $(date +%F)"
   git push
fi
