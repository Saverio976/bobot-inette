echo "install source folder to /opt"
cd /opt/
sudo rm -rf botbot-inette
sudo git clone "https://github.com/Saverio976/bobot-inette.git" botbot-inette
cd botbot-inette
python3 -m pip install requirements.txt || \
    pip install -r requirements.txt || \
    py -3 -m pip install -r requirements.txt

echo ""
echo "install of external dependencies"
if command -v apt &>/dev/null
then
    sudo apt install python-tk
    sudo apt install portaudio
    sudo apt install ffmpeg
elif command -v pacman &>/dev/null
then
    sudo pacman -S tk
    sudo pacman -S portaudio
    sudo pacman -S ffmpeg
fi

echo ""
echo "You can put botbot-inette to systemd service"
echo "Do you want to do it ? [y/n] > "
read CHOICE
if [[ "$CHOICE" == "y" ]]; then
    sudo cp ./botbot-inette.service /etc/systemd/system/

    systemctl enable --now botbot-inette.service
fi
