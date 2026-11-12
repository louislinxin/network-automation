"""
网络设备备份命令生成器

读取 devices.txt（每行：设备名 空格 IP），
生成批量备份命令并写入 backup_commands.txt。

用法：python lesson4.py
"""

INPUT_FILE = "devices.txt"
OUTPUT_FILE = "backup_commands.txt"


def load_devices(path):
    """读取设备清单，返回 [(设备名, IP), ...]"""
    devices = []

    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()          # 去掉首尾空白和换行
            if not line:                 # 跳过空行
                continue

            name, ip = line.split()      # 按空格拆成两段
            devices.append((name, ip))

    return devices


def build_command(name, ip):
    """生成一条备份命令"""
    return f"backup {ip} 配置到 {name}.cfg"


def main():
    devices = load_devices(INPUT_FILE)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        for name, ip in devices:
            cmd = build_command(name, ip)
            print(cmd)
            out.write(cmd + "\n")

    print(f"共 {len(devices)} 台设备，已写入 {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
