echo "install source file to /opt"

cd /opt/
sudo git clone "https://github.com/Saverio976/bobot-inette.git" botbot-inette
cd botbot-inette

echo "You can put botbot-inette to systemd service"
echo "Do you want to do it ? [y/n] > "
read CHOICE

if [[ "$CHOICE" == "y" ]]; then
    sudo cp ./botbot-inette.service /etc/systemd/system/

    systemctl enable --now botbot-inette.service
fi
