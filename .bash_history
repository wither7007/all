cat .bash_history |sort | uniq > .bash_history
h3
nn 1
ll
!
fc ld | rg  "\."
ls ~ > $(pwd)t
ls ~ > $(pwd)/t
lt
rm t
sudo lshw | less
h3
d
ld
ld | rg -v 'yarn'
ld | rg  '^yarn'
ld | rg  '^\.yarn'
ld | rg  '^a'
rgh
als
rg -hel
alias rg
apps | v --
apps | v -
ripgrep
source .bash_aliases 
rgh
alias rgh
man rg
alias rg
wi rg
ls | rg 'a'
ls | rg -v 'a'
ls | rg  '^a'
ld | rg  '^a'
ld
ld -l
fd -td
fd -d 1 -td
nn 2
nn 22
nn 220
se 'declare'
fc declare -f nn
ech declare -f nn
echo 
echo ~313
echo declare -f nn
fc -l
v 
exit
h3
his
ld
cd wsl2
lt
cd all_wsl/
gst
git diff
lt
v x.py
git diff
u
sc install.sh 
lt
fd d 1 -esh
fd -d 1 -esh
fd -d 1 -esh | xargs cat
fd -d 1 -esh | xargs cat {}
fd -d 1 -esh | xargs echo
fd -d 1 -esh | xargs printf "%s.\n"
fd -d 1 -esh | xargs printf "%s.\n\n"
fd -d 1 -esh | xargs printf "file is \%s.\n\n"
fd -d 1 -esh | xargs printf "file is %s.\n\n"
fd -d 1 -esh | xargs printf "file is %s.\n"
fd -d 1 -esh | xargs printf "cat %s.\n"
fd -d 1 -esh | xargs printf "cat %s.\n" > jj.sh
sc jj.sh 
v jj.sh 
fd -d 1 -esh | xargs printf "cat %s\n" > jj.sh
sc jj.sh 
fd -d 1 -esh | xargs echo; printf "cat %s\n"
fd -d 1 -esh | xargs printf "cat %s.\n"
fd -d 1 -esh | xargs printf "cat %s\n"
lt
ld
rm Untitled-0 
lt
rm scan.py xx k hx
lt
his
fd -esh
ls | xargs
ls | xargs printf '\n'
ls | xargs printf '%s\n'
ls | rg 'a' | xargs printf '%s\n'
ls | rg 'a' | xargs printf cat '%s\n'
h3
ls | rg 'a' | xargs printf  'cat %s\n'
xargs find . -name

echo "f1 f2 f3"|xargs echo
echo "f1 f2 f3"|xargs 
cd wsl2/
lt
for i in {1..5}; do touch $1; done
for i in {1..5}; do touch $i; done
lt
for i in {1..5}; do touch $ixx; done
for i in {1..5}; do touch $i xx; done
lt
find .
find . -name 
find . -name '*'
find . -name '*' | xargs
find . -name '*' -print0| xargs
find . -name '*' -print0| xargs -0
find . -name '*' -print0| xargs -0 cat
find . -name '*' -print0| xargs -0 -p cat
find . -name '*' -print0| xargs -0 -p cat #! xargs preview
fd -d 1
fd -d 1 tf
fd -d 1 -tf
lt
exit
tmux
exit
lt
sc install.sh 
cd wsl2/
lt
fd -d 1
fd -d 1 -tf
h3
ls
fd -d 1 -tf | xargs -p rm
lt
fd -d 1 -tf | xargs  rm
lt
cd all_wsl/
gst

for s in server1 server2 server3; do     echo "Server ${s}: $(ssh vivek@${s} uptime)"; done
his
for s in server1 server2 server3; do     echo "Server ${s}: "; done
gst
git diff
v x.py
git diff
v x.py 
git diff
v x.py 
git diff
v x.py 
git diff
lt
v jim
git diff
lt
v jim
git diff
cd
date >> daily_log.txt 2>&1
v daily_log.txt 
dater >> daily_log.txt 2>&1
v daily_log.txt 
cd wsl
ld
cd wsl2/
ld
u
ld
rm -rf all_wsl/
ld
ls
fd -td
fd -d 1 -td
cd scripts/
lt
u
fd -esh
cat fc.sh 
fd -esh
v jj.sh
rm jj.sh 
v jj.sh
chmod +x jj.sh 
lt
./jj.sh "jim"
fd -esh | xargs
fd -esh | xargs ./jj.sh 
fd -esh -exec ./jj.sh {}
fd -esh -exec ./jj.sh {} \;
fd -esh -exec echo {} \;
fd -esh -exec echo  \;
fd -esh -exec echo 
fd -esh -exec echo '{}'
fd -esh
fd -esh -exec echo '{}'\;

