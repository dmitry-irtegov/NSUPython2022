import functools


class LoggingMeta(type):

    def __new__(cls, name, bases, dct):

        def pretty_string_invocation(func, args, kwargs):
            method_name = func.__name__
            args_no_self = args[1:]
            args_pretty = ", ".join(map(str, args_no_self))
            kwargs_pretty = ", ".join(
                [f"{arg}={val}" for arg, val in kwargs.items()])
            delimiter = ", " if len(args_no_self) > 0 and len(kwargs) > 0 else ""
            return f"{method_name}({args_pretty}{delimiter}{kwargs_pretty})"

        def logging_wrap(func):
            @functools.wraps(func)
            def wrapped(*args, **kwargs):
                self = args[0]
                self.invocations_log += pretty_string_invocation(
                    func, args, kwargs) + "\n"
                return func(*args, **kwargs)
            return wrapped

        logger_attrs = {'invocations_log': ""}
        dct.update(logger_attrs)

        for name, value in dct.items():
            if callable(value):
                dct[name] = logging_wrap(value)

        return super().__new__(cls, name, bases, dct)


class Logging(metaclass=LoggingMeta):
    pass
