# SciLifeLab Research Data Management Guidelines
This is the repository for SciLifelab Research Data Management (RDM) guidelines, a central resource to provide information about data management.

## Background and motivation

* There is an information and competence gap regarding data management in the Swedish life science community

* SciLifeLab and NBIS had many sources of information regarding research data management 

* There is a need to make a unified set of guidelines that can then be used as a resource and reference for the life science community  in Sweden.

* Information can be unified and kept up do date by the team and the community if there is only one set of guidelines, and not multiple sources, as well as clear and easy ways of contributing.

## Project goals
* Create the authoritative set of Research data management (RDM) best practice guidelines for life science research in Sweden, hosted at data.scilifelab.se (to ensure that unified information is conveyed to all recipients), including information about human data

* A single point of entry web portal/resource for national use and to connect to other efforts, eg. Training, RDMkit

## How to contribute

For internal / editorial contribution process, please see [internal contribution page](https://github.com/ScilifelabDataCentre/RDM-guidelines/blob/main/internal-contribution.md).

### Step 1: Github account

The code is hosted on [GitHub](http://github.com/), so you'll need an account. 2-factor authentication is required, to decrease the risk of unauthorised access, and all commits needs to be signed.

#### Setting up 2-factor authentication (2FA)

* The easiest way is to follow the instructions from Github: [Configuring two-factor authentication - GitHub Docs](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)

* TOTP, Github app, and security key are recommended

* Make sure that you keep the backup codes and/or set up multiple ways to login in case you e.g. lose your phone

#### Setting up git commit signing
Git commits can be signed using e.g. GPG or SSH keys. All software required for SSH keys is installed by default on most computers, while GPG may require some software to be installed.

**SSH**

[About commit signature verification - GitHub Docs](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification#ssh-commit-signature-verification)

1. Create a ssh key (unless you want to reuse an existing one) [Generating a new SSH key and adding it to the ssh-agent - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent):
    ```
    ssh-keygen -t ed25519 -f ~/.ssh/id_github_sign
    ```
1. Add your public key to the clipboard (so it can be pasted using cmd-v):
    
    *On macOS*
    ```
    pbcopy < ~/.ssh/id_github_sign.pub
    ```

    *On Windows*
    ```
    clip < ~/.ssh/id_github_sign.pub
    ```
    **Note:** If you in PowerShell get an error message about `The '<' operator is reserved for future use`, write instead `cat ~/.ssh/id_github_sign.pub | clip` 
1. Add the generated key to your Github account (**change key type to be: Signing**): [Adding a new SSH key to your GitHub account - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account)

1. Tell git to use your ssh key:
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
    
**GPG**

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

### Step 2: Access the code

Next, visit the code repository: [https://github.com/ScilifelabDataCentre/RDM-guidelines](https://github.com/ScilifelabDataCentre/RDM-guidelines)

In the top right, you'll see a button that says _"Fork"_. Click this, then select your username.
This makes a copy of the repository under your personal account that you can edit.

### Step 3a: Edit the files (online)

> This is best if you only want to make one or two minor tweaks.
> If you want to make more substantial edits over a longer time frame, we recommend editing locally (_Step 3b_).

The easiest way to edit the website files is on the GitHub website.

On the web page of your _forked_ copy of the repository, look in the `content/` directory. Go to the markdown file that you want to edit, then click the Pencil icon :pencil2: in the top right.

This opens a web-based editor where you can add and edit content. When you're finished, scroll to the bottom and fill in / submit the _"Commit changes"_ form.

You're nearly done - you can now skip to _Step 4_.

### Step 3b: Edit the files (locally)

#### Git setup

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

#### Testing locally

To view your changes as they will appear in the final website, you need to install Hugo.
You can find instructions on the Hugo website: [getting-started/installing/](https://gohugo.io/getting-started/installing/)

If you're using Mac OSX, it's recommended to use [Homebrew](https://brew.sh/) -
if homebrew is already set up, installing Hugo is just a case of:

```bash
brew install hugo
```

For Windows users (additional instructions can be found [here](https://gohugo.io/getting-started/installing/#windows)):

1. Open Windows Explorer.

2. Create a new folder: C:\Hugo, assuming you want Hugo on your C drive, although this can go anywhere

3. Create a subfolder in the Hugo folder: `C:\Hugo\bin`

4. Go to the [Hugo Releases](https://github.com/gohugoio/hugo/releases) page. The latest release is announced on top. Scroll to the bottom of the release announcement to see the downloads. They’re all ZIP files. Find the Windows files near the bottom (they’re in alphabetical order, so Windows is last) – download either the 32-bit or 64-bit file depending on whether you have 32-bit or 64-bit Windows. (If you don’t know, see [here](https://esupport.trendmicro.com/en-us/home/pages/technical-support/1038680.aspx).)

5. Move the ZIP file into your `C:\Hugo\bin` folder.

6. Double-click on the ZIP file and extract its contents. Be sure to extract the contents into the same `C:\Hugo\bin` folder – Windows will do this by default unless you tell it to extract somewhere else.

7. In PowerShell or your preferred CLI, add the hugo.exe executable to your PATH by navigating to `C:\Hugo\bin` (or the location of your hugo.exe file) and use the command `set PATH=%PATH%;C:\Hugo\bin`. If the hugo command does not work after a reboot, you may have to run the command prompt as administrator.

Once Hugo is installed, simply run the following command in the repository root (RDM-guidelines) directory:

```console
$ hugo serve
```

Use the URL printed at the bottom of the message (`http://localhost:1313/`) to view the site.
Every time you save a file, the page will automatically refresh in the browser.

### Step 4: Make a pull request

Once you're finished with your edits and they are committed and pushed to your forked repository, it's time to open a pull request.

You can find full documentation on the [GitHub help website](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests), however in short:

- Visit the main repository: [https://github.com/ScilifelabDataCentre/RDM-guidelines](https://github.com/ScilifelabDataCentre/RDM-guidelines)
- Click the button that reads _"New Pull Request"_
- Click the text link near the top that says _"compare across forks"_
- In the right-hand _"head repository"_ drop down, select your username / fork.
- If you're happy with the list of commits shown, and the diff in the _"Files Changed"_ tab, fill in a title and description and click _"Create pull request"_

Once created, a member of the website team will review your changes.
Once approved, they will be merged and deployed.

## How to get help

If in doubt, you can ask for help by emailing [data-management@scilifelab.se](mailto:data-management@scilifelab.se).

## License

The content documents are dedicated to the public domain under a CC-0 license. Software are made available under an MIT license. More information about our license can be found on our [license](LICENSE) page.

## Credits

The website was built by [SciLifeLab Data Centre](https://www.scilifelab.se/data/) and [NBIS](https://nbis.se/).
