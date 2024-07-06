# Restaurant-Chains
Identify if there are any restaurant chains present in the dataset. Analyze the ratings and popularity of different restaurant chains.

Data Analysis:

Identify restaurant chains by counting occurrences of restaurant names.
Filter data to include only restaurant chains.
Calculate average ratings and popularity (number of outlets) for each chain.
GUI Design:

Used ttk for modern and attractive widgets.
Created a main window with buttons to open separate analysis windows.
Each analysis (average ratings and popularity) opens in a new window.
Visualization:

Used Seaborn for bar plots to visualize average ratings and popularity of restaurant chains.
Configured the plot for better readability (e.g., rotated x-axis labels).
Improved README:
Restaurant Data Analysis
This project is a Tkinter-based application for analyzing restaurant data from a CSV file. It identifies restaurant chains and analyzes their ratings and popularity. The results are displayed both in text format and through graphical visualizations using Matplotlib and Seaborn.

Features
Identify Restaurant Chains: Detects restaurant chains by counting occurrences of restaurant names.
Average Ratings of Restaurant Chains: Analyzes and visualizes the average ratings of different restaurant chains.
Popularity of Restaurant Chains: Analyzes and visualizes the popularity (number of outlets) of different restaurant chains.
Graphical Visualizations: Provides bar charts to visualize the ratings and popularity of restaurant chains.
Prerequisites
Python 3.x
pandas
tkinter
matplotlib
seaborn
Installation
Clone the repository:
bash
cd restaurant-data-analysis
Install the required libraries:
bash
Copy code
pip install pandas tkinter matplotlib seaborn
Usage
Make sure your dataset CSV file is properly formatted and placed in the correct directory. Update the file path in the script if necessary.
Run the script:
bash
Copy code
python main.py
Code Overview
Data Loading
The dataset is loaded using pandas.read_csv and processed to identify restaurant chains and analyze their ratings and popularity.

Tkinter Interface
A Tkinter window is created to display the results. The interface includes buttons to open separate windows for each type of analysis.

Matplotlib and Seaborn Visualizations
Two bar charts are generated using Matplotlib and Seaborn:

One for the average ratings of restaurant chains.
Another for the popularity (number of outlets) of restaurant chains.
Dataset
Ensure that your dataset CSV file contains at least the following columns:

Restaurant Name: The name of the restaurant.
Aggregate rating: The rating of the restaurant.
Price range: The price range category of the restaurant.
Has Online delivery: Whether the restaurant offers online delivery (Yes/No).
Has Table booking: Whether the restaurant offers table booking (Yes/No).
Example Dataset
Here's a snippet of what your dataset might look like:

csv
Copy code
Restaurant Name,Aggregate rating,Price range,Has Online delivery,Has Table booking
Restaurant A,4.5,3,Yes,Yes
Restaurant B,4.0,2,No,No
Restaurant A,4.2,3,Yes,Yes
...
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
This project was developed by [kartik jain].
Special thanks to the open-source community for providing the necessary libraries and tools.
