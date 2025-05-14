import tkinter as tk

ogrenciler = [
    "İlker Barış Akgül", "Ahmet Asım Akkaş", "Kerem Altay", "Busenur Aygör", "Taha Selim Aysan",
    "Yusuf Esad Bozok", "Ekrem Efe Çelik", "Görkem Çetinkaya", "Eda Nur Duman", "Kürşat Efe Ergin",
    "Hüseyin Can Göktepe", "Azra Rana Gülümser", "Arif Selim Güneş", "Furkan Han", "İclal Kahramanoğlu",
    "Abdulkadir Kalaç", "Sude Kapramcı", "Berke Karahasan", "Eren Kartal", "Görkem Adem Kızılarslan",
    "Çağtay Aksoy", "Sinem Koç", "Mert Köroğlu", "Mustafa Mutlu", "Ali Emre Ötün", "Yunus Emre Özdemir",
    "Taha Özdemir", "Abdulkadir Sayan", "Eren Tınaztepe", "Onat Tuğlu", "Emre Turgarlar", "Mehmet Ali Uygun",
    "Sami Kerem Uysal", "Yağmur Yavaş", "Ufuk Yazgan", "Bahar Yılmaz", "Volkan Yılmaz"
]

katilanlar = []

def burada(isim):
    if isim not in katilanlar:
        katilanlar.append(isim)

def yoklama_bitti():
    print("\n📌 Katılanlar:")
    for isim in katilanlar:
        print("-", isim)
    print("\n❌ Katılmayanlar:")
    for isim in ogrenciler:
        if isim not in katilanlar:
            print("-", isim)

# Pencere
pencere = tk.Tk()
pencere.title("Yoklama Sistemi")
pencere.geometry("1000x700")  # Geniş ve yüksek pencere

# Başlık
tk.Label(pencere, text="📋 Yoklama Listesi", font=("Arial", 16)).grid(row=0, column=0, columnspan=5, pady=10)

# Her öğrenciye butonları 5 sütun şeklinde yerleştir
satir = 1
sutun = 0
for isim in ogrenciler:
    tk.Button(pencere, text=isim, width=25, command=lambda i=isim: burada(i)).grid(row=satir, column=sutun, padx=5, pady=5)
    sutun += 1
    if sutun == 5:  # 5 sütun olunca bir alt satıra geç
        sutun = 0
        satir += 1

# Sonuç butonu
tk.Button(pencere, text="✅ Yoklama Bitti", bg="green", fg="white", command=yoklama_bitti).grid(row=satir+1, column=0, columnspan=5, pady=20)

pencere.mainloop()
