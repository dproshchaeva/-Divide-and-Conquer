def div_con(x):
    integer = []
    string = []
    for el in x:
        if type(el) == int:
            integer.append(el)
        else:
            string.append(int(el))
    return sum(integer) - sum(string)

array = [10, '20', 30, '40', '50']
result = div_con(array)
print(result)