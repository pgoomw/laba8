from PIL import Image, ImageDraw, ImageFont

def z1():
    image1 = Image.open("hb.jpg")
    crop_image1 = image1.crop((50,50,1150,1150))
    crop_image1.save("crop_otcrtca.jpg")
print(z1())

def z2():
    holiday = {
        "23 февраля": "23.jpg",
        "Новый год": "newyear.jpg",
        "8 марта": "otcrtca.jpg",
        "День матери": "mama.jpg"
    }

    name = input("Выберите праздник: 23 февраля, Новый год, 8 марта или день матери: ")
    holidayname = holiday.get(name)

    if holidayname:
        image2 = Image.open(holidayname)
        image2.show()
    else:
        print("Такой открытки нет")
print(z2())

def z3():
    image3 = Image.open("hb.jpg")
    crop_image3 = image3.crop((45, 45, 400, 400))
    name = input('Кого Вы хотите поздравить? ')
    draw = ImageDraw.Draw(crop_image3) # создание объекта для добавления текста
    font = ImageFont.truetype('beer-money12.ttf', 25) # метод для загрузки шрифта
    text_color = (230,193,91)
    text_position = (70, 200)
    text = name + ', поздравляю!'
    draw.text(text_position, text, font=font, fill=text_color) # строка выполняет команду нарисовать текст
    crop_image3.save('name_image3.png')
print(z3())