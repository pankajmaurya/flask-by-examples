from flask import Flask, render_template

app = Flask(__name__)

@app.context_processor
def inject_global_data():
    # This function will be called for every template rendering
    # and the returned values will be added to the template context.

    # Injecting a constant value
    site_name = 'My Awesome Website'

    # Injecting a function
    def get_year():
        import datetime
        return datetime.datetime.now().year

    # Returning a dictionary of values
    return {
        'site_name': site_name,
        'current_year': get_year
    }

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
