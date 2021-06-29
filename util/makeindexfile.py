import hashlib
import os

######################################################################
def smd5(path):
    md5 = hashlib.md5()
    with open(path,"rb") as file:
        while True:
            data = file.read(2024)
            if not data:
                break
            md5.update(data) #update添加时会进行计算
        file.close()
    return md5.hexdigest()

# path="C:\\Users\\admin\\Desktop\\Proto\\DSC01628-Edit.jpg"
# print(smd5(path))

######################################################################

def treecall(dirpath,indexFile):
    for root,dirs,files in os.walk(dirpath):
        for dir in dirs:
            treecall(root+"\\"+dir,indexFile)
        for file in files:
            target_path=root+"\\"+file
            print(target_path+":")
            md5str=smd5(target_path)
            print("\t\t=>"+md5str)
            indexFile.write(target_path+" -> "+md5str+"\n");                

# dir="Q:\\publish"
# indexFile=open(dir+"\\index.txt", "w")
# treecall(dir,indexFile)
# indexFile.close()