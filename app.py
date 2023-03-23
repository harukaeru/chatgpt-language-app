from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

vocab = {
    'apple': 'りんご',
    'dog': 'いぬ',
    'cat': 'ねこ',
    'house': 'いえ',
    'car': 'くるま',
}

@app.route('/')
def home():
    word = random.choice(list(vocab.keys()))
    return render_template('index.html', word=word)

@app.route('/quiz', methods=['POST'])
def quiz():
    word = request.form['word']
    user_input = request.form['answer']
    meaning = vocab[word]

    if user_input == meaning:
        result = "正解です！"
    else:
        result = f"残念！正解は {meaning} です。"

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

