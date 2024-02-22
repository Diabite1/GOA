"""day 5:
homework:

შექმენით ცვლადები 10 წიგნისთვის ( სახელი ცალკე, ფასი ცალკე, 
5 წიგნს გაუკეთეთ 10%იანი ფასდაკლება, 5 წიგნს გაუკეთეთ 20%იანი ფასდაკლება) 

იგივე წესებით, რაც გაკვეთილზე ავხსენით"""

# წიგნის ცვლადები

book1_price = 20
book2_price = 30
book3_price = 40
book4_price = 50
book5_price = 60
book6_price = 70
book7_price = 80
book8_price = 90
book9_price = 100
book10_price = 110

# ფასდაკლებების ცვალდები

small_discount_percentage = 10
big_discount_percantage = 20

# წიგნის ფასები ფასდაკლების შემდეგ

book1_price_after_small_discont = book1_price - (book1_price * small_discount_percentage / 100)
book2_price_after_small_discont = book2_price - (book2_price * small_discount_percentage / 100)
book3_price_after_small_discont = book3_price - (book3_price * small_discount_percentage / 100)
book4_price_after_small_discont = book4_price - (book4_price * small_discount_percentage / 100)
book5_price_after_small_discont = book5_price - (book5_price * small_discount_percentage / 100)
book6_price_after_big_discont = book6_price - (book6_price * big_discount_percantage / 100)
book7_price_after_big_discont = book7_price - (book7_price * big_discount_percantage / 100)
book8_price_after_big_discont = book8_price - (book8_price * big_discount_percantage / 100)
book9_price_after_big_discont = book9_price - (book9_price * big_discount_percantage / 100)
book10_price_after_big_discont = book10_price - (book10_price * big_discount_percantage / 100)

# ვბეჭდავთ წიგნის ფასებს ფასდაკლებების შემდეგ

print("all of the books prices after big and small discount")
print(book1_price_after_small_discont)
print(book2_price_after_small_discont)
print(book3_price_after_small_discont)
print(book4_price_after_small_discont)
print(book5_price_after_small_discont)
print(book6_price_after_big_discont)
print(book7_price_after_big_discont)
print(book8_price_after_big_discont)
print(book9_price_after_big_discont)
print(book10_price_after_big_discont)

