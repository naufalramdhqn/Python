kelasA = [75,90,95,90,90]
kelasB = [90,90,100,10,75]
kelasC = [75,60,80,90,90]
kelasD = [55,25,90,90,55]

total = kelasA+kelasB+kelasC+kelasD

x = int(input("Input nilai yang ingin dihitung: "))
persentase = total.count(x)/len(total)
print(f"persentase kemunculan nilai {x} adalah {persentase*100}%")