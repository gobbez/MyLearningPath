# Write name and surname
echo "Write your name:"
read -r name
echo "Write your surname:"
read -r surname

# Create file output
touch output.txt

# Write date, name and surname in the file
date '+%d/%m/%Y' > output.txt
echo "$name" >> output.txt
echo "$surname" >> output.txt

# Copy file
cp output.txt backup.txt

# Show output
cat output.txt

