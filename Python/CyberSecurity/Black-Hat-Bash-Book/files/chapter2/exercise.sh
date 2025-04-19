firstparam=$1
secondparam=$2

if [[ -z "$firstparam" || -z "$secondparam" ]]; then
	echo "You must pass 2 params"
	exit 1
fi

ping -c 2 "${secondparam}" > exercise.csv
cat exercise.csv


