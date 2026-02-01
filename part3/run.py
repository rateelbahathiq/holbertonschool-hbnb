from app import create_app
<<<<<<< HEAD

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
=======
from app.config import DevelopmentConfig

app = create_app(DevelopmentConfig)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
