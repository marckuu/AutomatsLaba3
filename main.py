def countValue(alphabet, alphabetQ, graphTable, q, val):
    res = []
    stop = False
    isGo = False
    indxQ = alphabetQ.index(q)
    indxVal = alphabet.index(val)
    for a in alphabet:
        if a == 'E' or a == 'E':
            eIndx = alphabet.index(a)  # Дописать  проверку в начало на наличие Е


    # 1
    if graphTable[indxQ][indxVal] != '0':
        res.append(graphTable[indxQ][indxVal])
        indxQ = alphabetQ.index(graphTable[indxQ][indxVal])
        isGo = True
    if isGo:
        while True:
            if graphTable[indxQ][eIndx] == '0':
                break
            res.append(graphTable[indxQ][eIndx])
            indxQ = alphabetQ.index(graphTable[indxQ][eIndx])


    # Всегда переходит максимальное количство раз по Е, если есть путь Е - Е - а, то он не просчитает путь Е - а, если он будет

    # 2
    indxQ = alphabetQ.index(q)
    indxVal = alphabet.index(val)
    isGo1 = False
    isGo = False

    if graphTable[indxQ][eIndx] != '0': # ДОБАВИЛ FOR КОТОРЫЙ БУДЕТ ПРОХОДИТЬ ВСЕ ЭЭЛЕМЕНТЫ ПЕРВОГО ЭПСИЛОНА !!!!!!!
        indxQ = alphabetQ.index(graphTable[indxQ][eIndx])
        isGo1 = True
    if isGo1:
        if graphTable[indxQ][indxVal] != '0':
            res.append(graphTable[indxQ][indxVal])
       #     indxQ = alphabetQ.index(graphTable[indxQ][indxVal])
            isGo = True
    if isGo:
        while True:     # ДОБАВИЛ FOR КОТОРЫЙ БУДЕТ ПРОХОДИТЬ ВСЕ ЭЭЛЕМЕНТЫ ПОСЛЕДНЕГО ЭПСИЛОНА !!!!!!!
            if graphTable[indxQ][eIndx] == '0':
                break
            res.append(graphTable[indxQ][eIndx])
            indxQ = alphabetQ.index(graphTable[indxQ][eIndx])
    return res




from prettytable import PrettyTable
#Ввод алфавита входных символов
while True:
    inputData = input("Введите все символы алфавита подряд без пробелов(Е - принимается за эпислон):")
    alphabet = list(inputData)

    # Проверки алфавита   ДОБАВИТЬ ПРОВЕРКУ НА НАЛИЧИЕ Е

    if len(alphabet) < 2:
        print("Алфавит содержит менее 2 элементов. Повторите ввод:")
        continue

    flag = False
    for i in alphabet:
        if i == 'q':
            print("Алфавит не должен содержать q, т.к. через него обозначаются состояния. Повторите ввод:")
            flag = True
            break
        if i == ' ':
            print("Алфавит содержит пробел. Повторите ввод:")
            flag = True
            break
        if alphabet.count(i) > 1:
            print("Алфавит содержит повторяющиеся элементы. Повторите Ввод:")
            flag = True
            break
    if flag:
        continue

    flag2 = False
    print(alphabet)
    while True:
        isContinue = input("Продолжить с этим алфавитом? Введите 1, чтобы продолжить, или 0, чтобы повторить ввод.\n")
        if isContinue == "1":
            break
        if isContinue == "0":
            flag2 = True
            break
        else:
            print("Можно ввести только 1 или 0. Повторите выбор:")
            continue
    if flag2:
        continue

    if int(isContinue):
        break

# Ввод состояний q

while True:
    inputData = input("Введите все состояния q подряд через пробел:")
    alphabetQ = inputData.split()

    # Проверки
    if len(alphabetQ) < 2:
        print("Алфавит содержит менее 2 элементов. Повторите ввод:")
        continue

    flag = False
    for i in alphabetQ:
        if len(i) < 2:
            print("Состояния должны начинаться с q и заканчиваться цифрой. Повторите ввод:")
            flag = True
            break
        elif not i[1].isnumeric():
            print("Состояния должны начинаться с q и заканчиваться цифрой. Повторите ввод:")
            flag = True
            break
        if i[0] != 'q':
            print("Состояния должны начинаться с q и заканчиваться цифрой. Повторите ввод:")
            flag = True
            break
        if alphabetQ.count(i) > 1:
            print("Алфавит содержит повторяющиеся элементы. Повторите Ввод:")
            flag = True
            break
    if flag:
        continue

    flag2 = False
    print(alphabetQ)
    while True:
        isContinue = input("Продолжить с этим алфавитом? Введите 1, чтобы продолжить, или 0, чтобы повторить ввод.\n")
        if isContinue == "1":
            break
        if isContinue == "0":
            flag2 = True
            break
        else:
            print("Можно ввести только 1 или 0. Повторите выбор:")
            continue
    if flag2:
        continue

    if int(isContinue):
        break

# ВЫбор начальной и конечной вершин

