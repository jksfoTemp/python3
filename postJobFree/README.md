
Note that I could modify this to wget the URL ...

Just start with the file input ...

Boilerplate python3 template code with error handling that calls a sub that prints
the current time. It should have  reference to numpy, datetime, pdf and string libraries.

Demonstrates file access ...

TODO: Add and print arguments to the main function to accept the job posting file path as input.
TODO: Add parsing code to extract the job description from the job posting.

ext install mikoz.black-py

# Sample HTML snippet
html = '''
<h3 class="itemTitle"><a href="https://www.postjobfree.com/job/v1hyua/data-entry-clerk-san-francisco-ca" rel="nofollow">Data Entry Clerk</a></h3>
<div class="normalText">
	<span class="colorCompany">Sciolex Corporation / Advantech Global</span>
	&nbsp;–&nbsp;
	<span class="colorLocation">San Francisco, CA</span>
	<div class="colorSalary">22.5USD per hour</div>
	<div><span class="jdSnippet">... Responsibilities The <b>Data</b> <b>Entry</b> Clerk is a permanent,
	full-time position supporting the overall mission of the U.S. Citizenship and Immigration Services
	(USCIS) by facilitating the operations of a local Field Office. As a <b>Data</b> <b>Entry</b> Clerk,
	your ...</span> - <span class="colorDate">Feb 17</span></div>
</div>
'''

import sys
print ('argument list', sys.argv)
name = sys.argv[1]
print ("Hello {}. How are you?".format(name))

(.venv) jku@jkMain:~/git/jksfoTemp$ python3 ./python3/postJobFreeParse/pjfParse.py "/home/jku/git/jksfoTemp/python3/postJobFreeParse" "pjfParse.py" False

jksfoTemp$

python3 ./python3/postJobFreeParse/pjfParse.py "/home/jku/git/jksfoTemp/python3/postJobFreeParse" "pjfParse.py" False
python3 ./python3/postJobFreeParse/pjfParse.py "A" "B" False






