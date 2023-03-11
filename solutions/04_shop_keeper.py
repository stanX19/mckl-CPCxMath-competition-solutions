inventory = {}

n = int(input())
items = input().split()
quantities = list(map(int, input().split()))

for i in range(n):
    inventory[items[i]] = quantities[i]

while True:
    command = input().split()
    action = command[0]

    if action == "buy":
        item = command[2]
        quantity = int(command[1])
        if item in inventory and inventory[item] >= quantity:
            print("here you go")
            inventory[item] -= quantity
        else:
            print("out of stock")
    elif action == "brought":
        item = command[2]
        quantity = int(command[1])
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
    elif action == "close":
        print(sum(inventory.values()))
        break

# answer source: submission by DROP TABLE User;
