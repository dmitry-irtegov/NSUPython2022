from .logging_impl import Logging
import inspect


class A(Logging):
    def method(*args, **kwargs):
        pass


class B(A):
    def other_method(self, num):
        super().method("here i am")
        return num + 2


def test():
    s = A()
    s.method()
    s.method(somekwarg="some_value")
    s.method(1, 2, {"one": "two"}, whos="joe")
    print(s.invocations_log)

    b = B()
    b.other_method(2)
    print(b.invocations_log)


def main():
    print("Showcase on two classes:")
    print(inspect.getsource(A))
    print(inspect.getsource(B))

    print("For the following code:")
    print(inspect.getsource(test))
    print("...here is the output:\n------\n")

    test()


if __name__ == "__main__":
    main()
