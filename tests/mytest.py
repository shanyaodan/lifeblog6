from flask import Flask
import os.path
app = Flask(__name__)
print os.environ.keys()
@app.route('/testpath')
def testpath():
  pass

    # return os.pa/th.abspath(os.path.dirname(__file__))


if __name__ == '__main__':
    app.run(debug=True)