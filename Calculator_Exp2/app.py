from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        first_number = float(request.form['first_number'])
        second_number = float(request.form['second_number'])
        operation = request.form['operation']

        if operation == '+':
            result = first_number + second_number
        elif operation == '-':
            result = first_number - second_number
        elif operation == '*':
            result = first_number * second_number
        elif operation == '/':
            result = first_number / second_number
        else:
            result = 'Invalid operation'

        return render_template('calculator.html', first_number=first_number, second_number=second_number, operation=operation, result=result)
    else:
        return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
