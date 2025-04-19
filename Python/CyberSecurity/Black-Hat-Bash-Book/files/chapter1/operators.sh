# Lo sleep è eseguito in background tramite il comand &
echo "Sleeping 10s"
sleep 10 & 
echo "Creating the file test123"
touch test123
echo "Deleting the file test123"
rm test123
