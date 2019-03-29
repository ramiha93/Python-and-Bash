#!/bin/bash

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

# Must be run with an additional dot (.) in the terminal like so:
# $. climb.sh
# or
# $. climb.sh 2
