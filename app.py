from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # You can add code to save or send data here
        return render_template('feedback.html', success=True, name=name)
    return render_template('feedback.html', success=False)

if __name__ == '__main__':
    app.run(debug=True)
