# Grep

Global REgular exPression

1. ls -l
1. less names.txt
1. find some pattern
   1. contains 'sa': grep Sa names.txt
   1. contains 'sa' case ignore: grep -i Sa names.txt
   1. exactly match: grep -w Sa names.txt
   1. combine with pipe - search for all folders which has substring 'ma': ls ~/source/repos/ | grep -i ma

* Bash Redirections
  * https://www.gnu.org/software/bash/manual/html_node/Redirections.html#Redirections

* Bash Cheatsheet
  * https://devhints.io/bash

* Grep Cheatsheet
  * https://devhints.io/grep