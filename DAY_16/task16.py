import math
  
# Initialising hex string
h = "38006F45291200" 
h_size = len(h) * 4
  
  
# Code to convert hex to binary
#res = "{0:08b}".format(int(ini_string, 16))
h = ( bin(int(h, 16))[2:] ).zfill(h_size)
  
# Print the resultant string
print ("Resultant string", str(h))

