from playsound import playsound

number = 0

while number != -1:
    print('Enter a number:', end = ' ')
    number = int(input())

    if number == 0:
        print('You picked: ' + str(number) + ", this is it's pronunciation")
        print('Pinyin: ' + 'Líng'.lower())
        print('Hanzi: ' + '零')
        playsound('D:\Music\Counting-In_Chinese\\zero.wav')
    elif number == 1:
        print('You picked: ' + str(number) + ", this is it's pronunciation")
        print('Pinyin: ' + 'Yī'.lower())
        print('Hanzi: ' + '一')
        playsound('D:\Music\Counting-In_Chinese\\one.wav')
    elif number == 2:
        print('You picked: ' + str(number) + ", this is it's pronunciation")
        print('Pinyin: ' + 'Èr'.lower())
        print('Hanzi: ' + '二')
        playsound('D:\Music\Counting-In_Chinese\\two.wav')
    elif number == 2:
        print('You picked: ' + str(number) + ", this is it's pronunciation")
        print('Pinyin: ' + 'Èr'.lower())
        print('Hanzi: ' + '二')
        playsound('D:\Music\Counting-In_Chinese\\two.wav')
    elif number == 3:
        print('You picked: ' + str(number) + ", this is it's pronunciation")
        print('Pinyin: ' + 'Sān'.lower())
        print('Hanzi: ' + '三')
        playsound('D:\Music\Counting-In_Chinese\\three.wav')
    elif number == 4:
        print('You picked: ' + str(number) + ", this is it's pronunciation")
        print('Pinyin: ' + 'Sì'.lower())
        print('Hanzi: ' + '四')
        playsound('D:\Music\Counting-In_Chinese\\four.wav')
    elif number == 5:
        print('You picked: ' + str(number) + ", this is it's pronunciation")
        print('Pinyin: ' + 'Wǔ'.lower())
        print('Hanzi: ' + '五')
        playsound('D:\Music\Counting-In_Chinese\\five.wav')
    elif number == 6:
        print('You picked: ' + str(number) + ", this is it's pronunciation")
        print('Pinyin: ' + 'Liù'.lower())
        print('Hanzi: ' + '六')
        playsound('D:\Music\Counting-In_Chinese\\six.wav')
    elif number == 7:
        print('You picked: ' + str(number) + ", this is it's pronunciation")
        print('Pinyin: ' + 'Qī'.lower())
        print('Hanzi: ' + '七')
        playsound('D:\Music\Counting-In_Chinese\\seven.wav')
    elif number == 8:
        print('You picked: ' + str(number) + ", this is it's pronunciation")
        print('Pinyin: ' + 'Bā'.lower())
        print('Hanzi: ' + '八')
        playsound('D:\Music\Counting-In_Chinese\\eight.wav')
    elif number == 9:
        print('You picked: ' + str(number) + ", this is it's pronunciation")
        print('Pinyin: ' + 'Jiǔ'.lower())
        print('Hanzi: ' + '九')
        playsound('D:\Music\Counting-In_Chinese\\nine.wav')
    elif number == 10:
        print('You picked: ' + str(number) + ", this is it's pronunciation")
        print('Pinyin: ' + 'Shí'.lower())
        print('Hanzi: ' + '十')
        playsound('D:\Music\Counting-In_Chinese\\ten.wav')
