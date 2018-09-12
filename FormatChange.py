

import os             
# from os import rename, listdir
all_files = os.listdir("unknownFormat/")   # imagine you're one directory above test dir
thisFile = all_files[1]
# print (thisFile)
# !==>     ren *.* ?????.*
# !==>     ren *.* ???????????????????.*
# print(all_files)  # won't neces


# with open('tempture/decrease_temp.txt', "r") as f:
#     variable = f.readlines()

# 
# paths = (os.path.join(root, filename)
        # for root, _, filenames in os.walk('C:\Users\Admin\Documents\NRF\nrf rev\Delogger\unknownFormat')
        # for filename in filenames)
# 
# for path in paths:
    # the '#' in the example below will be replaced by the '-' in the filenames in the directory
    # newname = path.replace('#', '-')
    # if newname != path:
        # os.rename(path, newname)


# for fileName in os.listdir("unknownFormat/."):
#     os.rename(fileName, fileName.replace(all_files[fileName], "CHEESE_"))
# badprefix = "cheese_"
# fnames = listdir('unknownFormat/.')

# for fname in fnames:
#     if fname.startswith(badprefix*2):
#         rename(fname, fname.replace(badprefix, '', 1))

# thisFile = "mysequence.fasta"
# base = os.path.splitext(thisFile)[0]
# os.rename(thisFile, base + ".aln")

from pathlib import Path
from pathlib import PurePosixPath
filename = all_files[10]
new_filename = Path(filename).stem + ".txt"
PurePosixPath('unknownFormat/filename').suffix +".rdr"
# print (u)
# p = Path('unknownFormat/filename')
# p.rename('target')
p = Path('C:/Users/Admin/Documents/NRF/nrf rev/Delogger/unknownFormat/filename')
new_p = Path(p.parent.as_posix() + '/' + p.stem + '.aln')
# b = Path.PurePosixPath('unknownFormat/filename').stem 