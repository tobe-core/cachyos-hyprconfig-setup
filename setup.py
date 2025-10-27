import os

def setup(backup):
    if backup:
        os.system("cp -r .config .config.bak")
    
   os.system("git clone https://github.com/tobe-core/cachyos-hyprconfig.git cachyos-hyprconfig && cp -r cachyos-hyprconfig/* .config/ && rm .config/README.md")
    
    if not os.path.exists("Documentos/code/PyWall"):
        os.system("git clone https://github.com/tobe-core/PyWall.git Documentos/code/PyWall && rm Documentos/code/PyWall/README.md")
    
    os.system("rm -rf cachyos-hyprconfig")

    exit()

print("Want to do a backup?")
user = input("(y, n) > ")

if user == "y":
    setup(True)
elif user == "n":
    setup(False)
else:
    exit()