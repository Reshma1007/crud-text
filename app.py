from init import init_app

app=init_app()
db=flask_sqlalchemy.SQLAlchemy


if __name__ ==  '__main__':
    app.run(debug=True)
