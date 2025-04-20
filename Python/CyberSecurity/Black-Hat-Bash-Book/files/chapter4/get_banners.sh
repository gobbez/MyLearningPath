#!/bin/bash

FILE="${1}"
PORT="${2}"

while read -r ip; do
	echo "Running Netcat on ${ip}:${PORT}"
	result=$(echo -e "\n" | nc -v "${ip}" -w 1 "${PORT}" 2 > /dev/null)
	if [[ -n "${result}" ]]; then
		echo "======="
		echo "+IP Adress: ${ip}"
		echo "+Banner: ${result}"
		echo "======="
	fi
done < "${FILE}"
