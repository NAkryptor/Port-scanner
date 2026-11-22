import argparse
import socket
from concurrent.futures import ThreadPoolExecutor
# прочитать хост и диапазон портов из командной строки
parser = argparse.ArgumentParser()
parser.add_argument("host")
parser.add_argument("-s", "--start", type=int, default=1)
parser.add_argument("-e", "--end", type=int, default=1024)
args = parser.parse_args()

# функция: проверить один порт
def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        if s.connect_ex((args.host, port)) == 0:
            return port
    return None

# раздать проверку потокам
with ThreadPoolExecutor(max_workers=100) as pool:
    results = pool.map(check_port, range(args.start, args.end + 1))

# напечатать открытые
for port in results:
    if port is not None:
        print(f"Порт {port} открыт")
