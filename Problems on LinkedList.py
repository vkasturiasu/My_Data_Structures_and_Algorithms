class HashTable:
    def __init__(self):
        self.max = 10
        self.Hash = [[] for i in range(self.max)]

    def getHash(self,key):

        asky = hash(key)
        return asky%10

    def __setitem__(self,key, value):  #To handle collitions- Chaining- Inplace of value, store tuple
        asky = self.getHash(key)
        for index, val in enumerate(self.Hash[asky]):
            found = False
            if len(val)==2 and val[0]==key:
                self.Hash[index][val] = (key, value)

            self.Hash[asky].append((key, value))

        self.Hash[asky] = value
        print(self.Hash)

    def __getitem__(self, key):            #To handle collitions
        asky = self.getHash(key)
        if self.Hash[asky] == []:
            return "Empty"
        else:
            return self.Hash[asky]

if __name__ == "__main__":
    trying = HashTable()
    print(trying.getHash("apple"))
    print(trying.getHash("pplea"))

    trying["apple"]=25
    trying["pplea"]=65
    print(trying)
    print(trying["orange"])



