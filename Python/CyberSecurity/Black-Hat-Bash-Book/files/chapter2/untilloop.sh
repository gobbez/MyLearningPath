value=10
until [[ $value -le 0 ]]; do
	echo "${value} is bigger than 0"
	value=$((value-1))
done
