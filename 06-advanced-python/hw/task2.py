"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""


class GraphIterator:
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor
        self.v = ''
        self._vers = []
        self.used = []

    def __next__(self):
        if not self._cursor:
            keys = list(self._collection.keys())
            self.v = keys[self._cursor]
            self._cursor += 1
            self.used.append(self.v)
            return self.v
        else:
            if self._cursor == len(self._collection[self.v]) + 1:
                if not self._vers:
                    raise StopIteration
                else:
                    self.v = self._vers[0]
                    self._vers = self._vers[1:]
                    self._cursor = 1
            if not self._collection[self.v]:
                return self.__next__()
            a = self._collection[self.v][self._cursor-1]
            if a not in self.used:
                self._vers.append(self._collection[self.v][self._cursor-1])
                self._cursor += 1
                self.used.append(a)
                return a
            self._cursor += 1
            return self.__next__()


class Graph:
    def __init__(self, E):
        self.E = E

    def __iter__(self):
        return GraphIterator(self.E, 0)


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)
vertices = []
for vertice in graph:
    vertices.append(vertice)
