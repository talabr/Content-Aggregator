from jinja2 import Template
from flask import Flask, render_template
import datetime
from utils import get_news_from_nbc, get_news_from_fox, get_news_from_washington_post

app = Flask(__name__)


@app.template_filter()
def datetimefilter(value, date_format='%Y/%m/%d %H:%M'):
    """Convert a datetime to a different format."""
    return value.strftime(date_format)


app.jinja_env.filters['datetimefilter'] = datetimefilter
# current_time = datetime.datetime.now()


@app.route("/")
def template_test():
    return render_template('template.html', nbc_list=get_news_from_nbc(), fox_list=get_news_from_fox(),
                           wash_list=get_news_from_washington_post())


@app.route("/home")
def home():
    return render_template(
        'template.html', nbc_list=get_news_from_nbc(), fox_list=get_news_from_fox(),
        wash_list=get_news_from_washington_post())


@app.route("/about")
def about():
    return render_template(
        'template.html', nbc_list=get_news_from_nbc(), fox_list=get_news_from_fox(),
        wash_list=get_news_from_washington_post())


@app.route("/contact")
def contact():
    return render_template(
        'template.html', nbc_list=get_news_from_nbc(), fox_list=get_news_from_fox(),
        wash_list=get_news_from_washington_post(), title="Contact Us")


if __name__ == '__main__':
    app.run(debug=True)
