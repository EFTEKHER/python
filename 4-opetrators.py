from datetime import date
a=input(" whats your name ?\n");
today=date.today();
print("Hello "+a);
age=input("How old are you?\n");
print("your age is"+age);
birth_year=int(today.year)-int(age);
print("Your bitrh_year:"+str(birth_year));
