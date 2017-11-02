def draw_tree(h, s):
    for i in range(h):
        print((h - i - 1) * ' ' + (2 * i + 1) * str(s))

draw_tree(3, 1)
draw_tree(4, s='#')
draw_tree(s='*', h=5)
