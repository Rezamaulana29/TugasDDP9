#Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
#nilai (80) #lulus
#nilai(60) #gagal

def keterangan_lulus(nilai):
    if nilai >= 80:
        return "Lulus"
    elif nilai < 60:
        return "Gagal"
    else:
        return "Tidak Lulus"
    
print(keterangan_lulus(80))  
print(keterangan_lulus(60))  
print(keterangan_lulus(59))  
