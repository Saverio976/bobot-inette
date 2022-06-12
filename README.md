# botbot-inette

control you pc with the voice
still work in progress

this will run only on linux, with x11 x server (most disro use it)

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

1. install tkinter

- arch: pacman -S tk
- debian: apt install python-tk

2. install PortAudio

- arch: pacman -S portaudio
- debian: apt install portaudio

3. install xdotool

- arch: pacman -S xdotool
- debian: apt install xdotool

3. install ffmpeg

- arch: pacman -S ffmpeg
- debian: pacman -S ffmpeg

2. install python packages dependences

pip install -r requirements.txt

or

python3 -m pip install -r requirements.txt

## start

python3 main.py -h

or

./main.py -h

## what can you do

1. open (en) / ouvre (fr)

open a input box for you to specify which program you want to launch

2. play (en) / joue (fr)

open a input box to ask for music name and open the first result in youtube

3. go to (en) / va (fr)

open a input box to ask what application you want to switch to

4. quit (en) / quitte (fr)

open a confirm box to kill your old current application

5. talk (en) / parle (fr)

get a chatbot to talk to
