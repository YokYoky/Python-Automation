import os

# list of subdirectories to be created
Folders = ['Prelims/Notes', 'Midterms/Notes', 'Finals/Notes']

def create_directory_structure(path_dir, sem, subj):
    try:
        sem_int = int(sem)
        if sem_int == 1:
            semPath = "1stSem"
        elif sem_int == 2:
            semPath = "2ndSem"
        else:
            raise ValueError("Invalid semester input. Please enter 1 for 1stSem or 2 for 2ndSem.")
        subPath = subj.strip()

        # join user input to path_dir
        chdir_input = os.path.join(path_dir, semPath, subPath)
        print("Creating directory structure at: ", chdir_input)
        os.makedirs(chdir_input, exist_ok=True)

        for path_items in map(lambda x: os.path.join(chdir_input, x), Folders):
            os.makedirs(path_items, exist_ok=True)

        print("Directory structure created successfully!")
    except ValueError as e:
        print("Error: ", e)

# get user input for path_dir
path_dir = input("Enter the path to store your Sem and Subj Management: ")

# loop input
while True:
    sem = input("Enter 1 for 1stSem or 2 for 2ndSem (enter done to exit): ")
    sem = sem.strip().lower()
    if sem == "done":
        break
    subj = input("what subject: ")
    create_directory_structure(path_dir, sem, subj)
