# Birthday Greeter
<p>This name reflects the main purpose of the program, which is to greet colleagues with upcoming birthdays during the week.</p>
<h2>Why we have 2 files? </h2>
<p>File main2.py has better code style(I recommend you to use it), but main.py is working too</p>
<h1>What this project can do ?</h1>
<p>Here is an implementation of the program to display a list of colleagues who need to be greeted with their upcoming birthdays during the week.</p>
<h1>Details about the program ?</h1>
<p>You have a list of dictionaries called "users," where each dictionary must have the keys "name" and "birthday." This structure represents a model of a user list with their names and birth dates. Where "name" is a string with the user's name, and "birthday" is a datetime.date object containing the birth date.

For example:
{"name": "Bob", "birthday": datetime.datetime(1995, 9, 30)},

The project has a function called "get_birthdays_per_week" that takes the "users" list as input and returns a dictionary of users who need to be greeted by their birthdays on the upcoming week. What does this mean? You get days from Monday till Friday and the names of your friends

For example: Monday: Bob

If the birthday is on weekend, program accurately considers weekends and shift them to Monday.</p>
<h1>How to use?</h1>
<ol>
<li>First of all you should clone the repository, you can use:</li>
<p><b>git clone https://github.com/OlgaTsuban/Birthday-Greeter.git</b></p>
<li><p>You can write this for MacOS <b>python3 main.py </p> </b>
<p>You can write this for Windows <b>python main.py </p> </li>
</ol>
