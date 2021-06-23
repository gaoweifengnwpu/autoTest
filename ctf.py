from PIL import Image
import glob as gb  # 导入glob模块
# 第一题
# str = 'c8e9aca0c6f2e5f3e8c4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0e8eafae3f9e4eafae2eae4e3eaebfaebe3f5e7e9f3e4e3e8eaf9eaf3e2e4e6f2'
# flag = ''
# for i in range(0, len(str), 2):
#     str1 = str[i] + str[i + 1]
#     value = int(str1, 16)
#     flag = flag + chr(value - 128)
# print(flag)
# 第二题
# 返回该路径下所有的 jpg 文件的路径
# img_path = gb.glob(r"D:\autoTest\gif\*.jpg")
# result = ''
# for i in range(0,104):
#     image = Image.open("D:\\autoTest\gif\\"+str(i)+".jpg")
#     image = image.convert('RGB')
#     r, g, b = image.getpixel((1, 1))
#     if r != 255:
#         result = result + '1'
#     else:
#         result = result + '0'
# for i in range(0, len(result), 8):
#     byte = result[i:i + 8]
#     print(chr(int(byte, 2)), end='')
# 第三题
str='BABA BBB BA BBA ABA AB B AAB ABAA AB B AA BBB BA AAA BBAABB AABA ABAA AB BBA BBBAAA ABBBB BA AAAB ABBBB AAAAA ABBBB BAAA ABAA AAABB BB AAABB AAAAA AAAAA AAAAB BBA AAABB'
str=str.replace('A','.')
print(str)
str=str.replace('B','-')
print(str)
