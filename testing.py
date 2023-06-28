class a:
    def __init__(self, num):
        self.num = num

    def one(self, mult):
        print(self.num*mult)



class az:
    b = a(1)
    c = a(2)
    d = a(3)
    e = a(4)
    f = a(5)
    listed = [b,c,d,e,f]

for i in az.listed:
    i.one(2)



