def sinusoid(s):
    top, mid, bot = '', '', ''
    for i, _ in enumerate(s):
        if i % 4 == 1:
            top += s[i]
        elif i % 4 == 3:
            bot += s[i]
        else:
            mid += s[i]
    return top + mid + bot

if __name__ == '__main__':
    print(sinusoid('Hello World!'))