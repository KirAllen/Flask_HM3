from flask import Flask, flash
from models import db, User
from flask import Flask, render_template, redirect, url_for, request
from forms import RegistrationForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = b'f3e171cfa5c1f4f65be19ac8e485913682afbad57d81d506fb4eb6d68bd948f3'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return redirect(url_for('main'))

@app.route('/main/')
def main():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data.capitalize()
        second_name = form.second_name.data.capitalize()
        email = form.email.data
        password = form.password.data
        user = User(username=username, email=email, second_name=second_name, password=password)
        db.session.add(user)
        db.session.commit()
        flash(f'Вы успешно зарегистрировались!')
        return redirect(url_for('main'))
    return render_template('form.html', form=form)

# @app.cli.command("init-db")
# def init_db():
#     db.create_all()
#     print('OK')
#
#
# @app.cli.command("add-kir")
# def add_user():
#     user = User(username='Kir', email='kir@Great.com', second_name='Allein', password='12346')
#     db.session.add(user)
#     db.session.commit()
#     print('Kir added to the DB')
#
#
# @app.cli.command('edit-kir')
# def edit_user():
#     user = User.query.filter_by(username='Kir').first()
#     user.email = 'first_Kir@Great.com'
#     db.session.commit()
#     print("Kir's e-mail edited!")
#
#
# @app.cli.command('del-kir')
# def del_user():
#     user = User.query.filter_by(username='Kir').first()
#     db.session.delete(user)
#     db.session.commit()
#     print("Kir was deleted from db!")


# @app.cli.command("fill-db")
# def fill_tables():
#     count = 5
#     # Добавляем пользователей
#     for user in range(1, count + 1):
#         new_user = User(username=f'user{user}',
#                         email=f'user{user}@mail.ru')
#         db.session.add(new_user)
#     db.session.commit()
#     # Добавляем статьи
#     for post in range(1, count ** 2):
#         author = User.query.filter_by(username=f'user{post % count + 1}').first()
#         new_post = Post(title=f'Post title {post}', content=f'Post content {post}', author=author)
#         db.session.add(new_post)
#     db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