startVertex = []
while True:
    inputDt = input("Укажите какая вершина является начальной:")
    startVertex.append(inputDt)

    flag = True
    for i in alphabetQ:
        if i == inputDt:
            flag = False
            break
    if flag:
        print("Данной вершины нет в указанном графе. Повторите ввод этой вершины")
        continue
    while True:
        choice = input("Закончить ввод начальных вершин? Да - 1, Нет - 0: ")
        if choice == "1":
            break
        if choice == "0":
            flag2 = True
            break
        else:
            print("Можно ввести только 1 или 0. Повторите выбор:")
            continue
    if choice == '1':
        break

endVertex = []
while True:
    inputDt2 = input("Укажите какая вершина является конечной:")
    endVertex.append(inputDt2)

    flag = True
    for i in alphabetQ:
        if i == inputDt2:
            flag = False
            break
    if flag:
        print("Данной вершины нет в указанном графе. Повторите ввод этой вершины")
        continue
    while True:
        choice = input("Закончить ввод конечных вершин? Да - 1, Нет - 0: ")
        if choice == "1":
            break
        if choice == "0":
            flag2 = True
            break
        else:
            print("Можно ввести только 1 или 0. Повторите выбор:")
            continue
    if choice == '1':
        break

# Создаем массив, который хранит граф
graphTable = []
for i in range(len(alphabetQ)):
    graphTable.append([0] * len(alphabet))

# Заполнение таблицы, которая описывает граф

# ДОПИСАТЬ ЧТОБЫ МОНЖО БЫЛО ВВОДИТЬ БОЛЛЕ ОДНОЙ ВЕРШИНЫ В ТАБЛИЦУ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for (i, a) in zip(alphabetQ, range(len(alphabetQ))):
    for (j, b) in zip(alphabet, range(len(alphabet))):
        while True:
            # Дописать, чтобы можно было вводить 0
            currentValue = input("Введите в какое состояние можно пойти из " + i + " по " + j + " (Если это невозможно, укажите 0): ")
            if ((inputData.find(currentValue) == -1) and (currentValue != '0')) or currentValue == 'q':
                print("Данной вершины нет в графе. Введите корректную вершину:")
                continue
            break
        graphTable[a][b] = currentValue


# Вывод таблицы графа
mytable = PrettyTable()
columns = alphabet.copy()
columns.insert(0, "Состояние")
mytable.field_names = columns
for i in range(len(alphabetQ)):
    strName = alphabetQ[i]
    string = graphTable[i].copy()
    string.insert(0, strName)
    mytable.add_row(string)
print(mytable)

# Создание массива для Е-замыканий
eTable = []
for i in range(len(alphabetQ)):
    eTable.append([])

# Нахождение Е-замыканий (Дописать в начале проверку на наличие эпсилонов)
for i in range(len(alphabet)):
    if i == 'E' or 'E':
        eIndx = i

for i in range(len(alphabetQ)):
    eTable[i].append(alphabetQ[i])
    for a in alphabet:
        if a == 'E' or a == 'E':
            eIndx = alphabet.index(a)
    for j in range(i, len(alphabetQ)):
        if graphTable[j][eIndx] == '0':
            break
        eTable[i].append(graphTable[j][eIndx])
        nextIndx = alphabetQ.index(graphTable[j][eIndx])
        j = nextIndx - 1


# Вывод таблицы с Е-замыканиями
print("Е-замыкания:")
for i in range(len(alphabetQ)):
    print(alphabetQ[i] + ":", eTable[i])


#  Создание масиива для хранения таблицы с S
sTable = []
for i in range(len(eTable)):
    sTable.append([0] * len(alphabet))



# Подсчет значений для таблицы S
tempData = set()
res = []
curElem = []
for i in range(len(alphabetQ)):
    for k in alphabet:
        if k == "E":
            continue
        for j in range(len(eTable[i])):
            res.append(countValue(alphabet, alphabetQ, graphTable, eTable[i][j], k)) # во время прохода q1,b выдает q2 и q3 хотя должно быть только q3
        for f in res:
            for g in f:
                tempData.add(g)  # Все вершины одной "ячейки" таблицы   УЧИТЫВАТЬ, ЧТО ЗДЕСЬ МОЖЕТ НИЧЕГО НЕ БЫТЬ, ТОГДА В ТАБЛИЦУ НУЖНО ДОБАВИТЬ 0

        # Дописать проверку на вложенность и тогда добавлять элемент
        if len(tempData) == 0:
            curElem.append('0')
            print(curElem)
        else:
            for w in range(len(eTable)):
                is_subset = False
                is_subset = set(eTable[w]).issubset(tempData)
                if is_subset:
                    print("\n")
                    curElem.append("S" + str(w))
                    print(curElem)
                    print(tempData)
        res = []
        curElem = []
        tempData = set()

# Звполнять таблицу
# Выводить таблицу


''' 
Берется множество из Е, одно из значений и проверяется на три исхода:
1 в другую вершину можно пойти по переданному значению
2 значение -> Е...
3 Е - значение...
каждая полученная вершина добавляется в множество, которое по итогу будет содержать неповторяющийся набор состояний, которые можно достичь 

далее множество сравнивается со списками из Е и таблица заполняется

При этот стоит записать в ноый список какие S являются начальными, а какие - конечными
'''


                






