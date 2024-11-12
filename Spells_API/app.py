from flask import Flask, jsonify, request, make_response
import json

app = Flask(__name__)

def load_spells():
    with open('spells.json', 'r', encoding='utf-8') as file:
        return json.load(file)

spells = load_spells()

@app.route('/spells', methods=['GET'])
def get_spells():
    response = make_response(json.dumps(spells, ensure_ascii=False, indent=4), 200)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

@app.route('/spells/<int:id>', methods=['GET'])
def get_spell(id):
    spell = next((spell for spell in spells if spell['id'] == id), None)
    if spell:
        response = make_response(json.dumps(spell, ensure_ascii=False, indent=4), 200)
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    return jsonify({"error": "Spell not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
