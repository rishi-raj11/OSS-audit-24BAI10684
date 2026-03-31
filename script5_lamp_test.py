import mysql.connector
import platform

def lamp_test():
    print("=== LAMP STACK TEST ===")
    print(f"OS: {platform.system()} {platform.release()}")
    
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # agar password hai toh use kro
        )
        if connection.is_connected():
            print("MySQL Server Connection: SUCCESS")
            connection.close()
    except Exception as e:
        print(f"MySQL Server Connection: FAILED ({e})")

if __name__ == "__main__":
    lamp_test()
