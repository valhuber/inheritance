# import src.inheritance_pkg.sub as sub  # works PyC only
# from inheritance_pkg import Sub  #  inheritance_pkg  # .sub as sub  # FAILS
import sub  # works PyC & vsc

print("running local to package")
my_sub = sub.Sub()
