from os import walk


justTest = False
# justTest = True
allA = []
b = {}
a = {}

class imagesData():
    def __init__(self):
        mypath = "photos/dataset_brand_cut"
        global a
        global b
        global allA
        for (dirpath, dirnames, filenames) in walk(mypath):
            for i in range(len(dirnames)):
                childListA = []
                childListB = []
                for (ch_dirpath, ch_dirnames, ch_filenames) in walk(dirpath+'\\'+dirnames[i]):
                    for j in range(len(ch_filenames)):
                        if 'before' in ch_filenames[j]:
                            childListB.append(ch_dirpath+'\\'+ch_filenames[j])
                        elif 'after' in ch_filenames[j]:
                            childListA.append(ch_dirpath + '\\' + ch_filenames[j])
                        if justTest == True:
                            break
                a[dirnames[i]]=childListA
                if justTest == True:
                    b[dirnames[i]]=childListA
                else:
                    b[dirnames[i]]=childListB
                allA.extend(childListA)
            break
        print(a)
        print('*'*85000)
        print(b)
        print('*'*85000)
        print(allA)

if justTest == True:
    imagesData()
