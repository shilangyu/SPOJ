#!/bin/fish

if test (count $argv) -eq 1
	set name $argv[1]
	mkdir $name
	cd $name
	touch input
	touch output
	touch main.py
else 
	echo -e "Usage: \n\t./new.fish <problem_name>"
end
