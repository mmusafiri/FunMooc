def substitue(message, dictionnaire):

    phrase = ""
    for ab in message.split():
        phrase += dictionnaire.get(str(ab), str(ab)) + " "

    return(phrase.strip())

