# Simple bubble algorithm
def bubble(src):
    for i in range(len(src)):
        for j in range(len(src)-1-i):
            if src[j] < src[j+1]:
                src[j], src[j+1] = src[j+1], src[j]
    return src
