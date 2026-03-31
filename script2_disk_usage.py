import shutil

def disk_report():
    total, used, free = shutil.disk_usage("/")
    print("=== DISK USAGE REPORT ===")
    print(f"Total: {total // (2**30)} GB")
    print(f"Used: {used // (2**30)} GB")
    print(f"Free: {free // (2**30)} GB")

if __name__ == "__main__":
    disk_report()
