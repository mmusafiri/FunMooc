def my_insert(li, para):

    lis = li.copy()

    if not isinstance(para, int):
        return None

    for ch in lis:
        if ch > para:
            v = lis.index(ch)
            lis.insert(v, para)
            break
        if ch == lis[-1]:
            lis.append(para)
            break

    return lis
