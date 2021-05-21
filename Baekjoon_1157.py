import collections
from typing import Text

S = input().upper()
S = list(S)
counts = collections.Counter(S)
TEST = list(counts.values())

if TEST.count(max(TEST)) > 1:
     print('?')
else:
     print(counts.most_common(1)[0][0])