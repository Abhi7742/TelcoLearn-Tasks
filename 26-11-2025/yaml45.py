import subprocess
import json

def parse_ip_route_line(line):
    parts = line.split()
    route = {}

    i = 0
    while i < len(parts):
        word = parts[i]

        # First token is either 'default' or subnet
        if i == 0:
            route["route"] = word
            i += 1
            continue

        # Field mappings
        if word == "via":
            route["gateway"] = parts[i + 1]
            i += 2
        elif word == "dev":
            route["interface"] = parts[i + 1]
            i += 2
        elif word == "proto":
            route["protocol"] = parts[i + 1]
            i += 2
        elif word == "scope":
            route["scope"] = parts[i + 1]
            i += 2
        elif word == "src":
            route["src_ip"] = parts[i + 1]
            i += 2
        else:
            i += 1

    return route


def ip_route_to_json():
    # Run & extract output of ip route
    output = subprocess.run(["ip", "route"], capture_output=True, text=True)
    lines = output.stdout.strip().split("\n")

    routes = []
    for line in lines:
        if line.strip():
            routes.append(parse_ip_route_line(line))

    # Print formatted JSON
    print(json.dumps(routes, indent=4))


if __name__ == "__main__":
    ip_route_to_json()