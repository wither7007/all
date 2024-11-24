$programName = "AutoHotkeyU64"
$isRunning = (Get-Process | Where-Object { $_.Name -eq $programName }).Count -gt 0
echo $isRunning
if($isRunning -eq 'False'){Write-Host "autokey running"}else{start "C:\all\note\first.ahk"}
#start "C:\all\note\first.ahk"
