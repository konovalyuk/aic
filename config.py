import os


class AppConfig:
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', '/home/maksym/my/dc/contracts')
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')  # Установите уникальный ключ


class ModelConfig:
    CKPT_DIR = os.getenv('CKPT_DIR', '/home/maksym/.llama/checkpoints/Llama3.2-1B-Instruct')
    MAX_SEQ_LEN = os.getenv('MAX_SEQ_LEN', 1024)
    MAX_BATCH_SIZE = os.getenv('MAX_BATCH_SIZE', 1)  # 4
    MODEL_PARALLEL_SIZE = os.getenv('MODEL_PARALLEL_SIZE', 1)
    TEMPERATURE = os.getenv('TEMPERATURE', 0.6)
    TOP_P = os.getenv('TOP_P', 0.9)
    MAX_GEN_LEN = os.getenv('MAX_GEN_LEN', 256)
    MAX_DIALOG_LENGTH = os.getenv('MAX_DIALOG_LENGTH', 1024)


class PDFConfig:
    FONT_PATH = os.getenv('FONT_PATH', 'app/static/font/FreeSans.ttf')
