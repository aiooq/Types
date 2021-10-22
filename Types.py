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

# Конфигурируем программу добавляя задачи в список
# В каждой задаче настраиваем ввод, вывод, исполняющую функцию и тип ожидаемых данных от пользователя
# Последовательноть выволнения задач будет в соответствии со списком tasks 
# Если необходимо, то список можно сортировать, так как номера задач весьма условны
# Сортировка внутри кортежа (одной задачи), недопустима!

tasks = list()
'''tasks.append((  {"in":"Введите целое число: ", "def":ForTask1, "type":int}, 
                {"in":"Введите дробное число: ", "def":ForTask1, "type":float},
                {"in":"Введите строку: ", "def":ForTask1, "type":str},
                {"in":"Введите ещё строку: ", "out":" Вы ввели: {0}, {1}, {2}, {3}", "def":ForTask1, "type":str}))

tasks.append(({"in":"Введите время в секундах: ", "out":"Результат в формате времени чч:мм:сс = {0}:{1}:{2}", "def":ForTask2, "type":int}))
tasks.append(({"in":"Введите число n для формулы n + nn + nnn: ", "out":"Результат = {0}", "def":ForTask3, "type":int}))
tasks.append(({"in":"Введите целое положительное число из нескольких цифр: ", "out":"Самая большая цифра в числе = {0}", "def":ForTask4, "type":int}))
tasks.append(({"in":"Введите значения выручки фирмы: ", "def":ForTask5},
            {"in":"Введите значение издержек фирмы: ", "out":"Финансовый результат фирмы = {0}", "def":ForTask5},
            {"in":"Введите численность сотрудников фирмы: ", "out":"Прибыль фирмы в расчете на одного сотрудника = {0:2f}", "def":ForTask5, "type":int}))

tasks.append(({"in":"Введите строку, например: a = 2, b = 3: ", "out":"Ответ: на {0}-й день спортсмен достиг результата — не менее {1} км.", "def":ForTask6, "type":str}))'''   

# Основной цикл
while True:
    one = 'one'
    two = 'two'
    three = 'three'

    print(three)
    print(two)
    print(one)

    # Основная функция
    main(tasks)
    if 'y' != input("Введите 'y', чтобы повторить, а для выхода нажмите Enter: "):
        break

print("Завершение программы")
