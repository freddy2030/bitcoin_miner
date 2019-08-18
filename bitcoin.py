import hashlib, struct, binascii

ver = 1
prev_block = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
mrkl_root =  "0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098"
time = 1231469665
bits = 486604799
nonce = 2573394689

def int2hex(num):
    return struct.pack("<L", num)

def str2hex(string):
    return bytes.fromhex(string)[::-1]



header = int2hex( ver ) +  \
         str2hex( prev_block ) + str2hex( mrkl_root ) + \
         int2hex( time ) + int2hex( bits ) + int2hex( nonce )

header_hash = hashlib.sha256( hashlib.sha256( header ).digest()).digest()

cur_block = header_hash[::-1].hex()

print(cur_block)
# print(dir(cur_block))
tx = "0100000001dbb2a784426fb2d90ed2a55e0ba4c5bcb178e4d86649f533b0d402be0c7e0b95000000006a473044022002cc832c1c624a59f197713b37267392d435afe0207e346d631a8c192a6de76602200a882dc8fbdca761338393da6457580e92b76833d42eae580fce25ce43c377490121022896f495e32ae3bcc71c0215a5fb8f6b4f8f7d35d00b2406caa9c33a9dc4eb28ffffffff02d489086c000000001976a9144c8c7ba9495a1b079003188f0ec4e172be23641088ac60481b00000000001976a9143dcfd69d432f90d2a3d00c69d3096c1672975c7d88ac00000000"
tx_hash = shlib.sha256( hashlib.sha256( bytes.fromhex(tx) ).digest()).digest()[::-1].hex()
