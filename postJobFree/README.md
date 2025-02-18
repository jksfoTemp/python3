
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

Given python and the use of beautiful soup, I am identifying this class element by it's name, how do I extract the hyperlink?
<h3 class="itemTitle"><a href="https://www.postjobfree.com/job/v1hyua/data-entry-clerk-san-francisco-ca" rel="nofollow">Data Entry Clerk</a></h3>

import sys
print ('argument list', sys.argv)
name = sys.argv[1]
print ("Hello {}. How are you?".format(name))

(.venv) jku@jkMain:~/git/jksfoTemp$ python3 ./python3/postJobFreeParse/pjfParse.py "/home/jku/git/jksfoTemp/python3/postJobFreeParse" "pjfParse.py" False

jksfoTemp$

python3 ./python3/postJobFreeParse/pjfParse.py "/home/jku/git/jksfoTemp/python3/postJobFreeParse" "pjfParse.py" False
python3 ./python3/postJobFreeParse/pjfParse.py "A" "B" False
python3 /home/jku/git/jksfoTemp/python3/postJobFree/pjfParse.py  "A" "B" False


> git push -u origin dev
To https://github.com/jksfoTemp/python3.git
 ! [rejected]        dev -> dev (non-fast-forward)
error: failed to push some refs to 'https://github.com/jksfoTemp/python3.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.



just fucking commit


> git push -u origin dev
To https://github.com/jksfoTemp/python3.git
 ! [rejected]        dev -> dev (non-fast-forward)
error: failed to push some refs to 'https://github.com/jksfoTemp/python3.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.





git status head detached trying to push to dev branch


Git Detached Head Error
When you encounter a "HEAD detached" state in Git and want to push changes to a development branch, you can follow these steps:

Create a New Branch: First, create a new branch from the current commit to attach your changes to a branch. This can be done with the command:
  git checkout -b new-feature
This command creates a new branch named new-feature and switches to it, effectively reattaching your HEAD to a branch.
Push Changes: Once you are on the new branch, you can push your changes to the remote repository:
  git push origin new-feature
This will push the branch to your remote repository, so the branch will be tracked and stored remotely.
Merge into Development Branch: If you need to merge these changes into an existing development branch, switch to the development branch and merge the new branch into it:
  git checkout dev
  git merge new-feature
After merging, you can push the changes to the remote development branch:
  git push origin dev
Alternative Method: If you want to directly push your changes to the remote development branch without creating a new branch, you can use:
  git push origin HEAD:dev
This command pushes the current commit to the dev branch on the remote repository.
By following these steps, you can resolve the detached HEAD state and successfully push your changes to the development branch.



