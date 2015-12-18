import hashlib

code = "bgvyzdsv"
def do():
    problem()
    problem2()

def problem():
    i = 0
    while True:
        m = hashlib.md5()
        final_str = code + str(i)
        m.update(final_str.encode("utf-8"))
        if m.hexdigest()[0:5] == "00000":
            break
        i+=1
    print(i)

def problem2():
    i = 0
    while True:
        m = hashlib.md5()
        final_str = code + str(i)
        m.update(final_str.encode("utf-8"))
        if m.hexdigest()[0:6] == "000000":
            break
        i+=1
    print(i)
