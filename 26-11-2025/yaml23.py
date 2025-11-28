import yaml

with open("docker-yaml.yaml") as f:
    data = yaml.safe_load(f)

services = data.get("services", {})

for service_name, service_data in services.items():
    print("Service:", service_name)

    depends = service_data.get("depends_on",[])
    print(f"depends_on:",depends if depends else "None")