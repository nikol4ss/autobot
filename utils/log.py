from datetime import datetime

def log(label: str, level: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] - [{level}] -> [{label}]")
