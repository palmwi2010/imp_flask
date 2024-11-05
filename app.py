from flask import Flask, render_template, request
from utils import Analyzer

import math
import requests

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


def make_request(username):
    response = requests.get(f"https://api.github.com/users/{username}/repos")
    if response.status_code == 200:
        repos = response.json()
        return repos
    return []
    
def make_commit_request(commit_url):
    """Returns the latest commit"""
    commit_url = commit_url.replace("{/sha}", "")
    print(commit_url)
    response = requests.get(commit_url)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 0:
            return data[0]
    return {}

def get_result_object(data):
    result = []
    for row in data[:1]:
        repo_name = row["full_name"].split("/")[1]
        commit_data = make_commit_request(row["commits_url"])
        print(commit_data)
        new_dict = {"repo_name": repo_name, "updated_at": row["updated_at"], "hash": commit_data["sha"],
                    "author": commit_data["commit"]["author"]["name"], "message": commit_data["commit"]["message"],
                    "url": row["html_url"], }
        result.append(new_dict)
    return result


@app.route("/githubapi", methods=["GET", "POST"])
def githubapi():
    if request.method == "POST":
        username = request.form.get("ghusername")
        data = get_result_object(make_request(username))
        return render_template("ghapi.html", username=username, data=data)
    
    return render_template("ghapi.html")


def add_from_string(input: str):
    words = input.split()
    numbers = [int(words[2]), int(words[4][:-1])]
    return str(numbers[0] + numbers[1])


def minus_from_string(input: str):
    words = input.split()
    numbers = [int(words[2]), int(words[4][:-1])]
    return str(numbers[0] - numbers[1])


def find_largest_from_string(input: str):
    words = input.split()
    numbers = [int(words[8][:-1]), int(words[9][:-1]), int(words[10][:-1])]
    return str(max(numbers))


def multiply_from_string(input: str):
    words = input.split()
    numbers = [int(words[2]), int(words[5][:-1])]
    return str(numbers[0] * numbers[1])


def find_square_and_cube(input: str):
    words = input.split()[12:]
    numbers = [int(x[:-1]) for x in words]

    output = []

    for num in numbers:
        if round(num ** (1/6)) == num ** (1/6):
            output.append(str(num))
    
    return ', '.join(output)

def isprime(num):
    for i in range(2,math.floor(math.sqrt(num))):
        if round(num/i) == num/i:
            return False
    return True


def find_primes(input: str):
    words = input.split()[7:]
    numbers = [int(x[:-1]) for x in words]

    output = []
    for num in numbers:
        if isprime(num):
            output.append(str(num))
    
    return ', '.join(output)


def power_of(input: str):
    input = input.split()
    words = [input[2], input[-1][:-1]]
    numbers = [int(x) for x in words]
    return str(numbers[0] ** numbers[1])


def process_query(input):
    if input == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    if "your name" in input:
        return "Will"
    if "the largest" in input:
        return find_largest_from_string(input)
    if " plus " in input:
        return add_from_string(input)
    if " multiplied " in input:
        return multiply_from_string(input)
    if " square " in input:
        return find_square_and_cube(input)
    if " minus " in input:
        return minus_from_string(input)
    if "prime" in input:
        return find_primes(input)
    if "power" in input:
        return power_of(input)
    return "Unknown"


@app.route("/query", methods=["GET"])
def query():
    return process_query(request.args.get('q'))
