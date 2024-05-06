# Baruch AIS-A-THON Spring 2024

## Topic:

### Software Development

A backend API that takes user information and stores it in a database. Necessary information includes:
- **Id**: Unique identifier for each data entry.
- **Pregnancies**: Number of times pregnant.
- **Glucose**: Plasma glucose concentration over 2 hours in an oral glucose tolerance test.
- **BloodPressure**: Diastolic blood pressure (mm Hg).
- **SkinThickness**: Triceps skinfold thickness (mm).
- **Insulin**: 2-Hour serum insulin (mu U/ml).
- **BMI**: Body mass index (weight in kg / height in m^2).
- **DiabetesPedigreeFunction**: Diabetes pedigree function, a genetic score of diabetes.
- **Age**: Age in years.

## Tech Stack

**Backend**: Flask, SQLite

## Accomplishments 

- Figuring out how to authorize users using JWT tokens. It required using another external package, which allows you to integrate JWT authorization with Flask.

## Challenges Faced

- One challenge that was a particular struggle at first was setting up the HTTP routes for the API. A lot of the implementation for each request required many checks to make sure that either existing data was valid, or if creating new data matched with the database model. Each request was different in how it should be handled, so figuring out how to implement each one required time and thought.
- Additionally, figuring out what authorization system to use took some time.

## What We Learned

- We learned how to build a RESTful API using Python as our backend using a library called Flask, and also how to connect a SQLite database to our application, and also ensure that only those who know the proper credentials can access our API endpoints using JWT authorization.