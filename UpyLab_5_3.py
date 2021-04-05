import datetime

def duree(debut, fin):
    tmid= datetime.timedelta(hours=24, minutes = 0)
    td1 = datetime.timedelta(hours=debut[0], minutes = debut[1])
    td2 = datetime.timedelta(hours=fin[0], minutes = fin[1])

    if td1 > td2:
        td = td2-td1+tmid
    else:
        td = td2-td1

    delta_h = divmod(td.seconds, 3600)
    delta_m = divmod(delta_h[1], 60)
    return((delta_h[0], delta_m[0]))