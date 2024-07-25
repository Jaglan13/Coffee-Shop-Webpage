import matplotlib.pyplot as plt

# Sample data for coffee sales
coffee_types = ['Espresso', 'Latte', 'Cappuccino', 'Macchiato', 'Black Coffee', 'Doppio']
sales = [150, 200, 180, 120, 250, 100]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(coffee_types, sales, color='skyblue')
plt.xlabel('Coffee Types')
plt.ylabel('Sales')
plt.title('Coffee Sales by Type')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()
