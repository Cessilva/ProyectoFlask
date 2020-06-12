from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/procesar', methods=['POST'])
def procesar():
    descripcion = request.form.get("descripcion")
    return render_template("resultado.html", descripcion=descripcion)

if __name__=="__main__":
    app.run(debug=True)