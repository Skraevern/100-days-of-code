from flask import Flask
import random
app = Flask(__name__)

print(random.__name__) # random
print(__name__) # __main__

if __name__ == "__main__":
    app.run()
#  * Serving Flask app '421-__name__-__main__'
#  * Debug mode: off
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit