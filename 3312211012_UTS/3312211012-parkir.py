while (True):
    plat = input("Input nomor plat: ")

    if plat =="0":
        break
    kendaraan = input("Input jenis kendaraan: (motor/mobil/truk/bajay): ")

    waktu = int(input("Input waktu parkir (satuan menit): "))

    match kendaraan:
        case "motor":
            biaya = waktu/60 * 1000
            if waktu <10:
                print(f"Total biaya dari plat {plat} adalah: Rp gratis.")
                break
            else:
                print(f"Total biaya dari plat {plat} adalah Rp."+ str(int(biaya)))
                break
        case "mobil":
            biaya = waktu/60 * 3000
            if waktu <10:
                print(f"Total biaya dari plat {plat} adalah: Rp gratis.")
                break
            else:
                print(f"Total biaya dari plat {plat} adalah Rp."+ str(int(biaya)))
                break
        case "truk":
            biaya = waktu/60 * 5000
            if waktu <10:
                print(f"Total biaya dari plat {plat} adalah: Rp gratis.")
                break
            else:
                print(f"Total biaya dari plat {plat} adalah Rp."+ str(int(biaya)))
                break
        case "bajay":
            biaya = waktu/60 * 500
            if waktu <10:
                print(f"Total biaya dari plat {plat} adalah: Rp gratis.")
            else:
                print(f"Total biaya dari plat {plat} adalah Rp."+ str(int(biaya)))
                break
        case _:
            print("Program error")
