read -r -p "Write ip(s): " ips
whatweb ${ips} --log-json=/dev/stdout --quiet | jq
