def count_letters(word):
    hashtable={}
    for i in word:
        if i in hashtable:
            hashtable[i]+=1
        else:
            hashtable[i]=1
    print(f"The word {word} contains:")
    for k,v in hashtable.items():
        print(f"{k} : {v}")

word1="helloworld"
count_letters(word1)