
y=1
def factoriel(x):
    if(x<0):
        print('this is a negative number')
    elif(x==0 or x==1):
        return 1
    else:
        return x*factoriel(x-1)
    

def fizzBuzz(x):
    output=[]
    
    for i in range(1,x+1):
        if i%3==0 and i%5==0:
            output.append("FizzBuzz")

        elif i%3==0:
            output.append("Fizz")
        
        elif i%5==0:
            output.append("Buzz")
        
        else:
            output.append(str(i))
    
    result=' '.join(output)
    return result
    
       
def charFrequency(str):
    dict={}
    for i in str:
        if i in dict:
            dict[i] +=1
        else:
            dict[i]=1
    return dict

def retry():
    option=input("do you want to try another problem? (y/n)")
    if option=='n':
        global y
        y=2
            
while(y==1):
    choice=input("enter your problem of choice: (1/2/3): ")
    
    if choice=='1':
        nb=int(input("enter the number you want to factoriel: "))
        print(factoriel(nb))
        retry()
        
    elif choice=='2':
        nb=int(input("Enter a number to check the fizz buzz: "))
        print(fizzBuzz(nb))
        retry()
        

    elif choice=='3':
        str=input("enter the string you want to check: ")
        print(charFrequency(str))
        retry()

    else:
        print("wrong input")
        
