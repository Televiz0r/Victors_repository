def three_args(var1, var2, var3):
    res_dict = locals()
    result = {}
    value = None

    for key in res_dict:
        value = res_dict.get(key)
        if value is not None:
            result[key] = value
    print(f'Аргументы: {result}')

three_args(1, None, 3)