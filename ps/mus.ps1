#runs vlc with directory
$data = @( 'C:\you\cp','C:\music\mozart','C:\you\kb\miles', 'C:\music\Bach- Brandenburg Concertos #4-6', 'C:\you\funnyv','C:\you\class','C:\music\autumn','\you\lquart','C:\you\stand','C:\you\hawk')
$a = Get-Random -Minimum 0 -Maximum $data.count
cd $data[$a]
vlc -Z .
