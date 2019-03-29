import temperature_CO2_plotter as code_file
import time
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__, template_folder="templates")

@app.route("/co2")
def co2():

    int_input = request.args.get("startYear")
    #We assume that input is an integer
    if int_input is not None:
        range_min = request.args.get("startYear")
        range_max = request.args.get("endYear")
        y_axis_min = request.args.get("y_axis_min")
        y_axis_max = request.args.get("y_axis_max")
        code_file.read_CO2(int(range_min), int(range_max), int(y_axis_min), int(y_axis_max))

    return render_template("co2.html", hello="co2", image="result_CO2.jpg")

@app.route("/temp")
def temperature():

    int_input = request.args.get("startYear")
    #We assume that input is an integer
    if int_input is not None:
        month = request.args.get("month")
        range_min = request.args.get("startYear")
        range_max = request.args.get("endYear")
        y_axis_min = request.args.get("y_axis_min")
        y_axis_max = request.args.get("y_axis_max")
        code_file.read_temperature(month, int(range_min), int(range_max), int(y_axis_min), int(y_axis_max))

    return render_template("temp.html", hello="temp", image="result_temperature.jpg")

@app.route("/bycountry")
def bycountry():

    int_input = request.args.get("year")
    #We assume that input is an integer
    if int_input is not None:
        year = request.args.get("year")
        upper_threshold = request.args.get("upper_threshold")
        lower_threshold = request.args.get("lower_threshold")
        code_file.read_co2bycountry(year, int(upper_threshold), int(lower_threshold))

    return render_template("bycountry.html", hello="bycountry", image="result_CO2bycountry.jpg")

@app.after_request
def remove_cache(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response

@app.route("/")
def index():
    return redirect("/temp")

if __name__ == "__main__":
    app.run()
