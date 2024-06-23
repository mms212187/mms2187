import functools
import warnings


def type_check(*arg_types, **kwarg_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            valid = True

            for i, (arg, expected_type) in enumerate(zip(args, arg_types)):
                if not isinstance(arg, expected_type):
                    warnings.warn(
                        f"Argument {i + 1} of {func.__name__} is not of type {expected_type.__name__}.",
                        UserWarning,
                    )
                    valid = False

            for kwarg, expected_type in kwarg_types.items():
                if kwarg in kwargs and not isinstance(kwargs[kwarg], expected_type):
                    warnings.warn(
                        f"Argument '{kwarg}' of {func.__name__} is not of type {expected_type.__name__}.",
                        UserWarning,
                    )
                    valid = False

            if valid:
                return func(*args, **kwargs)
            else:
                return None

        return wrapper

    return decorator


@type_check(int, int, c=int)
def example_function(a, b, c=0):
    return a + b + c


result = example_function(1, "2", c=3.0)
print(result)

import functools.


def colorize(color_code):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            color_start = f"\033[{color_code}m"
            color_end = "\033[0m"
            result = func(*args, **kwargs)
            print(f"{color_start}{result}{color_end}")
            return result

        return wrapper

    return decorator


@colorize(31)
def say_hello(name):
    return f"Hello, {name}!"


@colorize(32)
def say_goodbye(name):
    return f"Goodbye, {name}!"


say_hello("Vasya")
say_goodbye("Mixa")
