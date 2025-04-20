# Get the list of words to try and the url
list_words=${1}
url=${2}

# Use Wfuzz to create fuzzing in order to find which words are real (200) urls
wfuzz --sc 200 -w ${list_words} ${url}/FUZZ
