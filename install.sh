echo "install source file to /opt"

cd /opt/
sudo git clone "https://github.com/Saverio976/bobot-inette.git" botbot-inette
cd botbot-inette

echo "You can put botbot-inette to systemd service"
echo "Do you want to do it ? [y/n] > "
read CHOICE

if [[ "$CHOICE" == "y" ]]; then
    mkdir $HOME/.config/ -p
    mkdir $HOME/.config/systemd/ -p
    mkdir $HOME/.config/systemd/user/ -p

    mv ./botbot-inette.service $HOME/.config/systemd/user/

    systemctl enable --now botbot-inette.service
fi
