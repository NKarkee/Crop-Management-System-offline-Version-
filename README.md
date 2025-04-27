# Crop Data Management System

A simple command-line application for managing crop price data with visualization capabilities.

## Features

- View a list of all crops and their prices
- Add new crops with their prices
- Update prices of existing crops
- Delete crops from the database
- Visualize crop prices with a graphical representation

## Requirements

- Python 3.x
- matplotlib (for graph visualization)
- JSON (for data storage)

## Installation

1. Clone this repository
2. Make sure you have the required dependencies:
   ```
   pip install matplotlib
   ```

## Usage

Run the application using Python:

```
python main.py
```

### Menu Options

1. **Show The list of all crops** - Displays all crops with their current prices
2. **Add new crop to the list** - Add a new crop with its price
3. **Update the price of a crop** - Change the price of an existing crop
4. **Delete crop from the list** - Remove a crop from the database
5. **Show crop price graph of the crops** - Visualize crop prices in a bar graph
6. **Quit** - Exit the application

## File Structure

- `main.py` - Main program entry point and menu interface
- `data_handler.py` - Functions for data operations (load, save, add, update, delete)
- `graph_handler.py` - Functions for visualizing crop price data
- `Data.json` - JSON file that stores the crop data

## Data Format

The crop data is stored in JSON format with the following structure:

```json
[
  {
    "name": "Crop Name",
    "price": 120.0
  },
  ...
]
```

## Features in Detail

- Low price notification: Crops with prices below 50 NRS are marked with a low price alert
- Data persistence: All changes are saved to the JSON file automatically
- Interactive graph: Visualize prices to easily compare different crops

## License

This project is open source and available for educational and personal use. 
