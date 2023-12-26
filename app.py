from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/parse1')
# def parse1():
#     return render_template('parse1.html')  # Assuming you have an HTML template named parse1.html

@app.route('/')
def index(name=None):
    return render_template('index.html',name=name)

@app.route('/exec')
def parse(name=None):
    import face_recognize
    print("done")
    return render_template('index.html',name=name)

@app.route('/exec2')
def parse1(name=None):
	import create_data
	print("done")
	return render_template('index.html',name=name)

if __name__ == '__main__':
    app.run()
    app.debug = True