spaces(){
	for i in $(seq 1 4); do
		echo " "
	done
}

# Get only IPs from file
awk '{print $1}' logs.txt
spaces

# Show first 3 rows
awk 'NR < 3' logs.txt
spaces

# Modify every 157 to 999 of the first 3 rows, writing in a new file
awk 'NR < 3' logs.txt | sed 's/157/999/g' > logsnew.txt
spaces

# Show new file
echo "Showing new file"
cat logsnew.txt
