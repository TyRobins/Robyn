import flask
import rolls

app = flask.Flask(__name__)

#Only implementing saving throws to start as a test
def run_roll(roll_name):
    if roll_name == "Strength Saving Throw":
        return rolls.strength_throw
    elif roll_name == "Dexterity Saving Throw":
        return rolls.dexterity_throw
    elif roll_name == "Constitution Saving Throw":
        return rolls.constitution_throw
    elif roll_name == "Saving Throw":
        return rolls.intelligence_throw
    elif roll_name == "Wisdom Saving Throw":
        return rolls.wisdom_throw
    elif roll_name == "Charisma Saving Throw":
        return rolls.charisma_throw
    else:
        return "I'm sorry, I can't help with that yet."

@app.route('/get-roll/<roll_name>')
def get_roll(roll_name):
    result = run_roll(roll_name)
    return flask.jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)