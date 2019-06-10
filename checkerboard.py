from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
# def hello_checkerboard():
#     return render_template('index.html')

def hello_checkerboard(times):
    return render_template('index.html', times=int(times))

# @app.route('/play/<times>')
# def index_play_x(times):
#     return render_template('index.html', times=int(times))

if __name__=="__main__":
    app.run(debug=True)

