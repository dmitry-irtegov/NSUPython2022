def translate(input, mapping, chars_to_delete=None):
    if chars_to_delete is None:
        chars_to_delete = set()

    def default_mapping(x): return x if x not in mapping else mapping[x]
    return ('' if x in chars_to_delete else default_mapping(x) for x in input)
