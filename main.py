from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
def find_next(s):
    i1 = s.find('"')
    s = s[i1 + 1:]
    i2 = s.find('"')
    found = s[0:i2]
    s = s[i2 + 1:]
    return s, found
if __name__ == '__main__':

    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    youtube = ""
    file = open(filename, "r").read()
    while '\tTITLE ' in file:
        index = file.find('\tTITLE ')
        file = file[index:]
        file, title = find_next(file)
        file, interpret = find_next(file)
        i1 = file.find('INDEX ')
        file = file[i1+9:]
        i2 = file.find('\n')
        time = file[0:i2]
        file = file[i2+1:]
        youtube = youtube + time + " " + interpret + " - " + title + "\n"
    print(youtube)
