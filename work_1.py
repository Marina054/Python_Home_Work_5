# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('1.txt', encoding = 'utf - 8') as f:
    old_text = f.read()

    
    text = old_text.split(" ")
    fragment = 'а'
    fr = 'б'
    fr2 = 'в'
    new_text = []
    for i in text:
        if fragment not in i:
            if fr not in i:
                if fr2 not in i:
                    new_text.append(i)
    new_text = ' '.join(new_text)
          
   

with open('2.txt','w',encoding = 'utf - 8') as f:
    f.write(new_text)

