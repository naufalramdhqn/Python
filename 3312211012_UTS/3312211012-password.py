file =  open("3312211012_UTS/password-lemah.txt","r")

sandi = str(file.read())

inputan = input("Input password yang akan di cek: \n")

if inputan in sandi :
    print(f"PASSWORD {inputan} TIDAK AMAN!")

else:
    print(f"PASSWORD {inputan} AMAN")


file.close()