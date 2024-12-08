
#SingleInstance Force
!a::run, "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Vim 9.1\gVim.lnk" 
!e::run, "C:\Program Files\Double Commander\doublecmd.exe"
!t::run, C:\Users\jayst\AppData\Local\Microsoft\WindowsApps\wt.exe
!p::runwait, PowerShell.exe -ExecutionPolicy Bypass -Command c:\all\ps\mus.ps1

^SPACE::  Winset, Alwaysontop, , A

!v:: send,  | v -

!d:: send, C:\Users\jimst\AppData\Local\nvim\init.vim\vim91\gvim.exe 

!c::run, C:\Users\jimst\AppData\Local\nvim\init.vim\vim91\gvim.exe    -p c:\all\note\notes c:\all\note\js c:\all\note\power c:\all\note\bash c:\all\note\python c:\all\note\other

!q:: Send !{f4}
return


!w::
send, | sed 's|\/mnt\/c|c\:|' | sed 's|\/|\\|g'
return

!y::
Send, And so from hour to hour we ripe and ripe And then from hour to hour we rot and rot And thereby hangs a tale As You Like It Act 2 Scene 7
return

!x:: Send, after:2020
return

!j::
Send, The thing that hath been, it is that which shall be; and that which is done is that which shall be done: and there is no new thing under the sun.
return

!k::
Send, Beware the Jabberwock, my son The jaws that bite the claws that catch Beware the Jubjub bird, and shun The frumious Bandersnatch  He took his vorpal sword in hand;  Long time the manxome foe he sought  So rested he by the Tumtum tree  And stood awhile in thought.
return


!l::
Send, in the chest of the out of tune No peito dos desafinados Also beats a heart Tambem bate um coracao
return

!b::
Send, Those who are hardest to love, need it the most- Be kind, for every one you meet is fighting a hard battle.  bumblescum North dakot - Simplicity is the final achievement. After one has played a vast quantity of notes and more notes, it is simplicity that emerges as the crowning reward of art
return

!m::
Send, The lady doth protest too much methinks
return

!z::
Send, 10/26/1964
return


