# 5. Slice out the first three items and the last three items from food_staff_lt list
fruits = ('apple', 'orange', 'banana')
vegetables = ('potato', 'rice', 'beans', 'lettuce')
animalProducts = ('meat', 'honey', 'milk', 'bacon', 'eggs')

foodStuffTp = fruits+vegetables+animalProducts
print(f"foodStuffTp = {foodStuffTp}")

foodStuffLt = list(foodStuffTp)
print(f"foodStuffLt = {foodStuffLt}")

foodStuffLt = foodStuffLt[3:]
foodStuffLt = foodStuffLt[:-3]
print(f"foodStuffLt = {foodStuffLt}")


