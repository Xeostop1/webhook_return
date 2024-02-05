from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
    data = request.json
    # 이제 data에는 웹훅을 통해 받은 JSON 데이터가 딕셔너리 형태로 저장되어 있습니다.
    # 필요한 처리를 여기서 수행하면 됩니다.
    print("웹훅 실행")
    print(data)
    return 'OK', 200

if __name__ == '__main__':
    app.run()

print("실행전")