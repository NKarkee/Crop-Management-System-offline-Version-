from asyncio import run
import json
import os

DATA_FILE = 'Data.json'
def load_dataset():
    if not os.path.exists(DATA_FILE):
     return print(f"Error: Missing {DATA_FILE}") or None

    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
    return data

#save data to json file
def save_crop_data(crops):
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(crops, file, indent=5)
    except IOError as e:
        print(f"Error saving data to {DATA_FILE}: {e}")


#show all data
def show_all_data(crops):
    if not crops:
        print("No data available.")
        return
    print("\n ---Crops Price ---")
    for crop in crops:
        notice = "🚨 Low price!" if crop ['price'] < 50 else ""
        print(f"{crop['name']} - NRS {crop['price']} per KG{notice}")

#Add new crop 
def add_crop(crops):
    name = input("Enter crop name: ")
    price = float(input("Enter crop price per KG: "))
    crops.append({"name": name, "price": price})
    save_crop_data(crops)
    print(f"{name} added successfully.")

#Update crop price
def update_list_of_crop(crops):
    name = input("Enter crop name to update: ")
    for crop in crops:
        if crop['name'].lower() == name.lower():
            new_price = float(input(f"Enter new price for {name}: "))
            crop['price'] = new_price
            save_crop_data(crops)
            print(f"{name} updated successfully.")
            return
    print(f"{name} not found.")

#Delete crop

def delete_crop_data(crops):
    name = input("Enter crop name you want to delete: ")
    for crop in crops:
        if crop['name'].lower() == name.lower():
            crops.remove(crop)
            save_crop_data(crops)
            print(f"{name} deleted successfully.")
            return
    print(f"{name} is removed from the list.")
