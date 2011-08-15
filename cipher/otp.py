""" One Time Pad Module
"""
import codings
from functools import partial as curry
#XXX: NOTE THAT THIS IS STILL NOT FULLY TESTED

## One Time Pad Translation Functions ########################################

def mod(x,y, direction='decode'):
    if x is None or y is None:
        return None
    if direction == 'decode':
        return (x-y) % 26
    else:
        return (x+y) % 26

def xor(x,y, *args, **kwargs):
    if x is None or y is None:
        return None
    return x^y

## Encode / Decode ###########################################################

def encode(message, pad, otp_func):
    otp_func = curry(otp_func, direction='encode')
    return map(otp_func, message, pad)

def decode(message, pad, otp_func):
    otp_func = curry(otp_func, direction='decode')
    return map(otp_func, message, pad)
