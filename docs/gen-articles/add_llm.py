import os

files = os.listdir(os.getcwd())
files = [x for x in files if x.endswith(".md")]

for fn in files:
    print(f"Working on {fn}")
    with open(fn) as f:
        s = f.read().strip()
    with open(fn, "w") as f:
        f.write(s + "\n\n**Disclaimer**: this article was generated using an LLM")
