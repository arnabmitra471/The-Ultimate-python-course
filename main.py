import os

root_dir = "C:/Users/User/Documents/B-Tech/2nd year/100Days of code revision"
for i in range(1,101):
    folder_name = f"Day_{i}"
    folder_path = os.path.join(root_dir,folder_name)
    # print(f"folder path  for day {i} is {folder_path}")
    os.makedirs(folder_path)

    file_path = os.path.join(folder_path,"main.py")

    with open(file_path,"w") as f:
        f.write(f"# This is the main.py file for day {i}")

print("100 folders with main.py created successfully")

