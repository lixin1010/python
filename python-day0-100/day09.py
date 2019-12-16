
class Person(object):
    __slots__ = ('_name', '_age')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age < 16:
            print('%s玩飞行棋' % self._name)
        else:
            print('%s玩斗地主' % self._name)


def main():

    person = Person('李鑫', 20)
    person.play()
    person.age = 10
    person.play()
    #person.name = '李二胖'


if __name__ == '__main__':
    main()
