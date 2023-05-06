import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Fungsi untuk melakukan pengecekan login
def check_login():
    username = username_entry.get()
    password = password_entry.get()

    # Lakukan pengecekan login dengan username dan password yang sudah ditentukan
    if username == "user" and password == "12345":
        # Jika login berhasil, tampilkan pesan sukses dan arahkan ke file lain
        messagebox.showinfo("Login Suuccess", "Welcome, " + username + "!")
        root.destroy()  # Tutup jendela login
  # Buka file lain setelah login berhasil
    else:
        # Jika login gagal, tampilkan pesan error
        messagebox.showerror("Login Failed", "Invalid username or password")

# Membuat instance object tkinter
root = tk.Tk()

# Menambahkan judul pada GUI
root.title("Login")

# Membuat frame untuk input login
frame_login = tk.Frame(root, padx=20, pady=20)
frame_login.pack()

# Menambahkan input untuk username dan password
username_label = tk.Label(frame_login, text="Username:")
username_label.grid(row=0, column=0, sticky=tk.W)
username_entry = tk.Entry(frame_login)
username_entry.grid(row=0, column=1)

password_label = tk.Label(frame_login, text="Password:")
password_label.grid(row=1, column=0, sticky=tk.W)
password_entry = tk.Entry(frame_login, show="*")
password_entry.grid(row=1, column=1)

# Menambahkan tombol login
login_button = tk.Button(frame_login, text="Login", command=check_login)
login_button.grid(row=2, column=1, pady=10)

# Menjalankan event loop tkinter
root.mainloop()




# Data array yang akan ditampilkan
data_array = [
    {"tanggal": "1 Januari 2023", "keterangan": "Tahun Baru"},
    {"tanggal": "22-23 Januari 2023", "keterangan": "Imlek"},
    {"tanggal": "14 Februari 2023", "keterangan": "Valentine Days"},
    {"tanggal": "8 Maeret 2023", "keterangan": "Hari Internasional Perempuan"},
    {"tanggal": "27 Maret 2023", "keterangan": "Hari Raya Nyepi"},
    {"tanggal": "21 April 2023", "keterangan": "Hari Kartini"}
]

# Fungsi untuk melakukan pencarian menggunakan algoritma linear search
def linear_search(name, data_array):
    for i in range(len(data_array)):
        if data_array[i]["keterangan"] == name:
            return data_array[i]["tanggal"]
    return None

# Fungsi untuk menampilkan hasil pencarian
def show_result(result):
    if result is not None:
        message = f"Tanggal {result}"
    else:
        message = "Hari besar yang Anda cari tidak ditemukan."
    result_label.configure(text=message)


# Fungsi untuk menambah data pada array dan memperbarui tampilan tabel
def add_data():
    keterangan = keterangan_entry.get()
    tanggal = tanggal_entry.get()
    data_array.append({"tanggal": tanggal, "keterangan": keterangan})
    update_table()

# Fungsi untuk menghapus data dari array dan memperbarui tampilan tabel
def delete_data():
    item = table.selection()[0]
    index = int(table.index(item))
    del data_array[index]
    update_table()

# Fungsi untuk memperbarui tampilan tabel
def update_table():
    table.delete(*table.get_children())
    for i, data in enumerate(data_array):
        table.insert("", "end", text=i+1, values=(data["keterangan"], data["tanggal"]))

# Membuat instance object tkinter
root = tk.Tk()

# Menambahkan judul pada GUI
root.title("Hari Besar di Indonesia Tahun 2023")

# Membuat frame untuk tabel dan input
frame_table = ttk.Frame(root, padding="20")
frame_table.pack(fill="both", expand=True)
frame_input = ttk.Frame(root, padding="10")
frame_input.pack(fill="x", expand=True)
frame_button = ttk.Frame(root, padding="10")
frame_button.pack(fill="x", expand=True)

# Membuat tabel untuk menampilkan data array
table = ttk.Treeview(frame_table, columns=("col1"))
table.heading("#0", text="No.")
table.heading("col1", text="Keterangan")

# Menampilkan tabel ke dalam GUI
table.pack(fill="both", expand=True)

# Menambahkan input untuk menambah data
keterangan_label = ttk.Label(frame_input, text="Hari Besar :")
keterangan_label.pack(side="left")
keterangan_entry = ttk.Entry(frame_input)
keterangan_entry.pack(side="left")
tanggal_label = ttk.Label(frame_input, text="Tanggal :")
tanggal_label.pack(side="left")
tanggal_entry = ttk.Entry(frame_input)
tanggal_entry.pack(side="left")

# Menambahkan tombol untuk menambah dan menghapus data
add_button = ttk.Button(frame_button, text="Tambah Data", command=add_data)
add_button.pack(side="left")
delete_button = ttk.Button(frame_button, text="Hapus Data", command=delete_data)
delete_button.pack(side="left", padx=10)

# Membuat input label dan button
input_label = ttk.Label(frame_input, text="Cari Hari Besar :")
input_label.pack(side="left")
input_entry = ttk.Entry(frame_input)
input_entry.pack(side="left")
search_button = ttk.Button(frame_input, text="Cari", command=lambda: show_result(linear_search(input_entry.get(), data_array)))
search_button.pack(side="left")

# Membuat label untuk menampilkan hasil pencarian
result_label = ttk.Label(root, text="")
result_label.pack()

# Memperbarui tampilan tabel dengan data array
update_table()

# Menjalankan GUI
root.mainloop()