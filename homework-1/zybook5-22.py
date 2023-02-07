# Angelo Angel (2076005)

shop_services = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12,
    '-': 0
}

print("""Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12
""")

first_service = input("Select first service:\n")
second_service = input("Select second service:\n\n")
print("Davy's auto shop invoice\n")

if first_service == "Oil change":
    print(f"Service 1: {first_service}, ${shop_services[first_service]}")
elif first_service == "Tire rotation":
    print(f"Service 1: {first_service}, ${shop_services[first_service]}")
elif first_service == "Car wash":
    print(f"Service 1: {first_service}, ${shop_services[first_service]}")
elif first_service == "Car wax":
    print(f"Service 1: {first_service}, ${shop_services[first_service]}")
else:
    print("Service 1: No service")

if second_service == "Oil change":
    print(f"Service 2: {second_service}, ${shop_services[second_service]}")
elif second_service == "Tire rotation":
    print(f"Service 2: {second_service}, ${shop_services[second_service]}")
elif second_service == "Car wash":
    print(f"Service 2: {second_service}, ${shop_services[second_service]}")
elif second_service == "Car wax":
    print(f"Service 2: {second_service}, ${shop_services[second_service]}")
else:
    print("Service 2: No service")

print("")
total = shop_services[first_service] + shop_services[second_service]
print(f"Total: ${total}")



