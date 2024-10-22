from flask import Blueprint, render_template, request
from modules import create_df, model
bp = Blueprint("pages", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/predict", methods=['GET', 'POST']) # type: ignore
def submit():
    if request.method == "POST":

        data = {}
        
        Income = request.form['income']
        Rating = int(request.form['rating'])
        Cards = int(request.form['cards'])
        Age = int(request.form['age'])
        Education = int(request.form['education'])
        Gender_Male = 1 if request.form['gender'] == "Male" else 0
        Student_Yes = 1 if request.form['student'] == "Yes" else 0
        Married_Yes = 1 if request.form['married'] == 1 else 0
        Ethnicity_Caucasian = 1 if request.form['ethnicity'] == "A" else 0
        Ethnicity_Asian = 1 if request.form['ethnicity'] == "B" else 0
        Balance = int(request.form['balance'])
    
        
       
        df = create_df(Income=Income, Rating=Rating, Cards=Cards, Age=Age,
                        Education=Education, Gender_Male=Gender_Male, Student_Yes=Student_Yes,
                       Married_Yes=Married_Yes, Ethnicity_Caucasian=Ethnicity_Caucasian, 
                       Ethnicity_Asian=Ethnicity_Asian, Balance=Balance)

        prediction = f"{float(model.predict(df)[0]):.2f}"


        return render_template("index.html", prediction_text=prediction)
    else:
        return render_template("index.html", error_message="An error encoutered during prediction. Please try again or contact the developer")

@bp.route("/about")
def about():
    return render_template("about.html")