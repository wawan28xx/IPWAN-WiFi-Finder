import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

# Rentang IP
base_ip = "172.18.1." #ganti rentang IP WAN Wi-Fi
ip_range = range(1, 255)  # 1-254

# Fungsi ping
def ping(ip):
    try:
        # -n (Windows) atau -c (Linux/Mac)
        count_flag = "-n" if os.name == "nt" else "-c"
        result = subprocess.run(
            ["ping", count_flag, "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if result.returncode == 0:
            print(f"{ip} is alive")
        else:
            print(f"{ip} is unreachable")
    except Exception as e:
        print(f"Error pinging {ip}: {e}")

# Eksekusi paralel
if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(lambda i: ping(f"{base_ip}{i}"), ip_range)