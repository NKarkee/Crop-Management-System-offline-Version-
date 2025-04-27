# crop management system 

from data_handler import load_dataset, save_crop_data, show_all_data, add_crop, update_list_of_crop, delete_crop_data
from graph_handler import show_graph

#Main function  
def main():
    try:

        crops = load_dataset()
        if crops is None:
            return

        while True:
            print("\n--- Crop Data Management System ---")
            print("1. Show The list of all crops")
            print("2. Add new crop to the list")
            print("3. Update the price of a crop")
            print("4. Delete crop from the list")
            print("5. Show crop price graph of the crops")
            print("6. Quit")

            choose = input("Enter your choice: ")

            if choose == '1':
                show_all_data(crops)
            elif choose == '2':
                add_crop(crops)
            elif choose == '3':
                update_list_of_crop(crops)
            elif choose == '4':
                delete_crop_data(crops)
            elif choose == '5':
                show_graph(crops)
            elif choose == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    except KeyboardInterrupt:
        print("\nExiting the program.")



if __name__ == "__main__":
    main()
# this system helps the user to add, update, delete and show the crop prices