## Internal /editorial contribution process
The RDM-guidelines repository has an editorial group consisting of members of SciLifeLab's Data Centre and NBIS data management teams.

When adding content, keep in mind that the goal is not to duplicate what is in the [RDMkit](https://rdmkit.elixir-europe.org/) but rather add the Swedish flavour, and link to RDMkit for more information.

The steps below outlines the mutually agreed steps in order to update the RDM-guidelines repository:

1. Create a [New issue](https://github.com/ScilifelabDataCentre/RDM-guidelines/issues) describing the needed update. If appropriate, add a label with the level of priority.
1. The person(s) that decides to resolve the issue sets themselves as assignee, so that the others in the editorial group know that the update is ongoing.
1. The assignee creates a branch: under **Development** in the menu on the right, click on the link `Create a branch`.
1. If the issue is a missing page:
    1. Create the new page either in folder [content/topics](./content/topics) (most likely) or [content/data-life-cycle](./content/data-life-cycle).
    1. Add metadata header to the top of the page by copying the header in [TEMPLATE_topic.md](./TEMPLATE_topic.md).
    1. Remember to add link to the new page in the main index page ([content/_index.md](./content/_index.md)) (if this is a new data-life-cycle page, update also [content/data-life-cycle/_index.md](./content/data-life-cycle/_index.md)). -->
    1. If this is a new topic page, also [shortcode for display topics](./layouts/shortcodes/display-topics.html) needs to be updated with the new topic. <!-- not sure if more info is needed? -->
    1. If appropriate, add links from other pages to this new page.
    1. If there is a resource, remove the commented out characters in the Resources section, change '--add topic/title--' to the topic title, and add the resource to the [resources.json](./data/resources.json) page as outlined [below](#about-resources).
1. When it is time for a **Pull request**, if the branch wasn't created as described above, add a link to the issue in the describing text (type a `#` and suggestions of possible links will appear). It is up to everyone in the editorial group to check if there are pull requests waiting to be approved. All PRs should be reviewed by another member, if the update isn't minor (i.e. unlikely that typo:s or wrong links have been included).
2. When **merging** a Pull request, delete the branch being merged. Note that the linked issue will be automatically closed if using closing words. 

### About resources
A resource is any **external** link with information that is of added value for a page (topic or data life cycle page). Note that links to internal pages should only appear in the text. 

A resource *can* be explicitly linked to in the text, but most importantly is that it is listed under the Resources heading at the end of a page (see below on how to make that happen).

There are currently three types/targets of resources:

* Tool - any type of tool to assist in a data management task
* Training - courses or course catalogue links
* Guidance - any form of digital information material that is not explicitly training material (i.e. self paced training material is of type Training, not Guidance)

#### How to add a resource

1. Copy the item text (everything within the curly brackets, including the brackets themselves) in [TEMPLATE_resource.json](TEMPLATE_resource.json), and put it at the end of the [resources.json](./data/resources.json) file. 
1. Remember to add a comma after the last closing curly bracket of the previous item.
1. Remove all rows for which information does not exist, and update the values of the other rows as appropriate. Note that the last row of an item (before the closing curly bracket) should not end with a comma.

Note: If the resource itself already exist, and a page should have this resource appearing on its page, update the item in the [resources.json](./data/resources.json) file by adding the title of the page in the topic or phase row (e.g. `topic: ["Metadata","README files],` or `phase: ["Collect", "Share"],`).

#### TEMPLATE_resource.json
Currently the template has 14 fields, some of them are mandatory and some are optional meaning they can be excluded/deleted.

Mandatory fields:
* **title** - the full title as found in the external link provided
* **short_title** - one-liner, shortened title, to fit the row of a card
* **target** - either "training", "tool", or "guidance"
* **type** - either "Web page", "Video", "Material", or "Tool" (currently only used to identify videos, so that they get an icon)
* **search_tags** - add at least full title, and any suitable keywords
* **phase** - one or more of "Plan", "Collect", "Process", "Analyse", "Preserve", "Share", "Reuse" (can be excluded if topic is filled)
* **topic** - (can be excluded if phase is filled)
* **url** - full link to the external resource
* **description** - describe the resource using text from the source
* **provider** - list all providers and enclose with ", e.g. "KI, KTH, SU"

Optional fields:
* **level** -  one or more of "Basic", "Intermediate", or "Advanced" (currently not used since most resources are 'Basic')
* **DOI** - e.g. "10.17044/scilifelab.23987985", if available
* **DOIurl** - e.g. "https://doi.org/10.17044/scilifelab.23987985.v1", if available
* **licence** - e.g. "GPL 3.0+", if available

### How to work in GitHub

The following steps are required in order to contribute to RDM guidelines via GitHub:
* [Step 1: GitHub account](#step-1-github-account)
* [Step 2: Access the code](#step-2-access-the-code)
* [Step 3a: Edit the files online](#step-3a-edit-the-files-online)
* [Step 3b: Edit the files locally](#step-3b-edit-the-files-locally)
* [Step 4: Make a pull request](#step-4-make-a-pull-request)

#### Step 1: Github account

The code is hosted on [GitHub](http://github.com/), so you'll need an account. 2-factor authentication is required, to decrease the risk of unauthorised access, and all commits needs to be signed.

##### Setting up 2-factor authentication (2FA)

* The easiest way is to follow the instructions from Github: [Configuring two-factor authentication - GitHub Docs](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)

* TOTP, Github app, and security key are recommended

* Make sure that you keep the backup codes and/or set up multiple ways to login in case you e.g. lose your phone

##### Setting up git commit signing
Git commits can be signed using e.g. GPG or SSH keys. All software required for SSH keys is installed by default on most computers, while GPG may require some software to be installed.

* **SSH**

    The steps outlined below is adapted from [About commit signature verification - GitHub Docs](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification#ssh-commit-signature-verification)

    1. Create a ssh key (unless you want to reuse an existing one) (for additional information see [Generating a new SSH key and adding it to the ssh-agent - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)):
        ```
        ssh-keygen -t ed25519 -f ~/.ssh/id_github_sign
        ```
    1. Add your public key to the clipboard (i.e. put it in the computer's memory, so that it can be pasted in the next step by pressing the keys cmd-v (macOS) or ctrl-v (Windows) on the keyboard):
        
        *On macOS*
        ```
        pbcopy < ~/.ssh/id_github_sign.pub
        ```

        *On Windows*
        ```
        clip < ~/.ssh/id_github_sign.pub
        ```
        **Note:** If you in PowerShell get an error message about `The '<' operator is reserved for future use`, write instead `cat ~/.ssh/id_github_sign.pub | clip` 
    1. Add the generated key to your Github account (**change key type to be: Signing**) by following the instructions given in [Adding a new SSH key to your GitHub account - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account)

    1. Next, tell git to use your ssh key:
        ```
        git config --global gpg.format ssh
        git config --global user.signingkey ~/.ssh/id_github_sign.pub
        ```

        **Note:** If you mind writing your password when doing commits, you can change the second command above to:
        
        ```
        git config --global user.signingkey "key::$(cat ~/.ssh/id_github_sign.pub)"
        ```
        and load your ssh key into ssh-agent (needs to be repeated each time you reboot your computer):
        ```
        ssh-add ~/.ssh/id_github_sign
        ```
    
* **GPG**

    Follow the instructions at [Signing git commits using GPG (Ubuntu/Mac)](https://gist.github.com/ankurk91/c4f0e23d76ef868b139f3c28bde057fc)

    *Recommended settings*
    * Perform commit signing automatically (you can use git commit instead of git commit -S):
    ```
    git config --global commit.gpgsign true
    git config --global tag.gpgsign true
    ```

    * Allow verification (or even display) of signatures with an ssh key (not required):
    ```
    git config --global gpg.ssh.allowedSignersFile ~/.ssh/allowed_signers
    echo  "$(git config --global user.email) $(cat ~/.ssh/id_github_sign.pub)" > ~/.
    ```

#### Step 2: Access the code

Next, visit the code repository: [https://github.com/ScilifelabDataCentre/RDM-guidelines](https://github.com/ScilifelabDataCentre/RDM-guidelines)

In the top right, you'll see a button that says _"Fork"_. Click this, then select your username.
This makes a copy of the repository under your personal account that you can edit.

#### Step 3a: Edit the files (online)

> This is best if you only want to make one or two minor tweaks.
> If you want to make more substantial edits over a longer time frame, we recommend editing locally (_Step 3b_).

The easiest way to edit the website files is on the GitHub website.

On the web page of your _forked_ copy of the repository, look in the `content/` directory. Go to the markdown file that you want to edit, then click the Pencil icon :pencil2: in the top right.

This opens a web-based editor where you can add and edit content. When you're finished, scroll to the bottom and fill in / submit the _"Commit changes"_ form.

You're nearly done - you can now skip to _Step 4_.

#### Step 3b: Edit the files (locally)

##### Git setup

If you prefer, you can edit the website files on your computer in your favourite text editor.
Just fork the repository to your machine:

```bash
git clone git@github.com:[YOUR-USERNAME]/RDM-guidelines
cd RDM-guidelines
```

To make it easier to pull in changes made by others, you can add the main repository as a remote:

```bash
git remote add upstream https://github.com/ScilifelabDataCentre/RDM-guidelines.git
```

Then you can fetch changes at any time from this remote:

```bash
git pull upstream main
```

When you have finished editing, commit and push to your fork:

```bash
git add .
git commit -m "My changes"
git push
```

##### Testing locally

To view your changes as they will appear in the final website, you need to install Hugo.
You can find instructions on the Hugo website: [getting-started/installing/](https://gohugo.io/getting-started/installing/)

If you're using Mac OSX, it's recommended to use [Homebrew](https://brew.sh/) -
if homebrew is already set up, installing Hugo is just a case of:

```bash
brew install hugo
```

For Windows users (additional instructions can be found [here](https://gohugo.io/getting-started/installing/#windows)):

1. Open Windows Explorer.

2. Create a new folder: C:\Hugo, assuming you want Hugo on your C drive, although this can go anywhere.

3. Create a subfolder in the Hugo folder: `C:\Hugo\bin`

4. Go to the [Hugo Releases](https://github.com/gohugoio/hugo/releases) page. The latest release is announced on top. Scroll to the bottom of the release announcement to see the downloads. They’re all ZIP files. Find the Windows files near the bottom (they’re in alphabetical order, so Windows is last) – download either the 32-bit or 64-bit file depending on whether you have 32-bit or 64-bit Windows. (If you don’t know, see [here](https://esupport.trendmicro.com/en-us/home/pages/technical-support/1038680.aspx).)

5. Move the ZIP file into your `C:\Hugo\bin` folder.

6. Double-click on the ZIP file and extract its contents. Be sure to extract the contents into the same `C:\Hugo\bin` folder – Windows will do this by default unless you tell it to extract somewhere else.

7. In PowerShell or your preferred CLI, add the hugo.exe executable to your PATH by navigating to `C:\Hugo\bin` (or the location of your hugo.exe file) and use the command `set PATH=%PATH%;C:\Hugo\bin`. If the hugo command does not work after a reboot, you may have to run the command prompt as administrator.

Once Hugo is installed, use PowerShell or your preferred CLI and navigate to the repository root directory (i.e. where RDM-guidelines resides, e.g. `cd C:\Users\firstname.lastname\GitHub\RDM-guidelines`), and run the command:

```console
$ hugo serve
```

Use the URL printed at the bottom of the message (`http://localhost:1313/`) to view the site.
Every time you save a file, the page will automatically refresh in the browser.

#### Step 4: Make a pull request

Once you're finished with your edits and they are committed and pushed to your forked repository, it's time to open a pull request.

You can find full documentation on the [GitHub help website](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests), however in short:

- Visit the main repository: [https://github.com/ScilifelabDataCentre/RDM-guidelines](https://github.com/ScilifelabDataCentre/RDM-guidelines)
- Click the button that reads _"New Pull Request"_.
- Click the text link near the top that says _"compare across forks"_.
- In the right-hand _"head repository"_ drop down, select your username / fork.
- If you're happy with the list of commits shown, and the diff in the _"Files Changed"_ tab, fill in a title and description and click _"Create pull request"_.

Once created, a member of the website team will review your changes.
Once approved, they will be merged and deployed.
