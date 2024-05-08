<h1 align="center">Title : Medical Insurance Cost Prediction</h1>

<div align= "center">
    <h3>Business Problem: To predict the approximate cost of medical insurance based on availabe information of patients</h3><br>
    <img src= >
</div>

#### 1) Create environement
```
conda activate -p .conda -y
```
#### 2) Create setup.py--> copy the code from my git hub repository
#### 3) Pip install requirements.txt file
```
pip install -r requirements.txt

```
#### 4) Created notebook
* Loaded data set insurance.csv
* Preprocess it and done EDA
* **EDA Observations**: (To have deeper understanding go .ipynb file)
  * Person between 18 to 22 years are more taking insurance.
  * Count of taking insurance which is of less costs/charges are more.
  * South-East region has more smokers with respect to all regions.
  * South-East region has higher Insurance charges as compared to all other regions.
  * Charges for females as per bmi is mostly below 20K and on other hand charges for male are higher as per bmi.
  * From plot is clear that male and females which are smoker their charges are much higher as compared to non-smokers.
  * We have observed that the charges are increasing with age.
* Applied various models on data and calculated metrics such as **R2 Score and RMSE" for various models.
* Model used : Linear Regresion, Ridge Regression, SVR and Decision Tree Regressor.
* Based on R2 Score and RMSE **Decision Tree Regressor** was perfoming best.
* Tuned its hyperparameters.
* Deployed it using streamlit.

#### 5) Created app.py file which was use in deploment.

#### 6) Run the app.py as-->streamlit run app.py
```
streamlit run app.py
```
#### 7) Streamlit app will open
#### 8) Insert data to be predicted insurance cost for


