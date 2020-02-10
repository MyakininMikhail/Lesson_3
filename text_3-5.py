with open("text_1.txt", "r") as f:
    input_list = f.read()

input_list1 = input_list.rsplit(" ")
input_list2 = dict()

for key in input_list1:
    if not key in input_list2:
        input_list2[key] = 1
    else:
        input_list2[key] += 1

input_list3 = list(input_list2.items())
input_list3.sort(key=lambda i: i[1], reverse = True)
input_list4 = input_list3 [0:5]

for i in input_list4:
    print(i[0], ":", i[1])

print("Количество разных слов :", len(input_list3))

# вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set)