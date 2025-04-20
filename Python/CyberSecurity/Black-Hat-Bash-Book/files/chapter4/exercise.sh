# Send an email when new hosts are found by arp-scan
#!/bin/bash

# Send a notice when a new host is found
KNOWN_HOST="172-16-10-hosts.txt"
NETWORK="172.16.10.0/24"
INTERFACE="br_public"
FROM_ADDR="kali@blackhatbash.com"
TO_ADDR="security@blackhatbash.com"

while true; do
	echo "Performing an APR scan against ${NETWORK}..."

	sudo arp-scan -x -I ${INTERFACE} ${NETWORK} | while read -r line; do
		host=$(echo "${line}" | ark '{print $1}')
		if ! grep -q "${host}" "${KNOWN_HOST}"; then
			echo "Found a new host: ${host}!"
			echo "${host}" >> "${KNOWN_HOST}"
			sendemail -f "${FROM_ADDR}" \
				-t "${TO_ADDR}" \
				-u "ARP Scan Notification" \
				-m "A new host was found: ${host}"
		fi
	done
	sleep 10
done
