#!/bin/bash

label_name=""
the_logs=""


track_status () {
# Takes 2 parameters ONLY when used within track_start or track_stop
# $1 being the label_name
# $2 being a "flag" which allows the storage of label_name

# If this function is manually called upon through the terminal,
# it is done so without any variables.

	if [ "$2" = "1" ]
	then
		# Stores label name
		label_name="$1"
		return
	fi
	
	if [ -z "$label_name" ] 
	then
		echo "No active tasks."
		echo "No active tasks." >> $LOGFILE
	else
		echo "Tracking: $label_name"

		# Printed to the file
		echo "LABEL Tracking: $label_name" >> $LOGFILE
	fi
}


track_start () {

	# If a task is already running
	if [[ -n "$label_name" ]] 
	then
		# If true
		echo "Error message: Task $label_name already running."
	else
		# If none are running, then create a new task
		echo "Starting new task with the given label: $1"
		SECONDS=0
		echo "$(date +"%T")"

		# Printed to the file
		echo "START $(date +"%T")" >> $LOGFILE

		track_status "$1" "1"
	fi
}


track_stop () {

	# Checks if no tasks are running (singular)
	if [[ -z "$label_name" ]]
	then
		# If true, meaning none are running
		echo "Error message: No tasks are currently running."
	else
		# If a task is running, then stop the current task
		echo "Stopping task..."
		duration=$SECONDS # Figures out time spent on task

		# Appends into the list of tasks and their time spent
		the_logs="$the_logs$label_name: "$(($duration / 3600)):$((($duration / 60) % 60)):$(($duration % 60))$'\n'

		echo "$(date +"%T")"

		# Printed to the file
		echo "STOP $(date +"%T")" >> $LOGFILE
		echo "" >> $LOGFILE

		track_status "" "1"
		echo "Task has now been stopped."
	fi

}


track_log () {
	
	# Prints to termial time spent on tasks.
	echo "$the_logs"	
}

echo "WELCOME TO TRACKER.SH"

while :
do
	# Show menu
	echo ""
	echo "User commands:"
	echo "- track_start [label]"
	echo "- track_stop"
	echo "- track_status"
	echo "- track_log"

	# Varlabel is only needed for track_start
	# Otherwise remains as "" and completely ignored 
	read varfunction varlabel


	if [ "$varfunction" = "track_start" ] && [[ -n "$varlabel" ]]
	then
		echo ""
		echo "Entering function track_start..."
		track_start $varlabel

	elif [ "$varfunction" = "track_stop" ]
	then
		echo ""
		echo "Entering function track_stop..."
		track_stop

	elif [ "$varfunction" = "track_status" ]
	then
		echo ""
		echo "Entering function track_status..."
		track_status

	elif [ "$varfunction" = "track_log" ]
	then
		echo ""
		echo "Entering function track_log..."
		track_log

	else
		echo ""
		echo "No such function, please use one of the commands given in the menu."
		echo "example: track_start track1"
	fi
done
