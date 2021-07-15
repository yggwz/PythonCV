# 编写者:刘港
# 开发时间:2021/7/15 15:36
import os
import shutil

lit=[[1,23],[23,4],[12,55]]
with open('C:/Users/LGG/Desktop/111.txt','w+') as file:
    for i in range(len(lit)):
        file.write(str(lit[i]))
        print(lit[i])
        if i < len(lit)-1:
            file.write('\n')
