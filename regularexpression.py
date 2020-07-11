import re

cadena = "Dxs*"

if re.search('(^[&A-Z]+[-_a-z]{2,}\*?$){1,}', cadena):
    print("aceptada")
else:
    print("rechazada")



