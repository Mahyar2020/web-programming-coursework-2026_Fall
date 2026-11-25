# Orientation - Prepare Your Web-Programming Workstation

**Essential question:** How can a student prove that a computer is ready to edit,
run, inspect, test, and preserve web programs before the first programming lab?

This orientation assumes no previous experience with developer tools. Follow it
from beginning to end on the computer you will bring to laboratories. Do not stop
when an installer says *Finished*. An installation is complete only when you can
run the tool, observe its version, serve the course page, inspect the request, run
the tests, and record a Git commit.

## Orientation map

Table 0.1 defines the preparation task and the evidence that demonstrates
readiness.

**Table 0.1 - Workstation-preparation scope and evidence**

| Item | Plan |
|---|---|
| Audience | Students with no assumed web-development-tool experience |
| Time | Approximately 90-150 minutes, depending on download speed and operating system |
| Required result | One working local course repository opened as a folder in the editor |
| Primary programming language | Modern JavaScript, first in the browser and later in Node.js on the server |
| Runtime | Node.js 26 Long-Term Support (LTS), including npm |
| Core evidence | Tool versions, passing course tests, a local HTTP response, a Network-panel observation, and a Git commit |
| Help threshold | Ask for laboratory support after recording the exact command, complete error text, operating system, and attempted remedy |

## Learning outcomes

After completing this orientation, you should be able to:

1. distinguish the editor, terminal, runtime, package manager, server, browser,
   developer tools, test runner, and version-control system;
2. install and verify a supported browser, Visual Studio Code, Git, Node.js 26
   LTS, and npm on Windows, macOS, or Linux;
3. identify the current directory, move safely through folders, and run a command
   without typing the displayed prompt symbol;
4. obtain and open the course repository without losing its folder structure;
5. run the course verification suite and local development server;
6. inspect a localhost request in browser developer tools;
7. configure Git identity, create a small meaningful commit, and push it to the
   approved remote repository; and
8. distinguish the JavaScript language from the browser and Node.js environments
   that execute it; and
9. collect useful diagnostic evidence without exposing passwords, access tokens,
   or private student information.

## 1. Understand the workstation before installing tools

A web-programming workstation is a cooperating set of programs, not one large
application. The **code editor** changes text files. The **terminal** provides a
text interface for running commands. **Node.js** executes JavaScript outside the
browser. **npm**, installed with Node.js, runs the scripts defined by a project.
A local **web server** listens for HTTP requests. The **browser** requests and
renders resources, while its **developer tools** expose evidence. Automated tests
check stated properties. **Git** records selected versions of the project.

Figure 0.2 shows the working loop used throughout this book. Read it clockwise.
Editing changes project files; a terminal command runs a Node.js-backed local
server; the browser requests `localhost`; developer tools support inspection;
tests check the project; and a deliberate Git commit preserves a meaningful
checkpoint. The arrows describe a working process, not a claim that the tools are
one program.

<!-- media:development-workstation-evidence-loop -->

### 1.1 Required equipment and access

Table 0.2 separates requirements from useful additions. The course does not
require an expensive gaming computer, a paid editor, a public server, or a second
monitor.

**Table 0.2 - Equipment and access for the course**

| Item | Required baseline | Recommended when available |
|---|---|---|
| Computer | A supported 64-bit Windows, macOS, or Linux laptop or desktop with a physical keyboard | A laptop that can be brought to class and connected to an external display |
| Memory | 8 GB RAM for the foundation laboratories | 16 GB or more for later databases, browser tooling, and concurrent services |
| Storage | At least 10 GB free after operating-system updates | 20 GB free so repositories, package caches, database files, and screenshots do not compete for space |
| Processor | A currently supported x64 or ARM64 processor | Four or more logical cores for smoother concurrent tools |
| Display | A readable display capable of browser zoom | A second display is useful but never required |
| Network | Reliable Internet access for installation, documentation, and repository synchronization | A wired connection for large downloads when wireless service is unstable |
| Input and audio | Physical keyboard; built-in pointer is sufficient | Headphones for media and screen-reader exercises; an external mouse is optional |
| Permissions | Permission to install approved software, or access to an administrator who can assist | A standard daily account plus separate elevation when installation requires it |
| Accounts | University account and access to the course repository or learning system | A Git-hosting account protected with multi-factor authentication when remote pushes are required |

A tablet or phone is valuable for responsive testing, but it is not a replacement
for the primary workstation. The course requires a file system, terminal, local
server, developer tools, and Git. Students using a managed laboratory computer
should confirm that work persists after sign-out and should push or copy approved
work to durable storage before leaving.

### 1.2 Record the machine you are preparing

Before downloading software, record:

- operating-system name and version;
- processor architecture, normally x64 or ARM64;
- available memory and storage;
- whether the account can install applications; and
- the folder in which course work will be stored.

Use a short local path that you can find again. Examples are
`C:\Users\Ada\Documents\web-course` on Windows and
`/Users/ada/Documents/web-course` on macOS. Avoid placing the active repository
inside a folder whose synchronization software repeatedly locks generated files.
Never work directly inside an email attachment, a compressed ZIP archive, or a
browser's temporary download preview.

## 2. Prepare the operating system and file view

1. Install pending security updates and restart the computer.
2. Confirm that the date, time, and time zone are correct. Incorrect clocks can
   break certificate checks, Git timestamps, and authentication.
3. Create the course-work folder in your own user account.
4. Configure the file manager to show complete filenames and extensions. A file
   named `index.html.txt` is a text file, not an HTML document.
5. Ensure that UTF-8 text files can be created. The repository's `.editorconfig`
   later asks a compatible editor to use UTF-8, Line Feed (LF) endings, two-space
   indentation, a final newline, and no trailing whitespace.
6. Decide where installation evidence will be stored. A plain text file named
   `setup-evidence.txt` inside your personal course notes is sufficient. Do not
   record passwords, recovery codes, or access tokens.

On Windows 11, File Explorer provides **View > Show > File name extensions**. On
macOS, Finder provides **Settings > Advanced > Show all filename extensions**.
Linux file managers vary; the important evidence is that you can distinguish
`index.html` from `index.html.txt`.

## 3. Install a current web browser

Install the current stable release of Chrome, Edge, or Firefox from the browser's
official site. The first browser is the course's primary inspection environment.
A second browser engine is useful later for compatibility checks, but it is not
required for the first laboratory.

1. Download the installer from the official publisher.
2. Check that the site uses HTTPS and that the publisher name is correct.
3. Run the installer and allow the browser to update automatically.
4. Open the browser and visit `https://example.com/`.
5. Open developer tools. On Windows and Linux, use `F12` or
   `Ctrl+Shift+I`. On macOS, use `Command+Option+I`.
6. Select the **Network** panel, reload the page, and confirm that a document
   request appears.

The exact panel layout changes between releases. Learn the evidence, not the
color or screen position: request URL, method, status, response headers, timing,
and initiator. Do not install a large collection of browser extensions. An
extension can change requests, inject content, consume memory, or confuse a
laboratory observation. Use a clean browser profile when results are surprising.

