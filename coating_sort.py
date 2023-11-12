def coating_sort(l):
    w = [0 for x in range(max(l)+2)]
    for i in l:
        w[i] += 1

    j = list(range(len(w)-1))
    for i in j:
        w[i+1] += w[i]
    print(w)

    sorted_list = [0 for x in range(len(l))]
    for i in l:
        sorted_list[w[i]-1] = i
        w[i] -= 1

    return sorted_list


print(coating_sort([2, 34, 45, 5, 3, 3333333333, 5563666,
                    6366343363463346346346346, 6663663636364363636,  6, 68986555556]))
