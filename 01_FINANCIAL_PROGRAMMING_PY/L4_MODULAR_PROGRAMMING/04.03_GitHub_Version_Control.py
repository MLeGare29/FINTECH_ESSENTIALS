# NOTES ON HOW TO EXECUTE VERSION CONTROL IN GIT:
# **NO CODE, ALL COMMENTS**

# STEP 1: CONFIG GIT
# Since you have configured Git, confirm using:
# git config --list
# This will break down the git configuration on your computer

# STEP 2: CREATE A GITHUB REPO
# Create a new Repo in GitHub
# In the CODE tab, clone the HTTPS by copying the link to your clipboard
# In Bash, cd to the desired folder you want clone the Repo to
# Input the following command:
# git clone <paste link here> **paste using CTRL+SHIFT+V**
# cd into the Repo and you will see the cloned folder
# You'll also notice that the only file within is the README.md

# STEP 3: CHANGE AND ADD FILES
# In Notepad, open README.md
# **To access in Notepad, open in VSCode and follow path to file location and open into Notepad there**
# Add some text to the file in Notepad and save the changes
# In Bash, make sure you're working directory is the repo you created - cd if necessary
# To find out if Git has been keeping track of your changes, type:
# git status
# A prompt saying that changes not staged for commit, yet also modified: READ.md, should pop up
# To tell Git to keep track of that file type the following in Bash:
# git add README.md
# Then input the following again:
# git status
# Changes to your files should now be committed and track

# STEP 4: TRACK NEW FILES
# Create a new text file by using the following command
# touch version-test.txt
# Once the new text file is created, input the following:
# ls - to list the files within the Repo - then:
# git status
# You'll see the new file is 'Untracked', input the following command:
# git add version-test.txt
# Then:
# git status
# You'll see that both the README.md and version-test.txt have both had their changes committed

# STEP 5: COMMIT YOUR LOCAL CHANGES
# Now that you've staged the files you want Git to track
# You need to commit them
# REMEMBER - a commit is a save point that you can track and revert back to
# So if something goes wrong in the future, you can double back to a point where the code worked
# And figure out what happened to cause any errors
# Both you and your collaborators will be able to observe your commits
# You'll need to add a short message about what you're changing
# To include a commit message, type the following:
# git commit -m "<Insert your message here>"
# After that, input the status test:
# git status
# NOTICE THE LINE:
# "Your branch is ahead of 'origin/main' by 1 commit."

# STEP 6: PUSH YOUR LOCAL CHANGES TO THE REMOTE REPO
# You've gotten git to track the changes you've made
# However, these only exist on your local computer
# To back up your work and share with collaborators, you need to push your local changes to your remote repo
# Input the following:
# git push
