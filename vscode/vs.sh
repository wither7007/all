alias fd="fdfind"
cd ~/all_wsl/
echo "$(ls)"
echo "done"
echo "the sh extensions are $(fd -esh)"
compgen -c > ~/all_commands
