from sqlalchemy.sql.functions import current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dima_shop1.db'
db = SQLAlchemy(app)
res_busy = []
class Things(db.Model):
    __tablename__ = 'things'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    product_information = db.Column(db.Text(300), nullable=False)
    cost = db.Column(db.Float)

class Tovar(db.Model):
    __tablename__ = 'tovar'
    id = db.Column(db.Integer, primary_key=True)
    opis = db.Column(db.Text(300), nullable=False)
    photo = db.Column(db.Text(300), nullable=False)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=True)


class Cart(db.Model):
    __tablename__ = 'cort'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    thing_id = db.Column(db.Integer, db.ForeignKey("things.id"))
    quantity = db.Column(db.String)


class SiteInfo(db.Model):
    __tablename__ = 'site_inf'
    id = db.Column(db.Integer, primary_key=True)
    website_info = db.Column(db.Text(300), nullable=False)


@app.route("/")
def index():
    with open("design.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/add_cors", methods=('POST', 'GET'))
def i1():
    if request.method == 'GET':
        try:
            s = Cart(user_id=current_user.id, thing_id=1, quantity=1)
            bob = Tovar(id=current_user.id, opis="товар: модная толстовка белая цена: 3000 руб",
                        photo="https://i.ibb.co/J7qXqPh/photo-2024-04-13-19-46-34-2.jpg")
            db.session.add(bob)
            db.session.add(s)
            db.session.commit()
            print(9)
            with open("add_to_kors.html", 'r', encoding='utf-8') as html_stream:
                return html_stream.read()
        except Exception as e:
            print(e)
            return 'Авторизируйтесь или проверьте наличие товара'
    else:
        print(8)
    with open("add_to_kors.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/add_cors2")
def i4():
    if request.method == 'GET':
        try:
            sw = Tovar.query.all()
            print(sw[0].opis)
            print(sw[0].photo)
            admin = Tovar.query.filter_by(opis=sw[0].opis).first()
            admin2 = Tovar.query.filter_by(photo=sw[0].photo).first()
            admin.opis = sw[0].opis + ", товар: модная толстовка черная цена: 3000 руб"
            admin2.photo = sw[0].photo + ", https://i.ibb.co/vZgyWrj/photo-2024-04-13-19-46-34.jpg"
            db.session.commit()
            print(9)
            with open("add_to_kors2.html", 'r', encoding='utf-8') as html_stream:
                return html_stream.read()
        except Exception as e:
            print(e)

            return 'Авторизируйтесь или проверьте наличие товара'
    else:
        print(8)
    with open("add_to_kors2.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/add_cors3")
def i5():
    if request.method == 'GET':
        try:
            sw = Tovar.query.all()
            print(sw[0].opis)
            print(sw[0].photo)
            admin = Tovar.query.filter_by(opis=sw[0].opis).first()
            admin2 = Tovar.query.filter_by(photo=sw[0].photo).first()
            admin.opis = sw[0].opis + ", товар: модные стринги белые цена: 3000 руб"
            admin2.photo = sw[0].photo + ", https://i.ibb.co/s5LGJnD/photo-2024-04-13-19-32-50.jpg"
            db.session.commit()
            print(9)
            with open("add_to_kors3.html", 'r', encoding='utf-8') as html_stream:
                return html_stream.read()
        except Exception as e:
            print(e)

            return 'Авторизируйтесь или проверьте наличие товара'
    else:
        print(8)
    with open("add_to_kors3.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/add_cors4")
def i6():
    if request.method == 'GET':
        try:
            sw = Tovar.query.all()
            print(sw[0].opis)
            print(sw[0].photo)
            admin = Tovar.query.filter_by(opis=sw[0].opis).first()
            admin2 = Tovar.query.filter_by(photo=sw[0].photo).first()
            admin.opis = sw[0].opis + ", товар: модные стринги черные цена: 3000 руб"
            admin2.photo = sw[0].photo + ", https://i.ibb.co/16Kx2JC/photo-2024-04-13-19-32-50-2.jpg"
            db.session.commit()
            print(9)
            with open("add_to_kors4.html", 'r', encoding='utf-8') as html_stream:
                return html_stream.read()
        except Exception as e:
            print(e)

            return 'Авторизируйтесь или проверьте наличие товара'
    else:
        print(8)
    with open("add_to_kors4.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/add_cors5")
def i7():
    if request.method == 'GET':
        try:
            sw = Tovar.query.all()
            print(sw[0].opis)
            print(sw[0].photo)
            admin = Tovar.query.filter_by(opis=sw[0].opis).first()
            admin2 = Tovar.query.filter_by(photo=sw[0].photo).first()
            admin.opis = sw[0].opis + ", товар: модная футболка белая цена: 3000 руб"
            admin2.photo = sw[0].photo + ", https://i.ibb.co/Px80n8M/photo-2024-04-13-19-32-50-4.jpg"
            db.session.commit()
            print(9)
            with open("add_to_kors5.html", 'r', encoding='utf-8') as html_stream:
                return html_stream.read()
        except Exception as e:
            print(e)

            return 'Авторизируйтесь или проверьте наличие товара'
    else:
        print(8)
    with open("add_to_kors5.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/add_cors6")
