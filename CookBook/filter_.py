values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def fil(value):
    try:
        int(value)
        return True
    except:
        return False


print(list(filter(fil, values)))
