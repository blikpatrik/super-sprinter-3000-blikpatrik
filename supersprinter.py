from flask import Flask,request,url_for,render_template,redirect
from database import Database
from models import *

app=Flask(__name__,template_folder="templates")
@app.route('/')
@app.route('/list',methods=['GET'])
def storyteller():
    stories=Story.select().order_by(Story.id)
    return render_template('list.html', stories=stories)
@app.route('/story/', methods=['POST'])
def add_story():
    update=Story.create(title=request.form['title'],
                             text=request.form['text'],
                             criteria=request.form['criteria'],
                             value=request.form['value'],
                             estimation=request.form['estimation'],
                             status=request.form['status'])
    update.save()
    return redirect(url_for('storyteller'))
@app.route('/story/<story_id>', methods=['POST'])
def edit_story(story_id):
    edits=Story.update(title==request.form['title'],
                       text=request.form['text'],
                       criteria=request.form['criteria'],
                       value=request.form['value'],
                       estimation=request.form['estimation'],
                       status=request.form['status']).where(Story.id==story_id)
    edits.execute()
    return redirect(url_for('storyteller'))
@app.route('/delete/<story_id>',methods=['POST'])
def delete_story(story_id):
    story=Story.select().where(Story.id==story_id).get()
    story.delete_instance()
    story.save()
    return redirect(url_for('storyteller'))
@app.route("/form",methods=["GET","POST"])
def form():
    story=[]
    return render_template("form.html",story=story,header="Create story",button="Create")
@app.route("/story/<story_id>",methods=["GET"])
def edit(story_id):
    story=Story.get(Story.id==story_id)
    return render_template("form.html",story=story,header="Edit story",button="Update")

if __name__=='__main__':
    CreateTables.createtables()
    app.run(debug=True)

