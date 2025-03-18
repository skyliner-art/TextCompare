from flask import Flask, render_template, request
import webbrowser
import compareText
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取用户输入的两个文本
        standard_text = request.form['standard_text']
        test_text = request.form['test_text']
        print(standard_text)
        print(test_text)
        # 比对文本并返回结果
        diff_result = compareText.compare_texts(standard_text, test_text)
        return render_template('index.html', diff_result=diff_result, standard_text=standard_text, test_text=test_text)
    return render_template('index.html', diff_result=None)
if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5555')
    app.run(host='127.0.0.1', port=5555, debug=True)