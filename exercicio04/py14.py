import os

os.chdir('/Users/fons/Desktop/ex10')

 print(os.getcwd())

 print(dir(os))

 Print all the current file names
for f in os.listdir():
    If .DS_Store file is created, ignore it
    if f == '.DS_Store':
        continue

    file_name, file_ext = os.path.splitext(f)
    print(file_name)

    f_title, f_course, f_number = file_name.split('-')

     print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

     Need to remove whitespace
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_number = f_number.strip()

   
    f_number = f_number.strip()[1:]

    
    f_number = f_number.strip()[1:].zfill(2)

     print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

    
    print('{}-{}{}'.format(f_number, f_title.strip(), file_ext.strip()))

    new_name = '{}-{}{}'.format(file_num, file_title, file_ext)

    os.rename(fn, new_name)

 print(len(os.listdir()))
