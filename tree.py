import os
from pathlib import Path


def directory_jawn(dir):
    for file in os.listdir(dir):
        for child in dir.iterdir():
            pyt8 = open('python_eight.txt', 'a')
            pyt8.writelines(file + '\n' + child + '\n')
            # pyt8.writelines(child + '\n')
            pyt8.close()

directory_jawn('/Users/rmaiale/dev/PythonFundamentals.Exercises.Part8')


