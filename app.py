from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 1000000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 1500000'
    },
    {
        'id':3,
        'title':'Frontend Engineer',
        'location': 'Remote',
        'salary': 1200000
    },
    {
        'id':3,
        'title':'Backend Engineer',
        'location': 'San fransisco, USA',
        'salary': "$120000"
    }            

]

@app.route("/")
def home():
    return render_template('home.html', jobs=JOBS)

if __name__ == "__main__":
    app.run(debug=True)
    