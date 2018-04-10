from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG']= True



@app.route("/signup", methods=['POST'])
def signin():
    
    user_name_input = request.form['user_name']
    password_input = request.form['password']
    confirm_pass_input = request.form['conf_pass'] 
    email_input = request.form['user_email']    

    user_name_error = ''
    pass_error = ''
    conf_pass_error = ''
    email_error = ''

    if user_name_input.strip()=="":
        user_name_error = "Please enter the user name"
        #user_name_input = ''
        
    else:
        if len(user_name_input)<7:
            user_name_error = "User name should be minimum 7 characters"  
            #user_name_input = ''
        #return render_template("index.html", error1=error1)
    
    if password_input.strip()=="":
        pass_error = "Please enter a valid password"
        password_input = ''
    else:
        if password_input == user_name_input:
            pass_error = "User name and password cannot be same"
        elif len(password_input)<3 or len(password_input)>20:
            pass_error = "Password too weak"
            password_input = ''
            if ' ' in password_input:
                pass_error = "No blank space allowed in password"
                password_input = ''
        #return redirect("/?error="+error2)
        #return render_template("index.html", error2=error2)
    
    if confirm_pass_input.strip()=="":
        conf_pass_error = "Please re-enter the password"
        confirm_pass_input = ''
    else:
        if confirm_pass_input != password_input:
            conf_pass_error = "Password doesn't match"
            confirm_pass_input = ''
            if ' ' in confirm_pass_input:
                conf_pass_error = "No blank space allowed in password"
                confirm_pass_input = ''
        #return redirect("/?error="+error3)
        #return render_template("index.html", error3=error3)
    
    if email_input != "":
        if len(email_input)<=3 or len(email_input)>20:
            email_error = "Please enter a valid email ID"
            if '@' not in email_input:
                if '.' not in email_input:
                    email_error = "Please enter a valid email ID"
                    if ' ' in email_input:
                        email_error = "No blank space allowed in email ID"
                    
        

    if not user_name_error and pass_error and conf_pass_error:
        return render_template('index.html', user_name=user_name_input, password=password_input, 
        conf_pass=confirm_pass_input, user_email=email_input, error1=user_name_error, error2=pass_error, 
        error3=conf_pass_error, error4=email_error)
    elif email_error and not user_name_error and not pass_error and not conf_pass_error:
        return render_template('index.html', user_name=user_name_input, password=password_input, 
        conf_pass=confirm_pass_input, user_email=email_input, error1=user_name_error, error2=pass_error, 
        error3=conf_pass_error, error4=email_error)
    elif not user_name_error and not pass_error and conf_pass_error:
        return render_template('index.html', user_name=user_name_input, password=password_input, 
        conf_pass=confirm_pass_input, euser_email=email_input, error1=user_name_error, error2=pass_error, 
        error3=conf_pass_error, error4=email_error)
    elif not user_name_error and not pass_error and not conf_pass_error:
        return render_template("welcome.html", user_name=user_name_input)
    else:
        return render_template('index.html', user_name=user_name_input, password=password_input, 
        conf_pass=confirm_pass_input, user_email=email_input, error1=user_name_error, error2=pass_error, 
        error3=conf_pass_error, error4=email_error)

@app.route("/")
def index():
    #encoded_error = request.args.get("user_name_error")
    #return render_template('index.html', user_name_error=encoded_error and cgi.escape(encoded_error, quote=True))
    return render_template('index.html')


app.run()
