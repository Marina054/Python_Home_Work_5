# Декодирование

fileObject = open('3.txt', 'r',encoding = 'utf - 8')
data = fileObject.read()
# print(data)

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode      

decoded_val = rle_decode(data)
print(decoded_val)     