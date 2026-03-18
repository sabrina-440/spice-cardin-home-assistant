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
    parser = argparse.ArgumentParser(description='spicecard')
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
    player1    = config.get('cards', 'card')
    side       = int(config.get('cards', 'P'))
    pin        = config.get('cards', 'pin')

    # connect to spice

    print(f'Connect to SpiceAPI... host: {spice_host}, port: {spice_port}')
    try:
        con = connect_spice(spice_host, spice_port, spice_pass)
    except Exception:
        print("connection failed")
    
    card_insert(con, side, player1)
    time.sleep(7) #need to set a delay before inserting pin or game will not be ready
    spiceapi.keypads_write(con,side,pin)
    print('inserted')
    return 1

if __name__ == "__main__":
    main()
