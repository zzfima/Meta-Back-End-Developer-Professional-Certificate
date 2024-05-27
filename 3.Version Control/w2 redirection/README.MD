# redirection

Everything in unix/linux is a file.
There are three types of IO or input/output redirections. Standard input - 0 , standard output - 1, and standard error - 2

## Standard input

input: >
Storing input to txt file: cat > keyboard_input.txt
finish: ctrl + d

## standard output

when you do: ls -l, os sent output of ls.exe to stdout

output <
file to screen: cat < keyboard_input.txt
dir contain to file: ls -l > dir_output.txt

## standard error

if there is error you can redirect it to file:
ls -l kakax 2> error_input.txt
we will get: ls: cannot access 'kakax': No such file or directory

redirect to file error and not:
ls -l kakax > error_input.txt 2>&1
ls -l > error_input.txt 2>&1
