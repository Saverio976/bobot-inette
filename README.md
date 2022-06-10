# botbot-inette

## requirements

### use the installation script

```bash
git clone https://github.com/Saverio976/bobot-inette.git botbot-inette
cd botbot-inette
./install.sh
```

or

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/Saverio976/bobot-inette/main/install.sh)"
```

### manualy

```
git clone https://github.com/Saverio976/bobot-inette.git botbot-inette
cd botbot-inette
```

1. you need to install tkinter if you are on linux

- arch: pacman -S tk
- debian: apt install python-tk

2. install python pip packages

pip install -r requirements.txt

or

python3 -m pip install -r requirements.txt

3. install PortAudio if you are on linux

- arch: pacman -S portaudio
- debian: apt install portaudio

4. install ffmpeg

- arch: pacman -S ffmpeg
- debian: pacman -S ffmpeg

## start

python3 main.py -h

or

./main.py -h

## what can you do

1. open

open a input box for you to specify which program you want to launch

2. play

open a input box to ask for music name and open the first result in youtube

3. go to

open a input box to ask what application you want to switch to
