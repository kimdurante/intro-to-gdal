---
layout: default
title: Glossary
nav_order: 9
---
# Glossary

## General:



**The ArcGIS Metadata Format** – [Info](https://desktop.arcgis.com/en/arcmap/10.3/manage-data/metadata/the-arcgis-metadata-format.htm)



**Jekyll** – [Jekyll](https://jekyllrb.com/) is a static site generator used for creating a variety of online content. GitHub Pages relies on Jekyll behind the scenes. The site you're looking at right now was created using Jekyll.

**Markdown** – [Markdown](https://en.wikipedia.org/wiki/Markdown) is a super-simple [markup language](https://en.wikipedia.org/wiki/Markup_language). Markdown is popular for creating documentation and readme files. When used in tandem with Jekyll templates, it can be used to generate static web pages. This page was created in Markdown.

**Ruby** – [Ruby](https://www.ruby-lang.org/en/) is an open-source programming language, and is used as a framework for Jekyll.  

<!-- **Terminal** – -->



## Git Commands:
Use these on your local terminal. Note that these are just a few of the most common basic commands. See [Git documentation](https://git-scm.com/docs).

**Init (command)** - `git init`. Use init to initiate a new repository within a directory (folder) on your computer.

**Add (command)** – `git add myfile.txt`. Add is the first step in adding a new file or a modified file into a Git repository. The Add command adds new/modified files to a staging area.

**Commit (command)** – `git commit -m "I made some edits"`. Commit is the second step in adding a new/modified file to the Git repository. Commit moves new/modified files from the staging area to the repository. You must include a message following the `-m` flag. Be sure to make your commit message descriptive in case you need it later.

**Clone (command)** – `git clone https://github.com/user/repo-name` Make a copy of a remote repository from GitHub.com on your local computer. This is one method of creating a connection between a local and remote repository that you can use to push or pull changes.

**Pull (command)** – `git pull origin master` Use this to pull updates from the remote repository down to your local copy.

**Push (command)** – `git push origin master` Use this to push updates made to your local repository to the remote repository.

**Status (command)** – `git status` Check if you have any un-added/committed changes to your local repository.

**Log (command)** – `git log` See past commit history including comments and hash ID of each commit. `q` to exit Log interface. Use `git log --oneline` for a condensed log.

**Revert (command)** – `git revert [hash id]` Use this to revert to an earlier commit. Use the Log command to find previous commits' hash IDs.



[Octocat]: https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Font_Awesome_5_brands_github.svg/232px-Font_Awesome_5_brands_github.svg.png "GitHub logo."
