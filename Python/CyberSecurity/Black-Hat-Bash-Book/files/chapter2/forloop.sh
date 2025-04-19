start=$1
end=$((start+10))

for i in $(seq "$start" "$end"); do
	echo "${i}"
done
