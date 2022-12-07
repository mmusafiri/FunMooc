def list_strip(liste):
    for n in range(len(liste)):
        liste[n] = liste[n].strip()

    return liste

def comp(f_passfail,f_count):
    dic = {}
    with open(f_passfail, encoding="utf-8") as fpf:
        ex_name = list_strip(fpf.readline().split(sep=";"))
        with open(f_count, encoding="utf-8") as fc:
            lig_c = fc.readline()
            while True:
                list_pf = list_strip(fpf.readline().split(sep=";"))
                list_count = list_strip(fc.readline().split(sep=";"))

                if len(list_pf) == 1 or len(list_count) == 1:
                    break
                for n in range(len(ex_name)):
                    if not list_count[n].isnumeric():
                        val = 0
                    else :
                        val = int(list_count[n])
                    l = (list_pf[n], val)
                    v = dic.get(ex_name[n])
                    if v == None:
                        dic.setdefault(ex_name[n], [l])
                    else:
                        v.append(l)
                        dic[ex_name[n]] = v

            liste_ap_fiable = []
            nb_ap = len(dic[ex_name[0]])

            for n in range(nb_ap):
                fiable = True
                for ex in range(len(dic)):
                    app_cond = dic[ex_name[ex]][n][0]
                    app_count = dic[ex_name[ex]][n][1]
                    if not ((app_count <= 10 and (app_cond == "VRAI" or app_cond == "FAUX")) or app_cond == ''):
                        fiable = False
                        break
                if fiable:
                    liste_ap_fiable.append(n)

            dico_app_f = {}

            for ex in range(len(dic)):
                nb_appf_by_ex = 0
                for app in liste_ap_fiable:
                    app_cond = dic[ex_name[ex]][app][0]
                    if app_cond == "VRAI":
                        nb_appf_by_ex += 1
                v = dic.get(ex_name[ex])
                v.append(nb_appf_by_ex)
                dic[ex_name[ex]] = v
                dico_app_f[ex_name[ex]] = nb_appf_by_ex

            sort_dic_val = dict(sorted(dico_app_f.items(), key=lambda t: t[1], reverse=True))
            sort_dic_cle = dict(sorted(dico_app_f.items(), key=lambda t: t[0], reverse=True))
            liste_ex = []

            for exv in sort_dic_val:
                for exc in sort_dic_cle:
                    if sort_dic_val[exv] == sort_dic_cle[exc]:
                        print(exc)
                        break
                sort_dic_cle.pop(exc)

           

f_passfail = "result-pass-fail-0.csv"
f_count = "result-count-0.csv"


comp(f_passfail, f_count)
