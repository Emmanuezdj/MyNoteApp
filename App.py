from flask import Flask, request, render_template, redirect, url_for
import sqlite3

import random


app = Flask(__name__)



def get_conn():
    conn = sqlite3.connect("site.db")
    return conn
    




ADD_QUERY = "INSERT INTO history(note,id) VALUES(?,?)"
SEARCH_QUERY = "SELECT * FROM history WHERE id=?"
SEARCH_ALL_NOTE_QUERY="SELECT * FROM history"




@app.route("/")
@app.route("/home",methods=["POST","GET"])
def home():
    return render_template("Home.html")





@app.route("/createNote", methods=["POST"])
def create_note():
    if request.method == "POST":
        note = request.form["note"]
        i_d=random.randint(1, 10000000000000000000)
        
        
        
        

        conn = get_conn()
        c = conn.cursor()
        
        c.execute(ADD_QUERY, (note,i_d))
        conn.commit()
        
         # Close the connection after the operations
        
        # After creating the note, redirect to a confirmation page or the home page
        row="success"
        
        
        return redirect(url_for('home',row=row))
        
        conn.close() 




@app.route("/pre_creating")
def pre_creating():
    return render_template("create.html")






@app.route("/viewNotes",methods=["GET","POST"])
def view_note():
  conn = get_conn()
  c = conn.cursor()
  c.execute(SEARCH_ALL_NOTE_QUERY)
  res=c.fetchall()
  conn.commit()
  return render_template("view.html",res=res)
  conn.close()
  
  

@app.route('/delete_note/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    
    conn=get_conn()
    c=conn.cursor()
    
    SEARCH_QUERY = "SELECT * FROM history WHERE id=?"
    
    c.execute(SEARCH_QUERY,(note_id,))
    conn.commit()
    
    w=c.fetchone()
    
    DELETE_QUERY="DELETE FROM history WHERE id=?"
    
    c.execute(DELETE_QUERY,(note_id,))
    conn.commit()
    
    
    return "success"
    conn.close()






if __name__ == "__main__":
    app.run(debug=True)
