# Function
check_if_root(){
	if [[ "$[EUID]" -eq "0" ]]; then
		return 0
	else
		return 1
	fi
}

# Calls the function inside an If condition
if check_if_root; then
	echo "User is root!"
else
	echo "User is not root"
fi
