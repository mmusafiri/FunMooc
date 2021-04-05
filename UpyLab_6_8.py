def store_email(liste_mails):
    email_tries={}
    for email in liste_mails:
        email_s = email.split("@")
        if email_tries.get(email_s[1], "noexist") == "noexist":
            email_tries.setdefault(email_s[1],[email_s[0]])
        else:
            liste_e = email_tries[email_s[1]]
            liste_e.append(email_s[0])
            email_tries[email_s[1]] = sorted(liste_e)
    return email_tries







print(store_email(["ludo@prof.ur", "andre.colon@stud.ulb","thierry@profs.ulb", "sébastien@prof.ur", "eric.ramzi@stud.ur", "bernard@profs.ulb",
             "jean@profs.ulb" ]))