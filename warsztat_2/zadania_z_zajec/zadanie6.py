def draw_tree(h, s='*'):
    symbols_count = 0
    for i in range(h):
        print((h - i - 1) * ' ' + (2 * i + 1) * str(s))
        symbols_count += (2 * i + 1)
    return symbols_count

total_symbols_count = 0
total_symbols_count += draw_tree(3, 1)
total_symbols_count += draw_tree(h=4, s='#')
total_symbols_count += draw_tree(5)
total_symbols_count += draw_tree(h=6)
print(total_symbols_count)
