from init import init_app

app=init_app()


@app.route('/')
def hello world():
    return "hello world"

if __name__ ==  '__main__':
    app.run(debug=True)
