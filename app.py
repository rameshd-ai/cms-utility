from flask import Flask, render_template

app = Flask(__name__)

# Define a route
@app.route("/")
def show_projects():
    return render_template("index.html")


@app.route("/project/<project_id>")
def show_tasks(project_id):
    return render_template("project-tasks.html", project_id = project_id)

@app.route("/add/project", methods=['POST'])
def add_project():
    return "Project added successfully"




# Run the app
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=3000)
