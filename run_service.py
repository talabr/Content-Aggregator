from flask import Flask, render_template
from utils import make_list_of_nbc_top_news, make_list_of_fox_top_news, make_list_of_washington_post_top_news

app = Flask(__name__)


@app.template_filter()
def datetimefilter(value, date_format='%Y/%m/%d %H:%M'):
    """Convert a datetime to a different format."""
    return value.strftime(date_format)


@app.route("/")
def template_test():
    return render_template('home.html')


@app.route("/coronavirus")
def coronavirus():
    return render_template(
        'coronavirus.html', nbc_list=make_list_of_nbc_top_news(), fox_list=make_list_of_fox_top_news(),
        washington_list=make_list_of_washington_post_top_news())


if __name__ == '__main__':
    app.run(debug=True)
