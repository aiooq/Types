def main(tuple):
    i=0
    while len(tuple)>i:
        if not isinstance(tuple[i], dict):
            main(tuple[i])
            i+=1
            continue

        out = None
        value = None
        if "in" in tuple[i]:    
            if "out" in tuple[i]:
                out = tuple[i]["out"]

            value = input(tuple[i]["in"])

            if "type" in tuple[i]:
                try:
                    if tuple[i]["type"] == str:
                        if value.isdigit():
                            raise Exception()
                    elif tuple[i]["type"] == float:
                        if value.isdecimal():
                            raise Exception()
                    else:
                        value=tuple[i]["type"](value)
                except:
                    print("Некорректное значение, ожидается {0}, пожалуйста повторите ввод!".format(tuple[i]["type"]))
                    continue

        try:
            value = tuple[i]["def"](value,out)
            if value != None:
                print(value)
        except Exception as e:
            if e.args[0]=="PositiveNumber":
                i-=1
                print("Некорректное значение, ожидается положительное число, пожалуйста повторите ввод!")
            elif e.args[0]=="StrIsNotNumeric":
                i-=1
                print("Некорректное значение, ожидается число, пожалуйста повторите ввод!")
            elif e.args[0]=="StrFormatIsNotValid":
                i-=1
                print("Некорректный формат, пожалуйста смотрите пример и повторите ввод!") 
            else:
                print("Ошибка в конфигурации: "+e)               
            continue
        finally:
            i+=1

def ForTask1(value, out):
    values=[
        True,
        int(5),
        float(1.2),
        complex(3.14 - 0j),   
        str("stirng"),
        bytes(25),
        bytearray([25,50]),
        list([1,2,3]),
        tuple((1,2,3)),
        set({3,1,2}),
        frozenset({3,1,2}),
        dict({"key":"value"})]

    types=[
        bool,int,float,complex,str,bytes,bytearray,list,tuple,set,frozenset,dict
    ]

    for i in range(len(values)):
        print("Значение {0}, тип: {1}, соответсвие: {2}".format(
            values[i],
            type(values[i]), 
            isinstance(values[i], types[i])))

    return None

def ForTask5(value, out):
    if(value<0):
        raise Exception("PositiveNumber")
    my_list = [7, 5, 3, 3, 2]
    my_list.append(value)
    my_list.sort(reverse=True)
    return out.format(my_list)

# Конфигурируем программу добавляя задачи в список
# В каждой задаче настраиваем ввод, вывод, исполняющую функцию и тип ожидаемых данных от пользователя
# Последовательноть выволнения задач будет в соответствии со списком tasks 
# Если необходимо, то список можно сортировать, так как номера задач весьма условны
# Сортировка внутри кортежа (одной задачи), недопустима!
tasks = list()
tasks.append(({"def":ForTask1}))
#tasks.append(({"in":"Введите натуральное число (новый элемент рейтинга): ", "out":"Результат = {0}", "def":ForTask5, "type": int}))

# Основной цикл
while True:
    # Основная функция
    main(tasks)
    if 'y' != input("Введите 'y', чтобы повторить, а для выхода нажмите Enter: "):
        break

print("Завершение программы")
