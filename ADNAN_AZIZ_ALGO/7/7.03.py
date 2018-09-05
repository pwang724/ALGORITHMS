def column_to_num(str):
    result = 0
    for i in str:
        num = ord(i) - 65 + 1
        result = result * 26 + num
    return result

if __name__ == '__main__':
    print(column_to_num('AA'))