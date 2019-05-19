import random
Array=[]
for i in range(100):
   Array.append(random.randint(1,1000))
print(Array)
max_num=Array[0]
sum=0
for i in range(len(Array)):
        sum=sum+Array[i]

mean=sum/(len(Array))
print("Mean of Array: ", mean)
for i in range(1,len(Array)):
        if Array[i]>max_num:
                max_num=Array[i]
  
print ("Maximum Number: ",max_num)
print("Index of Maximum Number is: ",Array.index(max_num))
min_num=Array[0]
for i in range(1,len(Array)):
        if Array[i]<min_num:
                min_num=Array[i]
print ("Minimum Number:", min_num)
print("Index of Minimum Number is: ",Array.index(min_num))
