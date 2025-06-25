from flask import Flask, render_template, send_from_directory, url_for
import os
app = Flask(__name__, static_folder='static')  # Set current directory as static folder

@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

@app.route('/')
def index():
    image_url = url_for('static', filename='images/graduation.webp')
    print("Generated image URL:", image_url)  # Debugging output
    return render_template('index.html')

@app.route('/blogs.html')
def blogs():
    return render_template('blogs.html')

@app.route('/career-timeline.html')
def career():
    return render_template('career-timeline.html')

@app.route('/career-experience.html')
def career_experience():
    return render_template('career-experience.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(debug=True)
