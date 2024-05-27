# Pipes

Pipes allow you to pass the output from one command as the input to another.

1. calculate words in file: wc -w. For example: wc text1.txt -w
1. create pipe for count words in both files: cat text1.txt text2.txt | wc -w
