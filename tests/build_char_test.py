#!/usr/bin/env python3

from upacc import character_dict as ch_d


def main():
    test_char_d = ch_d.CharacterDict()

    test_char = test_char_d._build_character(2)

    return isinstance(test_char, ch_d.ch.Character)

if __name__ == "__main__":
    print(main())
