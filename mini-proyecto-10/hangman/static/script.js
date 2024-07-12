document.addEventListener('DOMContentLoaded', () => {
    const wordDisplay = document.getElementById('word-display');
    const guessedLetters = document.getElementById('guessed-letters');
    const remainingAttempts = document.getElementById('remaining-attempts');
    const message = document.getElementById('message');
    const alphabet = document.getElementById('alphabet');
    const newGameBtn = document.getElementById('new-game-btn');

    function updateGameState(gameState) {
        wordDisplay.textContent = gameState.word_state;
        guessedLetters.textContent = `Letras adivinadas: ${gameState.guessed_letters.join(', ')}`;
        remainingAttempts.textContent = `Intentos restantes: ${gameState.remaining_attempts}`;

        if (gameState.game_over) {
            if (gameState.has_won) {
                message.textContent = '¡Felicidades! Has ganado.';
            } else {
                message.textContent = '¡Oh no! Has perdido.';
            }
            disableAlphabetButtons();
        } else {
            message.textContent = '';
        }
    }

    function createAlphabetButtons() {
        const letters = 'abcdefghijklmnñopqrstuvwxyz';
        alphabet.innerHTML = '';
        for (let letter of letters) {
            const button = document.createElement('button');
            button.textContent = letter.toUpperCase();
            button.addEventListener('click', () => guess(letter));
            alphabet.appendChild(button);
        }
    }

    function disableAlphabetButtons() {
        const buttons = alphabet.getElementsByTagName('button');
        for (let button of buttons) {
            button.disabled = true;
        }
    }

    function guess(letter) {
        fetch('/guess', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ letter: letter }),
        })
        .then(response => response.json())
        .then(gameState => {
            updateGameState(gameState);
        });
    }

    function newGame() {
        fetch('/new_game', { method: 'POST' })
        .then(response => response.json())
        .then(gameState => {
            updateGameState(gameState);
            createAlphabetButtons();
        });
    }

    newGameBtn.addEventListener('click', newGame);
    newGame();
});