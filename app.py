from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    data = request.get_json()
    stage = data["stage"]
    user_input = data["input"].lower()

    if stage == 1:
        if user_input == "left":
            return jsonify(message='You have reached a lake. Do you want to "swim" or "wait"?', stage=2, game_over=False)
        else:
            return jsonify(message="You have fallen into a hole! Game Over.", game_over=True)
    elif stage == 2:
        if user_input == "swim":
            return jsonify(message="You have been attacked by the trout! Game Over.", game_over=True)
        elif user_input == "wait":
            return jsonify(message='You have reached an island. Choose a door: "red", "yellow", or "green":', stage=3, game_over=False)
        else:
            return jsonify(message="Invalid choice. Game Over.", game_over=True)
    elif stage == 3:
        if user_input == "red":
            return jsonify(message="Oh no! You have entered into fire. Game Over.", game_over=True)
        elif user_input == "yellow":
            return jsonify(message="You Win!", game_over=True)
        elif user_input == "blue":
            return jsonify(message="Eaten by the beast! Game Over.", game_over=True)
        else:
            return jsonify(message="Invalid door. Game Over.", game_over=True)
    else:
        return jsonify(message="Invalid stage.", game_over=True)

if __name__ == "__main__":
    app.run(debug=True)
