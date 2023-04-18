from PIL import Image
import time

def welcome_messages():
    print("Hello! In this program you'll have option to do the following to jpeg pictures:")
    list = ['resize', 'rotate', 'convert to png and save them', 'blur', 'convert B/W', 'chose which one to open', 'view all jpeg and png', 'change it to color blue', 'open all the edited images', 'makes all these changes to an image']
    for i in list:
        print(i)
        time.sleep(1)
        return

def user_select():
    image1 = Image.open('keshi.jpeg')
    image1.show()
    
user_select()