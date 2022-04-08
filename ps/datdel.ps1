$root = '.'
$limit = (Get-Date).AddDays(-15)

Get-ChildItem 'l*.mp3' $root -Recurse | ? { -not $_.PSIsContainer -and $_.CreationTime -lt $limit } | Remove-Item -WhatIf
