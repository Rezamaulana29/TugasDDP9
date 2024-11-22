#Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
#bilangan(20) # 1,3,5,7,9,11,13,15,17,19

def bilangan(n):
    ganjil = [str(i) for i in range(1, n) if i % 2 != 0]
    return ','.join(ganjil)

print(bilangan(20)) 