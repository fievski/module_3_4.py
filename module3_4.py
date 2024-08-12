import re

def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i in other_words:
            re.search(root_word, i)
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)



#def my_sum(n, *args, txt="Сумма чисел"):
    #s =0
    #for i in range(len(args)):
        #s += args[i] ** n
    #print(txt + ":", s)


#my_sum(1, 1, 2, 3, 4)
#my_sum(2, 2, 3, 4, 5, txt="Сумма квадратов")



#def info(value, *types, names_author="Sam", **values):
    #print("Тип:", type(values))
    #print("Аргумент:", values)
    #for key, value in values.items():
        #print(key, value)
    #print(types)

#info("Пример типов", 2, 3, 4, name_author="Sam", name ="Samuel", course="Python")


#def summator(txt, *values, type="sum"):
    #s = 0
    #for i in values:
        #s += i
    #return f'{txt}{s} {type}'
#print(summator("Сумма чисел: ", 2, 3, 4, type="summator"))


#def summator(*values):
    #s = 0
    #for i in values:
        #s += i
    #return s
#print(summator(1, 2, 3, 4))


#def test_func(*params):
    #print("Тип:", type(params))
    #print("Аргумент:", params)
#test_func(1, 2, 3, 4)