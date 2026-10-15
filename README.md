# Tranquillity

What is Tranquillity?

Tranquillity is a project that aims to recreate a personal assistant with GLaDOS AI voice, capable of assisting with any task on a PC.

Inspired by the famous AI from the video game Portal 2, as well as projects already created throughout the Internet.

<img src="https://github.com/user-attachments/assets/1f69f6fd-e8fd-4431-956d-32d97b91bb56" 
        alt="Picture" 
        width="800" 
        height="600" 
        style="display: block; margin: 10" />

***

Features:

* **Personal AI Assistant** with GLaDOS voice synthesis (TTS).
* **Voice Recognition** - French language support with rapid command parsing.
* **Music Control** - Spotify integration (pause, resume, device management).
* **Lighting Control** - Smart light management.
* **Discord Integration** - Send messages to Discord directly from commands.
* **ctOS CLI** - Custom command-line interface created specifically for Tranquillity.
* **Voice-to-Voice LLM** - Direct voice conversation with AI processing.

***

Planned Features:

* Enhanced gesture recognition and commands.
* Extended camera vision capabilities.
* Additional smart home integrations.
* More language support.
* And much more.

***

### For dev :

For Linux or Windows:

```bash
./env/bin/python -m pip install -r requirement.txt
```

For NixOS, devenv is already setup you need just

```bash
devenv init
```
then

```bash
devenv start
```

For other you need to create env.

### For use

For installation you have 2 possibility : Docker Pypi or Github installation
Warning : Github installation use YOUR environement. IA have instruction for do not use rm command but its IA and i posibly use this or other dangerous command
Docker have "secure" environement with no rm command

For Github installation, clone or install zip file and launch with this

```bash
python ctOS.py --init
python ctOS.py --start
```


For Docker Pypi you have this docker : https://hub.docker.com/r/tadomika/tranquillity

```bash
pip install tranquillity
docker pull -f tranquillity:latest
TRANQUILLITY_IMAGE=tranquillity:latest
tranquillity --version
```

or 

```bash
docker build -f docker/Dockerfile -t tranquillity:local .
TRANQUILLITY_IMAGE=tranquillity:local python docker_launcher.py --help

```

The `tranquillity` command from `pyproject.toml` runs `docker_launcher.py` on the host. The Docker image itself runs `ctOS.py` and forwards the arguments supplied to the launcher.

***

Inspiration:

This project wouldn't exist without inspiration and help.
The project is primarily educational, and here are the repositories that helped me:

* https://github.com/dnhkng/GLaDOS

***

I welcome any help!


