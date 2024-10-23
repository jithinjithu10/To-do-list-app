from app import create_app  # Make sure this line is correct

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
