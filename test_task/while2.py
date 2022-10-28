totalNo = None
sum=None
n = 0
while (n == -1):
    n = input("Enter Number: ")
    n = int (n)
    sum += n
    totalNo +=1
     
average  = sum / totalNo
print ("average of", totalNo ,"using while loop ", average)