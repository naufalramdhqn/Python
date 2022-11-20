from statistics import mean, median, mode, stdev

nilai = [90,75,77,60,65,65]
nilai.sort()
print(nilai)

# MEAN / Nilai rata rata

print("#Mean dari list nilai adalah " + str(mean(nilai)))

# MEDIAN / Nilai tengah

print("#Median dari list nilai adalah " + str(median(nilai)))

# MODUS / Nilai terbanyak

print("#Modus dari list nilai adalah " + str(mode(nilai)))