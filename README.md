# basePractices
This is learning and improving session 
1. Creating a Repository
# Create a new repository on GitHub
# Initialize a local repository
git init

# Add a remote repository
git remote add origin https://github.com/username/repo.git

# Add files to the staging area
git add .

# Commit the files
git commit -m "Initial commit"

# Push the commit to the remote repository
git push -u origin master

2. Cloning a Repository

# Clone a repository from GitHub
git clone https://github.com/username/repo.git

3. Checking the Status
bash
# Check the status of the repository
git status

4. Adding and Committing Changes

# Add changes to the staging area
git add file_name

# Commit the changes
git commit -m "Commit message"
5. Pushing Changes

# Push changes to the remote repository
git push origin branch_name

6. Pulling Changes

# Pull changes from the remote repository
git pull origin branch_name


7. Creating a Branch

# Create a new branch
git branch branch_name

# Switch to the new branch
git checkout branch_name

# OR create and switch to the branch in one command
git checkout -b branch_name


8. Merging Branches

# Switch to the branch you want to merge into (typically master or main)
git checkout master

# Merge the branch into the current branch
git merge branch_name


9. Fixing Merge Conflicts
When you encounter merge conflicts, Git will mark the conflicts in the files. You need to manually resolve these conflicts.


# After resolving conflicts, add the resolved files
git add file_name

# Commit the merge
git commit -m "Resolved merge conflict"


10. Checking the Commit History

# View the commit history
git log
11. Viewing Differences

# View the changes between the working directory and the staging area
git diff

# View the changes between the staging area and the last commit
git diff --cached

# View the changes between two commits
git diff commit1 commit2


12. Stashing Changes

# Stash changes
git stash

# Apply stashed changes
git stash apply
13. Deleting a Branch

# Delete a local branch
git branch -d branch_name

# Force delete a local branch
git branch -D branch_name

# Delete a remote branch
git push origin --delete branch_name
