# GOODNIGHT
A Google VoiceKit Application to help you do your ritual right before your bedtime.

## Description
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

Define your ritual in bedtime.yaml, and let the application notify you so you
have enough time to complete your ritual. Uses previous days actual time for
next day to adjust your config accordingly

## Getting Started
### Prerequisites

If you own a voicekit, follow these instructions:

https://aiyprojects.withgoogle.com/voice/

### Installation

**Locally:**

There isn't much you can do locally other than run tests. I'd recommend
to create a virtual environment and then install this project requirements

    pip install -r requirements.txt
    pytest # or ptw (for continuous running of tests)

**VoiceKit:**

Use scp to transfer files to your voicekit, or on your voicekit, git pull
this repository.

Then create a soft link from the goodnight.service file to the systemd
folder

    pip3.7 install -r requirements.txt
    sudo ln -s `pwd`/goodnight.service /lib /systemd/system

Then use systemctl commands to start/stop/debug `goodnight.service`

You may have to install Python37 manually:
https://serverfault.com/questions/918335/best-way-to-run-python-3-7-on-ubuntu-16-04-which-comes-with-python-3-5


When you update the .service file, don't forget to run

    sudo systemctl restart goodnight
    sudo systemctl daemon-reload

### Entry point
VoiceKit uses systemctl to start programs. The entrypoint is defined in the service file (goodnight.service)
This script get's run by systemctl automatically.

goodnight.service runs main.py

## FAQs

How to run your script on startup: https://aiyprojects.withgoogle.com/voice/#makers-guide--run-your-app-at-bootup
