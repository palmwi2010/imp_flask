from flask import Flask, render_template, request
from utils import Analyzer
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/analyse", methods=["POST"])
def analyse():
    input_text = request.form.get("textcontent")
    input_checkboxes = request.form.getlist("properties")

    num_sentences, num_words, num_characters = None, None, None

    if 'words' in input_checkboxes:
        num_words = Analyzer.count_words(input_text)

    if 'characters' in input_checkboxes:
        num_characters = Analyzer.count_characters(input_text)

    if 'sentences' in input_checkboxes:
        num_sentences = Analyzer.count_sentences(input_text)

    return render_template("results.html", text=input_text, n_words=num_words,
                           n_chars=num_characters, n_sentences=num_sentences)


def process_query(input):
    if input == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    return "Unknown"


@app.route("/query", methods=["GET"])
def query():
    return process_query(request.args.get('q'))
