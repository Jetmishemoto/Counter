from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'Password1'



@app.route('/')         
def index():

    
    

    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")

   
    # Here we add two properties to session to store the name and email
   
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']

    

    return redirect('/show')

@app.route('/show')

def show_user():

    session['visiter'] = ''
    if "visiter" in session:
        print("A Visiter is in the session")


    print("Showing the User Info From the Form")
   
    print(request.form)
   
    return render_template("show.html")


if __name__=="__main__":   
    app.run(debug=True)    