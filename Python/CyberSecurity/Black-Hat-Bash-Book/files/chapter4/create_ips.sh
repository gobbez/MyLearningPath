# Generate IPs of an interval
for ip in $(seq 1 254); do
	echo "172.16.10.${ip}" >> 172-16-10-hosts.txt
done
