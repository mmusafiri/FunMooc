def next_line(line):
    if len(line) == 0:
        return [1]
    lcount = []
    line.append("E")
    count = 1
    n = 0
    while line[n] != "E":
        if line[n] !=  line[n+1]:
            lcount.append(count)
            lcount.append(line[n])
            del line[:n+1]
            count = 1
            n = 0
        else:
            count += 1
            n += 1

    return lcount




next_line([1, 2, 1, 2, 1])