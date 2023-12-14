def maxstring(input):
    seen={}
    for char in input:
        if char in seen:
            seen[char]+=1
        else:
            seen[char]=1
    max_count=max(seen.values())
    for char,count in seen.items():
        if count==max_count:
            return char
st='haiaia'
print("maximum freequency charecter of this ",st," is :",maxstring(st))
st1='apple'
print("maximum freequency charecter of this ",st1," is :",maxstring(st1))
