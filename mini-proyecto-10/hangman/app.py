from flask import Flask, render_template, request, jsonify
from hangman_logic import HangmanGame

app = Flask(__name__)

game = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_game', methods=['POST'])
def new_game():
    global game
    game = HangmanGame()
    return jsonify(game.get_game_state())

@app.route('/guess', methods=['POST'])
def guess():
    if game is None:
        return jsonify({'error': 'No game in progress'}), 400

    letter = request.json.get('letter', '').lower()
    if len(letter) != 1 or not letter.isalpha():
        return jsonify({'error': 'Invalid input'}), 400

    game.guess(letter)
    return jsonify(game.get_game_state())

if __name__ == '__main__':
    app.run(debug=True)