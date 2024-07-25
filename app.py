from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class CoffeeMachine:
    def __init__(self):
        self.water = 1000  # Initial water level in ml
        self.milk = 500  # Initial milk level in ml
        self.coffee_beans = 300  # Initial coffee beans level in grams
        self.money = 0  # Initial money collected

    def check_resources(self, choice):
        if choice == 1:  # Espresso
            if self.water < 50 or self.coffee_beans < 20:
                return False
        elif choice == 2:  # Latte
            if self.water < 100 or self.milk < 100 or self.coffee_beans < 20:
                return False
        elif choice == 3:  # Cappuccino
            if self.water < 100 or self.milk < 50 or self.coffee_beans < 20:
                return False
        return True

    def make_coffee(self, choice):
        if choice == 1:
            self.water -= 50
            self.coffee_beans -= 20
        elif choice == 2:
            self.water -= 100
            self.milk -= 100
            self.coffee_beans -= 20
        elif choice == 3:
            self.water -= 100
            self.milk -= 50
            self.coffee_beans -= 20
        self.money += self.process_payment(choice)
        return True

    def process_payment(self, choice):
        if choice == 1:
            return 2.50
        elif choice == 2:
            return 3.00
        elif choice == 3:
            return 3.50

coffee_machine = CoffeeMachine()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    data = request.get_json()
    choice = int(data['choice'])
    if coffee_machine.check_resources(choice):
        success = coffee_machine.make_coffee(choice)
        if success:
            return jsonify({'status': 'success', 'message': 'Coffee is ready! Enjoy!'})
        else:
            return jsonify({'status': 'error', 'message': 'Failed to make coffee!'})
    else:
        return jsonify({'status': 'error', 'message': 'Not enough resources to make coffee!'})

if __name__ == '__main__':
    app.run(debug=True)
