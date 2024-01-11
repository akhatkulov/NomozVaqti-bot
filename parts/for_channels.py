

def set_kanal_1(x):
    with open("data/kanal1.txt",'w+') as f:
        f.write(x)
def get_kanal_1():
    with open("data/kanal1.txt",'r+') as f:
        x = f.read()
        return x
def set_main(x):
    with open("data/main.txt",'w+') as f:
        f.write(x)
def get_main():
    with open("data/main.txt","r+") as f:
        x = f.read()
        return x
def set_kanal_1(x):
    with open("data/kanal2.txt",'w+') as f:
        f.write(x)
def get_kanal_2():
    with open("data/kanal2.txt",'r+') as f:
        x = f.read()
        return x