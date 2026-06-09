import time
import random
from datetime import datetime

log_file = "app.log"

users = ["alice", "bob", "david", "charlie"]
actions = ["login", "logout", "upload", "download", "delete"]
ips = ["192.168.1.1", "10.0.0.5", "172.16.0.3", "192.168.0.9"]
levels = ["INFO", "WARN", "ERROR", "Done"]

def generate_log_entry():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level = random.choice(levels)
    user = random.choice(users)
    action = random.choice(actions)
    ip = random.choice(ips)
    return f"[{timestamp}] {level} User {user} performed {action} from IP {ip}\n"

while True:
    with open(log_file, "a") as f:
        f.write(generate_log_entry())
    time.sleep(7) # wait 7 second between logs