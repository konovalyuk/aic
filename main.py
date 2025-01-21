import fire
from app.text_completion import complete_text
from app.chat_completion import chat_completion


def main():
    fire.Fire(chat_completion)


if __name__ == '__main__':
    main()
