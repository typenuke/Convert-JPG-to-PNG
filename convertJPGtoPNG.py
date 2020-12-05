import sys
import os
from PIL import Image

#grab first and second argument
jpg_fol = sys.argv[1];
png_fol = sys.argv[2];
#check new/ exists, if not create it
if not os.path.isdir(png_fol):
    os.mkdir(png_fol)
#loop through Pokedex folder
count = 0
for file_name in os.listdir(jpg_fol):
    if file_name.endswith('.jpg'):
        img = Image.open(f'{jpg_fol}{file_name}')
        #get filename with no filetype
        name_clean = os.path.splitext(file_name)[0]
        # convert and save
        img.save(f'{png_fol}{name_clean}.png', 'png')
        count+=1
        print(f'{count} done')