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
            elif e.args[0]=="ValueOutOfRange":
                i-=1
                print("Значение вне диапазона, пожалуйста повторите ввод!")                 
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

def ForTask2(value, out):
    try:
        values=eval(value)
        for i in range(1,len(values),2):
            value=values[i]
            last=i-1
            values[i]=values[last]
            values[last]=value
    except:
        raise Exception("StrFormatIsNotValid")

    return out.format(values)

def ForTask3(value, out):
    if value<0 or value>12:
        raise Exception("ValueOutOfRange")

    # Реализация через list
    '''values = ["зима","весна","лето","осень"]
    if (value>=1 and value<=2) or value==12:
        return out.format(values[0])
    elif value>=3 and value<=5:
        return out.format(values[1])
    elif value>=6 and value<=8:
        return out.format(values[2])
    elif value>=9 and value<=11:
        return out.format(values[3])
    else:
        raise Exception("StrFormatIsNotValid")'''

    # Реализация через dict, для экономии ресурсов нужно объявлять на глобальном уровне
    values = dict()
    values[12]="зима"
    for i in range(1,3):
        values[i]="зима"
    for i in range(3,6):
        values[i]="весна"
    for i in range(6,9):
        values[i]="лето"
    for i in range(9,12):
        values[i]="осень"
    return out.format(values[value])        

def ForTask4(value, out):
    values=value.split(" ")
    i=1
    for word in values:
        if word=="":
            continue
        print("#{0} {1}".format(i,word[0:10]))
        i+=1

    return None

def ForTask5(value, out):
    if value<0:
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
#tasks.append(({"def":ForTask1}))
#tasks.append(({"in":"Введите список, например: [1,2,4,6,3] : ", "out":"Результат = {0}", "def":ForTask2, "type": str}))
#tasks.append(({"in":"Введите номер месяца: ", "out":"Время года = {0}", "def":ForTask3, "type": int}))
tasks.append(({"in":"Введите несколько слов: ", "def":ForTask4, "type": str}))
#tasks.append(({"in":"Введите натуральное число (новый элемент рейтинга): ", "out":"Результат = {0}", "def":ForTask5, "type": int}))


# Основной цикл
while True:
    # Основная функция
    main(tasks)
    if 'y' != input("Введите 'y', чтобы повторить, а для выхода нажмите Enter: "):
        break

print("Завершение программы")
