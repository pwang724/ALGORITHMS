def shorten_dir(str):
    if str[0] == '/':
        first_slash = True
    else:
        first_slash = False

    dirlist = str.split('/')
    modified_list = [l for l in dirlist if l not in ['.','']]

    path_name = []
    for item in modified_list:
        if item == '..':
            if not path_name and first_slash:
                return 'wtf'
            else:
                if not path_name or path_name[-1] == '..':
                    path_name.append(item)
                else:
                    path_name.pop()
        else:
            path_name.append(item)

    out = '/'.join(path_name)
    if first_slash:
        out = '/' + out

    return out


if __name__ == '__main__':
    a = shorten_dir('nQbIPdMXp/../././..//')
    print(a)