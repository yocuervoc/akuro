import re

cadena = "&-d*&-d*"

if re.search('(^[&A-Z]+[-_a-z]{2,}\*?$){1,}', cadena):
    print("Si")
else:
    print("no")
        