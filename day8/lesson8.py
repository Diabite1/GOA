"""3) შექმენით 2 ცვლადი სადაც შეტანილი გექნებათ ადამიანის წონა და სიმაღლე,
 (required_weight,required_height) რომლის მნიშვნელობაც იქნება 50 და 170 ,
შემდეგ მომხმარებელს შემოატანინეთ მისი წონა input ფუნქციის მეშვეობით
და შეამოწმეთ მომხმარებლის წონა თუ უდრის required_weight ცვლადს
და მომხარებლის სიმაღლე თუ უდრის required_height,
აგრეთვე მეორე პრინტში შეამოწმეთ თუ აღემატება წონას და ნაკლებია სიმაღლეზე,
თითქმის ყველა კომბინაცია შედარების ოპერატორების.
თქვენ გაგზავნეთ
4) მომხმარებელს შემოატანინეთ აჯიმანიებისა და ბუქნების რაოდენობა,
ტქვენ კი შეამოწმეთ უდრის ტუ არა აჯიმანიების რაოდენობა აუცილებელს
ან ბუქნების რაოდენობა აუცილებელს"""

# variables for required height and weight
required_weight = 50
required_height = 170

# variables for users height and weight
users_weight = input("please enter your weight")
users_height = input("plese enter your height")

# comparing users height and weight with required height and weight
print(required_weight == users_weight)
print(required_weight > users_weight)
print(required_weight < users_weight)
print(required_height == users_height)
print(required_height < users_height)
print(required_height > users_height)

# variables for the amount of squats and pushups that user did
squats_done_by_user = input("please enter the amount of squats that you have done")
pushups_done_by_user = input("please enter the amount of pushups that you have done")

# variables for required pushups and squats
required_squats = 50
required_pushups = 20

print(squats_done_by_user == required_squats)
print(pushups_done_by_user == required_pushups)
