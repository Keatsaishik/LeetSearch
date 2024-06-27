import operator
import math
import pickle
from flask import Flask, jsonify
from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

def load_links():
    with open("LC Data/final_links.txt") as f:
        links = f.readlines()
    return links

def load_idf():
    with open('LC Data/final_idf', 'rb') as f:
        idf = pickle.load(f)
    return idf

def load_idf2():
    with open('LC Data/final_idf2', 'rb') as f:
        idf2 = pickle.load(f)
    return idf2

def load_data():
    with open("LC Data/final_data.txt", 'r') as f:
        data = f.readlines()
    return data

links = load_links()
idf = load_idf()
idf2 = load_idf2()
data = load_data()

for i, item in enumerate(data) :
    data[i] = data[i][:-1]

def process(query) :
    query = query.lower()
    tfidf = {}
    final = {}
    total_docs = len(data)

    for w in query.split() :
        if w not in idf.keys() :
            continue
        for i in range(len(idf[w])) :
            a = idf[w][i]+1/len(data[i].split())+1
            b = math.log10(1+total_docs/(1+len(idf2[w])))+1
            tfidf[i] = a*b
        final[w] = tfidf

    final2 = {}

    for j in range(0, len(query.split())) :
        if query.split()[j] not in idf.keys() :
            continue
        for i in range(len(idf[ query.split()[j] ] )) :
            sum = 0
            for key in final.keys() :
                sum += final[key][i]
            final2[i] = sum/len(query.split())

    final3 = dict(sorted(final2.items(), key=operator.itemgetter(1),reverse=True))

    if(len(final3) == 0) :
        # print("No results found")
        return ["No results found :( Try again with a different query!!"]

    ans = []
    for item in list(final3.keys())[:100] :
        ans.append(links[item])
    
    return ans

class SearchForm(FlaskForm):
    search = StringField('Enter your search term :')
    submit = SubmitField('Search')

app.config['SECRET_KEY'] = 'your-secret-key'

@app.route("/<query>")
def return_links(query):
    return jsonify(process(query))


@app.route("/", methods=['GET', 'POST'])
def home():
    form = SearchForm()
    results = []
    if form.validate_on_submit():
        query = form.search.data
        results = process(query)
    return render_template('sample.html', form=form, results=results)

if __name__ == '__main__':
    app.run()