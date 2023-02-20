from functools import partial
import os

# main directory
# change the current_dir to your designated directory/folder path to create the folders
# current_dir = "<your_folder_path>"
current_dir = "C:\\Users\\cvanj\\Desktop\\CPEtest\\"
# list of subdirectories to be created
Folders = ['Prelims/Notes', 'Midterms/Notes', 'Finals/Notes']

print("Current Directory: ", current_dir)

# loop input 
while True:
    sem = input("1stSem or 2ndSem (enter done to exit): ")
    sem = sem.upper()
    if sem == "DONE":
        break
    subj = input("what subject: ")
    #remove whitespaces from user input
    semPath = sem.strip()
    subPath = subj.strip()
    

    # join user input to current_dir
    chdir_input = os.path.join(current_dir, semPath, subPath)
    isdir = os.path.isdir(chdir_input)
    print(os.linesep + chdir_input)
    
    # exist_ok=True ignore existing files
    # os.makedirs create multiple directories at once
    os.makedirs(chdir_input, exist_ok=True)

    
    concat_root_path = partial(os.path.join, chdir_input)
    make_directory = partial(os.makedirs, exist_ok=True)
    
    for path_items in map(concat_root_path, Folders):
        make_directory(path_items)
    print("Directory exist. Creating Subfolders...\n")
