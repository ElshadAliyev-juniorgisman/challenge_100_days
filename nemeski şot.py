print(" Alman üsulu  ilə hesab  ödəmə sisteminə xoş gəlmisiz:) \n Zəhmət olmasa məlumatları daxil edin:) ")
hesab=int(input("Hesab:"))
adam_say=int(input("Adamların sayı:"))
bəxşiş=int(input("Vermək istədiyiniz bəxşişi seçin: (10,12,16):"))
ümumi_hesab=int(hesab+(bəxşiş*hesab/100))
print(f"Sizin adam başına düşən hesab {(ümumi_hesab/adam_say)} AZN-dir")

