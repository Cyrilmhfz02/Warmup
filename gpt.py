import os


file1=input("enter the csv file")

if os.access(file1,os.R_OK):
    with open(file1,"r") as f:
        col=input("enter the col name that you want to get the max value: ")
        header=f.readline().strip().split("\t")

        if col in header:
            index=header.index(col)
            max_val=0
            for line in f:
                if(int(line.strip().split("\t")[index])>max_val):
                    max_val=int(line.strip().split("\t")[index])
            
            print(max_val)