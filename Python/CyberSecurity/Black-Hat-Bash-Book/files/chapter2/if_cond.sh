#!/bin/bash
FILENAME="examplefile.txt"

# Creates file if it doesn't exists
if [[ -f "${FILENAME}" ]]; then
	echo "${FILENAME} already exists"
	exit 1
else
	echo "Created file ${FILENAME}"
	touch "${FILENAME}"
fi
