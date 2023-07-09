from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'Password1'



@app.route('/')         
def main_page():
    
    if not 'num_visits' in session:
        session['num_visits'] = 0
        
    else:
       session['num_visits'] += 1
       print("A Visiter is in the session")
       print( "Num of Visiters : " + str(session['num_visits']))

    return render_template("index.html" ,num_visits = session['num_visits'] )

@app.route('/reset',methods=['POST'] )         
def reset():
       
    session['num_visits'] = 0

    return redirect('/')


@app.route('/clear',methods=['POST'] )         
def clear_session():
       
    session['clear'] = session.clear()

    return redirect('/')



@app.route('/add2',methods=['POST'] )         
def add2_session():
    
    session['num_visits'] += 1

    return redirect('/')



@app.route('/users', methods=['POST'])
def create_user():
  
    return redirect('/')




if __name__=="__main__":   
    app.run(debug=True)    