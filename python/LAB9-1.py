import string
src_str = string.ascii_uppercase
src_str1 = string.ascii_lowercase
dst_str = src_str[3:] + src_str[:3]
dst_str1 = src_str1[3:] + src_str1[:3]

def ciper(a):
    idx = src_str.index(a)
    return dst_str[idx]

def ciper1(a):
    idx1 = src_str1.index(a)
    return dst_str1[idx1]

src = input("문장을 입력하세요 :" )
print('암호화 된 문장 : ', end ='')

for ch in src:
    if ch in src_str:
        print(ciper(ch), end ="")
    else :
        print(ciper1(ch), end = "")

print()

