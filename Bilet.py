print("Bilet satış məntəqəsinə xoş gəlmisiz ")
boy = int(input("İstifadə edəcək səxsin boyu? "))

if boy > 120:
    age = int(input("Yaşınızı qeyd edin:"))
    if age < 12:
        print("Qiymət 5 azn")
    elif 12 <= age <= 18:
        print("7 azn")
    elif 18 < age < 45:
        print("12 azn")
    elif 45 <= age <= 55:
        print("Bilet ödənişsizdir")

    şəkil = str(input("Şəkil istəyirsiz? (bəli/xeyr) "))
    if şəkil == "xeyr":
        print(f"Borcunuz {age} azn")
    else:
        print(int(input(f"sizin borcunuz {age+3} azn dir")))

else:
    print("Təəsüfki sizə bilet düşmür;)")





