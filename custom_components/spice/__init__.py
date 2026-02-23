#!/usr/bin/env python3

import spiceapi
from spiceapi import card_insert
import argparse
from configparser import RawConfigParser


#### helper functions ####

def connect_spice(host, port, password):
    return spiceapi.Connection(host, port, password)

def p1Card():

    #  get config from default.ini
    parser = argparse.ArgumentParser(description='spice')
    parser.add_argument("--config", type=str, default='default.ini')
    args = parser.parse_args()
    
    config = RawConfigParser()
    config.optionxform = lambda option: option

    config.read(args.config)
    spice_host = config.get('spice', 'Host')
    spice_port = config.getint('spice', 'Port')
    spice_pass = config.get('spice', 'Password', fallback='')
    player1    = config.get('cards', 'PersonA')

    # connect to spice

    print(f'Connect to SpiceAPI... host: {spice_host}, port: {spice_port}')
    try:
        con = connect_spice(spice_host, spice_port, spice_pass)
    except Exception:
        print("Sconnection failed")
    
    card_insert(con, 0, player1)

def p2Card():

    #  get config from default.ini
    parser = argparse.ArgumentParser(description='spice')
    parser.add_argument("--config", type=str, default='default.ini')
    args = parser.parse_args()
    
    config = RawConfigParser()
    config.optionxform = lambda option: option

    config.read(args.config)
    spice_host = config.get('spice', 'Host')
    spice_port = config.getint('spice', 'Port')
    spice_pass = config.get('spice', 'Password', fallback='')
    player2    = config.get('cards', 'PersonB')

    # connect to spice

    print(f'Connect to SpiceAPI... host: {spice_host}, port: {spice_port}')
    try:
        con = connect_spice(spice_host, spice_port, spice_pass)
    except Exception:
        print("Sconnection failed")
    
    card_insert(con, 1, player2)

###########

DOMAIN = "spice"

async def async_setup(hass, config):
    async def handle_p1_cardin(call): 
        p1Card()
    async def handle_p2_cardin(call): 
        p2Card()
    async def handle_both_cardin(call): 
        p1Card()
        p2Card()

    hass.services.async_register(
        DOMAIN,
        "P1CardIn",
        handle_p1_cardin
    )

    hass.services.async_register(
        DOMAIN,
        "P2CardIn",
        handle_p2_cardin
    )

    hass.services.async_register(
        DOMAIN,
        "MultiplayerCardIn",
        handle_both_cardin
    )

    return True





