import mysql.connector


def connectToMySQL():
    cnx = mysql.connector.connect(password = 'pass', user='user')
    cursor = cnx.cursor()
    return cursor, cnx

def query(term):
    connectToMySQL()
    cursor, connection = connectToMySQL()
    cursor.execute("USE Info;")
    sql = "SELECT * FROM states WHERE State = '" + term +"';"
    print(sql)


def main():
    connectToMySQL()
    cursor, connection = connectToMySQL()
    cursor.execute("USE Info;")
    query("Alabama")

def selectAll(cursor, connection):
    cursor.execute("SELECT * FROM states;")
    result = cursor.fetchone()
    print("State, Capitol, Latitude, Longitude")
    while result is not None:
        print(result[0],result[1],result[2],result[3], sep=",")
        result = cursor.fetchone()

        
main()
