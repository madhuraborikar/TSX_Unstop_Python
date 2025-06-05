import json
from flask import Flask, render_template

app = Flask(__name__)

def load_projects():
    with open('portfolio.json', 'r') as file:
        projects = json.load(file)
        return projects
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects = load_projects()
    
    return render_template('projects.html', projects=projects)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
# To run the application, use the command: python app.py
