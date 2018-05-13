#!/usr/bin/env python3
from upacc import character as ch

def main():
    all_chars = ch.char_d(1, 2)
    players = ch.player_d(all_chars)
    nonplayers = ch.nonplayer_d(all_chars)

    return players, nonplayers

if __name__ == "__main__":
    print(main())
