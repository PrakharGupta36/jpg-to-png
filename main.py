from PIL import Image
import os

def all_images():
    jpg_img = [img for img in os.listdir() if img.endswith('.jpg')]
    if len(jpg_img) == 0:
        print("No jpeg images found")
    for i in range(len(jpg_img)): # loop over list of images
        x = Image.open(f"./{jpg_img[i]}") 
        filename = jpg_img[i]
        img_original =  filename.rsplit( ".", 1 )[ 0 ]
        x.save(f"{img_original}.png",dpi=[10,10],quality = 50)
    
def single_image():
    file_path = input("Enter jpg image name to convert (not extension) : ")
    x = Image.open(f"./{file_path}.jpg")
    x.save(f"{file_path}.png",dpi=[300,300],quality = 50)

def user():
    ask_user = int(input("Do you want to convert all jpg images (1) or single jpg image (2) :"))
    if ask_user == 1:
        all_images()
    elif ask_user == 2:
        single_image()
    else:
        print("Please choose 1 or 2\n")
        user()


if __name__ == '__main__':
    user()