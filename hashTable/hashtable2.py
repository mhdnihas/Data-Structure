class Hashtable:
    def __init__(self,size):
        self.size=size
        self.hashtable=[None]*self.size
    def hash_function(self,key):
        return key%self.size

    def insert(self,key,value):

        index=self.hash_function(key)
        if self.hashtable[index]==None:
            self.hashtable[index]=[(key,value)]
        else:
            self.hashtable[index].append((key,value))

    def get(self,key):
        index=self.hash_function(key)
        if self.hashtable[index] is None:
            return None
        for i,(k,v) in enumerate(self.hashtable[index]):
            if k==key:
                return v
        return None


obj=Hashtable(10)
obj.insert(3,"nihas")
obj.insert(13,"shalik")
obj.insert(4,"Ali")
obj.insert(11,"vayshnav")
obj.insert(14,"Shabeer")
for i in range(obj.size):
    print(f"index{i}: {obj.hashtable[i]}")
n=int(input("Enter a key:"))

print("value is:",obj.get(n))

