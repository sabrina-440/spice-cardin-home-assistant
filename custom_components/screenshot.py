#!/usr/bin/env python3
from pathlib import Path
import spiceapi
import argparse
from configparser import RawConfigParser

def connect_spice(host, port, password):
    return spiceapi.Connection(host, port, password)

def main():
    #  get config from default.ini
    parser = argparse.ArgumentParser(description='spice')
    parser.add_argument("--config", type=str, default='default.ini')
    parser.add_argument("--player", type=int, required=True)
    args = parser.parse_args()
    
    script_dir = Path(__file__).resolve().parent
    config_path = (script_dir / args.config).resolve()    
    config = RawConfigParser()
    config.optionxform = lambda option: option
    config.read(config_path)
    
    spice_host = config.get('spice', 'Host')
    spice_port = config.getint('spice', 'Port')
    spice_pass = config.get('spice', 'Password', fallback='changeme')

    # connect to spice
    print(f'Connect to SpiceAPI... host: {spice_host}, port: {spice_port}')
    try:
        con = connect_spice(spice_host, spice_port, spice_pass)
    except Exception:
        print("connection failed")
        return

    spiceapi.keypads_write(con, args.player, "9")

if __name__ == "__main__":
    main()
