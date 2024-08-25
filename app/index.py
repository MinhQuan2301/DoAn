from flask import Flask, render_template, redirect
from app import app
from flask_admin import Admin


@app.route("/")
def home():
    return redirect('/admin')