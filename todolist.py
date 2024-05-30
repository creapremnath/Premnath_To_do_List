from flask import Flask, render_template,redirect
from dotenv import load_dotenv
import os

load_dotenv()
port=os.getenv("portnumber")

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("Home.html")

if __name__=="__main__":
    app.run(port=port)