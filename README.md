## About

Code Engine - an efficient platform for you to search famous coding problems given a query topic. This is designed to help
problem solvers to enhance their learning experience and help them find relevant problems at their doorstep.

This search engine is designed with the hep of TF-IDF Algorithm

Key Tech Stacks used in this project are :
1. Python (for scraping problems' data, TF-IDF Implementation)
2. Flask (Framework for our back-end server)
3. HTML/CSS for Front-end Development

## Files
1. LC Data contains the dataset of our project on which we have applied our algorithm. It consists data of about 1000+
   problems of LeetCode, which can be scaled even further for optimisation.

2. Templates folder contains the html/css code which serves the front-end view of our site.
3. app.py is the root, it contains the flask app which serves the back-end server.

## Installation

1. Clone the repository: git clone https://github.com/banerjee-sarnab/AZ-Hackathon.git
2. Change to the project directory: cd repo-directory
3. Install dependencies: pip install flask flask-wtf gunicorn

## Usage
1. Run the application: python app.py
2. Open a web browser and navigate to `http://localhost:5000` to access the application.
