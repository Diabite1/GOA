"""2) გავაკეთოთ სიმულაცია სადაც მომხმარებელს შეეძლება რეგისტრაცია,
მომხმარებელი შემოიტანს 3 ცვლადს, სახელი, გვარი, ასაკი 
(int ფუნქცია არ არის სავალდებულო ასაკთან)
საბოლოოდ ამ ყველაფერს print'ის მეშვეობით გამოიტანთ ტერმინალში.
3) მომხმარებელს შემოატანინეთ 3 რიცხვი. შეინახეთ ისინი ცვლადებში
 და მათზე ცალცალკე გამოიტანეთ print'ის მეშვეობით
   გამრავლება, გაყოფა, მიმატება, გამოკლება. (თუ არ იცით კონკრეტული
     მათემატიკური ოპერაციები დასერჩეთ google'ში. e.g: how to multiply numbers in python)"""

# user enters their name,lastname and age
name = input("please enter your name")
lastname = input("pelase enter your lastname")
age = input("please enter your age")

# declaring variables: name,age and age
print(name,lastname,age)

# user enters 3 numbers of their choice
num1 = int(input("please enter a number of your choice"))
num2 = int(input("please enter a number of your choice"))
num3 = int(input("please enter a number of your choice"))

#declaring variavles: num,num2 and num3
print("addition")
print(num1 + num2)
print(num1 + num3)
print(num2 + num3)

print("subtraction")
print(num1 - num2)
print(num1 - num3)
print(num2 - num3)

print("multiplication")
print(num1 * num2)
print(num1 * num3)
print(num2 * num3)

print("division")
print(num1 / num2)
print(num1 / num3)
print(num2 / num3)

