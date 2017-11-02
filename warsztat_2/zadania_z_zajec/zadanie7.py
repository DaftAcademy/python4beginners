def draw_tree(s, *args):
    for h in args:
        for i in range(h):
            print((h - i - 1) * ' ' + (2 * i + 1) * str(s))

draw_tree('*', 3, 4, 5, 6)
