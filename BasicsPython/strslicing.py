# STRING SLICING PRACTICE

text = "kodnest"
print(text[2:2]) #empty

print("Original String:", text)
print("--------------------------------")

# POSITIVE INDEX SLICING
print("Q1:", text[0:4])    
print("Q2:", text[1:5])    
print("Q3:", text[2:7])    
print("Q4:", text[3:6])    
print("Q5:", text[4:7])    

# NEGATIVE INDEX SLICING
print("Q6:", text[-4:-1])  
print("Q7:", text[-7:-3])  
print("Q8:", text[-5:-2])  
print("Q9:", text[-6:-4])  
print("Q10:", text[-3:-1]) 

# MIXED POSITIVE & NEGATIVE
print("Q11:", text[1:-1])  
print("Q12:", text[2:-2])  
print("Q13:", text[0:-3])  
print("Q14:", text[-5:6])  
print("Q15:", text[-4:7])  

# EDGE CASES
print("Q16:", text[2:2])   
print("Q17:", text[5:3])   
print("Q18:", text[10:15]) 
print("Q19:", text[-10:3]) 
print("Q20:", text[-2:5])  

print("--------------------------------")

# String Slicing Questions on "KODNEST"

s = "KODNEST"

print(s[0:4])
print(s[2:7])
print(s[:5])
print(s[3:])
print(s[-4:])

print(s[0:7:2])
print(s[1:6:2])
print(s[::3])
print(s[2:7:3])
print(s[5:7:1])

print(s[6:0:-1])
print(s[::-1])
print(s[5:1:-2])
print(s[4:0:-1])
print(s[-1:-6:-1])

print(s[3:6:-1])
print(s[1:5:-1])
print(s[-2:0:-2])
print(s[0:7:-1])
print(s[3::-1])