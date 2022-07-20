
#%%
##
class HashTable:
    def __init__(self):
        self.hash = [[] for i in range(10)]

    def gethash(self, key):
        total =0
        for i in key:
            total += ord(i)
        return total%10

    def __getitem__(self,key):
        h = self.gethash(key)
        for index, val in enumerate(self.hash(h)):
            if val[0]==key: 
                return self.hash[h][index]
        return "Not found"

    def __setitem__(self,key, value):
        h = self.gethash(key)
        found = False
        for index, val in enumerate(self.hash[h]):
            if len(val) == 2 and val[0] == key:
                self.hash[h][index] = value
                found = True
                break
            if found == False:
                self.hash[h].append((key,value))





#%%
tt = HashTable()
tt['apple'] = 45
tt['apple']


#%%
c= 222
print(c)


#%%

