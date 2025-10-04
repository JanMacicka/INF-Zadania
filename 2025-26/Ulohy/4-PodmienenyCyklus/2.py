capacity = int(input("zadajte nosnost batohu: "))
weight_sum = 0
count = 0

while weight_sum < capacity:
    weight = int(input("zadajte hmotnost: "))

    if weight_sum + weight > capacity or weight == 0:
        break

    weight_sum += weight
    count += 1

print(f"beriete si so sebou {count} veci")