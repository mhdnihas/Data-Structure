
def hash_function(key):
    index=sum(ord(char)%table_size for char in key)
    return index
def insert(key,value):
    index=hash_function(key)
    hash_table[index].append((key,value))

def lookup(key):
    index=hash_function(key)
    for k,v in hash_table[index]:
        if k==key:
            return v
def delete(key):
    index=hash_function(key)
    for i,(k,v) in enumerate(hash_table[index]):
        if k==key:
            del hash_table[index][i]
            break
table_size=10
hash_table=[[] for i in range(0,table_size)]

table_size=10
print("\n\tHash Table\n")

insert("A","Ali")
insert("A","Abay")
insert("M","Muhammed")
insert("N","nihas")
insert("B","basith")
print(hash_table)
print("find the value contains in A in key word:",lookup("N"))

delete("B")
print("\nafter deletion:",hash_table)