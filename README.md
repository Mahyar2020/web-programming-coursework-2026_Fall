# Web Programming Coursework - Fall 2026

Student coursework repository for *Web Programming: From the Platform to
Production*, taught by Dr. Mahyar Teymournezhad.

This repository is a student-safe starting template. It contains laboratory
starters and the commands required to serve and verify them. Completed solutions,
answer keys, instructor notes, and book-production files are intentionally absent.

## Before you begin

Students should not develop directly in this template repository. Use the
instructor's official link and select **Use this template**, followed by **Create
a new repository**. Create a private repository using the naming convention
announced in the learning management system, and grant the instructor the
required access.

The repository page in the browser is the remote copy. After creating your own
remote repository, select **Code**, select **HTTPS**, and copy its address. In a
terminal opened in the parent folder where you keep coursework, run `git clone`
followed by that copied address.

## First local verification

Enter the newly cloned project folder. Before running an npm command, prove that
the terminal is in the repository root.

Windows Command Prompt:

```text
cd
dir package.json
node --version
npm --version
npm test
```

PowerShell:

```text
Get-Location
Get-Item package.json
node --version
npm --version
npm test
```

macOS or Linux:

```text
pwd
ls -l package.json
node --version
npm --version
npm test
```

The Node.js version must begin with `v24.`. The final command should report
`Coursework setup verification passed.`

## Repository map

```text
web-programming-coursework-2026_Fall/
  labs/
    week-01/
      index.html
    week-02/
      index.html
    week-03/
      index.html
      styles.css
  scripts/
    check-setup.mjs
    serve-static.mjs
  package.json
```

Each `labs/week-NN` folder is a starter, not a completed answer. Read the matching
book session and laboratory instructions before changing it.

## View a laboratory in the browser

Run only one server command at a time in the server terminal:

```text
npm run serve:week01
npm run serve:week02
npm run serve:week03
```

After the selected command prints `Open http://localhost:8000/`, leave that
terminal running. Put `http://localhost:8000/` in the browser address bar and
press Enter. Edit the corresponding file, save it, and reload the browser.

Stop the server with `Ctrl+C` before starting a different week's server. A second
terminal can remain available for `git status`, `npm test`, and other commands.

## Save work in Git and send it to GitHub

Saving, committing, and pushing are separate actions. At the end of each small,
working change, run:

```text
git status
git diff
git add path-to-the-file-you-changed
git diff --staged
git commit -m "Describe the completed change"
git push
```

Replace the example path and commit message. Do not use `git add .` without first
reviewing which files will be included. After pushing, refresh the personal
repository page on GitHub and confirm that the latest commit is visible.

## Security and academic integrity

- Never commit passwords, access tokens, private keys, recovery codes, `.env`
  files, or private student information.
- Keep the student repository private unless the instructor explicitly changes
  the policy.
- Do not copy another student's implementation or publish assessment material.
- Ask the instructor before adding packages or replacing the supplied project
  structure.

## Getting help

When reporting a problem, include the operating system, the exact command, the
terminal's current directory, and the complete error text. Remove passwords,
tokens, recovery codes, and unrelated personal information before sharing a
screenshot or log.