def i8():
    if request.method == 'GET':
        try:
            sw = Tovar.query.all()
            print(sw[0].opis)
            print(sw[0].photo)
            admin = Tovar.query.filter_by(opis=sw[0].opis).first()
            admin2 = Tovar.query.filter_by(photo=sw[0].photo).first()
            admin.opis = sw[0].opis + ", товар: модная футболка черная цена: 3000 руб"
            admin2.photo = sw[0].photo + ", https://i.ibb.co/D8fqwfw/photo-2024-04-13-19-32-50-3.jpg"
            db.session.commit()
            print(9)
            with open("add_to_kors6.html", 'r', encoding='utf-8') as html_stream:
                return html_stream.read()
        except Exception as e:
            print(e)

            return 'Авторизируйтесь или проверьте наличие товара'
    else:
        print(8)
    with open("add_to_kors6.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/add_cors7")
def i9():
    if request.method == 'GET':
        try:
            sw = Tovar.query.all()
            print(sw[0].opis)
            print(sw[0].photo)
            admin = Tovar.query.filter_by(opis=sw[0].opis).first()
            admin2 = Tovar.query.filter_by(photo=sw[0].photo).first()
            admin.opis = sw[0].opis + ", товар: модная кружка уауауа цена: 3000 руб"
            admin2.photo = sw[0].photo + ", https://i.ibb.co/5FfMCM2/photo-2024-04-14-21-33-29.jpg"
            db.session.commit()
            print(9)
            with open("add_to_kors7.html", 'r', encoding='utf-8') as html_stream:
                return html_stream.read()
        except Exception as e:
            print(e)

            return 'Авторизируйтесь или проверьте наличие товара'
    else:
        print(8)
    with open("add_to_kors7.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/add_cors8")
def i10():
    if request.method == 'GET':
        try:
            sw = Tovar.query.all()
            print(sw[0].opis)
            print(sw[0].photo)
            admin = Tovar.query.filter_by(opis=sw[0].opis).first()
            admin2 = Tovar.query.filter_by(photo=sw[0].photo).first()
            admin.opis = sw[0].opis + ", товар: страшная маска уауауа цена: 3000 руб"
            admin2.photo = sw[0].photo + ", https://i.ibb.co/JBJptGH/photo-2024-04-13-13-06-01.jpg"
            db.session.commit()
            print(9)
            with open("add_to_kors8.html", 'r', encoding='utf-8') as html_stream:
                return html_stream.read()
        except Exception as e:
            print(e)

            return 'Авторизируйтесь или проверьте наличие товара'
    else:
        print(8)
    with open("add_to_kors8.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/add_cors9")
def i11():
    if request.method == 'GET':
        try:
            sw = Tovar.query.all()
            print(sw[0].opis)
            print(sw[0].photo)
            admin = Tovar.query.filter_by(opis=sw[0].opis).first()
            admin2 = Tovar.query.filter_by(photo=sw[0].photo).first()
            admin.opis = sw[0].opis + ", товар: чтооооо это чтооо цена: 3000 руб"
            admin2.photo = sw[0].photo + ", https://i.ibb.co/cYhLN8m/199-20240424235154.png"
            db.session.commit()
            print(9)
            with open("add_to_kors9.html", 'r', encoding='utf-8') as html_stream:
                return html_stream.read()
        except Exception as e:
            print(e)

            return 'Авторизируйтесь или проверьте наличие товара'
    else:
        print(8)
    with open("add_to_kors9.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/info")
def i12():
    with open("info.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/regist", methods=('POST', 'GET'))
def i2():
    if request.method == 'POST':
        print(7)
        email = request.form['email_field']
        password = request.form['password_field']
        try:
            u = User(email=email,
                     password=password)
            db.session.add(u)
            db.session.commit()
            print(9)
            with open("regist_done.html", 'r', encoding='utf-8') as html_stream:
                return html_stream.read()
        except Exception:
            return 'При регистрации произошла ошибка'
    else:
        print(8)
        with open("regist.html", 'r', encoding='utf-8') as html_stream:
            return html_stream.read()


@app.route("/log_in", methods=('POST', 'GET'))
def i99():
    if request.method == 'POST':
        print(777777)
        email = request.form['email_field']
        password = request.form['password_field']
        print(email)
        print(password)
        try:
            s = db.session.query(User).filter(User.email == email).all()
            if password == s[0].password:
                current_user.id = s[0].id
                with open("regist_done.html", 'r', encoding='utf-8') as html_stream:
                    return html_stream.read()
            else:
                return 'При регистрации произошла ошибка'
        except Exception as e:
            print(e)
            return 'При регистрации произошла ошибка'
    else:
        print(8)
        with open("regist.html", 'r', encoding='utf-8') as html_stream:
            return html_stream.read()



@app.route("/reg_done")
def i3():
    with open("regist_done.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/workers")
def i13():
    with open("workers.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()
res_busy_2 = []
@app.route("/korza")
def i14():

    s = 0
    sw = Tovar.query.all()
    opis_for_spli = sw[0].opis
    print(opis_for_spli)
    photo_for_spli = sw[0].photo
    res_1 = opis_for_spli.split(',')
    res_2 = photo_for_spli.split(',')
    for i in res_1:
        res_cor = (i, res_2[s])
        res_busy.append(res_cor)
        s += 1
    #for j in res_busy:
        #print(j)
        #added_res = j.replace(j[1], res_2[s])
        #s += 1
        #res_busy_2.append(added_res)
    print(res_busy)

    res_3 = {"photos": res_2, "opiss": res_1}
    return render_template("korza.html", res_all=res_busy)

@app.route("/fin_buy")
def i31():
    db.session.query(Tovar).delete()
    #admin = Tovar.query.filter_by(opis=sw[0].opis).delete()
    ##admin2 = Tovar.query.filter_by(photo=sw[0].photo).delete()
    res_busy = []
    return render_template("fin_buy.html")


if __name__ == "__main__":
    app.run(port=8000, host='127.0.0.1', debug=True)
