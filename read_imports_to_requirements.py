import os;

nr = []
files = [] #= os.listdir("./") # list all files and dirs of this dir

def rec_dir(dir): #recursively go through all dirs
  for f in os.listdir(dir):
    if os.path.isfile(os.path.join(dir,f)):
      if f == os.path.basename(__file__) or f.find(".py") == -1: # skip this file and non python files
        continue
      fo = open(os.path.join(dir,f)) # read all imports in files, add to list
      for l in fo:
        if (l == "" or len(l.split("import")) == 1):
          break
        if l.split(" ")[1].endswith(";"): 
          nr.append(l.split(" ")[1].rstrip(";")) 
        else: 
          nr.append(l.split(" ")[1])
      fo.close()
    else:
      rec_dir(os.path.join(dir,f))

rec_dir("./")

nr = list(dict.fromkeys(nr)) # remove dupe imports
imps = ""

for s in nr: #convert to string
  imps+=s

f = open("./requirements.txt", "w") # write new imports to req.txt
f.write(imps)
f.close()