def draw_tree(s, **kwargs):
    for name, h in kwargs.items():
        print(name)
        for i in range(h):
            print((h - i - 1) * ' ' + (2 * i + 1) * str(s))

draw_tree('*', sosna=5, świerk=6)
