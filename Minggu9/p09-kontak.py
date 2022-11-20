contact = dict()

while(True):
    p = input("#Ketikkan show/add/edit/del/exit: ")

    match p :
        case "show":
            if len(contact) == 0:
                print("Belum ada kontak")
            else:
                for key, value in contact.items():
                    print(f"{key} : {value}")
        case "add":
            noHp = input("Input no. kontak: ")
            namaLengkap = input("Input nama lengkap kontak: ")
            contact.update({ noHp : namaLengkap})
            print("Data berhasil ditambahkan")
        case "edit":
            noHp = input("Input no. kontak yang ingin di edit: ")
            namaLengkap = input("Input nama lengkap kontak: ")
            contact.update({ noHp : namaLengkap })
            print("Data berhasil diedit")
        case "del":
            noHp = input("Input no. kontak yang ingin dihapus: ")
            contact.pop({ noHp })
            print("Data berhasil dihapus")
        case "exit":
            break
        case _:
            print("Menu tidak dikenali") 
