#!/bin/bash

#Creates a new virtualenv if one does not exist, activates the venv that is named

if [ $# -ne 1  ]; then
    echo Please provide 1 argument, which will be the name of the virutalenv environment
else
    dirname=/usr/local/bin/venv/$1

    if [ ! -d $dirname ]; then
	echo "Current virtualenvs include:"
	ls /usr/local/bin/venv
	echo # blank line
	read -p "Do you want to create a new environment at $dirname?(y/n) " -n 1 -r
	echo # blank line

	if [[ ! $REPLY =~ ^[Yy]$ ]]; then
	    echo No Environment created
	    return -1
	fi

	mkdir $dirname
	echo New environment being created at $dirname
	python3 -m virtualenv -p python3 $dirname
	chmod -R 777 $dirname/bin
	echo Activating new environment at $dirname...
    else
	echo "Environment already created at $dirname, activating.."
    fi
    echo "$dirname/bin/activate"
    source "$dirname/bin/activate"
    echo "Environment activated!"
fi
