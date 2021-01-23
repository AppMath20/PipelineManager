import functools

def pipeline():
    __funcs__ = {}
    def handle(func=None,depends_on=None):
        if func is None:
            def decorator(func):
                return handle(func=func,depends_on=depends_on)
            return decorator

        @functools.wraps(func)
        def inner():
            if depends_on is not None:
                for i in depends_on:
                    __funcs__.get(i)()
            func()

        __funcs__.update({func.__name__:inner})
        return inner
    return handle