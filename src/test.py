import re
import numpy as np
import ast
# File se data read karein
with open("images_frame.txt", 'r') as file:
    data_str = file.read()

# Regular expression se spaces ko commas mein replace karein
data_str = re.sub(r"\s+", ", ", data_str)  # Ek ya zyada spaces ko comma se replace karein
data_str = data_str.replace("[, ", "[")   # Agar starting mein extra comma ho toh use remove karein
data_str = data_str.replace(", ]", "]")   # Agar ending mein extra comma ho toh use remove karein

# Modified data ko nayi file mein save karein
with open("modified_images_frame.txt", 'w') as file:
    file.write(data_str)

with open("modified_images_frame.txt", 'r') as file:
    data_str = file.read()

data_list = ast.literal_eval(data_str)
data_arr = np.array(data_list)