
#SingleInstance Force
!a::run, C:\tools\neovim\Neovim\bin\nvim.exe -c "cd c:\all"      ; Correct
!t::run, C:\Users\jayst\AppData\Local\Microsoft\WindowsApps\wt.exe
!p::runwait, PowerShell.exe -ExecutionPolicy Bypass -Command c:\all\ps\mus.ps1

!z::
SendRaw, `%paste
return

!s::
SendRaw, `%run dataManager.py
return

!d::run, C:\tools\neovim\Neovim\bin\nvim.exe "c:\all\note\notes"

!c::run,  C:\tools\neovim\Neovim\bin\nvim.exe -p c:\all\note\notes c:\all\note\power c:\all\note\work c:\all\note\python

!q:: Send !{f4}
return


!h::
Send, The Queen of Hearts, she made some tarts,  All on a summers day, The knave of Hearts, he stole the tarts, And took them clean away.
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

F1::
Send, !^+1
Return

F2::
Send, !^+2
Return


F3::
Send, !^+3
Return


F4::
Send, !^+4
Return

F5::
Send, !^+5
Return

F6::
Send, !^+6
Return
!b::
Send, Those who are hardest to love, need it the most- Be kind, for every one you meet is fighting a hard battle.  bumblescum North dakot - Simplicity is the final achievement. After one has played a vast quantity of notes and more notes, it is simplicity that emerges as the crowning reward of art
return

!m::
Send, The lady doth protest too much, methinks
return




!1::
SendRaw, `%run vsc1.py
return

!2::
SendRaw, `%run vsc2.py
return


!3::
SendRaw, `%run vsc3.py
return

!4::
SendRaw, `%run idFinder.py
return
