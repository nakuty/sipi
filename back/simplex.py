import logging


logger2 = logging.getLogger(__name__)
logger2.setLevel(logging.INFO)
handler2 = logging.FileHandler(f"{__name__}.log", mode='a')
formatter2 = logging.Formatter("[%(asctime)s %(levelname)s] %(message)s")
handler2.setFormatter(formatter2)
logger2.addHandler(handler2)


def is_valid_float(element: str) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False


def simplex(func_input, input_min_max, input_count_ogr, input_ogr):
    logger2.info("inputs: (" + str(func_input) + "), " + str(input_min_max) + ", " + str(input_ogr))
    matrix = []
    count = 0
    Cj = []
    Xj = []


    F = func_input.strip().split()

    for item in F:  # Заполнение Cj и Xj
        if 'x' in item:
            count += 1
            Xj.append(item)
        if is_valid_float(item):
            if input_min_max == 'min':
                Cj.append(-1 * float(item))
            else:
                Cj.append(float(item))

    for i in range(input_count_ogr):
        Q = list(map(str, input_ogr[i].strip().split()))
        if Q[-2] != '=':
            matrix.append(Q)

    simplex_table = [[0] * input_count_ogr for p in range(count + 1)]
    Cb = []
    Xb = []

    for y in range(input_count_ogr):  # Заполнение Cb
        i = 0
        Cb.append(0)
        Xb.append('x{0}'.format(count + y + 1))
        while i <= count:
            for item in matrix[y]:
                if is_valid_float(item):
                    simplex_table[i][y] = float(item)
                    i += 1


    b = False
    Result = []

    for i in range(count):
        r = 0
        for y in range(input_count_ogr):
            r += Cb[y] * simplex_table[i][y]
        Result.append(r - Cj[i])
    for item in Result:
        b = item < 0

    print(simplex_table)

    while b:
        b = False

        column = Result.index(min(Result))  # Определение разрещающего столбца
        print(Result)
        value = simplex_table[count][0] / simplex_table[column][0]
        row = 0
        for y in range(input_count_ogr):  # Определение разрещающей строки
            if simplex_table[column][y] != 0:
                p = simplex_table[count][y] / simplex_table[column][y]
                if p < value:
                    value = p
                    row = y
        print(column, row)
        print(simplex_table[column][row])

        resolution_element = simplex_table[column][row]
        simplex_table[column][row] = 1 / resolution_element  # Замена разрещающего символа

        for i in range(count + 1):  # Замена элементов не разрещающих
            for y in range(input_count_ogr):
                if y != row and i != column:
                    simplex_table[i][y] = simplex_table[i][y] - (simplex_table[column][y] * simplex_table[i][row]) / resolution_element

        for i in range(count + 1):  # Замена элементов столбца
            if i != column:
                simplex_table[i][row] = simplex_table[i][row] / resolution_element

        for y in range(input_count_ogr):  # Замена элементов строки
            if y != row:
                simplex_table[column][y] = -1 * (simplex_table[column][y] / resolution_element)

        value = Cj[column]
        Cj[column] = Cb[row]
        Cb[row] = value

        value_char = Xj[column]
        Xj[column] = Xb[row]
        Xb[row] = value_char

        Result = []
        for i in range(count):  # Расчёт дельты
            r = 0
            for y in range(input_count_ogr):
                r += Cb[y] * simplex_table[i][y]
            Result.append(r - Cj[i])

        for item in Result:  # Проверка на положительность дельты
            if item < 0:
                b = True

        print(simplex_table)

    result_return = []

    for i in range(1, count + input_count_ogr + 1):  # Вывод x
        if 'x' + str(i) in Xb:
            result_return.append('x' + str(i) + ' = ' + str(round(simplex_table[-1][Xb.index('x' + str(i))], 2)))
        else:
            result_return.append('x' + str(i) + ' = 0')

    Q = 0
    for i in range(input_count_ogr):
        Q += Cb[i] * simplex_table[-1][i]

    result_return.append('Q = ' + str(Q))

    logger2.info("Result: " + str(result_return))


    return result_return
