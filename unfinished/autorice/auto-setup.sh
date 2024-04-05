#download balena etcher
#download alpine iso
#boot from usb
#login as root
#type setup-alpine
#walk through installer and enable community repos (c) option
#boot into new installation
#login
#git clone script
#chmod+x script
#./auto-setup.sh

echo "Installing AutoAlpine :D!"

apk update

setup-xorg-base

apk add font-terminus

apk add dbus

dbus-uuidgen > /var/lib/dbus/machine-id

rc-update add dbus

apk add xinit

apk add i3wm i3status dmenu xfce4-terminal thunar

apk add bash

#update /etc/passwd with bash instead of ash

apk add pulseaudio pulseaudio-alsa

apk add alsa-plugins-pulse

apk add pulseaudio-bluez

adduser $USER input
adduser $USER video
adduser $USER audio

#COPY ALL dot files and profiles

cp -r $PWD/.bashrc /home/$USER
cp -r $PWD/.xinitrc /home/$USER
cp -r #PWD/motd /etc/motd
cp -r #PWD/issue /etc/issue
cp -r $PWD/.config /home/$USER
cp -r $PWD/.xinitrc /home/$USER

apk add neofetch

apk add lolcat

apk add picom

apk add feh

#setup feh background
feh --bg-scale ~/auto/images/pillars.jpg

#change /etc/passwd to change ash to bash for root and $USER


#vimix cursors
#echo "Cloning vimix cursors and installing..."
#git clone https://github.com/vinceliuice/Vimix-cursors.git
#cd Vimix-cursors
#./install.sh

#papirus icons

#install flatpak
#apk add flatpak

#install librewolf through flatpak
#create symlink for dmenu
#ln -s /var/lib/flatpak/exports/bin/io.gitlab.librew
#olf-community  /usr/bin/librewolf

#reboot
echo rebooting!
#reboot
