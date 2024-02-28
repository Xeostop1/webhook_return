from flask import Flask, request, render_template_string
import json
import os

app = Flask(__name__)

RESULTS_FILE = 'results.json'
RETURN_RESULTS_FILE = 'return_results.json'

@app.route('/', methods=['GET', 'POST'])
def respond():
    print("Request arrived from IP: ", request.headers.get('X-Real-IP'))
    if request.method == 'POST':
        data = request.json
        print("웹훅 실행")
        print(data)
        # 결과를 JSON 형식의 문자열로 변환하고 파일에 저장
        with open(RESULTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return 'OK', 200
    elif os.path.exists(RESULTS_FILE):
        # 결과 파일이 있는 경우, 파일을 불러와서 결과를 반환
        with open(RESULTS_FILE, 'r', encoding='utf-8') as f:
            results = json.load(f)
        # JSON 데이터 포맷팅
        formatted_results = json.dumps(results, indent=4, ensure_ascii=False)
        # HTML 템플릿 렌더링
        return render_template_string('<pre>{{ results }}</pre>', results=formatted_results), 200
    else:
        return 'Hello, this is GET request!', 200

@app.route('/return', methods=['POST'])
def handle_return():
    print("Return request arrived from IP: ", request.headers.get('X-Real-IP'))
    data = request.json
    print("반품 웹훅 실행")
    print(data)
    # 결과를 JSON 형식의 문자열로 변환하고 파일에 저장
    with open(RETURN_RESULTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return 'OK', 200

if __name__ == '__main__':
    app.run()