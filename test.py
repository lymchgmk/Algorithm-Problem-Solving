import re


tmp = "$5.72B"
print(re.match(r'[-+]?[$](.+)([BM])', tmp).groups())




