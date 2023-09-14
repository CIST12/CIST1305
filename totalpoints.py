total_points = 0
results = [70,80,80,60,40,90,20,80]
for result in results:
    if result < 60:
        break
    print(result)
    total_points += result

print(f"Total point: {total_points}")

