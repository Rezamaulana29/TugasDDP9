#Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
#print(celcius_ke_fahrenheit(0))    # Output: 32.0
#print(celcius_ke_fahrenheit(100))  # Output: 212.0

def celcius_ke_fahrenheit(suhu_celcius):
    suhu_fahrenheit = (suhu_celcius * 9/5) + 32
    return suhu_fahrenheit

print(celcius_ke_fahrenheit(0))    
print(celcius_ke_fahrenheit(100))  