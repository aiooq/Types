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
                    type_value=tuple[i]["type"]
                    if type(type_value)==type:
                        type_value={type_value}
                    
                    result = False
                    for item in type_value:
                        try:
                            if item == str:
                                try:
                                    float(value)
                                    continue
                                except ValueError:
                                    if value.isnumeric():
                                        continue

                            elif item == int:
                                if not value.isnumeric():
                                    continue
                            else:
                                value=item(value)
                            result = True
                            break
                        except:
                            continue

                    if not result:
                        raise Exception()
                except:
                    print("Некорректное значение, ожидается {0}, пожалуйста повторите ввод!".format(tuple[i]["type"]))
                    continue
        elif "out" in tuple[i]:
            value = tuple[i]["out"]

        try:
            if "def" in tuple[i]:
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

# Функции ниже относится к задаче № 6
goods = list()
def ForTask6_1(value, out):
    global goods
    goods.append((len(goods)+1,{"название":value}))

def ForTask6_DictSet(name,value):
    global goods
    total=len(goods)
    goods[total-1][1][name]=value

def ForTask6_2(value, out):
    ForTask6_DictSet("цена",value)

def ForTask6_3(value, out):
    ForTask6_DictSet("количество",value)

def ForTask6_4(value, out):
    ForTask6_DictSet("ед.изм.",value)
    global goods
    return out.format(goods[len(goods)-1])

def ForTask6_5(value, out):
    if value != 'y' and value != 'yes':
        return ForTask6_Result()

    global tasks
    global task_6
    tasks.append(task_6)

def ForTask6_Result():
    values = dict()
    for i in range(len(goods)):
        for key, value in goods[i][1].items():
            if not key in values:
                values[key] = set()
            values[key].add(value)

    print(values)

# Конфигурируем программу добавляя задачи в список
# В каждой задаче настраиваем ввод, вывод, исполняющую функцию и тип ожидаемых данных от пользователя
# Последовательноть выволнения задач будет в соответствии со списком tasks 
# Если необходимо, то список можно сортировать, так как номера задач весьма условны
# Сортировка внутри кортежа (одной задачи), недопустима!

tasks = list()
tasks.append(({"def":ForTask1}))
tasks.append(({"in":"Введите список, например: [1,2,4,6,3] : ", "out":"Результат = {0}", "def":ForTask2, "type": str}))
tasks.append(({"in":"Введите номер месяца: ", "out":"Время года = {0}", "def":ForTask3, "type": int}))
tasks.append(({"in":"Введите несколько слов: ", "def":ForTask4, "type": str}))
tasks.append(({"in":"Введите натуральное число (новый элемент рейтинга): ", "out":"Результат = {0}", "def":ForTask5, "type": int}))
task_6=(
    ({"out":"Добавление товара в программу..."}),
    ({"in":"Введите название: ", "def":ForTask6_1, "type": str}),
    ({"in":"Введите цену: ", "def":ForTask6_2, "type": {int,float}}),
    ({"in":"Введите количество:", "def":ForTask6_3, "type": {int,float}}),
    ({"in":"Введите eдицину измерения: ", "out":"Товар добавлен: {0}", "def":ForTask6_4, "type": str}),
    ({"in":"Введите 'yes' или 'y', чтобы продолжить добавление товаров, а для аналитики нажмите Enter: ", "def":ForTask6_5, "type": str}))
tasks.append(task_6)    

# Основной цикл
while True:
    # Основная функция
    main(tasks)
    value = input("Введите 'yes' или 'y', чтобы повторить программу, а для выхода нажмите Enter: ")
    if value != 'y' and value != 'yes':
        break

print("Завершение программы")
