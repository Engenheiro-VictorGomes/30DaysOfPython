# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
fruits = ('apple', 'orange', 'banana')
vegetables = ('potato', 'rice', 'beans', 'lettuce')
animalProducts = ('meat', 'honey', 'milk', 'bacon', 'eggs')

foodStuffTp = fruits+vegetables+animalProducts
print(f"foodStuffTp = {foodStuffTp}")

foodStuffLt = list(foodStuffTp)
print(f"foodStuffLt = {foodStuffLt}")

if len(foodStuffLt)%2:
    middle1 = int(len(foodStuffLt)/2)
    foodStuffLt.remove(foodStuffLt[middle1])
else:
    middle1 = int(len(foodStuffLt)/2)
    foodStuffLt.remove(foodStuffLt[middle1])
    middle2 = int(len(foodStuffLt)/2)
    foodStuffLt.remove(foodStuffLt[middle2])

print(f"foodStuffLt = {foodStuffLt}")