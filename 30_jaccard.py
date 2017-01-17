import random

# Triangle inequality
targetFile = open('jaccard_input.txt')
rawtext_list = targetFile.read().splitlines()

base_text = rawtext_list.pop(0)		# pops first element from the list to make it base text

jaccard_distance_list = []
dice_coefficient_list = []

def jaccard_index(base_text, item):
	base_set = set(base_text.split())
	item_set = set(item.split())
	jaccard_index = float(len(base_set & item_set) / len(base_set | item_set))
	jaccard_distance = round(1 - round(jaccard_index, 2), 2)
	return jaccard_distance

def dice_coefficient(base_text, item):
	base_set = set(base_text.split())
	item_set = set(item.split())
	dice_coefficient_distance = round(1 - float((2 * len(base_set & item_set)) / (len(base_set) + len(item_set))), 2)
	return dice_coefficient_distance

for item in rawtext_list:
	jaccard_distance_list.append(jaccard_index(base_text, item))
	dice_coefficient_list.append(dice_coefficient(base_text, item))

def calculate_triangle_inequality(val, item):
	a = val[0]
	b = val[1]
	c = val[2]
	if(((a + b) >= c) & ((a + c) >= b) & ((b + c) >= a)):
		return "Values: \na: " +str(a)+ ",\nb: " +str(b)+ ",\nc: " +str(c)+ "\nSatisfies Triangle Inequality for " +item+ "\n" 
	else:
		return "Values: \na: " +str(a)+ ",\nb: " +str(b)+ ",\nc: " +str(c)+ "\nDoes not satisfies Triangle Inequality for " +item+ "\n"

def triangle_inequality(item):
	if(item == "Jaccard Distance"):
		val = random.sample(jaccard_distance_list, 3)
	else:
		val = random.sample(dice_coefficient_list, 3)
	res = calculate_triangle_inequality(val, item)
	return res
	
print("Jaccard Distance: ")
print("===============================")
print("\nBase Text: " + base_text + "\n")
for item1, item2 in zip(rawtext_list, jaccard_distance_list):
	print("Text: " + item1)
	print("Jaccard Distance: " + str(item2))
	print()
print("3 random values from above set for Triangle Inequality (for non-repeative items): ")
print(triangle_inequality("Jaccard Distance"))

print("Sørensen-Dice Coefficient: ")
print("===============================")
print("\nBase Text: " + base_text + "\n")
for item1, item2 in zip(rawtext_list, dice_coefficient_list):
	print("Text: " + item1)
	print("Sørensen-Dice Coefficient: " + str(item2))
	print()
print("3 random values from above set for Triangle Inequality (for non-repeative items): ")
print(triangle_inequality("Sørensen-Dice Coefficient"))