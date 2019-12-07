import mysql.connector

from utils.config import Config


class DBConnection:

    def create_connection(self):
        conn = mysql.connector.connect(
            host=Config.mysql_host,
            user=Config.mysql_user,
            passwd=Config.mysql_password,
            database=Config.mysql_db,
            auth_plugin='mysql_native_password'
        )

        return conn, conn.cursor()


