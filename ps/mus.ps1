#runs vlc with directory
$data = @('C:\you\funnyv','C:\you\class','C:\music\autumn','\you\lquart','C:\you\stand','C:\you\hawk')
$a = Get-Random -Minimum 0 -Maximum $data.count
cd $data[$a]
vlc -Z .
