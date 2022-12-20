
a=0
def asd():
    global a

    def aas():
        global a
        b=a
        a=b+5
    aas()

asd()
print(a)