DOMAIN="${1}"
FILE="${2}"

# Read file and creates domains
while read -r subdomain; do
	echo "${subdomain}.${DOMAIN}"
done < "${FILE}"


