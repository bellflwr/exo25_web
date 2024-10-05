from exo25_web import create_app

app = create_app()

if __name__ == "__main__":
    app.run("localhost", 8000, debug=True)
