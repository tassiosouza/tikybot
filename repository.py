import mysql.connector

COMMAND_CREATE_DATABASE = "CREATE DATABASE tikybot"

COMMAND_CREATE_CLIENTS_DATABASE = """CREATE TABLE customers (
                                    id INT AUTO_INCREMENT PRIMARY KEY,
                                    username VARCHAR(255),
                                    name VARCHAR(255));"""

COMMAND_CREATE_CLIENTS_DATABASE = """CREATE TABLE tiktokers (
                                    id INT AUTO_INCREMENT PRIMARY KEY,
                                    username VARCHAR(255),
                                    name VARCHAR(255)
                                    gender VARCHAR(1));"""

# class Repository:
#
#     tikybot_database = mysql.connector.connect(
#       host="localhost",
#       user="root",
#       password="1234",
#       database="tikybot"
#     )

    # def create_database(self):
    #     mycursor = self.tikybot_database.cursor()