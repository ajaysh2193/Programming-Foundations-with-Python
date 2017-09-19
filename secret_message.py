import os

def rename_files():
    
    file_list = os.listdir(r"G:\Secret_Message\prank\new file")
    print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir(r"G:\Secret_Message\prank\new file")
    
    for file_name in file_list:
        print("Old Name "+file_name)
        print("New Name "+file_name.translate(None, "0123456789"))
        os.rename (file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files() 
