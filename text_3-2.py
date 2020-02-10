a_list = [".", ")", ",", "?", "»", "—", "«", "!", "(", "-", ";", ":"]

with open("text_1.txt", "r") as f:
    old_abc = f.read()

new_abc = old_abc.split()
print(new_abc)

# сформировать list со словами (split)
