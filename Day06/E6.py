# 6. Delete the food_staff_tp tuple completely
fruits = ('apple', 'orange', 'banana')
vegetables = ('potato', 'rice', 'beans', 'lettuce')
animalProducts = ('meat', 'honey', 'milk', 'bacon', 'eggs')

foodStuffTp = fruits+vegetables+animalProducts
print(f"foodStuffTp = {foodStuffTp}")

del foodStuffTp
print(f"foodStuffTp = {foodStuffTp}")