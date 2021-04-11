#! /bin/bash

word=$(cat /dev/stdin)
echo ${word^^} >> ~/wordsmart/learnedwords.txt
