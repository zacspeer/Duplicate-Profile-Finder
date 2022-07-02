# Simple Duplicate Profile Finder app using Django framework

<h3><b> Description:</b></h3> This is a simple app which takes in the User profile and finds the duplicate/similar profiles. This is built using Django and uses fuzzywuzzy library for string matching(Learn more about it here: https://pypi.org/project/fuzzywuzzy/).
<hr>
Hi, to run this app please follow the instructions below.

* First clone this repository and extract it.
* Navigate your IDE to the extracted folder and open a terminal in the root of the Django project(where the manage.py is located)
* In the terminal run this command 'pip install -r requirements.txt'. This will install all the dependencies for this project.
* In the terminal you need to run two commands, 'python manage.py makemigrations' and 'python manage.py migrate'. This will initialize the app for use
* In the terminal, run this command. 'python manage.py shell'. This will open up Python's interactive shell. If there are no issues you should see ">>>" on the left side (please refer the image below)
![image](https://user-images.githubusercontent.com/42238198/177015958-1804988c-dd97-4e60-8c78-062eda20568c.png)

* Next, you need to import two libraries, for that type in 'from Profiles.models import Profile' and 'from Profiles.main import Dupe' (please refer the image below)
![image](https://user-images.githubusercontent.com/42238198/177016031-953a1eac-54d9-4d4c-8d8a-bbf9be5e466a.png)

* Now, to run the app create two Profile instances with required data. Note: Please enclose your data with single-quotes.
![image](https://user-images.githubusercontent.com/42238198/177016123-85210e52-fb18-4caa-9fb3-f6c545657d64.png)

* Pass the instances and the Fields to be calculated into the find_duplicates() method as arguments.
![image](https://user-images.githubusercontent.com/42238198/177016196-d72e49be-a178-449f-a587-53b2686a1b78.png)

* You should be able to see an output similar to this.
![image](https://user-images.githubusercontent.com/42238198/177016294-2cd5d561-58ce-4faf-9034-b45546c07bae.png)

<hr>
If you have any issues please feel free to reach out to me at manu190200@gmail.com
