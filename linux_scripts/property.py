from time import sleep


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('must be integer')
        self._score = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


L = {}
while True:
    s = Student()
    s.score = int(input('a score: '))
    s.name = input('a name:')
    L[s.name] = s.score
    print(L[s.name])
    a = int(input("0.exit,1.continue"))

    if a == 0:
        break

# sleep(10)



