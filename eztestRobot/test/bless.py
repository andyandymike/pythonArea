class oldstyleBase(object):
    def foo(self):
        print("oldstyleBase foo")


class oldstyleChildA(oldstyleBase):
    pass


class oldstyleChildB(oldstyleBase):
    def foo(self):
        print("oldstyleChildB foo")


class test(oldstyleChildA, oldstyleChildB, list):
    def __getattribute__(self, item):
        if item == 'append':
            print('getting append')
        return super(test, self).__getattribute__(item)


class inn(object):
    def __init__(self, value=1):
        self.value = value

    def __get__(self, instance, owner):
        print('get inn')
        return self.value

    def __set__(self, instance, value):
        print('set inn')
        self.__dict__['value'] = value


class testInn(object):
    tinn = inn()

class base(object):
    def __init__(self):
        self.attr1 = 1

class child(base):
    def __init__(self):
        print(super(child, self).attr1)

if __name__ == '__main__':
    t = test()
    t.foo()
    t.append(1)
    temp = testInn()
    temp.tinn = 2
    print(temp.tinn)
    c = child()
