from flask import Flask, redirect, render_template, url_for
from forms import conversionForm, measurementForm, temperatureForm
from conversion import convert, convert_temp

app = Flask(__name__)
app.config['SECRET_KEY'] = "pogi si owen"

@app.route("/", methods=['GET', 'POST'])
def index():
    form = conversionForm()
    if form.validate_on_submit():
        if form.convert_temperature.data:
            return redirect(url_for('temperature'))
        elif form.convert_measurement.data:
            return redirect(url_for('metric'))
    return render_template('index.html', form=form)

@app.route("/metric", methods=['GET', 'POST'])
def metric():
    form = measurementForm()
    result = None
    if form.validate_on_submit():
        value = form.value.data
        metric_from = form.metric_from.data
        metric_to = form.metric_to.data

        try:
            result = convert(value, metric_from, metric_to)
        except ValueError as e:
            result = f"Error: {e}"
    return render_template('metric.html', form=form, result=result)

@app.route("/temperature", methods=['GET', 'POST'])
def temperature():
    form = temperatureForm()
    result = None
    if form.validate_on_submit():
        value = form.value.data
        temp_from = form.temp_from.data
        temp_to = form.temp_to.data

        try:
            result = convert_temp(value, temp_from, temp_to)
        except ValueError as e:
            result = f"Error: {e}"
    return render_template('temperature.html', form=form, result=result)