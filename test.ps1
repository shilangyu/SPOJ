Get-ChildItem -Directory | ForEach-Object {
	Set-Location $_
	$name = $_
	try {
		if (Test-Path main.py) {
			$out = Get-Content ./input | python ./main.py | Out-String
		}
	 elseif (Test-Path main.go) {
			$out = Get-Content ./input | go run ./main.go | Out-String
		}
	 elseif (Test-Path main.bf) {
			$out = Get-Content ./input | brainfuck ./main.bf | Out-String
		}
	 elseif (Test-Path main.cpp) {
			 g++ main.cpp -o asd123.exe
			$out = Get-Content ./input | ./asd123.exe | Out-String
			rm asd123.exe
		}
	 else {
			Throw ''
		}
	
		$correct = Get-Content ./output | Out-String
		if ($out -ne $correct) {
			Write-Output "$_ was incorrect"
		}
	}
 catch {
		Write-Output "Didnt recognise file type in $name"
	}

	Set-Location ..
}
