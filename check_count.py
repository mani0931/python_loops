list_of_marks = [75, 98, 89, 86, 79, 62, 78, 61, 90, 97, 92, 61, 64, 97, 82, 69, 87, 96, 65, 75, 85, 76, 95, 83, 62, 80, 80, 77, 94, 71, 86, 94, 85, 99, 77, 68, 92, 91, 99, 90]
count = 0;

check_num = 62

for elem in list_of_marks:
  if (check_num == elem):
    count = count + 1

print(count)
