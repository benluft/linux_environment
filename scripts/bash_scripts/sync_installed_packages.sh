#!/bin/bash

#if [[ 'git status --porcelain' ]]; then
#   git -C ~/linux_environment/ add -A 
#   git -C ~/linux_environment/ commit -m "Daily update 1"
#   git -C ~/linux_environment/ push origin main > text.txt
#fi
if [ -z "$SSH_AUTH_SOCK" ]
then
    export SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
fi

git -C ~/linux_environment/ add -A 
git -C ~/linux_environment/ commit -m "Daily update 1"
git -C ~/linux_environment/ push origin main > text.txt
