### Program to Transform Images by Rotating 45 Degrees, and Flippings ###
### Horizontally and Vertically ###

# Import Modules
from os import listdir
from PIL import Image

# Provide Source and Destination Paths
source_path = r"D:/AI_ML_DL/Omdena_Projects/SA/Disaster_Images-26-11-22/source/"
dest_path = r"D:/AI_ML_DL/Omdena_Projects/SA/Disaster_Images-26-11-22/Transformed/"

# Counters for Rotations, Horizontal Flips and Vertical Flips
r = 0
hf = 0
vf = 0

# Creating a list of files present in the Source Path
folder = listdir(source_path)

# Start Transforming of each Image
for each_pic in folder:
    file = source_path + each_pic
    pic = Image.open(file)
    
    # Rotating 45 Degrees with New File Names
    rot_45 = pic.rotate(45)
    rot_45 = rot_45.save(dest_path + "rot_45_" + str(r) + ".jpg")
    r += 1
    
    # To use 90 Degrees Rotation, use:
    #rot_90 = pic.transpose(Image.Transpose.ROTATE_90)
    
    # Horizontal Flip with New File Names
    hoz_flip = pic.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    hoz_flip = hoz_flip.save(dest_path + "flr_" + str(hf) + ".jpg")
    hf += 1
    
    # Vertical Flipping with New File Names
    ver_flip = pic.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    ver_flip = ver_flip.save(dest_path + "ftb_" + str(vf) + ".jpg")
    vf += 1

# Report Completion of the Process with Total Images Saved
print("\n Finished Rotating 45 Degrees and Flipping Horizontally & Vertically.")
print("\n Total {} Images saved".format(r + hf + vf))