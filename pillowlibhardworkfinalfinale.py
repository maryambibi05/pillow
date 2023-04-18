from PIL import Image, ImageFilter
import time
import os
from os import listdir

def welcome_messages():
    print("Hello! In this program you'll have option to do the following to jpeg pictures:")
    list = ['resize', 'rotate', 'convert to png and save them', 'blur', 'convert B/W', 'chose which one to open', 'view all jpeg and png', 'change it to color blue', 'open all the edited images', 'makes all these changes to an image']
    for i in list:
        print(i)
        time.sleep(0.2)
    
def image_show():
    print('There are 10 image options to choose from and you can open all the images one by one and edit them as desired. The said 10 image options are: ')
    list2 = ['(e)ren', '(mi)kasa', '(l)evi', '(a)rmin', '(h)ange', '(m)iyamura', '(ka)neki', '(k)eshi', '(y)oasobi', '(ab)dul hannan']
    for a in list2:
        print(a)
        time.sleep(0.2)
    
    while True:
        user_input = input('Enter the letters (that are in brackets) of the image you want to open or enter "q" to quit: ')
        user_input = user_input.lower()
        
        if user_input == 'e':
            image1 = Image.open('eren.jpeg')
            image1.show()
             
        
        elif user_input == 'mi':
            image2 = Image.open('mikasa.jpeg')
            image2.show()
            
        
        elif user_input == 'l':
            image3 = Image.open('levi.jpeg')
            image3.show()
             
        
        elif user_input == 'a':
            image4 = Image.open('armin.jpeg')
            image4.show()
            
        
        elif user_input == 'h':
            image5 = Image.open('hange.jpeg')
            image5.show()
             
        
        elif user_input == 'm':
            image6 = Image.open('miyamura.jpeg')
            image6.show()
            
        
        elif user_input == 'ka':
            image7 = Image.open('kaneki.jpeg')
            image7.show()
             
        
        elif user_input == 'k':
            image8 = Image.open('keshi.jpeg')
            image8.show()
            break 
        
        elif user_input == 'y':
            image9 = Image.open('yoasobi.jpeg')
            image9.show()
     
        
        elif user_input == 'ab':
            image10 = Image.open('abdul hannan.jpeg')
            image10.show()
        
        
        elif user_input == 'q':
            break
        
        else:
            print('Invalid input! please try again.')
    
def image_png():
    print('You have an option to save these jpeg pictures as png')
    while True:
        user_input = input('Would you like convert them? Enter y/n: ')
        user_input = user_input.lower()
        if user_input == 'n':
            print('Alright bye:D')
            exit()
        elif user_input == 'y':
            for i in os.listdir('.'):
                if i.endswith('.jpeg'):
                    a = Image.open(i)
                    file_name, file_ext = os.path.splitext(i)
                    a.save('pngfolder/{}.png'.format(file_name))
        else:
            print('Invalid value. Please enter y/n.')

def image_resize():
    print('would you like to resize the images?')
    user_input = input('Enter your choice, y/n: ')
    user_input = user_input.lower()

    while True:
        print('what size would you like your photos to be? You have three options, 200, 400, or 600.')
        user = input('Enter your choice: ')
        if user == '200':
            resize_200 = (200, 200)
            for i in os.listdir('.'):
                    if i.endswith('.jpeg'):
                        a = Image.open(i)
                        file_name, file_ext = os.path.splitext(i)
                        
                        a.thumbnail(resize_200)
                        a.save('size200/{}_200{}'.format(file_name, file_ext))
            resize_200.show()
            break
                        
        elif user == '400':
            resize_400 = (400, 400)
            for i in os.listdir('.'):
                    if i.endswith('.jpeg'):
                        a = Image.open(i)
                        file_name, file_ext = os.path.splitext(i)
                        
                        a.thumbnail(resize_400)
                        a.save('size400/{}_400{}'.format(file_name, file_ext))
            resize_400.show()
            break
        
        elif user == '600':
            resize_600 = (600, 600)
            for i in os.listdir('.'):
                    if i.endswith('.jpeg'):
                        a = Image.open(i)
                        file_name, file_ext = os.path.splitext(i)
                        
                        a.thumbnail(resize_600)
                        a.save('size600/{}_600{}'.format(file_name, file_ext))
            break
        
        else:
            print('Invalid value. Please enter 200, 400, or 600.')  

def image_rotation():
    print('you can rotate an image now.')
    
    while True:
        angle_degrees = int(input('how much would you like to rotate all the images?: '))
        if type(angle_degrees) != int: 
            print('invalid input. Enter integers. Try again.')
            continue
        else:
            break
    
    if not os.path.exists('rotated_images'):
        os.makedirs('rotated_images')
    
    for file_name in os.listdir('.'):
        if file_name.endswith('.jpeg'):
            image1 = Image.open(file_name)
            rotated_image1 = image1.rotate(angle_degrees)
            rotated_image1.save('rotated_images/' + file_name)

    image1.show()
    
def image_bnw():
    print('You can also convert images into black and white.')
    while True:
        user_input = input('Would you like to turn all the images into black and white? y/n: ')
        if user_input == 'n':
            exit()
        elif user_input == 'y':
            break
        else:
            print('Invalid response. Try again.')
            
    if not os.path.exists('converted_images'):
        os.makedirs('converted_images')
    
    for file_name in os.listdir('.'):
        if file_name.endswith('.jpeg'):
            image = Image.open(file_name)
            bnw_image = image.convert('L')
            bnw_image.save('converted_images/' + file_name)  

