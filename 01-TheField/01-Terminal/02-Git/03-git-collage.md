# Goals

- Markdown skills improvements
- Git skills improvements
- Learning a workflow with contributors on GitHub

## Instructions

Create an [Exquisite Corpse](https://en.wikipedia.org/wiki/Exquisite_corpse) with GitHub.

### Step 1: Initialization

1. Create a GitHub repository named "Exquisite-corpse-Your-Name".
2. `clone` your repo on your machine.
3. Open the repo ("Exquisite-corpse-Your-Name") on your machine with the command `cd`.
4. Create a `README.md` file in the repo (in command line or by using your file explorer).
5. Using Markdown, give a title to your story.
6. Use `add` to add your changes.
7. Make a `commit` with a clear message.
8. Make a `push` and check if everything went well by looking on your online repo.

### Step 2: Contributions

#### Let people contribute to your repo

Using the GitHub interface:

1. Invite some of your colleagues as contributors to your repo
2. Let them work (see below) and do a Pull Request
3. Approve their Pull Requests and merge their branches on the `main` branch
4. Remove their branches
5. Make a _"main"_ `tag` named _"version-1"_

#### Contribute to the repo of someone else

1. Go to a repository where you have been invited
2. `clone` the repo on your local machine
3. Do `git branch -a` to display the list of branches on the server
4. Do `git branch <your_name>` to create your own branch
5. `checkout` the `<your_name>` branch
6. Add 3 lines of text to the current story in the `README.md` file following the previous user
7. Add the file to the changes with `git add`
8. Make a `commit` with a clear message
9. `push` the changes on the `<your_name>` branch
10. Go to the GitHub interface and create a Pull Request from your branch to the `main` branch
11. Wait for your colleague to merge your Pull Request
12. `pull` the `main` branch locally
13. `checkout` the `main` branch and check if your changes have been applied
14. Remove the `<your_name>` branch locally

## Resources

- [Git Basics](https://rogerdudler.github.io/git-guide/index.fr.html)
- [Git Cheat Sheet](https://rogerdudler.github.io/git-guide/files/git_cheat_sheet.pdf)
- [nano](https://help.ubuntu.com/community/Nano?_ga=2.171475168.110155971.1536746343-1962823923.1536746343)
  ![Git workflow](http://blog.launchdarkly.com/wp-content/uploads/2016/07/Slide2.jpg)
