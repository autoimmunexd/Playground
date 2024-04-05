printf "i3\ndmenu\nterminal\nfirefox\nnano\n"
read -p "select one program :"  program
case $program in
i3)
echo 'you selected i3'
::

dmenu)
	echo 'you selected dmenu'
::

nano)
echo 'you selected nano'
::

terminal)
echo 'you selected terminal'
::
esac

i3 -
windows + enter = new window
windows + 1 - 9 = change to workspace
windows + shift + q = close window
windows + arrow left, right, up, down = change focus to that window
windows + shift + r = reload i3 configuration
dmenu -
windows + d = type in program to launch then press enter
windows + shift + # of workspace to move the current working window to the workspace.

nano -
^ = windows button + modifier
m = alt

termina(bash) -
ctrl +a = go to front of line
ctrl +e = go to end of line

firefox -
ctrl + t = new tab
ctrl + w = delete tab
ctrl + tab = switch between tabs
ctrl + l = focus URL bar
