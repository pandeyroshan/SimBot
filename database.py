import sqlite3

def create_connection():
    bot_training_connection = sqlite3.connect('bot-training.db')


if __name__ == '__main__':
    create_connection()