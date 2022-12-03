# 1. Поиск и замена слов в содержимом текстового файла

# GitLab is an open source code repository and collaborative software development platform for large DevOps and DevSecOps projects. GitLab is free for individuals. GitLab offers a location for online code storage and capabilities for issue tracking and CI/CD.

def change_words(file, words_find, words_new):
    with open(file, mode="r") as f:
        li1 = f.readline()
    print(li1)

    with open(file, mode="w") as f:
        li1 = li1.split(" ")
        for i in range(len(li1)):
            if li1[i] == words_find:
                li1[i] = words_new
        li1 = " ".join(li1)
        f.writelines(li1)
    print(li1)

print(change_words('dz12.txt', "and", "or"))


# 2. Подсчет количества слов в содержимом текстового файла

def num_words(file):
    with open(file, mode="r") as f:
        li1 = f.readline()
        return len(li1.split())

print("Слов в содержимом файле:", num_words('dz12.txt'))


# 3. Вывести слова содержимого файла  в обратном порядке

def revers_words(file):
    with open(file, mode="r") as f:
        li1 = f.readline()
        li1 = li1.split(" ")
        return ' '.join(reversed(li1))

print("Слова в обратном порядке:", revers_words('dz12.txt'))


# 4. Удаление заданной по номеру строки из файла

def del_str(file, n:int):
    li1 = None
    with open(file, mode="r") as f:
        li1 = f.readlines()
    print(li1)

    with open(file, mode="w") as f:
        li1.pop(n)
        f.writelines(li1)
    print(li1)

print(del_str('dz12_2.txt', 1))
