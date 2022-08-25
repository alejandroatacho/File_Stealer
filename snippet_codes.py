for item in your_list:
    if item.endswith(".jpg"):
        print(item)
        break


for item in your_list:
    print(item.endswith(".jpg"))
    break

for idx, item in enumerate(your_list):
    if item.endswith(".jpg"):
        print(f"{idx}: {item}")
        break
