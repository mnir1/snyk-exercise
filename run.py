#!flask/bin/python

from app import app,cache

cache.init_app(app)
app.run(debug=True, host="0.0.0.0", port=5000)