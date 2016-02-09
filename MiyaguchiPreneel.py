#!/usr/bin/env python3
# -*- mode: python; coding: utf-8-unix -*-

def _bxor(a,b):
    return bytes(x ^ y for x, y in zip(a, b))

def _comp_step(e, g, h_pre, x_cur):
    h_key = g(h_pre)
    h_enc = e(h_key, x_cur)
    h_cur = _bxor(_bxor(h_enc, x_cur), h_pre)
    return h_cur

class compressor:
    def __init__(self, enc, g, padding, hbits):
        self.encfunc = enc
        self.keyfunc = g
        self.padfunc = padding
        self.hashlen = hbits
        self.blksize = hbits // 8

    def comp(self, IV, in_data):
        l = len(in_data)
        blksize = self.blksize
        nblk = (l + blksize - 1) // blksize
        out_cur = IV
        e = self.encfunc
        g = self.keyfunc
        for i in range(0, nblk-1):
            out_pre = out_cur
            dblk = in_data[i*blksize : (i+1)*blksize]
            if len(dblk) < blksize :
                x_cur = self.padfunc(dblk, blksize)
            else:
                x_cur = dblk
            out_cur = _comp_step(e, g, out_pre, x_cur)
        return out_cur

# EOF
