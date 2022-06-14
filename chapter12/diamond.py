

class A:
    def ping(self):
        print('ping: ', self)


class B(A):
    def pong(self):
        print('pong: ', self)



class C(A):
    def pong(self):
        print('PONG: ', self)


class D(C, B):
    def ping(self):
        super().ping()
        print('post-ping: ', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        B.pong(self)


"""
Lets see what happens
"""

d = D()

d.pong()
print("-------------")
d.pingpong()



