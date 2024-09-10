print("=====================[I N P U T]=============================")
s1 = int(input("Input score1 :"))
s2 = int(input("Input score2 :"))
s3 = int(input("Input score3 :"))
print("=====================[O U T P U T]===========================")
print(f"Score 1 = {s1}")
print(f"Score 2 = {s2}")
print(f"Score 3 = {s3}")
avg = (s1 + s2 + s3 )/ 3
print(f" Average of score :{avg}")

if avg < 0 and avg < 50:
    print(f"Grade : F ")
elif avg <= 50 and avg < 65:
    print(f"Grade : E ")
elif avg <= 65 and avg < 75:
    print(f"Grade : D ")
elif avg <= 75 and avg < 85:
    print(f"Grade : C ")
elif avg <= 85 and avg < 95:
    print(f"Grade : B ")
elif avg <= 95 and avg < 100:
    print(f"Grade : A ")
else:
    print(f"Invalid Score")
