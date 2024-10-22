import os
import subprocess
import signal
import sys
import time
from colorama import init, Fore, Style
from datetime import datetime

# Inisialisasi Colorama untuk penggunaan warna pada teks
init()

# ASCII Art untuk tampilan futuristik
FUTURISTIC_LOGO = r"""
   {instagram : muhammad arif_tp}
██████╗  █████╗ ████████╗███╗   ███╗ █████╗ ███╗   ██╗
██╔══██╗██╔══██╗╚══██╔══╝████╗ ████║██╔══██╗████╗  ██║
██████╔╝███████║   ██║   ██╔████╔██║███████║██╔██╗ ██║
██╔══██╗██╔══██║   ██║   ██║╚██╔╝██║██╔══██║██║╚██╗██║
██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    ╔══════════════════════════════════════════════╗
    ║          [ Tools By Tepaks v1.0 ]             
    ╚══════════════════════════════════════════════╝
"""

def list_python_files(directory):
    """Menampilkan semua file Python di direktori yang diberikan."""
    return [f for f in os.listdir(directory) if f.endswith(".py")]

def run_python_file(filepath):
    """Menjalankan file Python yang dipilih."""
    try:
        print(f"{Fore.YELLOW}[] Menjalankan {filepath}...{Style.RESET_ALL}")
        process = subprocess.Popen(['python', filepath])
        process.communicate()
        print(f"{Fore.GREEN}[] {filepath} selesai dijalankan.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Terjadi kesalahan saat menjalankan {filepath}: {e}{Style.RESET_ALL}")

def clear_screen():
    """Membersihkan layar konsol."""
    os.system('cls' if os.name == 'nt' else 'clear')

def futuristic_intro():
    """Menampilkan intro bertema futuristik sebelum aplikasi dimulai."""
    clear_screen()
    print(FUTURISTIC_LOGO)
    print(f"{Fore.LIGHTCYAN_EX}\nSelamat datang di Console Futuristik! Executor skrip Python Anda.")
    print("Tekan Enter untuk melanjutkan...{Style.RESET_ALL}")
    input()

def signal_handler(sig, frame):
    """Menangani Ctrl+C dan menampilkan pilihan kembali."""
    print(f"{Fore.RED}\n\n[!] Ctrl+C terdeteksi. Skrip yang sedang berjalan dihentikan.{Style.RESET_ALL}")
    time.sleep(1)
    print("[*] Kembali ke Console Futuristik...\n")
    time.sleep(1.5)
    clear_screen()
    main()

# Menangkap sinyal Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

def show_time():
    """Menampilkan waktu saat ini."""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def display_python_files(python_files):
    """Menampilkan daftar file Python dalam gaya kartu seperti Facebook."""
    print(f"{Fore.CYAN}=== Daftar Skrip Python ==={Style.RESET_ALL}\n")
    
    if not python_files:
        print(f"{Fore.YELLOW}Tidak ada skrip Python ditemukan di direktori ini.{Style.RESET_ALL}")
        return

    for idx, file in enumerate(python_files, 1):
        # Menampilkan setiap file dalam bentuk kartu
        print(f"{Fore.MAGENTA}🔹 {idx}. {file[:30]:<30}...{Style.RESET_ALL}")  # Batasi panjang nama file

    print(f"{Fore.MAGENTA}🔸 {len(python_files) + 1}. Keluar dari Console Futuristik{Style.RESET_ALL}")

def main():
    """Fungsi utama untuk menampilkan menu dan menjalankan file Python yang dipilih."""
    directory = os.getcwd()  # Mendapatkan direktori saat ini

    while True:
        clear_screen()
        print(FUTURISTIC_LOGO)
        print(f"{Fore.LIGHTCYAN_EX}=== Selamat datang di Console Futuristik ==={Style.RESET_ALL}\n")
        print(f"{Fore.WHITE}[{show_time()}]{Style.RESET_ALL}")  # Menampilkan waktu saat ini
        print(f"{Fore.MAGENTA}======================================={Style.RESET_ALL}")  # Garis pemisah

        # Menampilkan daftar file Python
        python_files = list_python_files(directory)
        display_python_files(python_files)  # Menggunakan fungsi baru untuk menampilkan file

        try:
            choice = int(input("\nPilihan Anda (masukkan nomor): "))
            if choice == len(python_files) + 1:
                print(f"{Fore.YELLOW}\n[] Keluar dari Console Futuristik...{Style.RESET_ALL}")
                break
            elif 1 <= choice <= len(python_files):
                filepath = os.path.join(directory, python_files[choice - 1])
                run_python_file(filepath)
            else:
                print(f"{Fore.RED}\n[!] Pilihan tidak valid, coba lagi!{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}\n[!] Harap masukkan nomor yang valid!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}\n[!] Terjadi kesalahan: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    futuristic_intro()  # Memulai dengan intro bertema futuristik
    main()  # Menjalankan program utama
