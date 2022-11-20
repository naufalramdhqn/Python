while(True):
    nim = input("1.Sebutkan NIM!: ""\n")

    
    if nim=="-1":
        break

    nama = input("2.Sebutkan Nama Lengkap!: ""\n")
    url = input("3.Apakah sudah mempublikasikan penelitian?? (ya/tidak) jika ya, masukan alamat web / URL-nya.: ""\n")

    if url =="tidak":
        print(f"{nim} - {nama} belum dapat mengikuti wisuda")
        break
    pembimbing = input("4.Apakah disetujui pembimbing?? (ya/tidak): ""\n")

    if pembimbing=="tidak":
        print(f"{nim} - {nama} belum dapat mengikuti wisuda")
        break

    tamu = input("5.Sebutkan jumlah tamu yang akan dibawa?? (ya/tidak). Jika ya, masukkan jumlah tamu (0, 1 atau 2): ""\n")

    if tamu=="tidak":
        print(f"{nim} - {nama} belum dapat mengikuti wisuda")
        break

    sidang = input("6.Apakah sudah lulus sidang akhir?? (ya/tidak): ""\n")
    
    match sidang:
        case "ya":
            with open("3312211012_UTS/wisuda.txt,",'a') as wisuda:
                wisuda.write(f"{nim} - {nama} - {url} - {tamu}\n")
                print("Data Wisuda tersimpan")
        case "tidak":
           print(f"{nim} - {nama} belum dapat mengikuti wisuda")
        case _:
            print("Prgram salah")