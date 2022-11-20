students = {
    "Ani":
    {
        "jenis_kelamin" : 'F',
        "nilai": {
            "tugas":90,
            "uts":65,
            "uas":40
        }
    },
    "Budi":
    {
        "jenis_kelamin" : 'M',
        "nilai": {
            "tugas":60,
            "uts":75,
            "uas":100
        }
    }
}

for key,value in students.items():
    n = value["nilai"]["uas"]
    if n>=60:
        print(f"{key} LULUS")
    else:
        print(f"{key} GAGAL")