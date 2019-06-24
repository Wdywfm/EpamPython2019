"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:

> print(folder1)

V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1

А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True

"""


class PrintableFolder:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self):
        return self.get_content(-1)

    def __contains__(self, item):
        check = False
        for smth in self.content:
            if item.name == smth.name:
                return True
            elif hasattr(smth, 'content'):
                check = smth.__contains__(item)
            if check:
                return True

    def get_content(self, lvl):
        lvl += 1
        resp = 'V ' + self.name
        for smth in self.content:
            if hasattr(smth, 'content'):
                resp += '\n' + lvl*'|   ' + '|-> ' + smth.get_content(lvl)
            else:
                resp += '\n' + lvl*'|   ' + '|-> ' + smth.name
        return resp


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


file1 = PrintableFile('file1')
file2 = PrintableFile('file2')
file3 = PrintableFile('file3')
file4 = PrintableFile('file4')
folder4 = PrintableFolder('folder4', [file3])
folder3 = PrintableFolder('folder3', [file3])
folder2 = PrintableFolder('folder2', [folder3, file2])
folder1 = PrintableFolder('folder1', [folder2, file1])
print(folder1)
print(file1 in folder1)
