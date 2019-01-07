from flask import Flask, render_template, url_for, request
from apriori import Apriori
from bruteforce import frequentDoubles, frequentTriples
import time


application = Flask(__name__)
@application.route('/')
def index():
    return render_template('index.html')

@application.route('/generaterule', methods = ['POST'])
def generaterule():
    if request.method == 'POST':
        print("inside recommend")
        minSupport = request.form['minSupport']
        minConfidence = request.form['minConfidence']
        apstart = time.time();
        items,rules = Apriori(minConfidence, minSupport)
        apend = time.time();
        bfstart = time.time();
        ordered = frequentDoubles(minSupport)
        bfend = time.time();
        tstart = time.time();
        tripleOrdered = frequentTriples(minSupport)
        tend = time.time();
        aptime = apend - apstart;
        bftime = bfend - bfstart;
        ttime = tend - tstart;
        return render_template('index.html', items = items, rules = rules, ordered = ordered, tordered = tripleOrdered, aptime = aptime, bftime = bftime, ttime = ttime)
    return render_template('index.html')


if __name__ == '__main__':
    application.run(debug = True)
