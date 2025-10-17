def my_decorator(n:int = 1):
    def inner_func(f):
        def wrapper():
            for _ in range(n): print("Before function")
            f()
            for _ in range(n): print("After function")
        return wrapper
    return inner_func


@my_decorator(5)
def execute_task():
    print("Executing task…")


def do_twice(f):
    def wrapper_do_twice(*args, **kwargs):
        f(*args, **kwargs)
        f(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def count_to(n):
    message = "".join([str(i) for i in range(1, n+1)])


if __name__ == "__main__":
    execute_task()