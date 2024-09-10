# Input the population quantities for each city
sr = int(input("Input quantity of population in Siem Reap: "))
btb = int(input("Input quantity of population in Battambang: "))
kps = int(input("Input quantity of population in Kompong Som: "))

# Calculate the average population
average = (sr + btb + kps) / 3
print(f"The average population is {average}")

# Determine the maximum population
if sr >= btb and sr >= kps:
    print(f"Max population is in Siem Reap with {sr}")
elif btb >= sr and btb >= kps:
    print(f"Max population is in Battambang with {btb}")
else:
    print(f"Max population is in Kompong Som with {kps}")

# Determine the minimum population
if sr <= btb and sr <= kps:
    print(f"Min population is in Siem Reap with {sr}")
elif btb <= sr and btb <= kps:
    print(f"Min population is in Battambang with {btb}")
else:
    print(f"Min population is in Kompong Som with {kps}")
