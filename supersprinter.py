from flask import Flask,request,url_for,render_template,redirect
from database import Database
from models import *

app=Flask(__name__,template_folder="templates")
fields=list(Story._meta.fields.keys())
states=["planning","todo","in_progress","review","complete"]

def createtables():
  Database.database.drop_tables([Story],safe=True)
  Database.database.create_tables([Story],safe=True)

@app.route('/')
@app.route('/list',methods=['GET'])
def storytable():
  records=Story.select()
  return render_template('list.html',records=records,fields=fields)

@app.route("/story",methods=["GET"])
def create_story():
  header="Create Story"
  return render_template("form.html",header=header,fields=fields,states=states,button="Create")

@app.route('/story',methods=['POST'])
def record_story():
  record=Story.create()
  for field in fields:
    setattr(record,field,request.form[field])
  return redirect(url_for('storytable'))

@app.route("/story/<record_id>",methods=["GET"])
def edit_story(record_id):
  header="Edit story"
  record=Story.get(Story.id==record_id)
  return render_template("form.html",header=header,fields=fields,record=record,states=states,button="Update")

@app.route('/story/<record_id>',methods=['POST'])
def update_story(record_id):
  record=Story.select().where(Story.id==record_id).get()
  for field in fields:
    setattr(record,field,request.form[field])
  return redirect(url_for('storytable'))

@app.route('/delete/<record_id>',methods=['GET'])
def delete_story(record_id):
  record=Story.select().where(Story.id==record_id).get()
  record.delete_instance()
  return redirect(url_for('storytable'))

if __name__=='__main__':
  createtables()
  app.run(debug=True)

