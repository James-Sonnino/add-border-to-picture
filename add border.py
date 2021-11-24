import os
from PIL import Image

#This script assumes your pictures are in a folder called "faces" in the same location as the script
dir_path = os.getcwd() + "\\faces\\"

#go through every picture in the folder
for pic in os.listdir(dir_path):
    old_im = Image.open(dir_path + pic)
    old_size = old_im.size

    #create a new image of solid grey, 800x800 pixel, then paste the old image in the center
    new_size = (800,800)
    new_im = Image.new("RGB", new_size, (128, 128, 128))
    new_im.paste(old_im, ((new_size[0]-old_size[0])//2, (new_size[1]-old_size[1])//2))
    #overwrite the old image
    new_im.save(dir_path + pic)