import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv(r"C:\Users\HP\Desktop\kartik\Dataset .csv")

# Identify restaurant chains by checking if the same restaurant name appears multiple times
restaurant_counts = data['Restaurant Name'].value_counts()
restaurant_chains = restaurant_counts[restaurant_counts > 1]

# Filter data for restaurant chains
chain_data = data[data['Restaurant Name'].isin(restaurant_chains.index)]

# Calculate average ratings for each restaurant chain
chain_avg_ratings = chain_data.groupby('Restaurant Name')['Aggregate rating'].mean()

# Calculate the popularity of each restaurant chain (number of outlets)
chain_popularity = chain_data['Restaurant Name'].value_counts()

# Function to create a window for restaurant chains average ratings
def chain_avg_ratings_window():
    window = tk.Toplevel(root)
    window.title("Restaurant Chains Average Ratings")
    window.geometry("800x600")

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=chain_avg_ratings.index, y=chain_avg_ratings.values, ax=ax, palette="viridis")
    ax.set_xlabel('Restaurant Chains')
    ax.set_ylabel('Average Rating')
    ax.set_title('Average Ratings of Restaurant Chains')
    ax.tick_params(axis='x', rotation=90)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Function to create a window for restaurant chains popularity
def chain_popularity_window():
    window = tk.Toplevel(root)
    window.title("Restaurant Chains Popularity")
    window.geometry("800x600")

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=chain_popularity.index, y=chain_popularity.values, ax=ax, palette="viridis")
    ax.set_xlabel('Restaurant Chains')
    ax.set_ylabel('Number of Outlets')
    ax.set_title('Popularity of Restaurant Chains')
    ax.tick_params(axis='x', rotation=90)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Create the main window
root = tk.Tk()
root.title("Restaurant Data Analysis")
root.geometry("400x300")

# Apply a theme
style = ttk.Style(root)
style.theme_use('clam')

# Set up font and colors
root.option_add("*Font", "Helvetica 12")
style.configure("TButton", padding=6, relief="flat", background="#ccc")
style.map("TButton", background=[('active', '#0052cc')], foreground=[('active', 'white')])

# Create a frame
frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

# Title label
title_label = ttk.Label(frame, text="Restaurant Data Analysis", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Create buttons to open each graph window
ttk.Button(frame, text="Restaurant Chains Average Ratings", command=chain_avg_ratings_window).pack(padx=10, pady=10)
ttk.Button(frame, text="Restaurant Chains Popularity", command=chain_popularity_window).pack(padx=10, pady=10)

# Start the main event loop
root.mainloop()
