from hashlib import sha256


def addAllKLength(set, prefix, n, k, stringset):

    if k == 0:
        #print(prefix)
        stringset.append(prefix)
        return

    for i in range(n):
        newPrefix = prefix + set[i]
        addAllKLength(set, newPrefix, n, k-1, stringset)


    return

set = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = len(set)
k = 1
blob = "a"
prevhash = "a9c1ae3f4fc29d0be9113a42090a5ef9fdef93f5ec4777a008873972e60bb532"
idofhash = sha256("999".encode('utf-8')).hexdigest()
input_ = "CPEN 442 Coin" + "2022" + prevhash + blob + idofhash

while(k<5):
    stringset = []
    addAllKLength(set, "", n, k, stringset)
    for blob in stringset:
        input_ = "CPEN 442 Coin" + "2022" + prevhash + blob + idofhash
        if (sha256(input_.encode('utf-8')).hexdigest()[0:4]) == "0000":
            print(sha256(input_.encode('utf-8')).hexdigest())
            print(blob)
    k += 1








