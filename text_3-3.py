with open("text_1.txt", "r") as f:
    old_abc = f.read()

old_abc = (map(lambda x: x.lower(), old_abc))
old_abc = "".join(old_abc)
print(old_abc)

# привести все слова к нижнему регистру (map)
