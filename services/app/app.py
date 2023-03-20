from dotenv import load_dotenv
from flask_socketio import SocketIO

from api import create_app

load_dotenv()

app = create_app()
socketio = SocketIO(app)


@socketio.on("message")
def handle_message(data):
    print("received message: " + data)


if __name__ == "__main__":
    socketio.run(app)
