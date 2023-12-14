class TrieNode:
    def __init__(self):
        self.child={}
        self.end=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for chr in word:
            if chr not in node.child:
                node.child[chr]=TrieNode()
            node=node.child[chr]
        node.end=True
    def searching(self,word):
        node=self.root
        for chr in word:
            if chr not in node.child:
                return False
            node=node.child[chr]
        return node.end

    def prefix_search(self,prefix):
        res=[]
        node=self.root
        for char in prefix:
            if char not in node.child:
                return res
            node=node.child[char]
        self.prefix_helper(node,prefix,res)
        return res
    def prefix_helper(self,node,prefix,res):
        if node.end:
            res.append(prefix)
        for char,child in node.child.items():
            self.prefix_helper(child,prefix+char,res)



trie=Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("muhammednihas")
trie.insert("muhammedAli")
trie.insert("muhammed")
trie.insert("muhammedRafi")
print(trie.searching("app"))
print(trie.prefix_search("app"))
print(trie.prefix_search("muhammed"))
