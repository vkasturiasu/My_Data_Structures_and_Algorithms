class Trees:
    def __init__(self,data):
        self.data = data
        self.children =[]
        self.parent = None


    def add_children(self,child):
        child.parent = self
        self.children.append(child)


    def print(self):
        for tr in self.children:
            print(tr.children)




if __name__ =='__main__':
    flipkart = Trees("Electronics")
    cell = Trees("cell")
    cell.add_children(Trees("Nokia"))
    cell.add_children(Trees("MI"))
    TV = Trees(Trees("TV"))
    TV.add_children(Trees("samsung"))
    TV.add_children(Trees("LG"))
    Laptop = Trees(Trees("Laptops"))
    Laptop.add_children(Trees("Dell"))
    Laptop.add_children(Trees("HP"))
    flipkart.add_children(TV)
    flipkart.add_children(Laptop)
    flipkart.print()

