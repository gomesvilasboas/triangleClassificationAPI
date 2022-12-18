import sys
from application import app

sys.path.insert(0, "./")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
