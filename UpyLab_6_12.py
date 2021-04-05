def belongs_to_file(word, filename):
    with open(filename) as f:
        lig = f.readline().strip()
        while lig != '':
            if word == lig:
                return True
            lig = f.readline().strip()
        return False

print(belongs_to_file("apl", "words.txt"))