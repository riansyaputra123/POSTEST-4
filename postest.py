nama_gitar = ["Yamaha  F-400", "Cort  AD-810E", "Cadenza CE203", "Segovia D-W07", "Prodinne 40CN"]
kode_barang = [101, 102, 103, 104, 105]
harga_barang = [1250000, 1750000, 1500000, 1850000, 1450000]
stock_barang = [12, 10, 15, 16, 10]
keuntungan_harian = []
EE = False
while not EE:
    xx = input("Login sebagai user/admin? : ")
    if xx == "user":
        xx1 = input("Username : ")
        yy1 = int(input("Password : "))
        while not yy1 == 210:
            print("\nPassword salah!")
            yy1 = int(input("Password : "))
        else:
            R = False
            while not R:
                print("=======================================================")
                print("              >> GUITAR ACCOUSTIC STORE <<             ")
                print("=======================================================")
                print("Kode:      Nama Gitar:             Harga:      Stock:\n")
                print("{}".format(kode_barang[0]),"   :    {}".format(nama_gitar[0]),"        :  Rp. {}".format(harga_barang[0]), ": {}".format(stock_barang[0]))
                print("{}".format(kode_barang[1]),"   :    {}".format(nama_gitar[1]),"        :  Rp. {}".format(harga_barang[1]), ": {}".format(stock_barang[1]))
                print("{}".format(kode_barang[2]),"   :    {}".format(nama_gitar[2]),"        :  Rp. {}".format(harga_barang[2]), ": {}".format(stock_barang[2]))
                print("{}".format(kode_barang[3]),"   :    {}".format(nama_gitar[3]),"        :  Rp. {}".format(harga_barang[3]), ": {}".format(stock_barang[3]))
                print("{}".format(kode_barang[4]),"   :    {}".format(nama_gitar[4]),"        :  Rp. {}".format(harga_barang[4]), ": {}".format(stock_barang[4]))
                print("=======================================================")
                print("=               --> DISKON SPESIAL! <--               =")
                print("=                                                     =")
                print("=     >Diskon 10% jika belanja lebih dari 5 juta      =")
                print("=     >Diskon 25% jika belanja lebih dari 7 juta      =")
                print("=======================================================")

                jumlah_tipe = int(input("Banyak tipe   : "))
                x = 0
                total = []
                while x < jumlah_tipe:
                    print("\nTipe ke -", 1 + x)
                    kode_produk = int((input("Kode produk   : ")))
                    jumlah_produk = int(input("Jumlah produk : "))
                    x += 1
    
                    y = kode_produk
                    if y == kode_barang[0]:
                        total.append(jumlah_produk*harga_barang[0])
                        total1 = jumlah_produk*harga_barang[0]
                        stock_barang[0] -= jumlah_produk
                        print("Sisa stock    :", stock_barang[0])
                        print("Total harga   : Rp.", total1)
                    elif y == kode_barang[1]:
                        total.append(jumlah_produk*harga_barang[1])
                        total2 = jumlah_produk*harga_barang[1]
                        stock_barang[1] -= jumlah_produk
                        print("Sisa stock    :", stock_barang[1])
                        print("Total harga   : Rp.", total2)
                    elif y == kode_barang[2]:
                        total.append(jumlah_produk*harga_barang[2])
                        total3 = jumlah_produk*harga_barang[2]
                        stock_barang[2] -= jumlah_produk
                        print("Sisa stock    :", stock_barang[2])
                        print("Total harga   : Rp.", total3)
                    elif y == kode_barang[3]:
                        total.append(jumlah_produk*harga_barang[3])
                        total4 = jumlah_produk*harga_barang[3]
                        stock_barang[3] -= jumlah_produk
                        print("Sisa stock    :", stock_barang[3])
                        print("Total harga   : Rp.", total4)
                    elif y == kode_barang[4]:
                        total.append(jumlah_produk*harga_barang[4])
                        total5 = jumlah_produk*harga_barang[4]
                        stock_barang[4] -= jumlah_produk
                        print("Sisa stock    :", stock_barang[4])
                        print("Total harga   : Rp.", total5)

                print("==============================================")
                sub_total =sum(total)
                print("sub total                    : Rp.", sub_total)
                diskon1 = sub_total * 0.10
                diskon2 = sub_total * 0.25
                if sub_total <= 5000000:
                    print("Diskon - %                   : Rp. -")
                    keuntungan_harian.append(sub_total)
                    print("\nTotal                        : Rp.", sub_total)
                    print("==============================================")
                    uang_tunai1 = int(input("Uang tunai                   : Rp. "))
                    kembalian1 = uang_tunai1 - sub_total
                    print("Kembalian                    : Rp.", kembalian1)
                    print("\n----------------------------------------------")
                elif sub_total <= 7000000:
                    print("Diskon 10%, potongan sebesar : Rp.", diskon1)
                    keuntungan_harian.append(sub_total - diskon1)
                    total_bayar2 = sub_total - diskon1
                    print("\nTotal                        : Rp.", total_bayar2)
                    print("==============================================")
                    uang_tunai2 = int(input("Uang tunai                   : Rp. "))
                    kembalian2 = uang_tunai2 - total_bayar2
                    print("Kembalian                    : Rp.", kembalian2)
                    print("\n----------------------------------------------")
                elif sub_total > 7000000:
                    print("Diskon 25%, potongan sebesar : Rp.", diskon2)
                    keuntungan_harian.append(sub_total - diskon2)
                    total_bayar3 = sub_total - diskon2
                    print("\nTotal                        : Rp.", total_bayar3)
                    print("==============================================")
                    uang_tunai3 = int(input("Uang tunai                   : Rp. "))
                    kembalian3 = uang_tunai3 - total_bayar3
                    print("Kembalian                    : Rp.", kembalian3)
                    print("\n----------------------------------------------")
                tanya1 = input("Apakah ingin kembali ke awal [Y]/[T] : ")
                if tanya1 == "T" or tanya1 == "t":
                    R = True
                    tanya2 = input("Lihat keuntungan hari ini [Y]/[T] : ")
                    if tanya2 == "t" or tanya2 == "T":
                        EE = True
                    else:
                        print("\nLogin sebagai admin untuk melihat keuntungan hari ini\n")
    
    elif xx == "admin":
        xx1 = input("Username : ")
        yy1 = input("Password : ")
        while not yy1 == "078":
            print("\nPassword salah!")
            yy1 = input("Password : ")
        else:
            print("Silahkan pilih menu berikut : ")
            print("[1]. Keuntungan harian","\n[2]. Menu Update", "\n[3]. Kembali ke menu kasir", "\n[4]. Keluar")
            xyz = int(input("Pilih 1/2/3/4 ?  : "))
            if xyz == 1:
                print("Keuntungan harian anda sebesar : Rp.", sum(keuntungan_harian))
            elif xyz == 3:
                print("\nLogin sebagai user untuk kembali ke menu kasir\n")
            elif xyz == 4:
                print("Silahkan Login")
            elif xyz == 2:
                stop = False
                while not stop:
                    print("Apa yang anda inginkan?")
                    print("[1]. Mengupdate stock ", "\n[2]. Mengupdate nama barang", "\n[3]. Mengupdate harga barang", "\n[4]. Mengupdate kode barang", "\n[5]. Hapus barang dari list kasir")
                    pilihan = int(input("Masukkan pilihan : "))
                    if pilihan == 1:
                        bj = int(input("Banyak barang yang ingin di update stocknya : "))
                        i = 0
                        while i < bj:
                            print("\nBarang ke -", i + 1)
                            print("Kode barang : ",kode_barang)
                            kd = int(input("Masukkan kode barang yang ingin di update : "))
                            tambah = int(input("Banyak penambahan stock (isi 0 jika tidak ingin ditambah) : "))
                            kurang = int(input("Banyak pengurangan stock (isi 0 jika tidak ingin dikurangi) : "))
                            i += 1
                            if kd == kode_barang[0]:
                                stock_barang[0] += tambah
                                stock_barang[0] -= kurang
                            elif kd == kode_barang[1]:
                                stock_barang[1] += tambah
                                stock_barang[1] -= kurang
                            elif kd == kode_barang[2]:
                                stock_barang[2] += tambah
                                stock_barang[2] -= kurang
                            elif kd == kode_barang[3]:
                                stock_barang[3] += tambah
                                stock_barang[3] -= kurang
                            elif kd == kode_barang[4]:
                                stock_barang[4] += tambah
                                stock_barang[4] -= kurang
                        print("\n===== Stock berhasil di update =====\n")
                    elif pilihan == 2:
                        bj = int(input("Banyak barang yang ingin diupdate namanya : "))
                        a = 0
                        while a < bj:
                            print("\nBarang ke -", a + 1)
                            print("Kode barang : ",kode_barang)
                            kd = int(input("Masukkan kode barang yang ingin di update : "))
                            ubah_nama = (input("Ubah nama menjadi : "))
                            a += 1
                            if kd == kode_barang[0]:
                                nama_gitar[0] = ubah_nama
                            elif kd == kode_barang[1]:
                                nama_gitar[1] = ubah_nama
                            elif kd == kode_barang[2]:
                                nama_gitar[2] = ubah_nama
                            elif kd == kode_barang[3]:
                                nama_gitar[3] = ubah_nama
                            elif kd == kode_barang[4]:
                                nama_gitar[4] = ubah_nama
                        print("\n===== Nama berhasil di update =====\n")
                    elif pilihan == 3:
                        b = 0
                        bj = int(input("Banyak barang yang ingin di update harganya : "))
                        while b < bj:
                            print("\nBarang ke -", b + 1)
                            print("Kode barang : ",kode_barang)
                            kd = int(input("Masukkan kode barang yang ingin di update : "))
                            ubah_harga = int(input("Ubah harga menjadi : "))
                            b += 1
                            if kd == kode_barang[0]:
                                harga_barang[0] = ubah_harga
                            elif kd == kode_barang[1]:
                                harga_barang[1] = ubah_harga
                            elif kd == kode_barang[2]:
                                harga_barang[2] = ubah_harga
                            elif kd == kode_barang[3]:
                                harga_barang[3] = ubah_harga
                            elif kd == kode_barang[4]:
                                harga_barang[4] = ubah_harga
                        print("\n===== Harga berhasil di update =====\n")
                    elif pilihan == 4:
                        c = 0
                        bj = int(input("Banyak barang yang ingin di update kodenya : "))
                        while c < bj:
                            print("\nBarang ke -", c + 1)
                            print("Kode barang : ",kode_barang)
                            kd = int(input("Masukkan kode barang yang ingin di update : "))
                            print("*kode tidak boleh diawali nol dan harus berupa angka")
                            ubah_kode = int(input("Ubah Kode menjadi : "))
                            c += 1
                            if kd == kode_barang[0]:
                                kode_barang[0] = ubah_kode
                            elif kd == kode_barang[1]:
                                kode_barang[1] = ubah_kode
                            elif kd == kode_barang[2]:
                                kode_barang[2] = ubah_kode
                            elif kd == kode_barang[3]:
                                kode_barang[3] = ubah_kode
                            elif kd == kode_barang[4]:
                                kode_barang[4] = ubah_kode
                        print("\n===== Kode baru berhasil di updat =====\n")
                    elif pilihan == 5:
                        d = 0
                        bj = int(input("Banyak barang yang ingin di hapus dari list menu : "))  
                        while d < bj:
                            print("\nBarang ke -", d + 1)
                            print("Kode barang : ",kode_barang)
                            kd = int(input("Input kode barang yang ingin di hapus dari menu : "))
                            d += 1
                            if kd == kode_barang[0]:
                                kode_barang[0] = "---"
                                nama_gitar[0] = "-------------"
                                harga_barang[0] = "-------"
                                stock_barang[0] = "-"
                            elif kd == kode_barang[1]:
                                kode_barang[1] = "---"
                                nama_gitar[1] = "-------------"
                                harga_barang[1] = "-------"
                                stock_barang[1] = "-"
                            elif kd == kode_barang[2]:
                                kode_barang[2] = "---"
                                nama_gitar[2] = "-------------"
                                harga_barang[2] = "-------"
                                stock_barang[2] = "-"
                            elif kd == kode_barang[3]:
                                kode_barang[3] = "---"
                                nama_gitar[3] = "-------------"
                                harga_barang[3] = "-------"
                                stock_barang[3] = "-"
                            elif kd == kode_barang[4]:
                                kode_barang[4] = "---"
                                nama_gitar[4] = "-------------"
                                harga_barang[4] = "-------"
                                stock_barang[4] = "-"
                            print("\n===== Barang berhasil di hapus =====\n")
                    
                    tanya = input("Apakah ingin kembali ke menu awal? {Y}/{T} : ")
                    if tanya == "T" or tanya == "t":
                        stop = True
                    else:
                        stop = False
            