import subprocess

ip_list = [
    "8.8.8.8",
    "192.168.1.1",
    "10.0.0.5",
    "127.0.0.1"
]

for ip in ip_list:
    print(f"\nChecking: {ip}")

    try:
        # timeout=0.5 → 500 ms
        result = subprocess.run(
            ["ping", "-n", "1", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=0.5     )

        if result.returncode == 0:
            print(f"IP address {ip} is reachable.")
        else:
            print(f"IP address {ip} is unreachable.")

    except subprocess.TimeoutExpired:
        print("slow ping")
