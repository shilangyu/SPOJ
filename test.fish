#!/bin/fish

for dir in */
	cd $dir
	set got (cat input | omnirun main.*)
	set correct (cat output)

	if test "$got" != "$correct"
		echo 'wrong: '$dir
		exit 1
	end

	cd ..
end
