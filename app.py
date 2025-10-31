from flask import Flask 
app = Flask("myapp") 
 
@app.route("/") 
def home(): 
    return "? TEST SUCCESS" 
 
if __name__ == "__main__": 
    app.run(port=5000) 
