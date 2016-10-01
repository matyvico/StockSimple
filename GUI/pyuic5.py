from subprocess import call
import os

print("Conversión recursiva de todos los archivos con extensión *.ui utilizando pyuic5")
for file in os.listdir("./"):
    if file.endswith(".ui"):
        call(["pyuic5" , "-x", file, "-o", os.path.splitext(file)[0] + ".py"])
call(["ls", "-l"])
