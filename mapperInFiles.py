
import os

counter = 0
all_files = os.listdir("BigData/")
Len_all_files = len(all_files)
for numberCounter in range(Len_all_files):
    Read_selected_files = all_files[numberCounter]
    Read_selected_files = str(Read_selected_files)

    print(Read_selected_files)
    
    inputmapper = raw_input("insert your map ==>  ")
    inputmapper = inputmapper.replace('\r', '')
    inputmapper = inputmapper + " "
    # inputmapper = str(inputmapper)
    # inputmapper = inputmapper + " "
    counter += 1
    strCounter = str(counter)
    print("counter =" ,counter)
    src = ""
    src ='BigData/' + Read_selected_files
    print(src)

    new_name = 'OutputAlgoritm/' + inputmapper + Read_selected_files 
    print("print(new_name)",new_name)
    os.rename(src, new_name)

