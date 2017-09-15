#!/usr/bin/env python3
# -*- mode: python; coding: utf-8-unix -*-

from Crypto.Cipher import AES
import MiyaguchiPreneel

from builtins import bytes

def _enc_aes(k,v):
    mode = AES.MODE_ECB
    enc  = AES.new(k, mode)
    result = enc.encrypt(v)
    return result

def _pad_zero(v,l):
    tmp = v + bytes([0 for i in range(l)])
    return tmp[0:l-1]

def _ident(k):
    return k

_hlen = 128
_IV = bytes([0 for i in range(_hlen//8)])

def comp(text):
    aes_mp = MiyaguchiPreneel.compressor(_enc_aes, _ident, _pad_zero, _hlen)
    result = aes_mp.comp(_IV, text)
    return result

# EOF
