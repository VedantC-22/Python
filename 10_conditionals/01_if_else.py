m1 = int(input(f"Enter marks of subject{1}: "))
m2 = int(input(f"Enter marks of subject{2}: "))
m3 = int(input(f"Enter marks of subject{3}: "))

total_percentage = (m1 + m2 + m3)/3;

if m1 <= 33 or m2 <= 33 or m3 <= 33: # 33% passing (subject out of 100)
    print("fail")
elif (total_percentage <= 44): # 40% passing of 300 marks
    print("fail")
else:
    print("pass with %: ", total_percentage)