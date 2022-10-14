# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

fileObject = open('1.txt', 'r', encoding = 'utf - 8')
data = fileObject.read()
print(data)


def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding     

encoding_val = rle_encode(data)
print(encoding_val)

with open('3.txt','w',encoding = 'utf - 8') as f:
    f.write(encoding_val)