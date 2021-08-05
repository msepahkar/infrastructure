import enum

class C(enum.Enum):
    a = 1
    b = 2

    def who(self):
        if self == self.a:
            print('aaa')
        if self == self.b:
            print('bbb')

C.a.who()
C.b.who()