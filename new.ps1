param (
	[string]$name
)

mkdir $name
cd $name
ni input
ni output
ni main.py