from app.routes import *


def main():
    os.makedirs(AppConfig.UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)


if __name__ == '__main__':
    main()
