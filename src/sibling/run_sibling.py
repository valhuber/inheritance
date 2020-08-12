import src.inheritance_pkg.sub as sub  # works PyC, FAILS vsc in sub.py

print("running from sibling of target code, ala https://github.com/valhuber/fab-quickstart")
my_sub = sub.Sub()
