import json

nama_file = r"D:\PRAKTIKUM DDP SEMESTER 1\PERTEMUAN 7\nilai.json"

while True:
    print("___________________________________________________")
    print("     === SISTEM PENDATAAN NILAI MAHASISWA ===      ")
    print("___________________________________________________")
    print("MENU : ")
    print("1. Lihat Data")
    print("2. Tambah Data Baru")
    print("3. Keluar")

    pilihan = input("PILIH MENU 1-3 : ")

    if pilihan == "1":
        try:
            with open(nama_file, "r") as file:
                data = json.load(file)
        except:
            data = []

        print("___________________________________________________")
        print("            === DATA NILAI MAHASISWA ===      ")
        print("___________________________________________________")

        for mahasiswa in data:
            print("Nama        :", mahasiswa["Nama"])
            print("NIM         :", mahasiswa["NIM"])
            print("Mata Kuliah :", mahasiswa["Mata Kuliah"])
            print("Nilai       :", mahasiswa["Nilai"])
            print("_____________________________")

    elif pilihan == "2":
        try:
            with open(nama_file, "r") as file:
                data = json.load(file)
        except:
            data = []
            print("Data belum tersedia.")

        nama = input("Masukkan Nama : ")
        nim = input("Masukkan NIM   : ")
        matkul = input("Masukkan Mata Kuliah : ")
        nilai = int(input("Masukkan Nilai    : "))

        data.append({
            "Nama": nama,
            "NIM": nim,
            "Mata Kuliah" : matkul,
            "Nilai": nilai
        })
    
        with open(nama_file, "w") as file:
            json.dump(data, file, indent=4)

            print(">>> DATA BERHASIL DISIMPAN! <<<")

    elif pilihan == "3":
        print(">>> PROGRAM SELESAI <<<")
        break

    else:
        print("Pilihan tidak tersedia, silakan pilih 1/2/3.")