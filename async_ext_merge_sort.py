import asyncio
import datetime

allnumbers=[]
async  def openfile(filepath,filename):
    filehandle = open(filepath + filename, "r");
    mystr = filehandle.readlines()
    # size = len(mystr.split(','))
    # numlist = mystr.split(',')
    numlist = list(map(int, mystr))
    #print(numlist)
    for i in numlist:
        allnumbers.append(i)


def run():
    for i in range(10):
        loop.run_until_complete(openfile("input/","unsorted_"+str(i+1)+".txt"))
    #print(allnumbers)
    print(MergerSort(allnumbers))

loop = asyncio.get_event_loop()

def MergerSort(lists):
    if len(lists)<=1:
        return lists
    num=int(len(lists)/2)
    left=MergerSort(lists[:num])
    right=MergerSort(lists[num:])
    return Merge(left,right)
def Merge(left,right):
    r,l=0,0
    result=[]
    while l<len(left) and r<len(right):
        if left[l]<=right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    result+=list(left[l:])
    result+=list(right[r:])
    return result

if __name__ =='__main__':
    starttime = datetime.datetime.now()
    run()
    

fileName = "output/asynsorted_1.txt"
f=open(fileName,"w")
resultList =MergerSort(allnumbers)
for i in range(0, len(resultList)):
    f.write(f"{resultList[i]}\n")
f.close()    



endtime = datetime.datetime.now()
print((endtime - starttime))
elapse = endtime - starttime
fileName = "output/async_time.txt"
f=open(fileName,"w")
f.write(f"{elapse}")
f.close()