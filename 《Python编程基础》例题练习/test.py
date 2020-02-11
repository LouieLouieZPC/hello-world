from functools import partial
 

 
hex2dec = partial( int, base=16 )
print hex2dec( '0x67' )  # 103
print hex2dec( '67' )  # 103