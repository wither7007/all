#Get-ChildItem -path c:\ -recurse -ErrorAction SilentlyContinue  |  Where-Object {$_.LastWriteTime -gt (Get-Date).AddDays(-1)}
Get-ChildItem  -File -recurse -Exclude node* -ErrorAction SilentlyContinue  |  Where-Object {$_.LastWriteTime -gt (Get-Date).AddDays(-1)}
