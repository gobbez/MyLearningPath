url=${1}
username=${2}
password=${3:-}

# Connect with ftp
ftp "ftp://${username}:${password}@${url}"
