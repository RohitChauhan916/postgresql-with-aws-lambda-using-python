import pg8000
import json

host = 'Host Name'
username = 'Database Username'
password = 'Database Password'
database = 'Database Name'

#Create Connection
conn = pg8000.connect(
    host = host,
    database = database,
    user = username,
    password = password
)

def lambda_handler(event, context):
    cur = conn.cursor()
    cur.execute("select * from accounts") #Execute Query
    result = cur.fetchall()
    json_result = json.dumps(result)
    print(json_result)
    return json_result #Display Result