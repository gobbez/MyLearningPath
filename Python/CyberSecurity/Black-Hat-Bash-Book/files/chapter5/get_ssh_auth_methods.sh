url=${1}

# Use Nmap to get the authentication methods for that url
nmap --script=ssh-auth-methods ${url}
