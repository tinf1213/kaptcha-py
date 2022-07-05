import os
os.chdir('C:/Users/ericd/PycharmProjects/pythonProject')
file = os.listdir()
index = 0
print(file)
for k in file:
    path = k
    index += 1
    #print(os.getcwd())
    files = os.listdir(path)
    print(files)
    n = 0
    re = 51
    for i in files:
        old = i
        os.chdir(path)
        new = str(re)+'.jpg'
        os.rename(old, new)
        re += 1
