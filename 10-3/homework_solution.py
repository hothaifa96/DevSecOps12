# #
#
# # d = {
# #     "id": 1,
# #     "name": "Leanne Graham",
# #     "address": {
# #         "street": "Kulas Light",
# #         "suite": "Apt. 556",
# #         "city": "Gwenborough",
# #         "zipcode": "92998-3874",
# #         "geo": {
# #             "lat": "-37.3159",
# #             "lng": "81.1496"
# #         }
# #     },
# #     "phone": "1-770-736-8031 x56442",
# #     "website": "hildegard.org",
# #     "company": {
# #         "name": "Romaguera-Crona",
# #         "catchPhrase": "Multi-layered client-server neural-net",
# #         "bs": "harness real-time e-markets"
# #     }
# # }
#
#
# # food = {
# #     "name": 'salmon',
# #     "calories": 1990,
# #     "category": 'fish',
# #     "grade": 3
# # }
# #
# # food2 = dict(name='pizza')
# #
# # print(food2)
# # print(food)
# #
# # food['weight'] = 500 # add new pair
# # print(food)
# #
# # food["calories"] = 100  # override
# # print(food)
# # food.pop("grade")
# # print(food)
#
# food = {
#     "name": 'salmon',
#     "calories": 1990,
#     "category": 'fish',
#     "grade": 3
# }
#
# print(food.keys())
# print(food.values())
# print(food.items())


# 7

# my_dict = dict()
#
# while True:
#     id = input('enter your id : ')
#     if id == '-1':
#         break
#     car = input('whats your ride : ')
#
#     if my_dict.get(id) is None:
#         my_dict[id] = car
#     else:
#         print(f'we have this id : {id}')
#
# print(my_dict)


Dict1 = {
 "apple": "fruit",
 "carrot": "vegetable",
 "dog": "animal",
 "chair": "fruit",
 "computer": "electronics",
 "book": "reading material",
 "rain": "weather",
 "mountain": "geography",
 "water": "liquid",
 "sun": "star"
}

print(set(Dict1.values()))