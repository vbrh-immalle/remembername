from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    if username == None:
        return '''
            <p id='notification'>Geef je naam: <input type="text" id="name_textfield"></p>
            <button id="send_button">Send!</button>
            <script>
            document.getElementById('send_button').addEventListener('click', function () {
                username = document.getElementById("name_textfield").value;
                console.log(username);
                document.cookie = "username=" + escape(username) + ";path=/;expires=Fri, 31 Dec 9999 23:59:59 GMT"
                document.getElementById('notification').innerHTML = "Dank u! Uw naam is bewaard in een cookie. De pagina kan nu gerefresht worden."
            });
            </script>
            '''
    else:
        return f'<p>Welkom terug <b>{username}</b></p><p><em>Verwijder manueel de cookies als de naam niet klopt ofzo ;-)!</em></p>'

app.run(host='127.0.0.2', port='8080', debug=True)
