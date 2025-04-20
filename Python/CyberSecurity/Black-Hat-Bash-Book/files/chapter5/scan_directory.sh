#!/bin/bash
# Get file with ips and the folder to save
FILE="${1}"
OUTPUT_FOLDER="${2}"

# If file empty exits
if [[ ! -s "${FILE}" ]]; then
	echo "You must provide a non-empy hosts file as an argument"
	exit 1
fi

# if output path empty, use data
if [[ -z "${OUTPUT_FOLDER}" ]]; then
	OUTPUT_FOLDER="data"
fi

# Read every line of ips and check for directories, if positive save the content
while read -r line; do
	url=$(echo "${line}" | xargs)
	if [[ -n "${url}" ]]; then
		echo "Testing ${url} for Directory indexing..."
		if curl -L -s "${url}" | grep -q -e "Index of /" -e "[PARENTDIR]"; then
			echo -e "\t -!- Found Directory Indexing page at ${url}"
			echo -e "\t -!- Downloading to the \"${OUTPUT_FOLDER}\" folder..."
			mkdir -p "${OUTPUT_FOLDER}"
			wget -q -r -np -R "index.html*" "${url}" -P "${OUTPUT_FOLDER}"
		fi
	fi
done < <(cat "${FILE}")
