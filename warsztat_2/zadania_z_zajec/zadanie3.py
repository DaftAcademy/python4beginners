def draw_tree(h):
    for i in range(h):
        print((h - i - 1) * ' ' + (2 * i + 1) * '*')

draw_tree(3)
draw_tree(4)
draw_tree(5)
