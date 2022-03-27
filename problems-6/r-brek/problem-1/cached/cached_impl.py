import functools

def cached(func):
    cache = {}
    @functools.wraps(func)
    def decorated(*args, **kwargs):
        key = (
            args,
            tuple(sorted(kwargs.items()))
        )
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return decorated