def image_blur():
    print('You can blur an image too.')
    while True:
        try:
            user_input = int(input('How much would you like to blur eren image? Enter integer values only: '))
            
            image1 = Image.open('eren.jpeg')
            image1.filter(ImageFilter.GaussianBlur(user_input)).save('eren_blur.jpeg')
            break
        
        except ValueError:
            print('Invalid input. Try again with an integer.')
    image1.show()
            
def image_diff_color():
    
    while True: 
        user_input = input('Would you like to convert mikasa picture to a different color? y/n: ')
        user_input = user_input.lower()
        
        if user_input == 'y':
            red_image = Image.open('mikasa.jpeg')
            red_image = red_image.convert('RGB')
            width, height = red_image.size
            
            for x in range(width):
                for y in range(height):
                    r, g, b = red_image.getpixel((x, y))
                    red_image.putpixel((x, y), (r, 0, 0))
                    
            red_image.save('mikasa_red.jpeg')
            break
        
        elif user_input == 'n':
            break
        
        else:
            print('Invalid input. Try again.')
            
    red_image.show()
    


folder2 = 'pngfolder'
def view_png_DUPE(filename):
    return filename.lower().endswith(('.jpeg', '.png'))

def view_png_images(folder):
    for filename in os.listdir(folder):
        if view_png_DUPE(filename):
            filepath = os.path.join(folder, filename)
            image = Image.open(filepath)
            image.show()

def view_bnw_images():
    folderbnw = 'converted_images'

    for filename in os.listdir(folderbnw):
        filepath = os.path.join(folderbnw, filename)
        try:
            with Image.open(filepath) as img:
                if img.mode == 'L':
                    img.show()
        except IOError:
            continue
             
def view_rotated_images():
    
    messedup_folder = 'rotated_images'
    for filename in os.listdir(messedup_folder):
        file = os.path.join(messedup_folder, filename)
        try:
            with Image.open(file) as img:
                if hasattr(img, '_getexif'):
                    exif = img._getexif()
                    if exif:
                        looks = exif.get(0x0112)
                        if looks in [3, 6, 8]:
                            if looks == 3:
                                angle = 180
                            elif looks == 6:
                                angle = 270
                            elif looks == 8:
                                angle = 90
                            img = img.rotate(angle, expand=True)
                img.show()
        except IOError:
            continue
        
def view_resized_200():
    folder_resize = 'size200'

    for filename in os.listdir(folder_resize):
        file = os.path.join(folder_resize, filename)
        try:
            with Image.open(file) as img:
                if img.size != (200, 200):
                    img.show()
        except IOError:
            continue
        
def view_resized_400():
    folder_resize = 'size400'

    for filename in os.listdir(folder_resize):
        file = os.path.join(folder_resize, filename)
        try:
            with Image.open(file) as img:
                if img.size != (400, 400):
                    img.show()
        except IOError:
            continue
        
def view_resized_600():
    folder_resize = 'size600'

    for filename in os.listdir(folder_resize):
        file = os.path.join(folder_resize, filename)
        try:
            with Image.open(file) as img:
                if img.size != (600, 600):
                    img.show()
        except IOError:
            continue
    
def view_jpeg_images():
    folder_path = 'jpeegfolder'

    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            img_path = os.path.join(folder_path, filename)
            with Image.open(img_path) as img:
                img.show()       

def view_all_edits_MAIN():
    while True:
        user = input('Would like to view all png files? y/n: ')
        user = user.lower()
        if user == 'y':
            view_png_images(folder2)
            break 
                
        elif user == 'n':
            break
        
        else:
            print('Invalid Input. Try again.')
       
    while True:
        user = input('Would like to view all black and white files? y/n: ')
        user = user.lower()
        if user == 'y':
            view_bnw_images()
            break 
                
        elif user == 'n':
            break
        
        else:
            print('Invalid Input. Try again.')
            
    while True:
        user = input('Would like to view all rotated files files? y/n: ')
        user = user.lower()
        if user == 'y':
            view_rotated_images()
            break 
                
        elif user == 'n':
            break
        
        else:
            print('Invalid Input. Try again.')
            
    while True:
        user = input('Would like to view resized to 200 files? y/n: ')
        user = user.lower()
        if user == 'y':
            view_resized_200
            break 
                
        elif user == 'n':
            break
        
        else:
            print('Invalid Input. Try again.')
            
    while True:
        user = input('Would like to view resized to 400 files? y/n: ')
        user = user.lower()
        if user == 'y':
            view_resized_400
            break 
                
        elif user == 'n':
            break
        
        else:
            print('Invalid Input. Try again.')
            
    while True:
        user = input('Would like to view resized to 600 files? y/n: ')
        user = user.lower()
        if user == 'y':
            view_resized_600
            break 
                
        elif user == 'n':
            break
        
        else:
            print('Invalid Input. Try again.')
            
    while True:
        user = input('Would like to view eren blurred file? y/n: ')
        user = user.lower()
        if user == 'y':
            image_blur()
            break 
                
        elif user == 'n':
            break
        
        else:
            print('Invalid Input. Try again.')
            
    while True:
        user = input('Would like to view mikasa colored file? y/n: ')
        user = user.lower()
        if user == 'y':
            image_diff_color()
            break 
                
        elif user == 'n':
            break
        
        else:
            print('Invalid Input. Try again.')
            
    while True:
        user = input('Would like to view all jpeg files? y/n: ')
        user = user.lower()
        if user == 'y':
            view_jpeg_images()
            break 
                
        elif user == 'n':
            break
        
        else:
            print('Invalid Input. Try again.')
            
    return
            
    
welcome_messages()
image_show()
image_png()
image_resize()
image_rotation()
image_bnw()
image_blur()
image_diff_color()           
view_jpeg_images()
