import os

#mkdir rename_test;cd rename_test;mkdir folder\ 1; mkdir folder\ 1/folder\ 2;touch folder\ 1/hel\ lo.txt; touch folder\ 1/folder\ 2/\ \ hi.txt;touch \ \ space\ \ .txt;mkdir \ \ \ \ myfolder\ \ \ 3;touch \ \ \ \ myfolder\ \ \ 3/file.txt;cd


def clean_dir(dirpath):
    os.chdir(dirpath)
    files = []
    for (dirpath, dirnames, filenames) in os.walk('.'):
        files.extend(filenames)
        break
    files = [i for i in files if i[0] != '.'] #remove hidden files
    files = [i for i in files if ' ' in i] #only include files with space
    dirs = [name for name in os.listdir('.') if os.path.isdir(os.path.join('.', name)) ]
    dirs = [i for i in dirs if i[0] != '.'] #remove hidden directories
    dirs = [i for i in dirs if ' ' in i] #only include dirs with space
    for i in files:
        os.system('mv ' + i.replace(' ', '\ ') + ' ' + ''.join(i.split()))
    for i in range(len(dirs)):
        os.system('mv ' + dirs[i].replace(' ', '\ ') + ' ' + ''.join(dirs[i].split()))
        dirs[i] = ''.join(dirs[i].split())
    for i in dirs:
        clean_dir(i)
        os.chdir('..')

dirpath = '.'
clean_dir(dirpath)

