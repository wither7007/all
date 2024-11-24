import re

from pydantic import EnumMemberError

ph = "Airlines and airports including MSP swiftly began repealing their requirements that passengers wear face coverings."
phs = re.split(r"\s", ph)
print(phs)

for i in enumerate(phs):
    print(i)

for s in dir():
    if not s.startswith("_"):
        print(f"{s} {type(s)}")

sf = filter(lambda sc: not sc.startswith("_"), m)
print(list(sf))

sq = lambda x: x * x
import pandas as pd

df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=["First", "Second", "Third"])
df["Forth"] = df.apply(lambda row: row["First"] * row["Second"] * row["Third"], axis=1)
