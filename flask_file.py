from jinja2 import Template
from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.template_filter()
def datetimefilter(value, date_format='%Y/%m/%d %H:%M'):
    """Convert a datetime to a different format."""
    return value.strftime(date_format)


app.jinja_env.filters['datetimefilter'] = datetimefilter
current_time = datetime.datetime.now()


@app.route("/")
def template_test():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0, 1, 2, 3, 4, 5], current_time=current_time)


@app.route("/home")
def home():
    return render_template(
        'template.html', my_string="Wheeeee!",
        my_list=[0, 1, 2, 3, 4, 5], title="Home", current_time=current_time)


@app.route("/about")
def about():
    return render_template(
        'template.html', my_string="Wheeeee!",
        my_list=[0, 1, 2, 3, 4, 5], title="About", current_time=current_time)


@app.route("/contact")
def contact():
    return render_template(
        'template.html', my_string="Wheeeee!",
        my_list=[0, 1, 2, 3, 4, 5], title="Contact Us", current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True)
