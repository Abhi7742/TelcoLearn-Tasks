Example = [20, 35, 50, 10, 60, 45]

def calculate_average(data):
    return sum(data) / len(data)

def get_summary(data):
    return {
        "min": min(data),
        "max": max(data),
        "average": calculate_average(data)
    }


result = get_summary(Example)
print(result)