def openfile():
  f = open('countries.csv')
  return f

def desplayinfo_1():
  global infofile 
  lines = infofile.readlines()
  print(lines)

def displayinfo():
  global infofile
  lines = infofile.readlines
  for i in range(0,len(lines),7):
    print(1,lines[i])

infofile = openfile()
displayinfo()