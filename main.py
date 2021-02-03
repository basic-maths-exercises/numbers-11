def isRational( p, q ) :
  # Your code goes here
  if q==0 : return 0
  return 1
  
print("The statement 3/4 is rational is", isRational(3,4))
print("The statement 4/4 is rational is", isRational(4,4))
print("The statement 4/3 is rational is", isRational(4,3))
print("The statement 4/0 is rational is", isRational(4,0))
print("The statement 0/4 is rational is", isRational(0,4))