## 4. Install and orient Visual Studio Code

This book uses **Visual Studio Code (VS Code)** because it is available on the
three supported desktop platforms. It is a text editor, not the same product as
Visual Studio. Students may use another capable editor, but instructors can only
guarantee that the published steps match VS Code.

### 4.1 Windows

1. Open the official [VS Code download page](https://code.visualstudio.com/Download).
2. Download the **User Installer** for the correct x64 or ARM64 architecture.
3. Run the installer. Keep the options that add VS Code to the `PATH` and allow a
   folder to be opened with Code when they are offered.
4. Close and reopen PowerShell after installation so it reads the updated `PATH`.

### 4.2 macOS

1. Download the macOS build from the official VS Code site. The Universal build
   supports both Intel and Apple silicon.
2. Open the downloaded disk image and drag `Visual Studio Code.app` into
   **Applications**.
3. Start VS Code from Applications.
4. Open the Command Palette with `Command+Shift+P`, run
   **Shell Command: Install 'code' command in PATH**, and restart Terminal.

### 4.3 Linux

1. Use the official `.deb` package on Debian or Ubuntu, the official `.rpm`
   package on Fedora or Red Hat compatible systems, or the documented package for
   your distribution.
2. Install through the distribution's package tool so updates can be delivered
   normally.
3. Start a new terminal after installation.

### 4.4 Verify the editor

In a new terminal, run:

```text
code --version
```

The first line should be a version number. If the graphical editor opens but the
command is unknown, VS Code is installed but its command-line launcher is not on
`PATH`. Repeat the relevant platform step. You can continue temporarily by using
**File > Open Folder**, but repair the command before later automation exercises.

Open a **folder**, not only an individual HTML file. The Explorer area should show
the project tree. VS Code includes basic HTML, CSS, JavaScript, JSON, Markdown,
terminal, and Git support; no extension is required for the first three sessions.
Extensions are executable software. Install only an instructor-approved extension,
review its publisher and permissions, and remove it if it changes course results.
AI completion is optional and must follow the university's assessment and privacy
policy; it is never a prerequisite for this book.

## 5. Learn the minimum terminal model

A terminal window displays output and accepts commands through a **shell**.
Windows students use PowerShell in this book. macOS commonly uses Z shell
(`zsh`), and Linux commonly uses Bash. Shell syntax differs, so use the code block
labelled for your platform.

The prompt may display a path followed by `>` or `$`. Do not type the prompt
symbol shown in a tutorial. Type only the command. Press Enter to run it. Commands
operate relative to a **current working directory**, so confirm the directory
before deleting, moving, installing, or starting a server.

**Table 0.3 - Essential navigation commands**

| Purpose | Windows Command Prompt | Windows PowerShell | macOS or Linux shell |
|---|---|---|---|
| Show current directory | `cd` | `Get-Location` | `pwd` |
| List items | `dir` | `Get-ChildItem` | `ls` |
| Enter a folder | `cd /d "full-path"` | `Set-Location "full-path"` | `cd "full-path"` |
| Move to parent | `cd ..` | `Set-Location ..` | `cd ..` |
| Create a folder | `mkdir web-course` | `New-Item -ItemType Directory web-course` | `mkdir web-course` |
| Clear the display | `cls` | `Clear-Host` | `clear` |
| Stop a foreground server | `Ctrl+C` | `Ctrl+C` | `Ctrl+C` |

Paths containing spaces must be quoted, for example
`Set-Location "C:\Users\Ada\Course Work"` or
`cd "/Users/ada/Course Work"`. Tab completion reduces spelling errors: type the
first few characters of a filename and press Tab. The Up Arrow recalls a previous
command. Before pressing Enter on an unfamiliar command, explain what it will
read, change, create, or remove.

### 5.1 The project root is a place, not an abstract idea

Every terminal is currently *inside* one folder. A command such as `npm run ...`
does not search the whole computer for the project you had in mind. npm begins
from the terminal's current folder and expects the project's `package.json`
there. For student work in this course, the **repository root** is the outer
`web-programming-coursework-2026_Fall-STUDENT_NUMBER` folder containing
`package.json`, `labs`, and `scripts`. The final part of the folder name contains
the student's real university number, not the literal text `STUDENT_NUMBER`.

For a hypothetical example, suppose Command Prompt begins like this:

```text
C:\Users\Student>
```

The path before `>` says that the current folder is `C:\Users\Student`. It is not
the course repository. If npm were run there, it would search that directory for
`package.json` and could report a path such as
`C:\Users\Student\package.json`. This is a troubleshooting example, not output
that should appear during the successful orientation procedure. Figure 0.3
contrasts the hypothetical wrong location with the correct repository root.

<!-- figure:terminal-directory-rescue -->

Use this four-part check before every project command:

**Step 1 - Locate the project folder.** In File Explorer, browse to the folder
that visibly contains `package.json`. If a student named `Student` cloned the
repository into the usual GitHub folder, an example location would be
`C:\Users\Student\Documents\GitHub\web-programming-coursework-2026_Fall-12345678`.
Here, `12345678` is a fictional student number. Your Windows account name,
student number, and chosen clone location will be different.

**Step 2 - Enter that folder.** In Command Prompt, type the following command
exactly. `/d` allows `cd` to change the drive as well as the folder:

```text
cd /d "C:\Users\Student\Documents\GitHub\web-programming-coursework-2026_Fall-12345678"
```

**Step 3 - Prove the location.** Run `cd`, followed by `dir package.json`. The
first command should print the repository path; the second should list
`package.json`. If the second command says **File Not Found**, stop. Do not run
npm yet.

**Step 4 - Run the project command only after the proof succeeds.** For example,
run `npm test` or `npm run serve:week01`.

There is also a convenient visual route. Open the correct project folder in File
Explorer, click its address bar, type `cmd`, and press Enter. Windows opens
Command Prompt already positioned in that folder. Alternatively, right-click an
empty area inside the folder and choose **Open in Terminal** when Windows offers
that command. Still run `dir package.json`; visual navigation can also end in the
wrong nested folder.

## 6. Install and configure Git

Git is the version-control system used for checkpoints, review, collaboration,
and recovery. Git and a hosting service such as GitHub are related but distinct:
Git works locally; a hosting service stores remote repositories and adds account,
review, and collaboration features.

### 6.1 Install Git

- **Windows:** download Git for Windows from the official
  [Git installation page](https://git-scm.com/install/). The standard options are
  suitable for this course. PowerShell and VS Code should be allowed to find Git.
- **macOS:** run `git --version`. macOS may offer to install its Command Line
  Tools. Alternatively, use the current official Git installer or an
  institution-approved package manager.
- **Debian or Ubuntu:** run `sudo apt update`, followed by
  `sudo apt install git`.
- **Fedora:** run `sudo dnf install git`.

Use your distribution's corresponding supported command if it is not listed.
Do not copy an installation command from an advertisement or unreviewed forum.

### 6.2 Verify and identify the author

Run:

```text
git --version
```

Then configure the identity that should be stored in new commits:

```text
git config --global user.name "Your Name"
git config --global user.email "your-address@example.edu"
git config --global init.defaultBranch main
```

Replace the examples with your own approved identity. If a public repository
must not expose a personal email address, use the privacy address offered by the
course's hosting service. Confirm the result:

```text
git config --global --list
```

The repository contains `.editorconfig` rules that standardize text files. After
obtaining the repository, run `git config core.autocrlf input` inside it. This is
a repository-local setting that helps preserve LF line endings without changing
unrelated repositories.

Git credentials are not the same as commit identity. Never place a password,
personal access token, private key, or multi-factor recovery code in a source
file. When remote access is introduced, use the hosting service's supported
credential manager or Secure Shell (SSH) workflow and enable multi-factor
authentication.

## 7. Install Node.js 26 LTS and npm

Node.js is a JavaScript runtime outside the browser. npm is the package manager
and project-script runner installed with Node.js. The repository declares
`>=26 <27` in `package.json`; its `.nvmrc` records the tested v26 release. Do not
substitute an end-of-life Node.js version merely because it was already installed.

At this book's technical review date, Node.js 26 is an LTS release. Always confirm
the maintained status on the official
[Node.js releases page](https://nodejs.org/en/about/previous-releases) before a
new academic year.

### 7.1 Windows and macOS installer path

1. Open the official [Node.js download page](https://nodejs.org/en/download).
2. Select the latest available **24.x LTS** installer for the computer's x64 or
   ARM64 architecture.
3. Run the installer and keep npm and `PATH` integration enabled.
4. Close every old terminal window and open a new one.

### 7.2 Linux path

Use the installation method linked from the official Node.js download page for
your distribution, or use an institution-approved Node version manager. Default
distribution repositories can contain an older major version, so version
verification is mandatory. Do not use an unexamined `curl ... | sudo bash`
command copied from a forum.

### 7.3 Optional version-manager path

A version manager is useful when different projects require different Node.js
majors. The manager and commands differ between Windows and POSIX systems, so it
is optional rather than the common classroom baseline. If you use one, install
the version recorded in `.nvmrc`, activate it in the current shell, and still run
all verification commands below. A version manager does not replace Node.js; it
selects which installed Node.js version the shell uses.

### 7.4 Verify Node.js and npm

Run:

```text
node --version
npm --version
```

The Node.js output must begin with `v26.`. npm should print its own version. The
two numbers are not expected to match because Node.js and npm are separate
packages. If `node` works in one terminal but not another, compare the shells,
restart VS Code, and inspect `PATH` before reinstalling software.

Do not use `sudo npm install -g ...` or an elevated PowerShell for ordinary course
packages. This repository currently needs no third-party package installation for
the foundation tests. Later chapters will use local project dependencies recorded
in `package.json` and a lockfile.

### 7.5 JavaScript is the course's primary programming language

This course teaches web programming primarily with **JavaScript**. JavaScript is
the programming language; a browser and Node.js are two different environments
that can execute programs written in that language. The standardized definition
of modern JavaScript is called **ECMAScript**. In normal conversation, developers
say *JavaScript* when referring to programs that follow that standard together
with the facilities supplied by their execution environment.

The distinction matters because the language and the environment contribute
different capabilities:

- JavaScript itself supplies values, variables, operators, decisions, loops,
  functions, arrays, objects, classes, promises, and modules.
- A browser adds browser-specific application programming interfaces (APIs),
  including the Document Object Model (DOM), events, `fetch`, and web storage.
  Browser JavaScript can respond to a click and change a page.
- Node.js adds server and operating-system APIs, including files, processes,
  streams, and HTTP servers. Node.js does not provide a browser page or DOM by
  default.
- npm is not another programming language. It installs project dependencies and
  runs named scripts, while Node.js executes the JavaScript used by those tools
  and servers.

Figure 0.4 shows one language entering two runtimes. The shared middle is why
students can transfer language knowledge from client-side code to server-side
code. The different host APIs are why code cannot always be copied unchanged
between the two environments.

<!-- figure:javascript-runtime-map -->

HTML and Cascading Style Sheets (CSS) remain essential, but they have different
jobs. HTML describes content and relationships. CSS describes presentation and
layout. JavaScript expresses algorithms, behavior, state changes, and application
logic. Calling all three “programming languages” hides distinctions that become
important during debugging.

### 7.6 Verify JavaScript in the browser

Every supported browser already includes a JavaScript engine; there is no
separate browser-JavaScript installer. To verify it without creating a file:

1. Open `https://example.com/` in the course browser.
2. Open developer tools and select **Console**. If Console is hidden, select the
   `>>` overflow menu and choose **Console**.
3. Click beside the `>` input prompt, type `1 + 2` yourself, and press Enter. The
   next line should be `3`.
4. Type `typeof document` and press Enter. The result should be `"object"`
   because the browser supplies a document for the current page.

The Console executes code immediately in the context of the open page. Never
paste an unknown command into it. Some browsers display a self-XSS warning to
protect users from being tricked into pasting malicious code. For this exercise,
type the two short expressions manually and do not bypass the warning.

### 7.7 Verify JavaScript in Node.js

From any terminal in which `node --version` succeeds, run:

```text
node -e "console.log(1 + 2)"
node -e "console.log(typeof document)"
```

The first command should print `3`. The second should print `undefined`. That
second result is expected: Node.js executed JavaScript correctly, but it does not
create a browser document. The `-e` option asks Node.js to evaluate the short
program that follows it. Later chapters will place programs in `.js` and `.mjs`
files, import modules, and test them rather than writing substantial programs on
the command line.

### 7.8 How JavaScript develops across the course

The sequence deliberately separates concerns before combining them:

1. Chapter 1 explains where JavaScript fits in a web request and rendered page.
2. Chapters 2 and 3 establish semantic HTML and professional CSS so that scripts
   enhance a sound document rather than replacing one.
3. Chapter 4 teaches JavaScript from first principles: values, variables, types,
   control flow, functions, scope, arrays, objects, errors, debugging, and tests.
4. Chapter 5 applies the language to the DOM, events, and forms in the browser.
5. Chapter 6 explains asynchronous JavaScript, promises, `async`/`await`,
   `fetch`, JavaScript Object Notation (JSON), and Web APIs.
6. Chapter 7 adds ECMAScript modules, npm tooling, and then TypeScript. JavaScript
   comes first so that students do not learn a language, a type system, and the
   DOM simultaneously.
7. Chapter 8 uses Node.js to teach server-side JavaScript and HTTP services.
   Later projects connect browser code, server code, and persistent data while
   preserving their separate responsibilities.

This means client-side and server-side programming are taught separately first,
then integrated in full-stack applications. The language is shared; the security
boundaries, available APIs, lifetime, and responsibilities are not.

## 8. Create or obtain your remote repository before developing

The safest course workflow begins with a **private remote repository** assigned
to the student. A repository is a project folder together with the history of
changes recorded by Git. A **Git hosting service** is a website that stores Git
repositories on an Internet-connected server and controls who may read or change
them. GitHub, GitLab, and Bitbucket are examples. This course uses **GitHub**, at
`https://github.com/`. Git is the version-control program on your computer;
GitHub is the online service. They cooperate, but they are not the same product.

The word **local** means “on this computer.” The word **remote** means “stored at
another location and reached through a network.” After cloning, the same project
therefore exists in two places: a local project folder that you edit and a remote
repository on GitHub that receives commits when you push. Saving a file does not
update Git history, committing does not upload it, and pushing does not
automatically include uncommitted changes.

Figure 0.5 shows the full relationship. The remote repository and local project
folder are two related locations, not one magical shared folder.

<!-- media:repository-first-workflow -->

### 8.1 Preferred course method: create from the instructor's GitHub template

This subsection describes one specific route: the instructor prepares a GitHub
**template repository**, and each student creates a separate private repository
from it. A template is a starting project whose folders and files can be copied
through a button on GitHub. It is not a document template in Microsoft Word, and
students do not edit the instructor's original repository.

#### Information that must come from the instructor

The Fall 2026 class uses the following private GitHub template repository. Open
the [Fall 2026 coursework template](https://github.com/Mahyar2020/web-programming-coursework-2026_Fall)
while signed in to the authorized GitHub account.

```text
https://github.com/Mahyar2020/web-programming-coursework-2026_Fall
```

The instructor must also publish that exact clickable address in the course's
**learning management system (LMS)**, such as Moodle, Canvas, or Blackboard.
Students should use the LMS copy rather than an address received from an
unverified account. In this address, `Mahyar2020` is the owner and
`web-programming-coursework-2026_Fall` is the repository name.

Do not confuse it with the repository containing this book. The
[course-book source repository](https://github.com/Mahyar2020/web-programming-course-book)
is used to produce the book and instructor resources; it is not the repository
in which students complete laboratory work.

If the LMS contains no assignment link, or the link opens a `404` page, stop and
ask the instructor for the semester's GitHub template or invitation. Do not guess
the address, create an unrelated empty repository, use a repository found through
a web search, or substitute **Fork** or **Download ZIP** unless the instructor
chooses one of those workflows. A private repository can also appear as `404`
when the signed-in account has not been granted access.

#### Step 1 - Create or sign in to the correct GitHub account

Open `https://github.com/` in a browser. Choose **Sign up** if you do not have an
account, or **Sign in** if you do. Use the account approved by the university. If
the university created a managed account, follow its sign-in instructions rather
than creating a second account. Confirm the signed-in username by selecting the
profile picture in the upper-right corner; GitHub displays the username in that
menu.

The browser is being used here to manage the online account. The terminal and
the `git` command will be used later to create the local copy.

#### Step 2 - Protect the account with multi-factor authentication

**Multi-factor authentication (MFA)** requires more than one kind of evidence
when signing in. GitHub calls its implementation **two-factor authentication
(2FA)**. A password is one factor; a changing code from an authenticator
application, a passkey, or a physical security key supplies another. This limits
the damage if somebody learns the password.

GitHub currently recommends a time-based one-time password (TOTP) authenticator
application rather than a text message. Prepare an authenticator application on
a phone or computer, then follow these steps in GitHub:

1. Select the profile picture in the upper-right corner and choose **Settings**.
2. In the left sidebar under **Access**, choose **Password and authentication**.
3. Find **Two-factor authentication** and choose **Enable two-factor
   authentication**.
4. Use the authenticator application to scan the displayed Quick Response (QR)
   code. If the device cannot scan it, GitHub can display a setup key for manual
   entry.
5. Enter the six-digit code produced by the authenticator application. The code
   changes periodically, so use the current one.
6. Download the recovery codes when GitHub displays them. Store them in a secure
   password manager or another protected location separate from the laptop.
7. Confirm that the recovery codes have been saved. Add a passkey or security key
   as a backup method when one is available.

Recovery codes can restore access if the authenticator device is lost. Never put
the QR image, setup key, password, authenticator code, or recovery codes in the
course repository, a screenshot submitted for grading, email, or a shared chat.
The detailed and update-sensitive procedure is maintained in GitHub's official
[two-factor authentication instructions](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication).

#### Step 3 - Open and verify the instructor's exact link

First accept the private-repository invitation sent by GitHub. Open the
notification while signed in to the GitHub account registered for this course,
confirm that the invitation names `Mahyar2020` and
`web-programming-coursework-2026_Fall`, and choose **Accept invitation**. If no
invitation is visible, check the GitHub notification inbox and the email address
registered with GitHub, then contact the instructor. Do not ask another student
to forward an invitation because repository invitations are account-specific.

Return to the LMS and select the template link posted for this semester. Do not
retype it when the clickable link is available. The browser address must be:

```text
https://github.com/Mahyar2020/web-programming-coursework-2026_Fall
```

The page should display course files and a **Use this template** button above the
file list. If the button is absent, one of three things is likely true: the link
is not a template, the wrong account is signed in, or the account lacks access.
Record the page address and ask the instructor which condition applies. Do not
choose a different button merely to continue.

#### Step 4 - Create your own remote repository from the template

Select **Use this template**, then **Create a new repository**. On the creation
page:

1. Set **Owner** to the personal account or university organization specified by
   the instructor.
2. Name the repository
   `web-programming-coursework-2026_Fall-STUDENT_NUMBER`, replacing
   `STUDENT_NUMBER` with your university student number. Do not include spaces.
3. Enter an optional description such as `Coursework for Web Programming`.
4. Choose **Private** unless the university explicitly requires another
   visibility. Private means only authorized accounts can read the repository;
   it does not mean security practices are unnecessary.
5. Leave the **Include all branches** checkbox **unchecked**. Unchecked means
   off: GitHub will copy only the default `main` branch. Select it only if the
   instructor explicitly announces that additional template branches are needed.
6. Do not add another README, `.gitignore`, or license. Those files already come
   from the template.
7. Choose **Create repository from template** and wait for the new page to load.

Confirm that the page now shows your chosen owner and repository name at the top.
This new page is your remote repository. Creating it did not yet place a project
folder on the computer.

#### Step 5 - Grant the instructor access to your private repository

The new repository belongs to the student, so access to the template does not
automatically give the instructor access to the student's copy. On the new
repository page, choose **Settings**, then **Collaborators** or **Collaborators
and teams**. Choose **Add people**, enter `Mahyar2020`, verify the account name,
and send the invitation. The instructor must accept it before private coursework
can be reviewed.

Return to the repository's **Code** page after sending the invitation. Never add
an unfamiliar account merely because its display name resembles the instructor's
name.

#### Step 6 - Copy the HTTPS clone address

On your new repository page, choose the green **Code** button. Select **Local**,
then **HTTPS**, and use the copy button beside the displayed address. It should
resemble the following example, with your real owner and repository name:

```text
https://github.com/YOUR_GITHUB_USERNAME/web-programming-coursework-2026_Fall-YOUR_STUDENT_NUMBER.git
```

Secure Shell (SSH) is another valid connection method, but use it only after the
course has taught SSH keys. Copying an address does not clone anything; it places
text on the clipboard for the next command.

#### Step 7 - Choose the parent folder on the computer

In Windows File Explorer, create or open a parent folder such as
`C:\Users\YourName\Documents\GitHub`. The parent folder will contain the project,
but it is not the project itself. Click the File Explorer address bar, type
`cmd`, and press Enter to open Command Prompt in that parent folder. The prompt
should end with `Documents\GitHub>`.

On macOS or Linux, open a terminal and use `cd` to enter the chosen parent folder.
Use `pwd` to print and verify its location.

#### Step 8 - Clone the remote repository to create the local project

At the terminal prompt, type `git clone`, add one space, paste the HTTPS address
copied in Step 6, and press Enter. A representative command is:

```text
git clone https://github.com/YOUR_GITHUB_USERNAME/web-programming-coursework-2026_Fall-YOUR_STUDENT_NUMBER.git
```

Replace the entire example URL with the address copied from your repository. Do
not type the placeholder words `YOUR_GITHUB_USERNAME` or
`YOUR_STUDENT_NUMBER`. Git creates a new subfolder, downloads the project files
and Git history, and normally names the remote connection `origin`. During the
first private-repository operation, Git Credential Manager may open a browser
and ask you to authorize Git. Complete that browser sign-in; do not put the
GitHub password into the command itself.

#### Step 9 - Enter the project and prove that the two locations are connected

In Windows Command Prompt, use the actual folder name created by `git clone`:

```text
cd /d "C:\Users\YourName\Documents\GitHub\web-programming-coursework-2026_Fall-YOUR_STUDENT_NUMBER"
dir package.json
git status
git remote -v
```

On macOS or Linux, use `cd` with the corresponding path and replace
`dir package.json` with `ls -l package.json`. Read the evidence rather than
assuming success:

- `dir package.json` or `ls -l package.json` must display the project file;
- `git status` must name the current branch and report the working-tree state;
- `git remote -v` must show the HTTPS address of **your** remote repository next
  to `origin` for fetch and push; and
- the owner and repository in that address must match the new GitHub page created
  in Step 4, not merely the instructor's template.

If `git clone` reports `Repository not found`, first confirm the copied address
and signed-in GitHub account. For a private repository, the message often means
that authentication failed or that the account lacks permission; it does not
necessarily mean that the repository has been deleted.

### 8.2 If the instructor supplies a clone URL instead of a template

Clone the supplied URL into the course-work parent folder, enter the new folder,
and perform the same four verification commands. You can push only if the remote
grants your account permission. Do not make experimental commits on a protected
shared book branch. The instructor may instead create one remote repository per
student or require a personal fork.

### 8.3 If you already have the repository on this computer

Do not clone a second copy merely because the terminal opened elsewhere. Find the
existing outer project folder in File Explorer. For the hypothetical Windows
location used in this orientation, the Command Prompt sequence is:

```text
cd /d "C:\Users\Student\Documents\GitHub\web-programming-coursework-2026_Fall-12345678"
dir package.json
git status
```

If all three succeed, continue in that folder. Two clones with similar names make
it easy to edit one copy and run another, so keep one clearly named working copy.

### 8.4 If the instructor provides a ZIP archive

1. Save the ZIP in the course-work parent folder and extract it completely.
2. Confirm that the extracted outer folder contains `package.json`; never work
   inside the compressed preview.
3. Run `git status` inside the extracted folder. If Git says it is not a
   repository, the ZIP contains files but no Git history.
4. Create the approved empty private remote repository in the browser. Do not add
   a README if the extracted project already has one.
5. In the extracted project root, follow the instructor's commands to initialize
   Git and connect that specific remote. Because a mistaken remote can publish
   work to the wrong place, the instructor should verify `git remote -v` before
   the first push.

### 8.5 Open the whole repository in VS Code

From the verified repository root, run:

```text
code .
```

The dot means **this current folder**. In VS Code, the Explorer should show
`labs`, `scripts`, `package.json`, and `.nvmrc`. The bottom terminal prompt should
end with the project-folder name. If Explorer shows only one HTML file,
use **File > Open Folder**, select the outer repository folder, and choose
**Select Folder**. When VS Code asks whether you trust the authors, first verify
that the repository came from the authorized course source.

### 8.6 Use the same save-check-commit-push cycle for developed work

At the end of each small, working change:

```text
git status
git diff
git add path-to-the-file-you-changed
git diff --staged
git commit -m "Describe the completed change"
git push
```

Read `git status` and both diffs. Replace the example path and message; do not add
every file blindly. The first push may ask the browser or a credential manager to
authenticate. Use the hosting service's approved sign-in flow, not an account
password embedded in a command. Refresh the remote repository page afterward and
confirm that the latest commit is visible. That visible remote commit is the
evidence that the push succeeded.

## 9. Run the reproducible readiness test

Do not begin with `npm test`. First prove where the terminal is. In Windows
Command Prompt, a successful preflight looks like this:

```text
cd
dir package.json
```

The first output must be the repository root. The second must display
`package.json`. In PowerShell use `Get-Location` and `Get-Item package.json`; on
macOS or Linux use `pwd` and `ls -l package.json`. Only then run these commands
one at a time:

```text
node --version
npm --version
git --version
npm test
```

`npm test` does not mean “test npm.” npm reads `package.json` and runs this
project's named `test` script. In the student coursework repository, the script
checks the required project files, the starter HTML documents, the Node.js major
version, and an HTTP response from each Week 1-3 server. A passing result
demonstrates that the runtime can read the project and execute the supplied setup
checks. It does not prove that every future program is correct.

Record the complete first failure, not only its final line. Common distinctions
include:

- **command not found:** the tool is missing or not available through `PATH`;
- **wrong major version:** another installation or version manager is active;
- **file not found:** the terminal is probably in the wrong directory;
- **permission denied:** the current account cannot read or execute the target;
- **test assertion failed:** the tools ran, but project content does not meet a
  checked requirement.

When the check finishes successfully, the last lines include messages such as
`Local Markdown link verification passed`, `Week 1 verification passed`, and
`Foundation verification passed`. Version numbers may differ in their minor and
patch parts, but the Node.js line must begin with `v26.` for this edition.

## 10. Start and inspect the local server

### 10.1 What the book means by two terminals

There are not two different terminal products to install. A **server terminal**
is simply an ordinary Command Prompt, PowerShell, macOS Terminal, or VS Code
terminal tab in which a server is currently running. A **command terminal** is a
second ordinary window or tab that remains free for `git status`, `npm test`, and
navigation commands.

You need two because a foreground server keeps running and keeps control of the
first terminal. When it is active, the normal prompt does not return. That is not
a freeze. It is evidence that the process is waiting for browser requests.
Figure 0.6 shows how to recognize the two roles.

<!-- figure:two-terminal-model -->

To create two terminals in VS Code:

1. Open the repository with `code .`.
2. Choose **Terminal > New Terminal**. A panel opens at the bottom. Check that its
   prompt path ends with the repository folder name.
3. In the terminal panel, select the plus sign (**+**) to create a second tab.
   Rename the tabs **SERVER** and **COMMANDS** if your VS Code version offers
   **Rename** in the tab's context menu.
4. Select **SERVER** before running the server command. Leave **COMMANDS** unused
   until you need another command.

In Windows Command Prompt you can instead open two separate windows. Run the same
`cd /d "..."` command in both windows because every terminal has its own current
directory.

### 10.2 Start the server and read its output

In the terminal designated **SERVER**, prove that `package.json` is present and
then start the server with the Week 1 page from the student coursework
repository:

```text
dir package.json
npm run serve:week01
```

At this point you are checking whether Node.js, the local server, and the browser
cooperate; you are not yet expected to complete the Campus Hub document. The
starter includes a visible setup message as well as comments marking the work
for Session 1, so a successful server does not produce an unexplained white page.

On macOS or Linux, replace `dir package.json` with `ls -l package.json`. The
expected final three server lines are:

```text
Serving ...\labs\week-01
Open http://localhost:8000/
Press Ctrl+C to stop.
```

The beginning of the first path depends on your computer. The important ending
is `labs\week-01` on Windows or `labs/week-01` on macOS and
Linux. Leave this terminal running. Figure 0.7 pairs the expected terminal state
with the expected browser result.

<!-- figure:server-browser-evidence -->

### 10.3 Open the address correctly

Click the browser's address bar, type exactly `http://localhost:8000/`, and press
Enter. Do not include Markdown brackets, parentheses, quotation marks, or a final
period. In particular, this is book-link notation, not something to type:
`[http://localhost:8000/](http://localhost:8000/)`. The browser receives only the
plain address.

`localhost` is a special host name for the current computer. `8000` is the port
on which this course server is listening. This step does not publish anything to
the Internet. The page should show the heading **Campus Hub setup check** and a
message stating that the browser received the Week 1 starter through the local
server. In Session 1, you will replace that setup content with the complete
Campus Hub structure.

If the address loads but the page is white, first confirm that the terminal's
`Serving ...` line ends with `labs\week-01`, then open
`labs/week-01/index.html` in VS Code and confirm that it contains the setup-check
heading. Save the file and reload the browser. This is different from **This site
can't be reached**, which means the browser could not connect to a listening
server.

### 10.4 Find Network in developer tools

The **Network** panel belongs to the browser's developer tools, not to VS Code and
not to Windows network settings.

1. Keep the Campus Hub tab selected.
2. Open developer tools with `F12` or `Ctrl+Shift+I` on Windows/Linux, or
   `Command+Option+I` on macOS.
3. A panel normally opens beside or below the page. Across its top are tabs such
   as **Elements**, **Console**, **Sources**, and **Network**. Select **Network**.
4. If **Network** is hidden because the panel is narrow, select the double-chevron
   `>>` overflow button and choose **Network**. You can also open the developer
   tools command menu and search for **Show Network**.
5. Network records activity from this point forward. If its table is empty,
   reload with `Ctrl+R`, `F5`, or the browser reload button while developer tools
   remains open.
6. Select the row named `localhost` or `/` whose **Type** is `document`. Do not
   select an image or icon row.
7. In the details pane, select **Headers**. Under **General**, find **Request
   URL**, **Request Method**, and **Status Code**. Under **Response Headers**, find
   **Content-Type**.

Figure 0.8 is a stable, representative screen map. Browser colors and exact tab
positions may change, but the evidence names remain recognizable.

<!-- figure:network-panel -->

Record these expected values:

**Table 0.4 - Expected evidence for the Week 1 localhost document request**

| Evidence | Expected value |
|---|---|
| Request URL | `http://localhost:8000/` |
| Request method | `GET` |
| Status code | `200 OK` |
| Resource type | `document` |
| Response `Content-Type` | `text/html; charset=utf-8` |

If the status is `404`, the server is reachable but the requested path does not
map to a file. That is different from **This site can't be reached**, which means
the browser could not establish the connection.

### 10.5 Stop the server deliberately

Return to the SERVER terminal, click inside it, and press `Ctrl+C` once. If
Windows asks `Terminate batch job (Y/N)?`, type `Y` and press Enter. The ordinary
prompt returns. Reload the browser: it should now report that the site cannot be
reached. This controlled failure proves that the page depended on the server
process rather than on a previously opened local file.

### 10.6 Optional troubleshooting: npm cannot find `package.json`

Skip this subsection when the server starts and the terminal prints the
`Serving`, `Open`, and `Press Ctrl+C` lines. It describes a different failure
that a learner may encounter later; it does not explain a white page.

`ENOENT` is an operating-system error name meaning that a required file or folder
was not found. For example, if a learner runs npm from the Windows profile folder
instead of the repository root, npm may print a line like this:

```text
npm error path C:\Users\Student\package.json
```

This line is illustrative, not expected output from the orientation. If it does
appear with your own account path, npm is functioning but the terminal is outside
the repository. Reinstalling npm would not move the terminal. Figure 0.9 shows
the diagnostic sequence for that hypothetical case.

<!-- figure:enoent-diagnosis -->

For the example path used in this chapter, the repair would be:

```text
cd /d "C:\Users\Student\Documents\GitHub\web-programming-coursework-2026_Fall-12345678"
dir package.json
npm run serve:week01
```

Do not open the browser until the terminal prints `Open
http://localhost:8000/`. If `dir package.json` fails, confirm the folder in File
Explorer instead of guessing another npm command.

If port 8000 is already in use, first check for a previous course server. On
Windows PowerShell, use `Get-NetTCPConnection -LocalPort 8000`. On macOS, use
`lsof -i :8000`. On Linux, use `ss -ltnp | grep 8000`. Do not terminate an unknown
institutional process. Ask for help with the recorded process information.

## 11. Prepare accessibility inspection tools

No paid accessibility product is required. Prepare the following:

1. Learn the browser's Elements, Accessibility, and Network inspection areas.
2. Confirm that Tab and Shift+Tab move focus and that the operating system is not
   intercepting those shortcuts.
3. Practice browser zoom at 200 percent and restore it afterward.
4. Identify the built-in screen reader available on your platform: Narrator on
   Windows, VoiceOver on macOS, or an institution-supported Linux screen reader
   such as Orca. Screen-reader operation requires its own instruction; turning it
   on for one minute is not a complete accessibility test.
5. Bookmark the [W3C Nu HTML Checker](https://validator.w3.org/nu/) and the
   [W3C accessibility evaluation overview](https://www.w3.org/WAI/test-evaluate/).

Do not upload private coursework or personal data to an online checker unless the
course and data policy permit it. Browser inspection, keyboard testing, validation,
automated accessibility checks, assistive technology, and representative-user
feedback provide different evidence. No single installation proves accessibility.

## 12. Create and push a personal proof-of-work commit

Use a student repository or branch designated by the instructor; do not commit
setup notes directly to a protected shared book branch. Create a plain text file
named `setup-evidence.txt` containing only non-secret evidence such as tool major
versions, test result, operating system, and the date. Then run:

```text
git status
git add setup-evidence.txt
git diff --staged
git commit -m "Record development environment verification"
git log -1 --oneline
git push
```

Read the staged diff before committing. `git add` selects content for the next
commit; it does not upload a file. `git commit` records a local snapshot; it does
not automatically push to a remote service. `git push` sends commits that are not
yet on the configured remote branch. After pushing, refresh the repository page
in the browser. Confirm that the newest commit message and time are visible. If
Git reports that no upstream branch exists, do not guess a destination; verify
`git remote -v` and use the exact first-push command supplied by the instructor.

Repeat this small cycle throughout the course: edit a coherent change, save it,
run the relevant check, review `git diff`, stage only the intended files, commit
with a meaningful message, and push. “Push everything” should mean “push every
reviewed commit needed for the project,” not “upload caches, passwords, generated
dependencies, or unrelated files.” `.gitignore` defines files that should remain
outside version history.

## 13. Troubleshoot from evidence

Table 0.5 maps common symptoms to productive checks. Reinstalling every tool is
rarely the best first response.

**Table 0.5 - Setup symptoms and productive first checks**

| Symptom | First checks |
|---|---|
| `code` is not recognized | Restart the terminal; verify VS Code's command-line launcher is on `PATH`; use Open Folder temporarily |
| `node --version` is older than v26 | Check which executable the shell finds; activate the intended version manager or reinstall the supported major |
| `npm` is blocked by PowerShell policy | Confirm the official Node installation; use the appropriate npm command shim or ask institutional support before changing execution policy |
| `npm test` cannot find `package.json` | Run the current-directory command and move to the repository root |
| Browser cannot reach localhost | Confirm the server terminal is still running, the URL and port match, and no firewall prompt was denied |
| Page does not change after saving | Save the file, verify the server root, inspect the requested URL, and reload with the Network panel open |
| Git refuses to commit | Read the message; configure author name/email, stage the intended file, and confirm the repository and branch |
| Git shows many unexpected line changes | Confirm `.editorconfig`, LF endings, and the repository-local `core.autocrlf` setting before committing |
| A managed computer rejects installation | Record the product, version, installer source, and error; use the university software center or request administrator support |

When asking for help, provide the command as text, the complete error as text, the
current directory, operating system, relevant version output, and what changed
immediately before the failure. A screenshot can supplement that evidence but
should not replace searchable error text. Remove usernames, private repository
addresses, tokens, and personal information when they are not needed.

## 14. Readiness record

Complete Table 0.6. “Installed” is not adequate evidence.

**Table 0.6 - Student workstation readiness record**

| Check | Evidence to record |
|---|---|
| Operating system and architecture | |
| Browser and successful DevTools opening | |
| VS Code version and repository folder opened | |
| Git version and configured author identity | |
| Node.js v26 output | |
| npm version output | |
| Browser Console: `1 + 2` and `typeof document` results | |
| Node.js: arithmetic and `typeof document` results | |
| `npm test` result | |
| Localhost URL, method, status, and `Content-Type` | |
| Server stopped with `Ctrl+C` and failure observed | |
| Latest personal Git commit | |
| Latest commit visible in the remote repository after push | |
| Accessibility tools identified | |

The workstation is ready when every row has observed evidence or an approved
accommodation. Keep this record for the first laboratory rather than repeating
installation during teaching time.

---

# Orientation exercises

## Exercise 1 - Name the responsible tool

For each task, name the primary tool: changing `index.html`, running an npm
script, interpreting HTML pixels, inspecting an HTTP status, preserving a local
snapshot, and executing server-side JavaScript.

## Exercise 2 - Diagnose the directory

`node --version` succeeds, but `npm test` reports that it cannot find
`package.json`. State the most likely cause and give a non-destructive diagnostic
sequence for Windows and for macOS/Linux.

## Exercise 3 - Explain the evidence

A student opens `index.html` with a `file:` URL and says that the local web server
works. Explain why that observation is insufficient and design the smallest test
that demonstrates an HTTP exchange with the course server.

## Exercise 4 - Protect secrets

A terminal error contains a remote URL with a personal access token. Explain how
the student should obtain help without publishing the token and what immediate
security action may be necessary.

## Exercise 5 - Assign the terminal roles

A student starts the server and then tries to type `git status` in the same
terminal, but no normal prompt is visible. Explain what has happened, how to keep
the server running, and where to run `git status`.

## Exercise 6 - Find an empty Network panel

Developer tools is open, but the Network table is empty. Give the exact sequence
that should produce and inspect the document request. State the expected method,
status, resource type, and `Content-Type`.

## Exercise 7 - Separate connection and path failures

Compare these two browser results: **This site can't be reached** and an HTTP
`404 Not Found` response. What does each observation prove, and which evidence
would you inspect next?

## Exercise 8 - One language, two environments

The expression `typeof document` returns `"object"` in the browser Console and
`undefined` in Node.js. Explain why both results can be correct JavaScript. Then
classify each facility as language-level, browser-provided, or Node.js-provided:
an array, `document.querySelector`, `fetch`, `process.argv`, and a function.

---

# Orientation worked answers

## Answer 1

The code editor changes `index.html`. npm reads `package.json` and runs the named
project script. The browser parses and renders HTML. Browser developer tools
expose the HTTP status. Git records the local snapshot. Node.js executes
JavaScript outside the browser. Several tools may participate in one task, but
these are their primary responsibilities.

## Answer 2

The shell is probably outside the repository root. First show the current
directory with `Get-Location` on PowerShell or `pwd` on macOS/Linux. List items
with `Get-ChildItem` or `ls` and look for `package.json`. Move with `Set-Location`
or `cd` into the repository folder, list again, and rerun `npm test`. These checks
do not change files. Reinstalling Node.js would not correct the current directory.

For the hypothetical Windows path used in the chapter, the complete
non-destructive recovery begins with `cd`, then `dir`, then
`cd /d "C:\Users\Student\Documents\GitHub\web-programming-coursework-2026_Fall-12345678"`, and
finally `dir package.json`. A learner must substitute the actual repository path.
Only after the last command displays the file should the student rerun npm. If an
ENOENT message exists, its path is evidence of the folder npm searched; when no
such message exists, this diagnosis does not apply.

## Answer 3

A `file:` URL lets the browser read a local file without an HTTP server. Start
`npm run serve:week01`, visit `http://localhost:8000/`, open the Network
panel, reload, and select the document request. A recorded HTTP method, status,
and response `Content-Type`, together with the running server process, demonstrate
the exchange. Stop the server and observe that the URL no longer responds to
confirm the process boundary.

## Answer 4

The student should revoke or rotate the exposed token immediately through the
hosting service, because redacting a later screenshot does not make an already
disclosed credential safe. The help request should replace the secret with a
marker such as `[REDACTED TOKEN]` while preserving the error type, command shape,
host, and non-sensitive context. The token must not be committed, pasted into a
chat, uploaded to an issue, or placed in setup evidence.

## Answer 5

The server is a foreground process and currently owns that terminal. The absent
prompt is expected while it listens for requests. Leave the first terminal open
and create a second ordinary terminal window or VS Code terminal tab. Enter the
repository root in the second terminal, prove that `package.json` is present, and
run `git status` there. “Server terminal” and “command terminal” describe their
current jobs; they are not different applications. Pressing `Ctrl+C` in the
server terminal would stop the server, so that is appropriate only when the
student intends to end the local session.

## Answer 6

Keep developer tools open, select **Network** (using the `>>` overflow menu if
necessary), and reload the page. Select the `localhost` or `/` row whose Type is
`document`, open **Headers**, and read the General and Response Headers sections.
For the Week 1 starter, the expected evidence is method `GET`, status `200 OK`,
type `document`, and `Content-Type: text/html; charset=utf-8`. Opening Network
after the page loaded may show an empty table because recording began too late;
reloading creates a new observable request.

## Answer 7

**This site can't be reached** means the browser could not complete a connection
to a responding process at the given host and port. Check whether the SERVER
terminal is still running, whether it printed the same port, and whether the URL
was typed as a plain address. A `404 Not Found` response proves that an HTTP
server did respond, but the requested path did not identify an available file.
In that case inspect the Network request URL and the server's configured root and
path. The distinction prevents a student from treating every browser failure as
the same problem.

## Answer 8

JavaScript defines the `typeof` operator, but the execution environment decides
which global objects exist. A browser creates `document` to represent the loaded
page, so `typeof document` is `"object"`. Node.js has no browser document by
default, so reading its type safely produces `undefined`. Neither result implies
that the language is different or broken.

Arrays and functions are language-level facilities. `document.querySelector` is
provided by the browser's Document Object Model. `process.argv` is provided by
Node.js. `fetch` began as a Web API and is now also supplied by current Node.js;
its availability therefore belongs to the host environment rather than to the
core language. This last example shows why developers check both the language
standard and the runtime documentation instead of assuming that every familiar
name is built into JavaScript itself.

---

# Orientation retrieval quiz

1. Why is opening an installer not proof that a tool is ready?
2. What is the difference between Node.js and npm?
3. What does `code .` mean?
4. Why does the current working directory matter?
5. What Node.js major version does this edition require?
6. Does `git commit` automatically upload work?
7. What evidence distinguishes a `file:` load from an HTTP load?
8. Why should browser extensions be kept minimal during laboratories?
9. What should never appear in `setup-evidence.txt`?
10. What is the productive first response to an unfamiliar error?
11. What makes an ordinary terminal a “server terminal”?
12. Why might Network be empty even when a page is visible?
13. What does the path in an npm ENOENT message tell you?
14. What is the difference between save, commit, and push?
15. What programming language is primary in this course?
16. Why can browser JavaScript use `document` while Node.js normally cannot?
17. When are client-side and server-side programming combined in the course?

## Quiz answers

1. Readiness requires executable evidence: version output and successful use in
   the course workflow.
2. Node.js is the runtime that executes JavaScript outside the browser; npm is a
   package manager and project-script runner distributed with Node.js.
3. It asks VS Code to open the current directory as a project folder.
4. Relative paths and project discovery begin there; a correct command in the
   wrong directory can read or change the wrong target.
5. Version 26.x, as constrained by `package.json` and recorded in `.nvmrc`.
6. No. It creates a local snapshot. A separate push operation communicates with
   a remote repository.
7. An HTTP URL plus a Network-panel document exchange with a method, status, and
   HTTP response fields.
8. Extensions can inject content, change requests, add panels, or introduce
   variables that obscure the behavior being studied.
9. Passwords, access tokens, private keys, recovery codes, or unnecessary private
   student and repository information.
10. Preserve the exact error, command, current directory, versions, and recent
    change; identify which layer failed before changing one factor.
11. A foreground server process is currently running in it and has not returned
    the normal shell prompt.
12. Developer tools may have begun recording after the request completed; reload
    while Network is open.
13. It identifies the location in which npm tried to find the missing file, such
    as `package.json`.
14. Save writes the working file, commit records selected content in local Git
    history, and push transfers local commits to the configured remote.
15. Modern JavaScript, standardized as ECMAScript; TypeScript is introduced only
    after students understand JavaScript and modules.
16. `document` is supplied by a browser's DOM environment, not by the core
    JavaScript language. Node.js does not create a browser DOM by default.
17. They are taught separately first, so their APIs and responsibilities are
    clear, and are then integrated in later full-stack application projects.

## Orientation summary

- A workstation is a system of cooperating tools with distinct responsibilities.
- Installation is complete only when version and workflow evidence both succeed.
- The course baseline is a current browser, VS Code, Git, Node.js 26 LTS, npm,
  browser developer tools, and the authorized repository.
- Modern JavaScript is the primary programming language; browser and Node.js
  execute the same core language with different host APIs.
- The repository root is the reference directory for course commands.
- `npm test`, a localhost request, Network evidence, a Git commit, and a verified
  remote push form the minimum reproducible readiness proof.
- Developer tools and automated checks provide evidence; they do not replace
  reasoning or user evaluation.
- Credentials and private data never belong in source, screenshots, logs shared
  publicly, or setup records.

## Orientation references

1. Node.js, [Node.js releases](https://nodejs.org/en/about/previous-releases).
2. Node.js, [Download Node.js](https://nodejs.org/en/download).
3. Microsoft, [Get started with Visual Studio Code](https://code.visualstudio.com/docs/getstarted/overview).
4. Git, [Install Git](https://git-scm.com/install/).
5. Chacon and Straub, [Pro Git - First-Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).
6. Chrome for Developers, [Open Chrome DevTools](https://developer.chrome.com/docs/devtools/open/).
7. Chrome for Developers, [Inspect network activity](https://developer.chrome.com/docs/devtools/network/).
8. GitHub Docs, [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
9. GitHub Docs, [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
10. GitHub Docs, [Pushing commits to a remote repository](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository).
11. GitHub Docs, [About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories).
12. GitHub Docs, [Configuring two-factor authentication](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication).
13. W3C, [Nu HTML Checker](https://validator.w3.org/nu/).
14. W3C Web Accessibility Initiative, [Evaluating Web Accessibility](https://www.w3.org/WAI/test-evaluate/).

## What changes often?

Installer screens, package versions, operating-system permission prompts, and
browser panel layouts change frequently. The responsibility of each tool and the
evidence-led workflow are more stable. Technical review date: **18 November
2026**.
