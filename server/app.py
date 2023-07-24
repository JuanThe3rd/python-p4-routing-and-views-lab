#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def text(text):
    print(text)
    return f'{text}'

@app.route('/count/<int:num>')
def count(num):
    count = ''

    for i in range(num):
        count += str(i) + '\n'

    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        sum = num1 + num2
        return str(sum)
    elif operation == '-':
        difference = num1 - num2
        return str(difference)
    elif operation == '*':
        product = num1 * num2
        return str(product)
    elif operation == 'div':
        quotient = num1 / num2
        return str(quotient)
    elif operation == '%':
        remainder = num1 % num2
        return str(remainder)
    else:
        return 'Invalid operation, Please try again'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
