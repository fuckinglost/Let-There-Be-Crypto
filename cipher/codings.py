import itertools as it
from functools import partial as curry

alpha = tuple('abcdefghijklmnopqrstuvwxyz')

def create_mapping(from_stream, to_stream, from_wrap=False, to_wrap=True):
    """Take two streams and make a mapping.

    Note that both streams must be lists or tuples.

    Here's an example of a set of mappings using a direct coding between the
    simple latin alphabet and their numeric position.

        >>> import codings
        >>> alpha_to_number = codings.create_mapping(codings.alpha, range(len(codings.alpha)))
        >>> alpha_to_number
        {'a': 0, 'c': 2, 'b': 1, 'e': 4, 'd': 3, 'g': 6, 'f': 5, 'i': 8, 'h': 7, 'k': 10, 'j': 9, 'm': 12, 'l': 11, 'o': 14, 'n': 13, 'q': 16, 'p': 15, 's': 18, 'r': 17, 'u': 20, 't': 19, 'w': 22, 'v': 21, 'y': 24, 'x': 23, 'z': 25}

    `wrap` denotes whether the mapping should be cut short when `to_stream`
    runs out of symbols or should be wrapped until it's the same length.

        >>> number_to_foo = codings.create_mapping(range(10), list('foo'))
        >>> number_to_foo
        {0: 'f', 1: 'o', 2: 'o', 3: 'f', 4: 'o', 5: 'o', 6: 'f', 7: 'o', 8: 'o', 9: 'f'}

    And without wrapping...

        >>> number_to_foo = codings.create_mapping(range(10), list('foo'), to_wrap=False)
        >>> number_to_foo
        {0: 'f', 1: 'o', 2: 'o'}

    Since these are direct mappings implemented with hash tables it would
    be pointless to wrap `from_stream` since each symbol would only take
    on the final value it was wrapped to, so it is off by default... but
    `from_wrap` is implemented for continuity of action.

        >>> bar_to_number = codings.create_mapping(list('bar'), range(10))
        >>> bar_to_number
        {'a': 1, 'r': 2, 'b': 0}

    And if you pass `from_wrap=True`...

        >>> bar_to_number = codings.create_mapping(list('bar'), range(10), from_wrap=True)
        >>> bar_to_number
        {'a': 7, 'r': 8, 'b': 9}

    Another effect of this is that any `from_stream` that has repeated
    elements will be reduced to the last mapping of any given element if
    `from_wrap=True`.

        >>> fooooo_to_number = codings.create_mapping(list('fooooo'), range(10), from_wrap=True)
        >>> fooooo_to_number
        {'o': 9, 'f': 6}

    """
    if not (isinstance(from_stream, tuple) or isinstance(from_stream, list)):
        raise TypeError("create_mapping() arg 1 must be a list or tuple.")
    if not (isinstance(to_stream, tuple) or isinstance(to_stream, list)):
        raise TypeError("create_mapping() arg 2 must be a list or tuple.")

    from_len = len(from_stream)
    to_len = len(to_stream)
    if to_wrap:
        if from_len > to_len:
            to_stream = it.cycle(to_stream)
    if from_wrap:
        if to_len > from_len:
            from_stream = it.cycle(from_stream)

    return dict(it.izip(from_stream, to_stream))

def transcode_char(x, mapping):
    if x is None or x not in mapping:
        return None
    return mapping[x]

def transcode_stream(stream, mapping):
    return map(curry(transcode_char, mapping=mapping), stream)

def right_shift(x):
    return x[1:]+[x[0]]

def left_shift(x):
    return x[-1]+[x[:-1]]

def rotate(stream, direction=1):
    if direction > 0:
        return right_shift(stream)
    if direction <= 0:
        return left_shift(stream)

def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    # For those who haven't seen doctest before... just run this file and
    # you will get testing output...
    _test()
