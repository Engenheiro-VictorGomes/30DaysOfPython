# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
fruits = ('apple', 'orange', 'banana')
vegetables = ('potato', 'rice', 'beans', 'lettuce')
animalProducts = ('meat', 'honey', 'milk', 'bacon', 'eggs')

foodStuffTp = fruits+vegetables+animalProducts
print(f"foodStuffTp = {foodStuffTp}")

foodStuffLt = list(foodStuffTp)
print(f"foodStuffLt = {foodStuffLt}")