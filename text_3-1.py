a_list = [".", ")", ",", "?", "»", "—", "«", "!", "(", "-", ";", ":"]

with open("text.txt", "r") as f:
    old_abc = f.read()

for i in range(len(a_list)):
    old_abc = old_abc.replace(a_list[i], "")

new_abc = old_abc
new_abc = new_abc.replace('\n', ' ')
new_abc = new_abc.replace('  ', ' ')

with open("text_1.txt", "w") as f:
    f.write(new_abc)

# методами строк очистить текст от знаков препинания
