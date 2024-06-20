from flask import Flask, request, render_template, redirect, url_for
import sqlite3




app = Flask(__name__)



def get_conn():
    conn = sqlite3.connect("site.db")
    return conn

ADD_QUERY = "INSERT INTO history(note) VALUES(?)"
SEARCH_QUERY = "SELECT * FROM history WHERE note=?"
SEARCH_ALL_NOTE_QUERY="SELECT * FROM history"





@app.route("/",methods=["POST","GET"])
def home():
    return render_template("Home.html")





@app.route("/createNote", methods=["POST"])
def create_note():
    if request.method == "POST":
        note = request.form["note"]
        
        conn = get_conn()
        c = conn.cursor()
        
        
        
        c.execute(ADD_QUERY, (note,))
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
  
  
  

  
  




if __name__ == "__main__":
    app.run(debug=True)
