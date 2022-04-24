from base64 import b64encode

import Crypto.Util.number
from Crypto.Util.number import *


def intro_ascii():
    pb = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    ret = "".join([chr(x) for x in pb])
    print(ret)


def intro_hex():
    pb = bytes.fromhex(
        "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d")
    print(pb)


def intro_base64():
    pb = bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")
    ret = b64encode(pb)
    print(ret)


def intro_convert():
    pb = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
    ret = Crypto.Util.number.long_to_bytes(pb)
    print(ret)


def intro_xorstart():
    pb = "label"
    key = 13
    ret = "crypto{" + "".join(
        [chr(ord(x) ^ key) for x in pb]
    ) + "}"
    print(ret)


def main():
    # intro_ascii()
    # intro_hex()
    # intro_base64()
    # intro_convert()
    intro_xorstart()
    print("Fin")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
