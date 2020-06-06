import pymysql, os, json, requests
from datetime import datetime

# read JSON file which is in the next parent folder
file = requests.get(url='YOURURLTOJSON')

#save JSON file to disk
data = file.json()
with open('YourData.json', 'w') as f:
    json.dump(data, f)

# Read JSON file
file = "YourData.json"
json_data=open(file).read()
json_obj = json.loads(json_data)


# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val


# connect to MySQL
con = pymysql.connect(host = 'localhost', port = 8889,user = 'root',passwd = 'root',db = 'test')
cursor = con.cursor()


# parse json data to SQL insert
for i, item in enumerate(json_obj["Sendungsnummern"]['Sendungen']):
    sdgid = validate_string(item.get("sdgid", None))
    kdlsnr = validate_string(item.get("kdlsnr", None))
    carrier = validate_string(item.get("carrier", None))
    nve = validate_string(item.get("nve", None))
    d = datetime.strptime(item.get("liefdatum"), '%d.%m.%Y')
    liefdatum = d.strftime('%Y-%m-%d')

    cursor.execute("INSERT IGNORE INTO testp (sdgid, kdlsnr, carrier, nve, liefdatum) VALUES (%s,%s,	%s, %s, %s)", (sdgid, kdlsnr, carrier, nve, liefdatum))
con.commit()
con.close()