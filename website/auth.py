from flask import Blueprint, render_template , redirect, url_for, request, flash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if not user:
             flash('Email does not exist.', category='error')

        if not check_password_hash(user.password, password):
              flash('Password is incorrect.', category='error')
              
        flash("Logged in!", category='success')
        login_user(user, remember=True)
        return redirect("/")
   
    return render_template("login.html")

@auth.route("/sign-up", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # Exemplo simples de validação:
        if password1 != password2:
            flash("Senhas não coincidem!", category="error")
            return render_template("signup.html", email=email, username=username)

        # Após sucesso, redirecione o usuário:
        flash("Conta criada com sucesso!", category="success")
        return redirect(url_for("auth.login"))  

    # Para GET, renderize a página de cadastro
    return render_template("signup.html")


@auth.route("/logout")
def logout():
    return redirect(url_for("views.home")) 