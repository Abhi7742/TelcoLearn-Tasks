import yaml

with open("docker-yaml.yaml") as f:
    data = yaml.safe_load(f)

for service, details in data.get("services", {}).items():
    print(f"\nService: {service}")

    # Get IPv4 Address (safely)
    ipv4 = details.get("networks", {}).get("public_net", {}).get("ipv4_address", "No IP")
    print(f"  IPv4 Address: {ipv4}")

    # Get depends_on
    depends = details.get("depends_on")
    if isinstance(depends, list):
        depends = ", ".join(depends)
    else:
        depends = "None"

    print(f"  Depends On: {depends}")