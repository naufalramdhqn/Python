bank_soal = {
  "soal1": {
    "pertanyaan"  : "1+1 = ...",
    "bidang":"mtk",
    "poin":20,
    "a": "0.5",
    "b": "1",
    "c": "2",
    "d": "3",
    "Jawaban_benar":"c"
  },
  "soal2": {
    "pertanyaan"  : "Jika ada teman yang sakit maka kita harus = ...",
    "bidang":"kwn",
    "poin":20,
    "a": "Menjenguknya",
    "b": "Menjauhinya",
    "c": "Berolahraga",
    "d": "Waspada",
    "Jawaban_benar":"a"
  },
  "soal3": {
    "pertanyaan"  : "Ular mana yang merupakan bahasa pemrograman = ...",
    "bidang":"IT",
    "poin":20,
    "a": "sanca",
    "b": "kobra",
    "c": "sawah",
    "d": "python",
    "Jawaban_benar":"d"
  },
  "soal4": {
    "pertanyaan"  : "Sebuah format data dengan panjang 4 bit hanyaa bisa di terapkan pada ...",
    "bidang":"ORKOM",
    "poin":20,
    "a": "PC",
    "b": "Kalkulator",
    "c": "Laptop",
    "d": "Smartphone",
    "Jawaban_benar":"b"
  },
  "soal5": {
    "pertanyaan"  : "Tiga perangkat .... yang umumnya digunakan adalah keyboard, mouse dan mikrofon",
    "bidang":"agama",
    "poin":20,
    "a": "output",
    "b": "software",
    "c": "input",
    "d": "storage",
    "Jawaban_benar":"c"
  }
}

total_poin = []

for i in bank_soal:
  print(f"{i}. {bank_soal[i]['pertanyaan']}")
  print("a.",bank_soal[i]["a"])
  print("b.",bank_soal[i]["b"])
  print("c.",bank_soal[i]["c"])
  print("d.",bank_soal[i]["d"])
  print("\n")
  user_input = input("Pilih jawaban Anda: (a/b/c/d) : ")    
  right_answer = bank_soal[i]["Jawaban_benar"]  
  poin_answer = bank_soal[i]["poin"]  
  if user_input == right_answer:
    total_poin.append(poin_answer)
    
print(f"Selamat! Skor akhir Anda adalah {sum(total_poin)}")