### Program to Resize Images. Please input the Source Path and Resizing Shape ###

# Importing Modules and Libraries 
from os import listdir
from PIL import Image
import numpy as np

# Provide Source Path
# Don't forget to copy the Original Files in the Folder Before Resizing
source_path = r"D:/AI_ML_DL/Omdena_Projects/SA/Disaster_Images-26-11-22/Transformed/"

# Provide Required Shape in the Form of Tuple
shape = (300, 300)

# Images to be Saved in the Form of Array
array_list = []

# Creating a list of files present in the Source Path
folder = listdir(source_path)

# Following will Resize, Convert to Gray-scale and Save Images
for each_pic in folder:
    file = source_path + each_pic
    pic = Image.open(file)
    img_resized = pic.resize(shape)
    
    # If Images to be Converted to Gray-Scale, Enable the Following Line
    #img_resized = img_resized.convert(mode='L')
    
    # Saving Images 
    img_resized = img_resized.save(file)
    
# Converting Images to Numpy Array
for new_pic in folder:
    new_file = source_path + new_pic
    pics_to_array = np.array(Image.open(new_file))
    array_list.append(pics_to_array)

# Converting to Final Array
final_array = np.array(array_list) 

# Report the Process
print("All images have been resized to ({} x {})".format(shape[0], shape[1]))

#print("All Images have been Gray-scaled")
#print(pics_to_array.shape)

# Show Shape Information of Each Converted Image
print("Shape of Each Image is {}".format(pics_to_array.shape))

# Print the Shape of Final Array
print("Shape of Final Numpy Array is {}".format(final_array.shape))
print("Resizing Completed. Total Resized Pictures:{}".format(final_array.shape[0]))
