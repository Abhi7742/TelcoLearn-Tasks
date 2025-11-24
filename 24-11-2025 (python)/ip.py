import subprocess

# Step 1: Define the IP list
ip_list = [
    "8.8.8.8",
    "1.1.1.1",
    "192.168.1.1",
    "10.10.10.10"
]

# Step 2 & 3: Use loop + subprocess to ping each IP
for ip in ip_list:
    print(f"Pinging {ip} ...")

    # Run ping command (Windows uses '-n 1')
    result = subprocess.run(["ping", "-n", "1", ip],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)

    # Check the result
    if "TTL=" in result.stdout:
        print(f"{ip} is reachable ✓\n")
    else:
        print(f"{ip} is NOT reachable ✗\n")