find . -type f | xargs -I{} echo {} {}
fd -d 1 | xargs -I{} echo {} {}
fd -d 1 | xargs -I{} echo {}
fd -d 1 -esh | xargs -I{} echo {}
fd -d 1 -esh | xargs -I{} echo {}; cat {}
fd -d 1 -esh | xargs  echo {}; cat {}
fd -d 1 -esh | xargs   cat {}
fd -d 1 -esh | xargs   ./jj.sh {}
fd -d 1 -esh | -exec   ./jj.sh {}
fd -d 1 -esh  -x   ./jj.sh {}
fd -d 1 -esh  -x   ./jj.sh 
v jj.sh
fd -d 1 -esh  -x   ./jj.sh 
v jj.sh
fd -d 1 -esh  -x   ./jj.sh 
exit
exit
tmux
exit
ld
cd wsl2/
ld
cd all_wsl
lt
gst
git reset -hard
git reset --hard
gst
git log --oneline 
gst
rm jim
gst
git push
lt
v greek.txt 
lt
gst
git diff
v pss
gst
git diff
git diff | v -
gst
git -m "testing changes"
git commit -m "testing changes"
gst
git commit -m "testing changes"
git add
git add .
gst
git commit -m "testing changes"
gst
git push
lt
fd --changed-within=1hours
sc ~/install.sh 
fd --changed-within=1hours
git diff
gst
git diff --cached
git log --oneline 
lt
v greek.txt 
git diff
gst
git add greek.txt 
gst
rg frumious
lt
git diff
gst
lt
gst
git commit -m "added frumious"
gst
git push
gst
git fetch
gst
lt
git pull
lt
gst
u
se 'tar'
exit
h3
ld
cd wsl2
lt
cd all_wsl/
gst
git fetch
gst
git diff
git pull
exit
v .bashrc 
lt
his
ld
cd wsl2
lt
u
md wsl3
ld
cd wsl2
ld
cd all_wsl/
cp -r ..
u
mv -rv wsl2/all_wsl wsl2/
mv -r wsl2/all_wsl wsl2/
cp -r wsl2/all_wsl wsl2/
cd wsl2/
ld
mv all_wsl/ 
mv all_wsl/ ~/wsl3/
lt
u
ld
cd wsl3/
ld
cd all_wsl/
ld
gst
h3
ld
ls
lt
tocuh nn
touch nn
mv -v nn ~/
lt
gst
u
mv -v all_wsl/ ~/
ld
u
ld
cd all_wsl/
ls
find .
gst
touch nn
gst
rm nn
lt
v ghist
gst
git diff
lt
v hisback 
git diff
git reset --hard
lt
git diff
gst
lt
touch nn
gst
git reset --hard
lt
git clean -f -d
lt
gst
git fetch
gst
git fetch
gst
git fetch
v note/notes 
git diff
git show
git -p
git log -p
git log -p 1
git log -p -1
git log -p -2
git merge
git log -p -2
u
la
la | grep 'it'
v .gitconfig 
ld
rm -rf wsl2 wsl3
lt
ld
cd all_wsl/
h3
git log -p -2
git log -p -3 | v -
alis wi
whereis dos2unix
whereis dos2unixss
u
dos2unix
exit
ld
cd all_wsl/
lt
gst
git fetch
git diff main origin/main
git fetch
git diff main origin/main
v note/notes 
git merge
v note/notes 
gst
git add .
git commit -m "more lines bs"
gst
git push
gst
git pull
gst
git commit -m "more lines bs"
exit
h3
his
ld
cd all_wsl/
lt
u
take win
als
md win || cd win
ld
cd win
curl -s "https://raw.githubusercontent.com/wither7007/all_wsl/main/whis" whis
lt
fc -l
curl -s "https://raw.githubusercontent.com/wither7007/all_wsl/main/whis" >whis
lt
v whis
u
lt
ls *.sh
lt *.sh
sh install.sh 
fd --changed-within=1days
cd all_wsl/
gst
git fetch
gst
git show
u
fd --changed-within=1days
fd -H -I --changed-within=1days
stat .gitconfig 
ld
cd win
lt
v whis
u
ld
cd win
lt
ld
cd all_wsl/
git diff main origin/main
git diff main origin/main | v -
lt
git merge
git diff main origin/main | v -
git log -p
git remote -v
gb
se 'ori.*main'
gb
git show
git show | -
git show | v -

echo "$TERM"
export TERM=xterm-mono
ll
echo "$TERM"
lt
v whis 
git show | v -
h3
echo 'export TERM=xterm-mon' >> ~/.bashrc 
u
fd -d 1 --modified-within=1hours
fd -d 1 --modified-within=1hour
se 'modif'
his
fdh
fd -H -I -d 1 --changed-within=1hours
v .viminfo 
apps| rg 'car'
fd -H -I -d 1 --changed-within=1hours -x cat
fd -H -I -d 1 -tf  --changed-within=1hours -x cat
fd -H -I -d 1 -tf  --changed-within=1hours -x echo
v list.sh
chmod + x list.sh 
chmod +x list.sh 
l
lt
chmod + x list.sh 
fd -H -I -d 1 -tf  --changed-within=1hours -x list.sh
fd -H -I -d 1 -tf  --changed-within=1hours -x ./list.sh
manv 
lt
fda
als
fd -H -I -d 1
fd -H -I -d 1 -tf
fdh
fd -H -I -d 1 -tf | xargs ls -ltr
fd -H -I -d 1 -tf | xargs ls -ltrh
touch vv
fd -H -I -d 1 -tf | xargs ls -ltrh
rm vv
fd -H -I -d 1 -tf | xargs ls -ltrh
lt
lt -a
lt -a | rg -v "^d"
lt -a | rg -v "^d" | rg 'fun'
v fund
f fun 
v fun
sc fun
v fun
sc fun
v fun
manv sd
cat fun
hism
type -a hism
cha(){ echo $1; }
cha
cha 1
cha(){ fdfind -H -I --changed-with $1mins; }
cha 5
cha(){ fdfind -H -I --changed-within $1mins; }
cha 5
cha 50
cha 250
cha 10
v fun
cha 10
v fu
v fun
sc fun
ld
type -a ld
v whis
fday
u
type -a fday
cha 60
lt
sc fun
cha 60
type -a cha
cha 360
cd all_wsl/
gst
u
qqq
1
222
lw
ls
pwd
exit
