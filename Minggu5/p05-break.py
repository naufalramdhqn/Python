awal=int(input("Inputkan bilangan awal: \n"))
akhir=int(input("Inputkan bilangan akhir: \n"))

for x in range(awal,akhir+1):
    if x%2==0 and x%3==0 and x%4==0 and x%5==0 and x%6==0 and x%7==0 and x%8==0 and x%9==0 and x%10==0:
        print(f"{x} ADALAH bilangan yang dicari!")
        break
    else:
        print(f"{x} BUKAN bilangan yang dicari!")