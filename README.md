# JSON2SQL
Dump JSON Data into MySQL Database
You need a running MySQL-DB.

# Download JSON File
    file = requests.get(url='YOURURLTOJSON')
Setup the URL of your JSON-Request

# connect to MySQL
    con = pymysql.connect(host = 'localhost', port = 8889,user = 'root',passwd = 'root',db = 'test')

Setup your MySQL-DB


# parse json data to SQL insert
    for i, item in enumerate(json_obj["Sendungsnummern"]['Sendungen']):
        sdgid = validate_string(item.get("sdgid", None))
        kdlsnr = validate_string(item.get("kdlsnr", None))
        carrier = validate_string(item.get("carrier", None))
        nve = validate_string(item.get("nve", None))
        d = datetime.strptime(item.get("liefdatum"), '%d.%m.%Y')
        liefdatum = d.strftime('%Y-%m-%d')
    
In this example I have an nestes JSON. So you have to setup your "json_obj" to your JSON
Next, the keys are read and validated as string. You have to adapt this part completely to your JSON.
As an example I convert a date into a different format below. 

# SQL Insert
    cursor.execute("INSERT IGNORE INTO testp (sdgid, kdlsnr, carrier, nve, liefdatum) VALUES (%s,%s,	%s, %s, %s)", (sdgid, kdlsnr, carrier, nve, liefdatum))
 
Here you must enter your JSON-Keys.
