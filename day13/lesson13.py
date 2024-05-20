"""1) დაწერეთ პროგრამა, რომელიც ეკითხება მომხმარებლის ასაკს 
და შემდეგ დაბეჭდავს შეტყობინებას ასაკის მიხედვით: using(if-elif-else)
If the age is less than 18, print "You are a minor."
If the age is between 18 and 65, print "You are an adult."
If the age is 65 or older, print "You are a senior citizen."

2) შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი 
და შემდეგ დაბეჭდოს რიცხვი ლუწია თუ კენტი. გამოიყენეთ ფორ ციკლი,
რომ სთხოვოთ მომხმარებელს 5 რიცხვი და შეამოწმეთ ხუთივე რიცხვი.

3) დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს ქულები ასოებით 
(A, B, C, D ან F) და შემდეგ დაბეჭდოს შეტყობინება ასოების მიხედვით: using(if-elif-else)
If the grade is A, print "Excellent!"
If the grade is B, print "Good job!"
If the grade is C, print "You passed."
If the grade is D, print "You can do better."
If the grade is F, print "You failed."

4) დაწერეთ პროგრამა, რომელიც ბეჭდავს რიცხვებს 1-დან 10-მდე while ციკლის გამოყენებით

5) შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი 1-დან 10-მდე.
გამოიყენეთ while loop, რათა გააგრძელოთ კითხვა, სანამ მომხმარებელი სწორად არ გამოიცნობს

6) დაწერეთ პროგრამა, რომელიც დაბეჭდავს მოცემული რიცხვის (მაგ 5) პირველ 10 ჯერადს for loop-ის გამოყენებით.

7) შექმენით პროგრამა, რომელიც ბეჭდავს უკუთვლას 10-დან 1-მდე for loop-ის გამოყენებით."""

#1
age = int(input("Please enter your age: "))

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

#2
for i in range(5):
    a = int(input('შეიყვანეთ რიცხვი'))
    if a%2==0:
        print('ლუწია')
    else:
        print('კენტია')

#3
grade = input("Please enter your grade (A, B, C, D, or F): ")

if grade == 'A':
    print("Excellent!")
elif grade == 'B':
    print("Good job!")
elif grade == 'C':
    print("You passed.")
elif grade == 'D':
    print("You can do better.")
elif grade == 'F':
    print("You failed.")
else:
    print("Invalid grade entered.")

#4
num = 1

while num <= 10:
    print(num)
    num += 1

#5
guess = int(input("გთხოვთ, მოითხოვეთ რიცხვი 1-დან 10-მდე: "))
secret_number = 7

while guess != secret_number:
    print("თქვენ არ შეეხებათ სწორად სცადეთ თავიდან")
    guess = int(input("გთხოვთ, შეიყვანოთ რიცხვი 1-დან 10-მდე: "))

print("გილოცავთ! თქვენ სწორად გამოიცნოთ რიცხვი 7")

#6
num = 5
for i in range(1,11):
    print(num*i)

#7
for i in range(10,0,-1):
    print(i)
