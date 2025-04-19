#!/bin/bash

# Executes ping on the argument 
SCRIPT_NAME="${0}"

# Loops over arguments and execute ping
echo "Running the script ${SCRIPT_NAME}.."
for arg in "${@}"; do
	echo "Pinging the target: ${arg}.."
	ping -c 4 "${arg}"
done
