from redis import Redis
from flask import Flask, request

redis = Redis()
app = Flask(__name__)
app.config['REDIS_QUEUE_KEY'] = 'my_queue'

@app.route('/set_user', methods=['POST'])
def set():
    for key, val in request.get_json().iteritems():
        redis.set(key, val)

@app.route('/get/<key>', methods=['GET'])
def get(key):
    return redis.get(key)

if __name__ == "__main__":
    app.run(port=80, debug=True)
