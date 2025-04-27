#Show crop price graph
import matplotlib.pyplot as plt
def show_graph(crops):
    if not crops:
        print("No data available.")
        return
    names = [crop['name'] for crop in crops]
    prices = [crop['price'] for crop in crops]
    
    plt.figure(figsize=(10, 5))
    plt.bar(names, prices, color='green')
    plt.xlabel('Crops')
    plt.ylabel('Price per KG (NRS)')
    plt.title('Crop Prices')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
