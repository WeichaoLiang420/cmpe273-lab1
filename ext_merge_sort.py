import datetime
def openfile(filepath,filename):
    filehandle = open(filepath + filename, "r");
    mystr = filehandle.readlines()
    #size = len(mystr.split(','))
    #numlist = mystr.split(',')
    numlist = list(map(int, mystr))
    return numlist



import threading

# 添加线程  创建5个线程名
threadList = ["unsorted_1.txt", "unsorted_2.txt", "unsorted_3.txt", "unsorted_4.txt", "unsorted_5.txt","unsorted_6.txt","unsorted_7.txt","unsorted_8.txt","unsorted_9.txt","unsorted_10.txt"]
threads = []
allnumber=[]
class ReadFileThread (threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        # self.threadID = threadID
        self.name = name
    def run(self):
        print ("开始线程：" + self.name)
        for i in openfile("input/",self.name):
            allnumber.append(i)
        print ("退出线程：" + self.name)

# 创建新线程
for tName in threadList:
    thread = ReadFileThread(tName)
    thread.start()
    threads.append(thread)


# 创建新线程

# 开启新线程
for t in threads:
    t.join()  #
print(allnumber)

#进行外部排序
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
print(MergerSort(allnumber))

#write data to the file
#f=openfile("output/synunsorted_1.txt","w")
#f.write(MergerSort(allnumber))
#f.close()
if __name__ =='__main__':

    starttime = datetime.datetime.now()

    fileName = "output/synunsorted_1.txt"
    f=open(fileName,"w")
    resultList = MergerSort(allnumber)
    for i in range(0, len(resultList)):
        f.write(f"{resultList[i]}\n")
    f.close()

#long running

    endtime = datetime.datetime.now()
    print((endtime - starttime))
    elapse = endtime - starttime
    fileName = "output/time.txt"
    f=open(fileName,"w")
    f.write(f"{elapse}")
    f.close()