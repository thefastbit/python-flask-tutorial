# Simple Python Flask WebServices
# By The FastBit   ( ._. ) 
#
#
#


from app import app
from flask import jsonify
from flask import request
#from flask_mysql import MySQL
from flaskext.mysql import MySQL


# DB conection (MySQL)
#
#



mysql = MySQL()

# MySQL configurations
#Yeah I know no root but this is just a simple code example :P 
app.config['MYSQL_DATABASE_USER'] = 'root'
# I have no fix a clear password on the script!!
app.config['MYSQL_DATABASE_PASSWORD'] = '1234admP'
app.config['MYSQL_DATABASE_DB'] = 'sistema'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

#Starting flask DB engine 
mysql.init_app(app)

conn = mysql.connect()



@app.route('/people/ws',methods=['GET'])
def getAll():
#Preparing a db cursor to hold db responses
    cursor = conn.cursor()
    cursor.callproc('getAll')
    data = cursor.fetchall()

    return jsonify({'data':data})





@app.route('/people/ws/<empId>',methods=['GET'])
def getEmp(empId):
#Preparing a db cursor to hold db responses
    cursor = conn.cursor()
    cursor.callproc('getEmp',empId)
    print '**************'
    print cursor
    print '**************'
  


    if  empty(cursor)  :
        conn.commit()
        return {'StatusCode':'000','Message':'Error no data found'}
    
    
    else:
         data = cursor.fetchall()
    return jsonify({'data':data})










people=[
 {
 'id':'1',
 'name':'TheFastBit',
 'title':'Python Dev'
 },
 {
 'id':'2',
 'name':'DarkOrk',
 'title':'Java Dev'
 },
 {
 'id':'3',
 'name':'BlueRabit',
 'title':'NET Dev'
 }

 ]

#Hello !!!
#
@app.route('/')
@app.route('/index')
def index():
    return 'Bienvenido a WebservicesFactory by TheFatsBit'

#Sent back all the data
#
@app.route('/people/team',methods=['GET'])
def getAllPeople():
    return jsonify({'team':people})


#Sent back an specific record
#
@app.route('/people/team/<peopleId>',methods=['GET'])
def getPeople(peopleId):
    usr = [ reg for reg in people if (reg['id'] == peopleId) ] 
    return jsonify({'people':usr})


#Create a new record
#
@app.route('/people/team',methods=['POST'])
def createPeople():
    request_data = request.get_json()    
    print '___________'
    print request_data
    print '___________'
    print is_json(request_data)   
    #Rejecting empty requests
    if is_json(request_data):
       return jsonify({'response':'failed not data received'})
    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'title':request.json['title']
    }
    people.append(dat) 
    return jsonify(people)
  

 # alternative  
 # return jsonfy({'response':'Success'}) 



#Update record
#
@app.route('/people/team/<peopleId>',methods=['PUT'])
def updatePeople(peopleId):
    if len(peopleId) == 0:
       return jsonify({'response':'failed not id provided'})  
    if not (request.data):
       return jsonify({'response':'failed not data received'})  
    reg = [ reg for reg in people if (reg['id'] == peopleId) ] 
    if 'name' in request.json : 
        reg[0]['name'] = request.json['name'] 
    if 'title' in request.json:
        reg[0]['title'] = request.json['title'] 
    #return jsonify({'emp':reg[0]})
    return jsonify({'response':'Success'})



#Delete record
#
@app.route('/people/team/<peopleId>',methods=['DELETE'])
def removePeople(peopleId): 
    usr = [ reg for reg in people if (reg['id'] == peopleId) ] 
    if len(usr) == 0:
       return jsonify({'response':'failed not found'})
    people.remove(usr[0])
    return jsonify({'response':'Success'})
  

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError, e:
    return False
  return True


def isBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return False
    #myString is None OR myString is empty or blank
    return True










