class TestClass1(object):
    'This is TestClass1'
    x=1
    y=2
    z=3
    def hello(self):
        print(TestClass1.x + TestClass1.y + TestClass1.z)


tc1 = TestClass1()
print(tc1.hello())

def testClosure(v1):
    def add(v2):
        return v1 + v2
    return add(2)

print(testClosure(1))
