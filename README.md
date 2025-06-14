# ProjectEdunet
# Movie Genre Classifier

This project is a small application that can learn from a set of movie plots and their genres.  
It can then use this knowledge to predict the genre of a new movie based on its plot.  

## Overview

The main idea is to take a CSV file with movie plots and genres, learn from it, and then check how well it performs.  
The code first prepares the data, then it trains a classifier on the movie plots.  
After training, it tests the classifier on some new plots to see how accurate it is at guessing the genre.  
This lets you know if the classifier is able to learn from the data and make good predictions.

## How to Use

1. Make sure Python 3 is installed on your system.

2. Install required Python libraries:  
   
   pip install pandas scikit-learn joblib

3. The CSV file used in this project is movie_data.csv.
Make sure movie_data.csv is placed in the same folder as the Python files.


4. Run the classifier script:

python MovieGenreClassifier.py


5. Check the output and accuracy shown in the console.


**##Dataset Format**

The movie_data.csv file should have at least two columns:

PLOT: Text description of the movie plot

GENRE: The genre of the movie (like Action, Comedy, Drama)


**##Future Work**

Improve the model or add features using the existing code.

Use the trained classifier(Multinomial Naive Bayes) to predict new movie genres easily.

Install Streamlit if it is not already installed.

Run the app by executing streamlit run App.py in the terminal.

The app will open a webpage in the browser at http://localhost:8501.

Enter or paste a movie plot description into the text box on the page.

Click the Predict Genre button.

The app processes the input using the trained model.

The predicted genre is displayed immediately below the input box.

This provides an easy way to test new movie plots without using the command line each time
