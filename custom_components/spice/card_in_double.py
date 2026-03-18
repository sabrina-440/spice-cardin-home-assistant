#!/usr/bin/env python3
from pathlib import Path
import spiceapi
from spiceapi import card_insert
import argparse
from configparser import RawConfigParser
import time

def connect_spice(host, port, password):
    return spiceapi.Connection(host, port, password)

def main():

    #  get config from default.ini
    parser = argparse.ArgumentParser(description='spice')
    parser.add_argument("--config", type=str, default='default.ini')
    args = parser.parse_args()
    script_dir = Path(__file__).resolve().parent
    config_path = (script_dir / args.config).resolve()    
    config = RawConfigParser()
    config.optionxform = lambda option: option

    config.read(args.config)
    spice_host = config.get('spice', 'Host')
    spice_port = config.getint('spice', 'Port')
    spice_pass = config.get('spice', 'Password', fallback='')
    player2    = config.get('cards', 'card2')
    player1    = config.get('cards', 'card')
    side       = int(config.get('cards', 'P'))
    pin        = config.get('cards', 'pin')
    pin2       = config.get('cards', 'pin2')
    # connect to spice

    print(f'Connect to SpiceAPI... host: {spice_host}, port: {spice_port}')
    try:
        con = connect_spice(spice_host, spice_port, spice_pass)
    except Exception:
        print("connection failed")
    
    card_insert(con, side, player1)
    card_insert(con, (1 if side == 0 else 0), player2)
    time.sleep(7)
    spiceapi.keypads_write(con,(1 if side == 0 else 0),pin2)
    time.sleep(1)
    spiceapi.keypads_write(con,side,pin)

if __name__ == "__main__":
    main()
