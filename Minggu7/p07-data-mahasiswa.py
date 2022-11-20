while(True):
    nim = input("Input NIM: ")

    #akhiri perulangan jika menginputkan -1
    if nim=="-1":
        break

    mhs = input("Input nama mahasiswa: ")
    prodi = input("Pilih program studi:(IF,MJ,GM,RKS): ")

    match prodi:
        case "IF" | "Informatika":
            with open("infotmatika.txt,",'a') as mhs_if:
                mhs_if.write(f"{nim} - {mhs} \n")
        case "MJ" | "multimedia":
            with open("multimedia.txt,",'a') as mhs_mj:
                mhs_mj.write(f"{nim} - {mhs} \n")
        case "GM" | "geomatika":
            with open("geomatika.txt,",'a') as mhs_gm:
                mhs_gm.write(f"{nim} - {mhs} \n")
        case "RKS" | "siber":
            with open("siber.txt",'a') as mhs_rks:
                mhs_rks.write(f"{nim} - {mhs} \n")
        case _:
            print("Prodi tidak dikenali")

print("=========================")