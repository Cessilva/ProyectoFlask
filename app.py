from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/procesar', methods=['POST'])
def procesar():
    #guardamos en una variable lo ingresado por el usuario
    textingres = request.form.get("descripcion")
    
    #codigo para trabajar la variable 

	
	#ponemos el resultado en una nueva web.    
    return render_template("resultado.html", resultado=textingres)

if __name__=="__main__":
    app.run(debug=True)