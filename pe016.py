#Project euler problem 16

n = 2**1000  

#initialising the sum to be zero 
tot=0 
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print(tot)    
