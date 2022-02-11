from flask import Flask

app = Flask (__name__)

@app.route("/")
def index():
    return "Hello World!"
@app.route('/dojo')
def success():
    return "Dojo!"
@app.route('/say/<name>')
def hello(name):
    return "Hi " + name + "!"

@app.route('/repeat/<int:count>/<something>')
def show_user_profile(something, count):
     return something * int(count)

# @app.route('/repeat/<int:num>/<string:word>')
# def repeat_word(num, word):
#     output = ''

#     for i in range(0,num):
#         output += f"<p>{word}</p>"

#     return output



if __name__ =="__main__":
    app.run(debug=True)
    


    
    
