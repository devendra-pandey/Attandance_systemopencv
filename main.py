from PIL import Image
from pytesseract import pytesseract 
import pandas as pd
import os
from datetime import date
# date_time = datetime.datetime.now()
# date_value = date_time.strftime("%d/%m/%Y") 
# print(date_value)

path_to_tesseract = "C:/Program Files/Tesseract-OCR/tesseract.exe"


path_to_images = r'F:/Attandance/images/'


pytesseract.tesseract_cmd = path_to_tesseract

list_name = []

for root, dirs, file_names in os.walk(path_to_images):
    #Iterate over each file name in the folder
    for file_name in file_names:

        img = Image.open(path_to_images + file_name)

   
        text = pytesseract.image_to_string(img)
        print("#######")
        print(text)
        list_name.append(text)

print(list_name)

final_list = []

for i in list_name:
    print(type(i))
    abc = i.split("\n\n")
    print(abc)
    final_list.append(abc)

print("&&&&&&&&&&&&")
print(final_list)


# df = pd.DataFrame(final_list)

df = pd.DataFrame(final_list) 
print(df)

df2 = df.T

df3 = df2.iloc[3:-2]


# df4 = df3.rename(columns={"0": "Student Name"})
# print(df4)
df3.to_excel("attandance_"+ str(date.today()) +".xlsx",index=False)