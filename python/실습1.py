bread = ["플랫", "위트", "허니오트", "화이트"]
meat = ["미트볼", "소시지", "닭가슴살"]
vegetables = ["양상추", "토마토", "오이"]
source = ["마요네즈", "케찹", "칠리"]

for a in bread:
    for b in meat:
        for c in vegetables:
            for d in source:
                print(a + "+" + b + "+" + c+ "+" + d)