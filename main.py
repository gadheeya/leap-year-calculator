# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇



l4 = year%4;
l100 = year%100;
l400 = year%400;

if l4 == 0 :
  if l100 == 0:
    if l400==0:
      print("leap");
      
    else:print("not leap");
        
  else: print("leap");
else :
    print("not leap");
