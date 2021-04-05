def my_insert(li, para):

    assert isinstance(para, int) is True

    for ch in li:
        if ch > para:
            v = li.index(ch)
            li.insert(v, para)
            break
        if ch == li[-1]:
            li.append(para)
            break

