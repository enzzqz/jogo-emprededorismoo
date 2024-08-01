from flask import Flask, request, jsonify, send_from_directory
import random
import os

app = Flask(__name__)

# Diretório onde o arquivo index.html está localizado
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Rotas para os jogos
@app.route('/play_rps', methods=['POST'])
def play_rps():
    data = request.json
    user_choice = data.get('choice')
    choices = ["pedra", "papel", "tesoura"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "empate"
    elif (user_choice == "pedra" and computer_choice == "tesoura") or \
         (user_choice == "papel" and computer_choice == "pedra") or \
         (user_choice == "tesoura" and computer_choice == "papel"):
        result = "você ganhou"
    else:
        result = "você perdeu"

    return jsonify({"user_choice": user_choice, "computer_choice": computer_choice, "result": result})

@app.route('/guess_number', methods=['POST'])
def guess_number():
    data = request.json
    guess = data.get('guess')
    # Lógica do jogo Adivinhe o Número aqui
    return jsonify({"message": "Resultado do Adivinhe o Número"})

@app.route('/start_quiz', methods=['GET'])
def start_quiz():
    # Lógica para começar o quiz
    return jsonify({"question": "Pergunta do Quiz", "answers": {"A": "Resposta A", "B": "Resposta B", "C": "Resposta C", "D": "Resposta D"}, "correct_answer": "A"})

@app.route('/answer_quiz', methods=['POST'])
def answer_quiz():
    data = request.json
    answer = data.get('answer')
    # Lógica para verificar a resposta do quiz
    return jsonify({"message": "Resultado da resposta do Quiz"})

@app.route('/start_hangman', methods=['GET'])
def start_hangman():
    # Lógica para começar o Forca
    return jsonify({"word": "PALAVRA", "word_display": "_ _ _ _ _", "attempts": 6, "used_letters": []})

@app.route('/guess_hangman', methods=['POST'])
def guess_hangman():
    data = request.json
    letter = data.get('letter')
    # Lógica para verificar a letra no Forca
    return jsonify({"word_display": "_ A _ _ _", "attempts": 5, "used_letters": ["A"], "message": "Tentativa correta", "game_over": False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
