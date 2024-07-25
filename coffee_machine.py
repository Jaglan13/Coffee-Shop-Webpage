import pandas as pd

class CoffeeMachine:
    def __init__(self):
        # Sample data for coffee varieties
        self.coffees = pd.DataFrame({
            'name': ['Espresso', 'Latte', 'Cappuccino'],
            'description': ['Strong and rich coffee made by forcing steam through finely-ground coffee beans.',
                            'Creamy coffee made with espresso and steamed milk.',
                            'Frothy coffee made with equal parts of espresso, steamed milk, and milk foam.'],
            'price': ['$2.50', '$3.00', '$3.50']
        })

    def check_resources(self, choice):
        # Assuming there are always enough resources
        return True

    def make_coffee(self, choice):
        # Dummy function for making coffee, assuming the order is always successful
        return True

    def get_coffee_info(self):
        return self.coffees.to_dict('records')

    def generate_index_html(self):
        # Generate HTML for the index page
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Coffee Machine</title>
        </head>
        <body>
            <h1>Welcome to Our Coffee Shop!</h1>
            <ul>
        """
        for coffee in self.coffees.itertuples():
            html += f"<li>{coffee.name} - {coffee.price}</li>"
        html += """
            </ul>
        </body>
        </html>
        """
        return html

    def generate_menu_html(self):
        # Generate HTML for the menu page
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Menu</title>
        </head>
        <body>
            <h1>Menu</h1>
            <ul>
        """
        for coffee in self.coffees.itertuples():
            html += f"<li>{coffee.name} - {coffee.description} - {coffee.price}</li>"
        html += """
            </ul>
        </body>
        </html>
        """
        return html

coffee_machine = CoffeeMachine()

# Example usage
index_html = coffee_machine.generate_index_html()
menu_html = coffee_machine.generate_menu_html()

# Write HTML to files
with open("index.html", "w") as file:
    file.write(index_html)

with open("menu.html", "w") as file:
    file.write(menu_html)
