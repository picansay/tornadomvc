
#print globals()

class A:
    def show_g(self):
        print globals()

a = A()
a.show_g()


if __name__ == "__main__":
    b = A()
    b.show_g()
