import os

class Path:
    def __init__(self, download, exe_des, file_des, ext_list):
        self.download = download        # Downloads Folder
        self.exe_des = exe_des          # Folder for Executables
        self.file_des = file_des        # Folder for other files
        self.ext_list = ext_list        # List of file extensions to send in exe_des


variables = Path(r"F:\Downloads", r"F:\Downloads\Exe", r"F:\Downloads\Files", ['exe', 'rar', 'msi', 'zip'])

with (os.scandir(variables.download) as ls):
    for item in ls:
        if not item.name.startswith('.'):
            if len(item.name.split('.')) > 1:
                if item.name.split('.')[-1].lower() in variables.ext_list:
                    os.rename(item.path, variables.exe_des + "\\" + item.name)
                else:
                    os.rename(item.path, variables.file_des + "\\" + item.name)
