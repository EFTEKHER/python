from cmath import sqrt

import math 
a=input('enter a');
b=input('enter b');
print('berfore swaping\n');
print(a+"  "+b);
print("after swaping\n");
temp=a;
a=b;
b=temp;


print(a+"  "+b);
print('ax^2+bx+c:\n');
a=input("enter a:");
b=input("enter b:");
c=input("enter c:");
a=int(a);
b=int(b);
c=int(c);
x=2;
x=math.sqrt(pow(b,2)-4*a*c);

x1=0;
x2=0;
x1=(-b+x)/2*a;
x2=(-b-x)/2*a;
print("your root is:",x1,x2);

