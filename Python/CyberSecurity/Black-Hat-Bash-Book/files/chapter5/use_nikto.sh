HOST=${1}
PORT=${2}

# Scan host net on port with Nikto
nikto -host ${HOST} -port ${PORT}
