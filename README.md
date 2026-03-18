This is intended to live on a server or some other machine that is on and you can access remotely while you are playing to allow you to trigger a script that will log you in. Personally I use Home Assistant to control this automation so that I can use watch/phone/voice to trigger the log-in script.
This machine needs to be on the same network as your spice PC (can be through vpn) or you need to expose your spice PC IP as public (not recommended)

## Installation

Download Repository onto server machine.

Edit custom_componenets/spice/default.ini with your card, pin, side, and ip address + password of your host (pc running spice)
note: need -iidxpoke and -spiceapi enabled on host

if you do not know the ip address and password of your host it is the same you use for spice companion app, default password is usually changeme.

## Usage

on Unix (Linux/MacOS) you can simply run the shell scripts

on Windows you can run `python custom_componenets/spice/card_in_single.py --config custom_componenets/spice/default.ini` for single or `python custom_componenets/spice/card_in_both.py --config custom_componenets/spice/default.ini`

Feel free to automate/trigger this however you like

## Credits

all credits go to the spice team for creating the spice API
