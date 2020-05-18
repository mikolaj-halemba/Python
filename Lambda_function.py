text_list = ['x','xxx','xxxxx','xxxxxxx','']
f = lambda x: len(x)

print(list(map(f,text_list)))
print(list(map(lambda s: len(s),text_list)))
