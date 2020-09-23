print("Calulate your results")
while True:
   a=int(input("Enter the marks for 1st subject:"))
   b=int(input("Enter the marks for 2nd subject:"))
   c=int(input("Enter the marks for 3rd subject:"))
   d=int(input("Enter the marks for 4th subject:"))
   e=int(input("Enter the marks for 5th subject:"))
   Average=int((a+b+c+d+e)/5)
   if Average<0:
      print("Improve your marks")
      break
   if Average==0 and Average<=50:
      print("You have failed")
      break
   if Average>=50 and Average<=60:
      print("Below average")
      break
   if Average>60 and Average<=70:
      print("Average")
      break
   if Average>70 and Average<=80:
      print("Good")
      break
   if Average>80 and Average<=90:
      print("Very Good")
      break
   if Average>90:
      print("Excellent")
      continue
print("Good Luck!")

