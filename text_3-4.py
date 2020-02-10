with open("text_1.txt", "r") as f:
    input_list = f.read()

input_list1 = input_list.rsplit(" ")
input_list2 = dict()

for key in input_list1:
    if not key in input_list2:
        input_list2[key] = 1
    else:
        input_list2[key] += 1

print(input_list2)

# получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
