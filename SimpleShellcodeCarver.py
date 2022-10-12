#!/usr/bin/env python3

with open('shellcode.txt', 'r') as f:

	hex_string = f.read().replace('0x', '').replace('byte[] rsrc = new byte[464] {', '').replace('};', '').replace(',', '') # Raw Shellcode String
	
	hex_encode = hex_string.encode() # Raw Byte String of the shellcode # This is what will help us to carve the raw shellcode data #

#print(hex_string)

#print(hex_encode)

with open('out.bin', 'wb') as out:   	# .bin becauses its a data file # wb for write-byte permission
	
	out.write(hex_encode)
