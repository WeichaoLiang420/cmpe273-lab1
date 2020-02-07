#abs_fp = "/Users/jinhanzhou/Desktop/273/cmpe273-spring20-labs-master/lab1/input/unsorted_1.txt"

#f=open("input/unsorted_1.txt","r") 
#f=open(abs_fp,"r")
#mem=f.readlines()
#print(mem)

#for i in range(len(mem)):
   # mem[i] = mem[i].strip('\n')
#print(mem)
#trs=int(line)
#
def read_file(abs_txt1):
    txt1=open(abs_txt1,'r')
    mem=txt1.readlines()
    for i in range(len(mem)):
        mem[i]=mem[i].strip('\n')
        mem[i]=int(mem[i]) 
    return mem


txt1="/Users/jinhanzhou/Desktop/273/cmpe273-spring20-labs-master/lab1/input/unsorted_1.txt"
txt2="/Users/jinhanzhou/Desktop/273/cmpe273-spring20-labs-master/lab1/input/unsorted_2.txt"
txt3="/Users/jinhanzhou/Desktop/273/cmpe273-spring20-labs-master/lab1/input/unsorted_3.txt"
txt4="/Users/jinhanzhou/Desktop/273/cmpe273-spring20-labs-master/lab1/input/unsorted_4.txt"
txt5="/Users/jinhanzhou/Desktop/273/cmpe273-spring20-labs-master/lab1/input/unsorted_5.txt"
txt6="/Users/jinhanzhou/Desktop/273/cmpe273-spring20-labs-master/lab1/input/unsorted_6.txt"
txt7="/Users/jinhanzhou/Desktop/273/cmpe273-spring20-labs-master/lab1/input/unsorted_7.txt"
txt8="/Users/jinhanzhou/Desktop/273/cmpe273-spring20-labs-master/lab1/input/unsorted_8.txt"
txt9="/Users/jinhanzhou/Desktop/273/cmpe273-spring20-labs-master/lab1/input/unsorted_9.txt"
txt10="/Users/jinhanzhou/Desktop/273/cmpe273-spring20-labs-master/lab1/input/unsorted_10.txt"


list_1 = read_file(txt1)
list_1.sort()
#print(list_1)
list_2 = read_file(txt2)
list_2.sort()
#print(list_2)
list_3 = read_file(txt3)
list_3.sort()
#print(list_3)
list_4 = read_file(txt4)
list_4.sort()
#print(list_4)
list_5 = read_file(txt5)
list_5.sort()
#print(list_5)
list_6 = read_file(txt6)
list_6.sort()
#print(list_6)
list_7 = read_file(txt7)
list_7.sort()
#print(list_7)
list_8 = read_file(txt8)
list_8.sort()
#print(list_8)
list_9 = read_file(txt9)
list_9.sort()
#print(list_9)
list_10 = read_file(txt10)
list_10.sort()
#print(list_10)
for i =list.index:
    minVal=min(list_1[i],list_2[i])
    sortedval=minVal.append()
print（sortedval）
#a= min(list_10[0],list_1[0])
#print(a)

#createfolder('/Users/jinhanzhou/Desktop/273/cmpe273-spring20-labs-master/lab1/')
#fileobject=open('sorted_1.txt','w')
#for i in mem:
#    fileobject.write(str(i))
#    fileobject.write('\n')
#fileobject.close() 


'''import numpy as np
array1=np.array([list_1])
array2=np.array([list_2])
array3=np.array([list_3])
array4=np.array([list_4])
array5=np.array([list_5])
array6=np.array([list_6])
array7=np.array([list_7])
array8=np.array([list_8])
array9=np.array([list_9])
array10=np.array([list_10])
mymatrix=np.mat([[array1],[array2],[array3],[array4],[array5],[array6],[array7],[array9],[array10]])
print(mymatrix)'''

#mymatrix= np.mat([[list_1],[list_2],[list_3],[list_4],[list_5],[list_6],[list_7],[list_8],[list_9],[list_10]])
#print(mymatrix)

'''def mergelists(self, lists):
    x=[]
    while lists:
        minVal=min([lists[i] for i in range(len(lists))])
        index=0
        for l.val ==minVal:
            x.append[l]
            if l.next is None:
                lists.remove(l)
            else:
                lists[index].next=l.next
            break
        index +=1
    x_length = len(x)-1
    for i in range(x_length):
        x[i].next = x[i+1] 
    x[x_length]   '''           

