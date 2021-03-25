hp = 280
hit = ""
print("현재 체력은 %d 입니다." %hp)

while hit != "save" and hp > 0:
    hit = input("데미지를 몇 입었습니까 : ")
    if hit == "save":
        f = open("c:/temp/save.txt", "w")
        f.write(str(hp))
        f.close()
    else:
        hit = int(hit)
        hp = hp - hit
        print("체력이 %d 남았습니다." %hp)