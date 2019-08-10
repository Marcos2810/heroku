from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aboutme") #para que acepte esta opcion
@app.route("/about_me") #para que acepte esta opcion
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        return render_template("contact.html", user=user_name)
    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")

        print(contact_name)
        print(contact_email)
        print(contact_message)

        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", contact_name)

        return response


if __name__ == '__main__':
    app.run()