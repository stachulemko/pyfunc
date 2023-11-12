def cycle_sort(do_sort):
    bg = do_sort[0]
    licznik = 0
    bk = do_sort[1::]
    for i in bk:
        if bg > i:
            licznik += 1
    bg = do_sort[licznik]
    return do_sort


print(cycle_sort([10, 1, 4, -1, 5, 0]))
