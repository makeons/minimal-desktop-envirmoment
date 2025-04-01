


import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


class FileManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Basit Dosya Yöneticisi")
        self.root.geometry("800x600")

        # Ana klasör alanı
        self.current_directory = os.path.expanduser("~")  # Başlangıç klasörü: Ev dizini

        # Menü çubuğu
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Dosya menüsü
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Dosya", menu=self.file_menu)
        self.file_menu.add_command(label="Yeni Klasör", command=self.create_folder)
        self.file_menu.add_command(label="Kopyala", command=self.copy_file)
        self.file_menu.add_command(label="Sil", command=self.delete_file)

        # Dizin Listeleme Alanı
        self.file_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=80, height=20)
        self.file_listbox.pack(pady=20)

        # Butonlar
        self.refresh_button = tk.Button(self.root, text="Yenile", command=self.refresh)
        self.refresh_button.pack()

        # Pencereyi yenile
        self.refresh()

        # Dosyaya çift tıklama işlevi
        self.file_listbox.bind("<Double-1>", self.open_file)

    def refresh(self):
        """Klasör içeriğini yeniler ve Listbox'a ekler."""
        self.file_listbox.delete(0, tk.END)  # Mevcut listeyi temizle
        try:
            # Mevcut dizindeki dosya ve klasörleri al
            files = os.listdir(self.current_directory)
            for file in files:
                self.file_listbox.insert(tk.END, file)
        except PermissionError:
            messagebox.showerror("Hata", "Bu dizine erişim reddedildi.")

    def create_folder(self):
        """Yeni bir klasör oluşturur."""
        folder_name = filedialog.askstring("Yeni Klasör", "Klasör adını girin:")
        if folder_name:
            folder_path = os.path.join(self.current_directory, folder_name)
            try:
                os.mkdir(folder_path)
                self.refresh()
            except FileExistsError:
                messagebox.showerror("Hata", "Bu klasör zaten mevcut.")
            except Exception as e:
                messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")

    def copy_file(self):
        """Bir dosyayı kopyalar."""
        selected = self.file_listbox.curselection()
        if not selected:
            messagebox.showwarning("Uyarı", "Lütfen bir dosya seçin.")
            return

        file_to_copy = self.file_listbox.get(selected)
        file_path = os.path.join(self.current_directory, file_to_copy)
        destination = filedialog.askdirectory(title="Kopyalamak için hedef klasörü seçin")
        if destination:
            try:
                shutil.copy(file_path, destination)
                messagebox.showinfo("Başarılı", f"{file_to_copy} başarıyla kopyalandı.")
            except Exception as e:
                messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")

    def delete_file(self):
        """Bir dosyayı siler."""
        selected = self.file_listbox.curselection()
        if not selected:
            messagebox.showwarning("Uyarı", "Lütfen bir dosya seçin.")
            return

        file_to_delete = self.file_listbox.get(selected)
        file_path = os.path.join(self.current_directory, file_to_delete)

        confirm = messagebox.askyesno("Onay", f"{file_to_delete} dosyasını silmek istediğinizden emin misiniz?")
        if confirm:
            try:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Klasörü sil
                else:
                    os.remove(file_path)  # Dosyayı sil
                self.refresh()
                messagebox.showinfo("Başarılı", f"{file_to_delete} başarıyla silindi.")
            except Exception as e:
                messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")

    def open_file(self, event):
        """Bir dosyayı açar (çift tıklama)."""
        selected = self.file_listbox.curselection()
        if selected:
            file_to_open = self.file_listbox.get(selected)
            file_path = os.path.join(self.current_directory, file_to_open)
            if os.path.isdir(file_path):
                # Eğer bir klasöre çift tıklanırsa, o klasöre geç
                self.current_directory = file_path
                self.refresh()
            else:
                # Eğer bir dosyaya çift tıklanırsa, dosya açılabilir (burada sadece yol gösteriyoruz)
                messagebox.showinfo("Dosya", f"{file_to_open} dosyasını açmak için uygun bir uygulama seçin.")


# Ana pencereyi başlat
if __name__ == "__main__":
    root = tk.Tk()
    fm = FileManager(root)
    root.mainloop()
