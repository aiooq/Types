def main(tuple):
    i=0
    while len(tuple)>i:
        if not isinstance(tuple[i], dict):
            main(tuple[i])
            i+=1
            continue

        if not "in" in tuple[i]:
            i+=1
            continue
        
        out = None
        if "out" in tuple[i]:
            out = tuple[i]["out"]

        value = input(tuple[i]["in"])

        if "type" in tuple[i]:
            try:
                if tuple[i]["type"] == str and value.isdigit():
                    raise Exception()
                elif tuple[i]["type"] == float and value.isdecimal():
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
            continue
        finally:
            i+=1

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
tasks.append(({"in":"Введите натуральное число (новый элемент рейтинга): ", "out":"Результат = {0}", "def":ForTask5, "type": int})) 

# Основной цикл
while True:
    # Основная функция
    main(tasks)
    if 'y' != input("Введите 'y', чтобы повторить, а для выхода нажмите Enter: "):
        break

print("Завершение программы")
