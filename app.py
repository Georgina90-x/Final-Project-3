import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# creates a list on the homepage of all workout records in db
@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.tasks.find())
    return render_template("tasks.html", tasks=tasks)

# search function that retrieves data records using keywords searched 
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("tasks.html", tasks=tasks)


# register function, checks against existing users in db and creates a new user when submitted
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            # put confirm password code here "confirm_password": check_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Congrats You're Registered!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# login function checks for username and password matching to db
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check is username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # check hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

# 
def confirm_password():
    if confirm_password != password:
        flash("Passwords do not match!")

# pulls logged in users username from db to display on profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the sessions user's username from the db
    username = mongo.db.users.find_one({"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))

# logout function for user
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You've been logged out")
    session.pop("user")
    return redirect(url_for("login"))

# adds a workout when the user fills in the form and submits
@app.route("/add_workout", methods=["GET", "POST"])
def add_workout():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        workout = {
            "category_name": request.form.getlist("category_name"),
            "workout_name": request.form.get("workout_name"),
            "workout_description": request.form.get("workout_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"],
        }
        mongo.db.tasks.insert_one(workout)
        flash("Workout Successfully Added")
        return redirect(url_for("get_tasks"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_workout.html", categories=categories)

# edits a workout when the user makes changes and submits
@app.route("/edit_workout/<workout_id>", methods=["GET", "POST"])
def edit_workout(workout_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "category_name": request.form.getlist("category_name"),
            "workout_name": request.form.get("workout_name"),
            "workout_description": request.form.get("workout_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"],
        }
        mongo.db.tasks.update_one({"_id": ObjectId(workout_id)}, {"$set": submit})
        flash("Workout Successfully Updated")

    workout = mongo.db.tasks.find_one({"_id": ObjectId(workout_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_workout.html", workout=workout, categories=categories)

# 'done' button function for completing workout
@app.route("/complete_workout/<workout_id>")
def complete_workout(workout_id):
    mongo.db.tasks.delete_one({"_id": ObjectId(workout_id)})
    flash("Workout Successfully Completed")
    return redirect(url_for("get_tasks"))

# appears for admin user to display all categories listed
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)

# allows an admin user to add a category to the database
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {"category_name": request.form.get("category_name")}
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")

# allows admin to edit a category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {"category_name": request.form.get("category_name")}
        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, {"$set": submit})
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)

# allows admin to delete a category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=False)

