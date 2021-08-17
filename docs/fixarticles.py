import os
import string

prefix = """---
hide:
  - navigation
---

"""

files = os.listdir(os.getcwd())
files = [x for x in files if x.endswith(".md")]

for fn in files:
    with open(fn) as f:
        s = f.read()
        header = s.split("\n")[0].strip()
        header = header.lower()
        header = header.replace("# ","")
        header = header.replace(" ", "-")
        header = ''.join([x for x in header if x in string.ascii_lowercase or x == "-"])
        header = header.strip()
        final_name = header + ".md"

    with open(f"new/{final_name}", "w") as f:
        f.write(prefix + s)



    
