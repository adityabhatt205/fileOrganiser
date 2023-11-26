# File Sorting Script

A Python script to organize files based on their extensions.

## Overview

This script automates the task of sorting files from a specified downloads folder into separate directories based on their file extensions. The user defines the folders for executables (`Exe`), other files (`Files`), and provides a list of file extensions to be moved to the executable folder.

## Usage

1. **Define Path Variables:**
   - `download`: The path to the downloads folder.
   - `exe_des`: The path to the folder for executables.
   - `file_des`: The path to the folder for other files.
   - `ext_list`: A list of file extensions to be moved to the executable folder.

   Example:
   ```python
   variables = Path(r"F:\Downloads", r"F:\Downloads\Exe", r"F:\Downloads\Files", ['exe', 'rar', 'msi', 'zip'])
   ```

2. **Run the Script:**
   Execute the script to automatically organize files from the downloads folder.

   ```bash
   python file_sorter.py
   ```

3. **Review Sorted Files:**
   Check the `Exe` and `Files` folders for organized files based on their extensions.

## Example

Suppose you have a downloads folder with various files, and you want to move executable files (with extensions 'exe', 'rar', 'msi', 'zip') to the `Exe` folder and other files to the `Files` folder. Configure the script with the appropriate paths and extensions, then run the script to sort the files accordingly.

## Note

Make sure to customize the script based on your specific folder paths and extension preferences.

