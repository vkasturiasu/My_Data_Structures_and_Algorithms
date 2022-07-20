class Tree:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_children(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while(p):
            level += 1
            p = p.parent
        return level



    def print(self,start):
        #print(self.get_level())
        if start ==0:
            print("|__" + self.data)

        elif start==1:
            prefix = " "*2*self.get_level()
            print(prefix + "|__"+self.data)
        for i in self.children:
            start = 1
            i.print(start)


if __name__ == "__main__":
    a = Tree("a")
    b = Tree("b")
    c = Tree("c")
    d = Tree("d")
    e = Tree("e")
    f = Tree("f")
    g = Tree("g")
    h = Tree("h")
    i = Tree("i")
    j = Tree("j")
    k = Tree("k")
    l = Tree("l")
    m = Tree("m")
    n = Tree("n")
    o = Tree("o")
    d.add_children(f)
    d.add_children(g)
    e.add_children(h)
    e.add_children(i)
    e.add_children(j)
    k.add_children(m)
    l.add_children(o)
    l.add_children(n)
    b.add_children(d)
    b.add_children(e)
    c.add_children(k)
    c.add_children(l)
    a.add_children(b)
    a.add_children(c)
    #a.print()
    b.print(start =0)




