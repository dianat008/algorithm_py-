import time
# the time of start
shorou_s = round(time.time() * 1000)

# the code we have --بعنوان مثال (n is the Number of calculations )
# line 10 is the calculate
n = int(input())
s = 0
for i in range(n):
    s = s + i
# the time code is done   
payan_e = round(time.time() * 1000)
#The final answer
print((payan_e - shorou_s)/1000)