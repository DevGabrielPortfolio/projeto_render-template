from flask import Flask, render_template
import random as rd
import os

app = Flask(__name__)



# Executa o app
if __name__ == '__main__':
    app.run(debug=True)
