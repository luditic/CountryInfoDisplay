def openfile():
  f = open('countries.csv')
  return f

def displayinfo_1():
  global infofile 
  lines = infofile.readlines()
  #print(lines)
  for line in lines:
    print(line)




def regeions():
  global infofile
  lines = infofile.readlines()
  for i in range(0,len(lines),7):
    list_line = lines[i].split(',')
    print(list_line[0])

infofile = openfile()
displayinfo_1()