#!/bin/bash

# In terminal, type: ". climb.sh" or ". climb.sh 2" depending on interations.

# "climb" returns you back one or several directories if $1 is given.
# If no argument $1 is added, performs the bash command "cd .." once.
# If $1 is given, performs "cd .." the given amount of times necessary.

climb () {
	i=0

	#default (no argument)
	if [ -z $1 ]
	then
		cd ..
	else
		i=$1

		#argument given
		while [ $i -gt 0 ]
		do
			cd ..
			i=$(( $i - 1 ))
		done
	fi
}

climb "$1"
