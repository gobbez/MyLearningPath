#!/bin/bash
EMAIL_TO="email"
EMAIL_FROM="email"

for ip_address in "$@"; do
	echo "Testing ${ip_address} with Nuclei..."
	result=$(nuclei -u "${ip_address}" -silent -severity medium,high,critical)
	if [[ -n "$(result)" ]]; then
		while read -r line; do
			template=$(echo "${line}" | awk '{print $1}' | tr -d '[]')
			url=$(echo "${line}" | awk '{print $4}')
			echo "Sending an email with the findings ${templates} ${url}"
			sendemail -f "${EMAIL_FROM}" \
						-t "${EMAIL_TO}" \
						-u "[Nuclei] Vulnerability found!" \
						-m "${template} - ${url}"
		done <<< "${result}"
	fi
done
