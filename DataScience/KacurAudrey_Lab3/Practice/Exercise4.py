def myFunction(li):
    for x in range(len(li)):
        li[x] *= 2
        # EQUIVALENT TO:
        #li[x] = li[x] * 2


li2 = [2, 5, 8, 1, 7]
myFunction(li2)
print(li2)
print(li2[::2])
del li2[-2:-1]  # -1 is not inclusive
print(li2)
