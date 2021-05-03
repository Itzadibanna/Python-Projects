import  os
import requests
check =int(input("Enter 1 to read Data From directory \n Enter 2 from Url "))
if check ==2:
    file = input("Enter Url")
    text =requests.get(file).content


else :
     file = input("Enter File Path")
     path= os.getcwd()+file
     data = open(path)
     text = data.readline()


#data =input()
def Counter(Text):
        List = Text.split()
        Data_set ={}
        Counter =0
        for data in List :
            Counter=0
            for data_cp in List:
                if data==data_cp:
                    Counter =1+Counter
            Data_set[data]=Counter
        return Data_set



print(Counter(text))
