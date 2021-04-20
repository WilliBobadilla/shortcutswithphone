from pynput.keyboard import Key, Controller
from flask import Flask, request, render_template, json, jsonify
from flask_cors import CORS,  cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
keyboard = Controller()


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def hello():
    if request.method == 'POST':
        data = request.form['key']
        print('value sent: ', data)
        if data == 'copy':
            keyboard.press(Key.ctrl)
            keyboard.press('c')
            keyboard.release('c')
            keyboard.release(Key.ctrl)
            message = "Copiado"
        elif data == 'paste':
            keyboard.press(Key.ctrl)
            keyboard.press('v')
            keyboard.release('v')
            keyboard.release(Key.ctrl)
            message = "Pegado"
        elif data == 'save':
            keyboard.press(Key.ctrl)
            keyboard.press('s')
            keyboard.release('s')
            keyboard.release(Key.ctrl)
            message = "Guardado"
        elif data == 'enter':
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            message = "Enter"
        elif data == 'space':
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            message = "Espacio"

        return jsonify(message=message)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, )  # host='0.0.0.0', port=80)
