# example: http://172.16.10.10:8081/files/acme-hyper-granding-5.csv
url_of_file=${1}

# Use Wget to download the file
wget ${url_of_file}
