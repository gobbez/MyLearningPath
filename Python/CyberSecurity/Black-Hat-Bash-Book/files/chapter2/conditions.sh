echo "Write first string"
read -r first
echo "Write second string"
read -r second

# Check if those are equal
if [[ "${first}" == "${second}" ]]; then
	echo "Equal"
else
	echo "Not equal"
fi

echo "Write first number"
read -r firstn
echo "Write second number"
read -r secondn

# Check if firstn is greater than secondn
if [[ "${firstn}" -gt "${secondn}" ]]; then
	echo "Bigger"
else
	echo "Smaller"
fi

# Check both conditions
if [[ "${first}" == "${second}" ]] && [[ "${firstn}" -gt "${secondn}" ]]; then
	echo "equal and bigger"
elif [[ "${first}" != "${second}" ]] && [[ "${firstn}" -gt "${secondn}" ]]; then
	echo "Not equal and bigger"
elif [[ "${first}" == "${second}" ]] && [[ "${firstn}" -le "${secondn}" ]]; then
	echo "equal and smaller"
else 
	echo "Not equal or smaller"
fi
