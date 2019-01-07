Steps to run Apriori and Bruteforce algorithm the project:

1. copy the entire project folder "recommend_system" on desktop.
2. Open the above project folder in Atom code editor.
   Link to download Atom text editor.
   https://atom.io/
3. Open terminal in Atom.
4. Navigate to project folder in terminal.
5. Install python and Flask in project folder using below command.
   a. install python
   b. pip install Flask
6. run below command to run the project.
   python app.py
7. Copy the http address given in terminal and paste it to browser and hit enter.
   http address would look something like this
   Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   Copy http://127.0.0.1:5000/
8. Enter minimum support and confidence and hit Run algorithm button.
   Idle values to enter
   minimum support - 0.01 - 0.05
   minimum confidence - 0.01 - 0.05

   You can enter other than this values also but rules generated will depend on the values you enter.
   If it does not display any support or rule, than it means no items qualify minimum support or confidence given.

Important files and folders description:

Folders:
1. Dataset
   Contains the .csv file which contains dataset used to implement this project.
2. Templates
   Contains the index.html file which contains GUI of the project.

Files:
1. app.py
   Contains integration of apriori.py with Flask framework. It also handles GET and POST request send from the browser.
2. apriori.py
   Contains the apriori algorithm implementation.
3. bruteforce.py   
   Contains the bruteforce algorithm implementation.
4. index.html
   It contains HTML code to interactively take user input and display item, support, confidence and association rules.
