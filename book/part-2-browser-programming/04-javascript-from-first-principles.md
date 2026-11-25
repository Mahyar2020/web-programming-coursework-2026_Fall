# Session 4 - JavaScript from First Principles

JavaScript turns the static Campus Hub page into a program. This chapter begins
before the first line of code. It assumes that you may never have installed a
programming runtime, opened a project folder, used a terminal, or interpreted an
error message. We will prepare the computer, run one deliberately small program
in Node.js, run another in a browser, and learn how to tell source code from its
output. Only then will we introduce values, names, decisions, repetition,
functions, arrays, objects, errors, and tests. The second half then develops the
language model that short introductions often omit: execution contexts,
closures, first-class functions, method calls, prototypes, classes, keyed
collections, iteration, JavaScript Object Notation (JSON), Unicode-aware text,
dates, internationalization, regular expressions, and modules.

Document Object Model (DOM) manipulation begins in Chapter 5. Keeping that
boundary clear is useful: first we learn the JavaScript language, and then we use
browser facilities to change a page. A reader who already programs should still
complete the environment checks because later laboratories depend on the same
folders, commands, and evidence.

## Session map

Table 4.1 maps each learning phase to the evidence students and instructors can
inspect before moving forward.

**Table 4.1 - Session 4 learning sequence and evidence**

| Phase | Main question | Evidence |
|---|---|---|
| Orient | Where does JavaScript run? | Browser and Node.js produce distinguishable results |
| Represent | What kinds of values can a program hold? | Predicted types and evaluated expressions |
| Decide and repeat | How does execution choose a path or revisit work? | Traced branches and loop iterations |
| Abstract | How does a function turn inputs into a result? | Calls, returns, and scope traces |
| Model | How do arrays and objects represent Campus Hub data? | Filtered and summarized event records |
| Verify | How do we know the program is correct? | Passing tests plus inspected browser output |

## Prerequisites

You need ordinary familiarity with opening files and visiting a web address.
Chapter 0 remains the complete orientation reference, but this chapter repeats
the exact preparation needed for JavaScript so that no reader is blocked by an
unexplained tool. No previous programming course is assumed. Readers with prior
programming experience should still complete the JavaScript-specific checkpoints
on equality, coercion, scope, and mutation.

## Learning outcomes

After this chapter, you should be able to:

1. install or verify the editor, browser, Git, Node.js, and npm required by the course;
2. identify the project folder, current terminal directory, source file, command, and output;
3. create and run a first JavaScript file with Node.js and in a browser;
4. distinguish the ECMAScript language from browser and Node.js host facilities;
5. create and inspect primitive values, arrays, objects, and functions;
6. choose `const` or `let` deliberately and explain `var` scope, initialization, redeclaration, and hoisting in legacy code;
7. trace expressions, statements, branches, and every basic loop form, including its state, condition, progress, and exit;
8. explain strict equality, truthiness, conversion, `null`, and `undefined`;
9. design functions with required, default, rest, and destructured inputs; consistent return shapes; and useful errors;
10. distinguish direct, method, constructor, callback, indirect, bound, recursive, and immediately invoked calls;
11. transform and manipulate arrays while stating whether each operation mutates, copies, searches, or accumulates;
12. explain the difference between rebinding a name and mutating an object;
13. diagnose syntax, reference, type, and assertion failures from evidence; and
14. write and run small automated tests with Node.js;
15. trace the call stack and explain how a closure retains lexical bindings;
16. distinguish a method call's `this` value from an ordinary function call;
17. explain prototype delegation and use a class when it clarifies a data model;
18. choose among arrays, objects, `Map`, and `Set` from the required operations;
19. convert data deliberately at JSON, date, text, and regular-expression boundaries;
20. read an ECMAScript module graph built from `export` and `import`; and
21. identify which language concerns are complete here and which browser,
    asynchronous, and tooling concerns continue in Chapters 5-7.

---

# 0. Prepare the computer and run your first JavaScript

A programming language is learned by making predictions and checking them
against a running program. Reading alone cannot provide that feedback. Before we
study JavaScript vocabulary, we therefore need a small, dependable path from a
file you edit to output you can observe.

Figure 4.1 shows the complete beginner workflow. The boxes are sequential steps,
not alternative technologies. Visual Studio Code edits the source file. Node.js
executes it. The terminal shows the output. Git records the useful change after
the program behaves as intended.

<!-- figure:javascript-first-run-workflow -->

## 0.1 Understand the five tools before installing them

The tools have different responsibilities.

- **Visual Studio Code (VS Code)** is the text editor used to open the project
  folder and write source files. It does not become JavaScript merely because a
  file is open in it.
- **Node.js** is a JavaScript runtime: a program that can read and execute a
  JavaScript file outside a browser.
- **npm** is the package manager installed with Node.js. It reads project
  instructions from `package.json` and runs named scripts such as `npm test`.
  Its official name is written lowercase and is not expanded as a current
  acronym. npm is not the JavaScript language and it is not the web server itself.
- A **web browser** runs client-side JavaScript and supplies browser Application
  Programming Interfaces (APIs) such as the DOM, events, and network requests. We use an up-to-date Chromium-
  based browser and also test important work in Firefox.
- **Git** records versions of the project. GitHub stores a remote copy and helps
  people collaborate, but Git and GitHub do not execute JavaScript.

Table 4.2 gives the command or visible evidence that proves each required tool is
available. A successful installation is not established by remembering that an
installer was clicked; it is established by current evidence.

**Table 4.2 - JavaScript workstation tools and verification evidence**

| Tool | Purpose in this chapter | Verification evidence |
|---|---|---|
| VS Code | Edit the complete project folder and its files | The Explorer shows `package.json` and the `labs` folder |
| Node.js 26 Long-Term Support (LTS) | Execute JavaScript and course tools | `node --version` prints a value beginning with `v26.` |
| npm | Run commands defined by the project | `npm --version` prints a version number |
| Browser | Run client-side code and expose Developer Tools | The Console accepts `2 + 3` and displays `5` |
| Git | Record and inspect changes | `git --version` prints a version number |

The course is tested with the latest available patch release in the Node.js 26
Long-Term Support (LTS) line. “LTS” means that the release line receives a longer
period of maintenance than a short-lived current release. Use the newest 26.x
patch offered by the official Node.js download page; do not search for an old
patch number copied from a screenshot. The repository records the expected major
version in both `.nvmrc` and the `engines.node` field of `package.json`.

## 0.2 Install Node.js on Windows, step by step

If `node --version` already reports `v26.x.x`, continue to Section 0.4. Otherwise,
use the following sequence.

1. Open a browser and visit the official download page at
   `https://nodejs.org/en/download`.
2. Select the latest **LTS** release in the 26.x line and the Windows Installer
   for your computer. Most current Windows computers use the x64 installer; an
   ARM-based Windows computer needs the ARM64 installer. Open **Settings > System
   > About > System type** if you do not know the architecture.
3. Open the downloaded `.msi` file. Windows may ask whether the installer is
   allowed to make changes. Confirm only when the publisher and download source
   are the official Node.js project.
4. Accept the license and keep the default installation features, including npm
   and the option that adds Node.js to `PATH`. `PATH` is the operating system's
   list of folders searched when you type a command such as `node`.
5. Finish the installer. Close every old Command Prompt, PowerShell, and VS Code
   terminal window. An already-open terminal may not know about the updated
   `PATH`.
6. Open a new terminal and run `node --version`, followed by `npm --version`.

On macOS, use the official `.pkg` installer for the current LTS release, finish
the installer, open a new Terminal window, and run the same verification
commands. On Linux, prefer the installation method approved for the course or
institution; distribution repositories can provide a different major version.
Whatever installation method is used, the evidence required by this book is the
same: a new terminal must report Node.js 26 and a working npm command.

Do not use an online playground as a substitute for this setup. Playgrounds are
useful for experiments, but they do not teach the local folders, module files,
tests, server process, and Git workflow used throughout the course.

## 0.3 Install or verify Visual Studio Code

Visit the official download page at `https://code.visualstudio.com/Download`.
On Windows, the **User Installer** is appropriate for most students because it
installs for the current account without requiring a system-wide installation.
Run the installer and keep the option that adds the `code` command to `PATH` when
it is offered. Then close and reopen terminals.

Open VS Code. Choose **File > Open Folder**, select your personal coursework
repository, and choose **Select Folder**. A folder opened this way is the
workspace. In the Explorer at the left, confirm that `package.json`, `labs`, and
`scripts` are visible at the top level. Opening only `events.js` is not
equivalent: npm commands depend on the project root that contains
`package.json`.

If VS Code displays **Workspace Trust**, trust the folder only if it is your own
coursework clone or the authorized course repository. Restricted Mode is the
appropriate place to inspect unfamiliar code before allowing it to run.

## 0.4 Open the correct terminal and prove its current directory

In VS Code, choose **Terminal > New Terminal**. The terminal panel normally
opens below the editor. The text before the cursor is the **prompt**. For
example, PowerShell may display the following prompt.

```text
PS C:\Users\Student\Documents\GitHub\web-programming-coursework-2026_Fall>
```

Do not type the `PS`, the path, or the final `>` when copying a command. They are
evidence showing which shell is running and which directory it currently uses.
Type the following commands one line at a time, pressing Enter after each line.

```text
dir package.json
node --version
npm --version
git --version
```

On macOS or Linux, `ls package.json` replaces `dir package.json`; the other
commands are the same. Stop if the first command says that `package.json` cannot
be found. The terminal is not at the repository root. Use **File > Open Folder**
again, or change directory with `cd` followed by the exact repository path. A
path containing spaces must be enclosed in quotation marks.

```text
cd "C:\Users\Student\Documents\GitHub\web-programming-coursework-2026_Fall"
```

Figure 4.2 distinguishes three things beginners often merge together: the file
saved on disk, the command typed into a shell, and the output produced by the
runtime. Editing the file does nothing until the updated file is saved and run.

<!-- figure:javascript-source-command-output -->

## 0.5 Create and run the first Node.js program

In the VS Code Explorer, expand `labs`, expand `week-04`, and open `hello.js`.
If your instructor has asked you to create the file, right-click `week-04`,
choose **New File**, type `hello.js`, and press Enter. The `.js` extension tells
tools that the file contains JavaScript source code.

Enter the following program exactly, then save it with **File > Save** or
Ctrl+S on Windows and Linux, or Command+S on macOS.

```js
const courseName = "Web Programming";
const sum = 2 + 3;

console.log(`Hello from ${courseName}!`);
console.log(`Two plus three is ${sum}.`);
```

Before running it, read the punctuation. Table 4.3 names each important symbol
and explains the job it performs in this first program.

**Table 4.3 - Symbols in the first JavaScript program**

| Source text | Meaning in this program |
|---|---|
| `const` | Declare a name that will not be assigned a different value later |
| `courseName` and `sum` | Names chosen by the programmer; JavaScript is case-sensitive |
| `=` | Assign the value on the right to the name on the left; it does not mean equality here |
| `"Web Programming"` | A string value: a sequence of text characters |
| `2 + 3` | An expression that adds two number values and produces `5` |
| `` `...${...}...` `` | A template literal that inserts an evaluated expression into text |
| `console.log(...)` | Call the `log` function of the host's `console` object |
| `(` and `)` | Enclose the argument supplied to the function call |
| `.` | Select the named `log` property from `console` |
| `;` | Mark the intended end of a statement in this course's style |

From the repository root, run the file with Node.js.

```text
node labs/week-04/hello.js
```

Expected terminal output follows. Do not type these two output lines as commands.

```text
Hello from Web Programming!
Two plus three is 5.
```

Change `2 + 3` to `2 * 3`, save, predict the new result, and run the same command
again. If the output still says `5`, the file was probably not saved or a
different file was executed. This small experiment establishes an essential
cycle: edit, save, predict, run, observe, and explain.

## 0.6 Run JavaScript in a browser

Node.js and a browser both implement JavaScript, but they are different host
environments. Open `hello-browser.html`. Near the end of its `<body>`, the
following element asks the browser to obtain and execute another file.

```html
<script src="hello-browser.js"></script>
```

The `src` attribute is a relative Uniform Resource Locator (URL). From
`hello-browser.html`, it identifies the neighboring `hello-browser.js` file. The
closing `</script>` tag is required even when the code lives in a separate file.

### Four files that answer four different questions

The Week 4 folder contains two deliberately small orientation programs and one
integrated Campus Hub program. The files are not duplicate versions of the same
page. Each file has one responsibility, one execution host, and one place where
its result becomes visible.

`hello.js` is the smallest **Node.js entry file**. Node.js reads it directly when
you type `node labs/week-04/hello.js`; no browser and no HTML document is
involved. Its messages appear in the terminal. We use this file first because it
isolates the language from browser loading, page structure, and the DOM.

`hello-browser.html` is the smallest **browser entry document**. It is the URL
the browser requests and the document the browser displays. Near the end of its
body, its `script` element requests `hello-browser.js`.

`hello-browser.js` is the corresponding **browser JavaScript source file**. It
calculates the same kind of simple values as `hello.js`, but it executes inside
the browser host and writes its evidence to Developer Tools > Console. Visiting
the `.js` URL by itself only displays or downloads source text; it does not create
the HTML page that gives the script a document context.

`index.html` is the **full Week 4 Campus Hub laboratory page**. It is not needed
for the two-message orientation exercise. It loads `events.js` as an ECMAScript
module, provides the visible `#program-output` element, and becomes the browser
interface for the event calculations developed throughout the laboratory.
`events.js` exports reusable domain functions so the browser page and automated
tests can use the same calculations.

Table 4.4 makes the two learning tracks explicit. A command is typed in the
terminal; a URL is entered in the browser address bar. Do not type a URL into
PowerShell, and do not type a Node.js command into the browser.

**Table 4.4 - Responsibilities of the Week 4 entry and source files**

| File | Role and host | How it starts | Where to observe the result | Direct dependency |
|---|---|---|---|---|
| `hello.js` | Minimal Node.js entry file | `node labs/week-04/hello.js` | Terminal | None |
| `hello-browser.html` | Minimal browser entry document | Visit `/hello-browser.html` through the local server | Visible heading plus Network evidence | Requests `hello-browser.js` |
| `hello-browser.js` | Minimal browser program | Loaded by the preceding `script` element | Developer Tools > Console | Uses the browser's `console` |
| `index.html` | Complete Week 4 Campus Hub laboratory page | Visit `/` through the local server | Page, Console, and Network | Imports `events.js` |
| `events.js` | Reusable event data and JavaScript module | Loaded by `index.html` and imported by tests | `#program-output`, Console, and test report | Exports event functions |

The browser pair still illustrates an important separation. `hello-browser.html` is the document
the browser displays. It gives the page its structure and meaning: headings,
paragraphs, links, and the place where the browser may load a program. It can be
opened and read as a document even when JavaScript is disabled.

`hello-browser.js` is a JavaScript source file. It contains instructions for the
JavaScript engine, such as calculating `2 + 3` and writing messages with
`console.log()`. It is not a second page and it is not HTML. The browser does not
execute it merely because both files are in the same folder; the `script` element
creates the explicit relationship.

Keeping the files separate gives each one a clear responsibility. HTML describes
the document, CSS describes presentation, and JavaScript describes computation
and interaction. The same JavaScript file can serve several pages, the HTML can
remain meaningful when the script fails, and each file can be tested and edited
without hiding one language inside another. In a larger application this
separation also makes the Network panel, source control history, and error
messages easier to interpret.

The browser follows the path in Figure 4.3. It first receives the HTML document,
discovers the script reference while parsing it, requests the JavaScript file,
and only then executes the source. If the HTML request succeeds but the script
request returns `404`, the page can still appear while the Console remains empty.
That is why the two files must be debugged separately: inspect the HTML request
and the script request in Network, then inspect execution messages in Console.

Start the local server from the repository root.

```text
npm run serve:week04
```

Leave that terminal open. When it prints a line containing
`http://localhost:8000/`, the server is waiting for browser requests; the absence
of a new prompt is normal. Open a second terminal for later commands.

In the browser, visit
`http://localhost:8000/hello-browser.html`. Open Developer Tools with F12 or
Ctrl+Shift+I on Windows and Linux, or Command+Option+I on macOS. Select
**Console**. The two messages from the JavaScript file should appear there.

Figure 4.3 shows the path. The browser first requests the HyperText Markup
Language (HTML) document. After
parsing the `script` element, it makes a second request for the JavaScript file.
Only then can the JavaScript engine execute the source and write to the Console.
These requests happen in sequence; the HTML file does not physically contain the
external JavaScript file.

<!-- figure:browser-javascript-load-path -->

Figure 4.4 shows the broader Week 4 relationship as two labeled execution paths.
The upper path teaches the smallest browser loading cycle. The lower path is the
continuing application. Neither path replaces the Node.js-only `hello.js`
experiment.

<!-- figure:javascript-four-file-map -->

The Console is a developer evidence panel, not part of the visible web page.
Changing page content uses the DOM and begins in Chapter 5. For now, logging is a
controlled way to observe values without adding another new concept.

## 0.7 Read the first failures instead of starting over

An error message is a report about an attempted operation. Read it before
changing anything. Table 4.5 maps common observations to the first useful check.

**Table 4.5 - First-run symptoms, meanings, and next checks**

| Observation | Likely meaning | First check or repair |
|---|---|---|
| `'node' is not recognized` or `command not found` | The shell cannot find Node.js | Install Node.js, close all terminals, then open a new one and run `node --version` |
| `Cannot find module ...hello.js` | Node.js cannot find the named file at that path | Run `dir labs\week-04` on Windows or `ls labs/week-04`; compare spelling and current directory |
| npm reports `ENOENT` for `package.json` | npm searched the wrong directory | Run `dir package.json`; return to the repository root before the npm command |
| The server command prints no prompt afterward | The server is still running normally | Leave it open; use a second terminal for tests and Git |
| The browser says it cannot reach the site | No server is listening at that address and port | Read the server terminal; start the server and copy the printed URL exactly |
| The HTML appears but no Console message appears | The script was not loaded or did not execute | Save both files, reload, inspect Console, then inspect the Network request for `hello-browser.js` |
| Network shows `404` for the script | The requested URL does not match an available file | Compare `src`, capitalization, filename, and folder location |
| `SyntaxError` names a line | JavaScript could not parse the source | Inspect that line and the preceding line for a missing quote, bracket, parenthesis, or backtick |
| `EADDRINUSE` mentions port 8000 | Another process already owns the port | Return to the earlier server terminal or stop that process with Ctrl+C before restarting |

Do not respond to every failure by reinstalling software. Installation repairs a
missing tool; it does not repair a misspelled filename, unsaved source, wrong
directory, or syntax error. Diagnose the boundary named by the evidence.

---

# 1. A program is an ordered explanation for a machine

The Campus Hub page already contains information and presentation, but HTML and
Cascading Style Sheets (CSS) do not calculate how many seats remain. A program supplies an ordered set of
instructions and decisions. Given capacity `80` and registrations `62`, it can
evaluate `80 - 62`, name the result, classify the event as open, and produce a
summary.

```js
const capacity = 80;
const registered = 62;
const remaining = capacity - registered;

console.log(remaining);
```

The expected console output is the number `18`. The code is source text; `18` is
runtime evidence. A semicolon ends each declaration here. JavaScript can insert
some omitted semicolons, but this course writes them consistently so statement
boundaries remain visible to beginners.

Figure 4.5 separates the language from two environments that can execute it.
Both environments understand subtraction, bindings, arrays, and functions. A
browser additionally supplies `document`, while Node.js supplies objects such as
`process`. Neither host object is part of the core language.

<!-- figure:javascript-host-boundary -->

## 1.1 ECMAScript and JavaScript

ECMAScript is the standardized language specification. JavaScript is the name
used for implementations of that language together with the surrounding
platform in which code runs. The standard defines values, operators, statements,
functions, objects, and built-in facilities. HTML, the DOM, browser storage, and
Node.js file access come from hosts and are studied at the appropriate boundary.

## 1.2 Your first file, from an exact directory

The first program proved that one file can execute. We now move to the continuing
Campus Hub example. In your personal coursework repository, open
`labs/week-04/events.js` in Visual Studio Code. From a terminal whose current
directory contains `package.json`, run:

```text
npm run serve:week04
```

Keep that terminal open; it is the server terminal. Visit
`http://localhost:8000/`, open Developer Tools, and select **Console**. The
starter prints a table of three event objects. If the page does not load, first
inspect the server terminal. If the page loads but the table is absent, inspect
the Console and Network panels for a failed `events.js` request or a JavaScript
error.

## 1.3 Execution order, comments, and case sensitivity

For the synchronous programs in this chapter, JavaScript normally evaluates
statements from top to bottom. A later statement can use a binding created by an
earlier declaration. Moving `console.log(sum)` above `const sum = 2 + 3` causes
an error because the program tries to read the binding before initialization.
Asynchronous work changes the timing model and is introduced in Chapter 6.

JavaScript is case-sensitive. `eventTitle`, `eventtitle`, and `EventTitle` are
three different names. Choose one spelling and capitalization, then use it
consistently. Course code uses lower camel case for variables and functions: the
first word begins in lowercase and each later word begins with a capital, as in
`seatsRemaining`.

Comments explain intent that the code itself cannot express clearly.

```js
// One-line comment: registration cannot create a negative seat count.
const remaining = Math.max(0, capacity - registered);

/* A block comment can span
   more than one source line. */
```

The engine ignores comments, but a comment is not a place to preserve obsolete
code. Git already records history. Prefer a meaningful name and a clear function
over a comment that merely translates syntax into English.

---

# 2. Values have types; bindings have names

A **value** is data the program can work with. A **type** describes the operations
and behavior associated with a value. JavaScript has seven primitive types:
string, number, bigint, boolean, undefined, symbol, and null. Everything else is
an object; arrays and functions are specialized objects.

JavaScript is dynamically typed. The value has a type at runtime; a variable
declaration does not permanently acquire one type from its name. A `let` binding
can therefore refer to a number and later to a string. That flexibility does not
make the two values interchangeable. Reliable programs keep a stable meaning for
each binding and validate data when it crosses a boundary.

A value written directly in source, such as `18`, `true`, or `"open"`, is a
**literal**. A program can also obtain values by evaluating expressions, reading
input, calling functions, or receiving network data. The same displayed text can
hide different types: the number `18` can be added numerically, while the string
`"18"` is text until deliberately converted.

To read an expression, first identify the value of each piece, then apply the
operator. In `"18" + 2`, the left operand is text, so `+` joins text and produces
`"182"`. In `18 + 2`, both operands are numbers and the result is `20`. The
characters look similar when printed, but the values have different types and
therefore different behavior. This is why input from a text field should be
converted and checked before arithmetic.

Table 4.6 collects the value categories used in this chapter. The examples are
values, while the final column explains the boundary that matters in programs.

**Table 4.6 - JavaScript values introduced in this chapter**

| Type | Example | Purpose and important boundary |
|---|---|---|
| String | `"Robotics night"` | Text; strings are immutable sequences |
| Number | `18`, `2.5`, `NaN`, `Infinity` | Floating-point numeric values; integers share this type |
| BigInt | `9007199254740993n` | Integers beyond safe Number precision; cannot be mixed directly with Number arithmetic |
| Boolean | `true`, `false` | Logical outcomes used by conditions |
| Undefined | `undefined` | Commonly means no value has been supplied or produced |
| Null | `null` | An intentional absence chosen by the program or data contract |
| Symbol | `Symbol("id")` | A unique primitive key; important later, uncommon in beginner application data |
| Object | `{ title: "Robotics night" }` | A mutable collection of keyed properties |

Use `typeof` as an observation tool, not as a complete theory of values.

```js
typeof "Robotics night"; // "string"
typeof 18;               // "number"
typeof true;             // "boolean"
typeof undefined;        // "undefined"
typeof null;             // "object" - a long-standing historical result
typeof [];               // "object"
typeof function () {};   // "function"
```

Use `Array.isArray(value)` to distinguish arrays from other objects. Test for
`null` directly with `value === null`; do not infer that `null` is an ordinary
object from the historical `typeof` result.

## 2.1 Expressions produce values

An expression can be evaluated to produce a value. `capacity - registered`,
`event.title`, and `seatsRemaining(event)` are expressions. A statement performs
an action in the program's execution, such as declaring a binding or choosing an
`if` branch. Figure 4.6 traces tokens through evaluation and assignment.

<!-- figure:javascript-evaluation -->

Evaluation works from smaller expressions toward a result. In
`capacity - registered`, JavaScript first reads the two operand values and then
applies subtraction. Parentheses make grouping explicit. Prefer
`(registered / capacity) * 100` to relying on a reader to remember every
precedence rule. Parentheses do not turn a value into a function call unless they
follow a callable expression.

## 2.2 `const`, `let`, and the meaning of reassignment

A declaration creates a **binding**, which connects a name to a value.

```js
const eventTitle = "Robotics night";
let registered = 62;
registered = registered + 1;
```

A declaration contains a keyword, an identifier, an assignment operator, an
initializer expression, and normally a semicolon. An **identifier** is a legal
source name. It may contain letters, digits after the first character,
underscores, and dollar signs, but it cannot contain spaces or be a reserved word
such as `if`. Prefer names that express domain meaning; `remainingSeats` carries
more information than `x`.

Use `const` by default. It prevents the name from being assigned a different
value. Use `let` when reassignment is part of the algorithm, as with a counter.
This is a design signal rather than a claim that a `const` value is eternally
unchangeable. The question is whether the **binding** will point to a different
value. A counter needs `let`; a reference that remains connected to the same
array normally uses `const`, even if an array method later changes that array.

`const` does not freeze an object:

```js
const event = { registered: 62 };
event.registered = 63; // mutation is allowed
// event = {};         // rebinding would fail
```

The binding remains connected to the same object; a property inside that object
changed. Figure 4.12 later makes this distinction visible.

## 2.3 Why `var` exists, how it behaves, and why modern code is cautious

Older JavaScript used `var` before `let` and `const` were added in ECMAScript
2015. You will encounter it in established applications, older books, interview
questions, and code copied from pre-2015 examples. A professional reader must
therefore understand `var`; avoiding it without understanding it leaves a real
language gap.

`var` is **function-scoped**, not block-scoped. An `if`, `for`, or ordinary
braced block does not contain the binding:

```js
function demonstrateVarScope() {
  if (true) {
    var message = "visible throughout this function";
  }
  console.log(message);
}

demonstrateVarScope();
// visible throughout this function
```

Replace `var` with `let` in that example and the final read throws a
`ReferenceError`, because the `let` binding belongs to the `if` block. That
smaller scope usually matches the programmer's intention and prevents unrelated
code later in the function from reusing the name accidentally.

A `var` binding is created and initialized to `undefined` when its containing
function or script environment is prepared. Its initializer still runs at the
original source position. This behavior is commonly described as **hoisting**:

```js
console.log(status); // undefined
var status = "open";
console.log(status); // "open"
```

The engine does not physically rewrite the file. A useful mental model is
`var status;` during environment setup, followed later by
`status = "open";`. By contrast, a `let` or `const` binding is inaccessible in
its temporal dead zone until its declaration is evaluated. Reading it early
throws instead of silently supplying `undefined`.

`var` also permits repeated declarations in the same scope. That compatibility
behavior can hide a mistaken duplicate name. Table 4.7 compares the three
declaration forms. The rule for new course code remains concise: use `const` by
default, `let` for deliberate reassignment, and read `var` accurately when
maintaining legacy code.

**Table 4.7 - Binding declarations and the differences that affect reasoning**

| Form | Scope | Read before declaration is evaluated | Redeclaration in same scope | Ordinary course use |
|---|---|---|---|---|
| `const` | Block | `ReferenceError` in temporal dead zone | Rejected | Default when the binding is not reassigned |
| `let` | Block | `ReferenceError` in temporal dead zone | Rejected | Counters and other deliberate reassignment |
| `var` | Function or script | `undefined` before initializer | Permitted in many cases | Understand legacy code; avoid in new modules |

## 2.4 Strings and template literals

Single and double quotes create strings. Backticks create a template literal,
which can interpolate an expression inside `${...}`.

```js
const message = `${eventTitle}: ${remaining} seats remaining`;
```

Interpolation converts the embedded result to text. It is clearer than a long
chain of `+` operations, where the same operator can mean numeric addition or
string concatenation.

Strings are immutable: operations produce new strings rather than changing the
characters inside an existing string. `message.length` reports the number of
UTF-16 code units, and `message[0]` reads the first one because indexes begin at
zero. Escape sequences represent characters that would otherwise end or disrupt
a literal: `"Line one\nLine two"` contains a newline, and `"She said \"hello\""`
contains quotation marks. Template literals can span lines, but preserve those
line breaks in the resulting string.

Common string operations return new strings. `trim()` removes whitespace at
the two ends, `toLowerCase()` changes letter case according to the method's
rules, `includes()` tests whether a substring occurs, and `slice(start, end)`
copies a range whose ending position is excluded. None modifies the original
string.

```js
const rawCategory = "  TECHNOLOGY  ";
const category = rawCategory.trim().toLowerCase();
console.log(category, category.includes("tech"));
```

Output:

```text
technology true
```

The original `rawCategory` still contains its spaces and uppercase letters.
This matters when normalizing user input: keep the received value if it is
needed for display or auditing, and use the normalized value for comparison.

---

# 3. Operators create relationships

Arithmetic operators include `+`, `-`, `*`, `/`, `%`, and `**`. Comparison
operators such as `<`, `<=`, `>`, and `>=` produce booleans. Use strict equality
`===` and strict inequality `!==` for ordinary application comparisons.

An operator receives one, two, or sometimes three operands. The unary `-` in
`-capacity` has one operand; `capacity - registered` has two. Assignment `=`
stores a value in a binding or property. Equality `===` asks a question and
produces a boolean. Confusing these roles can change program state instead of
testing it.

```js
18 === 18;    // true
18 === "18";  // false
18 == "18";   // true because loose equality converts a value
```

Loose equality is governed by defined coercion rules, not randomness, but those
rules add reasoning that most application comparisons do not need. This course
uses strict equality unless a specific algorithm deliberately requires another
sameness relation.

## 3.1 Conversion must be visible

Data from form controls and URL parameters commonly arrives as strings.

```js
const enteredCapacity = "80";
const capacity = Number(enteredCapacity);

if (!Number.isFinite(capacity)) {
  throw new TypeError("Capacity must be a finite number.");
}
```

`Number()` makes the conversion explicit. `Number.isFinite()` rejects `NaN` and
infinities. Remember that `NaN === NaN` is false; use `Number.isNaN()` when that
specific test is required.

Conversion can succeed syntactically while producing an unusable number.
`Number("")` produces `0`, while `Number("eighty")` produces `NaN`, whose name
means “Not a Number.” Validate the original input when an empty value must be
rejected, then validate the converted result. `parseInt()` and `parseFloat()`
accept numeric prefixes such as the `12` in `"12 seats"`; use them only when that
prefix behavior is part of the input contract, not as a general repair for bad
data.

## 3.2 Truthiness and short-circuiting

Conditions convert their expression to a boolean. `false`, `0`, `-0`, `0n`, an
empty string, `null`, `undefined`, and `NaN` are falsy. Objects and arrays are
truthy, including an empty array.

`&&` stops at the first falsy operand; `||` stops at the first truthy operand;
`??` uses the right operand only when the left is `null` or `undefined`.

```js
const label = suppliedLabel ?? "Untitled event";
```

Use `??` when `0`, `false`, or an empty string may be valid data. Using `||` in
that situation can replace a meaningful value accidentally.

## 3.3 Precedence, grouping, assignment, and the conditional operator

Operator precedence determines which operations bind first; associativity
resolves repeated operators at the same precedence. These are language rules,
not an invitation to write puzzles. Use parentheses whenever grouping is central
to the reader's reasoning.

```js
const percent = (registered / capacity) * 100;
const label = remaining === 0 ? "full" : "spaces available";
```

The conditional `condition ? whenTrue : whenFalse` operator is an expression and
therefore produces a value. Use it for one compact two-way choice. Prefer an
`if...else` statement when branches contain several statements, require distinct
side effects, or become difficult to scan.

Compound assignment such as `registered += 1` reads, calculates, and writes the
same binding. Prefix and postfix increment both add one, but they produce
different expression values; use a standalone `index += 1` when the produced
value is irrelevant. Bitwise operators convert numbers to fixed-width integer
representations and are valuable for masks and low-level protocols, but they are
not substitutes for ordinary boolean operators in Campus Hub application logic.

---

# 4. Control flow chooses and repeats work

An `if` statement selects a branch. Only one branch in the following chain runs.

```js
if (remaining === 0) {
  status = "full";
} else if (remaining <= 10) {
  status = "almost full";
} else {
  status = "open";
}
```

Figure 4.7 is a decision flow, not three independent tests. Once one condition
succeeds, execution skips the remaining branches and continues after the chain.

The expression inside `if (...)` is the condition. The braces delimit a block.
Indentation does not control execution, but it exposes the block structure to
human readers and should match the braces. Trace a branch by writing the current
input, the boolean result of each condition actually reached, the selected
branch, and the value after the chain. This prevents guessing from the final line
alone.

<!-- figure:javascript-control-flow -->

## 4.1 `switch` and the conditional operator serve narrower choices

A `switch` compares one expression against `case` values using strict comparison.
It is useful when several branches classify the same value. Execution continues
into following cases unless `break`, `return`, or `throw` ends the case, so
accidental fall-through is a common defect.

```js
switch (event.category) {
  case "technology":
    track = "engineering";
    break;
  case "arts":
    track = "culture";
    break;
  default:
    track = "community";
}
```

Deliberate fall-through should be rare and documented. An object or `Map` lookup
may communicate a stable value-to-value mapping more directly. Use the ternary
operator from Section 3.3 for one small two-way value choice, not for a deeply
nested decision tree.

## 4.2 A loop needs state, a condition, progress, and an exit

A loop repeats a statement or block, but repetition alone is not a sufficient
design. Before writing one, name four things:

1. the state that determines what remains to be done;
2. the condition that permits another iteration;
3. the progress step that changes the relevant state; and
4. the reason execution must eventually leave the loop.

If the condition never becomes false and no reachable `break` executes, the
program has an **infinite loop**. In a browser, an infinite synchronous loop can
prevent painting and interaction because the current JavaScript task never
returns control to the host. During development, stop the responsible process or
browser tab, then repair the progress argument rather than merely increasing a
limit.

Table 4.8 selects among the loop forms by the information the algorithm needs.
Figure 4.7's lower path shows the same decision: value, index, pre-test condition,
post-test condition, or object property key.

A loop should be chosen after the work has been stated in plain language. If the
task is “perform one action for each value,” iterate values. If the task is “look
at position 0, then 1, then 2,” an indexed loop makes position explicit. If the
task is “repeat while a changing condition remains true,” use a pre-test loop.
If one attempt must happen before asking whether to repeat, use the post-test
form. These choices are about the algorithm's question, not personal taste.

The following example computes the total capacity. Read the trace before running
the code; each row is one completed iteration.

```js
const capacities = [80, 120, 40];
let index = 0;
let total = 0;

while (index < capacities.length) {
  total += capacities[index];
  index += 1;
}
console.log(total);
```

| Check | `index` | `total` before body | Added value | `index` after update |
|---|---:|---:|---:|---:|
| 1 | 0 | 0 | 80 | 1 |
| 2 | 1 | 80 | 120 | 2 |
| 3 | 2 | 200 | 40 | 3 |
| Stop | 3 | 240 | body skipped because `3 < 3` is false | 3 |

Expected console output: `240`. If the update is removed, `index` stays at zero
and the condition never changes. If the condition is changed to `index <=
capacities.length`, the body eventually reads `capacities[3]`, which is
`undefined`; adding it makes `total` become `NaN`. A trace table helps locate
both errors before a long program is involved.

**Table 4.8 - JavaScript loop forms and the questions they answer**

| Form | Best question | Condition timing | Value produced directly? | Important caution |
|---|---|---|---|---|
| `for...of` | “What should happen for every value in this iterable?” | Iterator decides whether another value exists | No | Does not supply the numeric index automatically |
| `for` | “What should happen at each controlled index or counter value?” | Before every iteration | No | Keep initialization, condition, and update consistent |
| `while` | “Should work continue while this changing condition is true?” | Before every iteration | No | Body may execute zero times |
| `do...while` | “Must the body run once before continuation is tested?” | After every iteration | No | Body always executes at least once |
| `for...in` | “What enumerable property keys does this object expose?” | Property enumeration | No | Do not use it as an array-value loop |
| Array method | “Am I transforming, selecting, finding, testing, or accumulating values?” | Method controls visitation | Often | Callback result and source mutation contract must be understood |

## 4.3 `for...of` visits values from an iterable

Use `for...of` when you need each value from an array, string, `Map`, `Set`, or
another iterable and the position is not the main concern.

```js
for (const event of events) {
  console.log(event.title);
}
```

On each iteration, `event` is a new block-scoped binding connected to the next
array value. With three events, the body runs three times. The loop does not
create a result array; it performs the statements in its body. If the goal is to
construct one new value per element, `map()` in Section 6.4 usually states that
result more directly.

When both value and position are needed, use `entries()` and destructuring:

```js
for (const [index, event] of events.entries()) {
  console.log(`${index}: ${event.title}`);
}
```

Expected output:

```text
0: Robotics night
1: Campus orchestra
2: Sustainable gardens
```

Each `entries()` item is a two-element array containing the index followed by
the value. The iteration protocol asks the array iterator for the next pair;
`for...of` does not inspect arbitrary properties. This is why it is safe for
ordinary value traversal and why `for...in` has a different purpose.

## 4.4 A counted `for` loop exposes index control

A counted loop places initialization, continuation condition, and update in one
header.

```js
for (let index = 0; index < events.length; index += 1) {
  console.log(index, events[index].title);
}
```

`let index = 0` runs once. Before each iteration, `index < events.length` is
tested. After each completed body, `index += 1` runs. Replacing `<` with `<=`
would permit `index === events.length`, one position beyond the final valid
index. This is the classic **off-by-one error**.

The three header positions have distinct jobs. Initialization runs once before
the first test. The condition is checked before each pass. The update runs after
a normally completed body and also after a `continue`; `break` exits before the
update, and `return` exits the containing function. Knowing this order makes
control flow predictable.

```js
for (let index = 0; index < events.length; index += 1) {
  if (events[index].registered === events[index].capacity) continue;
  console.log(events[index].title);
}
```

Expected output:

```text
Robotics night
Sustainable gardens
```

The full event is skipped, then the `for` update still advances `index`. A
common beginner mistake is to write the update only in the non-skipped path,
which can leave the loop examining the same full event forever. Keep the progress
step in the header when possible so every path reaches it.

The three header fields are optional, so `for (;;) { ... }` is syntactically an
infinite loop. Omission should be deliberate and accompanied by an evident exit;
ordinary course code writes the controlling state explicitly.

## 4.5 `while` and `do...while` place the first test differently

Use `while` when the body may not need to run at all:

```js
let seconds = 3;
while (seconds > 0) {
  console.log(seconds);
  seconds -= 1;
}
// 3
// 2
// 1
```

Use `do...while` when one attempt must occur before deciding whether another is
needed. A command-line prompt is a familiar model, although browser form events
usually replace such synchronous prompting in web applications.

```js
let attempt = 0;
do {
  attempt += 1;
  console.log(`attempt ${attempt}`);
} while (attempt < 1);
// attempt 1
```

The post-test form is not automatically better for validation. Choose it only
when “run once before testing” is a true requirement.

## 4.6 `break`, `continue`, nesting, and labels change the ordinary path

`break` exits the nearest loop. `continue` abandons the remainder of the current
iteration and proceeds to the next one. They are useful when they make an exit
or skip condition clearer, but many scattered jumps can obscure the progress
argument.

```js
for (const event of events) {
  if (event.registered >= event.capacity) continue;
  console.log(`${event.title} accepts registrations`);
}
```

Nested loops run the inner loop for each outer iteration. A label can make
`break` or `continue` target an enclosing loop, but labeled control flow is rare
in application code; extracting a function or returning an answer is often
clearer. State the total work before nesting: two loops of lengths `m` and `n`
may execute the inner body `m × n` times.

## 4.7 `for...in` visits property keys, not array values

`for...in` enumerates string property keys. It is appropriate only when that is
the intended object operation, normally combined with an own-property check.

```js
const event = { title: "Robotics night", capacity: 80 };
for (const key in event) {
  if (Object.hasOwn(event, key)) console.log(key, event[key]);
}
```

Do not use `for...in` as an array-value loop. It yields keys such as `"0"`, can
include additional enumerable properties, and does not express the intended
value iteration. Use `for...of` for values, `entries()` when both index and value
matter, or a named array method when the operation has a result shape.

---

# 5. Functions give a calculation a name and boundary

A function receives inputs through parameters and can return an output.

```js
function seatsRemaining(event) {
  return Math.max(0, event.capacity - event.registered);
}

const remaining = seatsRemaining(events[0]);
```

Defining a function does not run its body. The body runs when a call expression
uses parentheses. For the call above, JavaScript evaluates `events[0]`, creates
the local parameter binding `event`, executes the body, evaluates the return
expression, ends the call, and places the returned number into the surrounding
declaration.

`event` is a parameter in the declaration. `events[0]` is the argument supplied
by this call. `return` ends the call and sends one value to the calling
expression. If execution reaches the end without `return`, the result is
`undefined`.

Figure 4.8 shows one call frame and the broader function contract. Arguments flow
in, parameters name them locally, the body performs work, and either a return
value or a thrown exception crosses the boundary back to the caller.

<!-- figure:function-call-boundary -->

## 5.1 Parameters describe inputs; arguments supply values

A function may declare zero or more parameters. JavaScript does not reject a
call merely because its argument count differs. Missing arguments become
`undefined`; extra arguments are evaluated but are not connected to named
parameters unless the function reads a rest parameter or the legacy
array-like `arguments` object.

```js
function labelEvent(title, prefix = "Event") {
  return `${prefix}: ${title}`;
}

labelEvent("Robotics night");              // "Event: Robotics night"
labelEvent("Robotics night", "Featured"); // "Featured: Robotics night"
labelEvent();                              // "Event: undefined"
```

A default parameter is used when the argument is omitted or explicitly
`undefined`, not when it is `null`, `false`, `0`, or an empty string. Required
domain inputs still need validation; a default is not a substitute for an input
contract.

A rest parameter collects remaining arguments into a real array. It must be the
last parameter and only one rest parameter may appear.

```js
function sum(...values) {
  return values.reduce((total, value) => total + value, 0);
}

sum(4, 8, 15, 16); // 43
```

Destructured parameters name required object fields at the boundary, but an
entirely missing argument still causes destructuring to fail unless a default
object is supplied. Use this form when it makes the accepted shape clearer, not
to conceal that validation is absent.

```js
function eventLabel({ title, category = "general" }) {
  return `${title} [${category}]`;
}
```

For a beginner, it helps to trace the call in two columns. In
`eventLabel({ title: "Robotics night" })`, the argument is an object; the
parameter pattern selects its `title` property and creates a local name called
`title`; because `category` is absent, its default becomes `"general"`. The
returned string is `"Robotics night [general]"`. Destructuring changes how
parameters are named; it does not validate the object's full shape or make an
absent required argument safe.

## 5.2 A call returns one JavaScript value

JavaScript functions do not declare a fixed runtime return type in their syntax.
One call may technically return a number and another a string, but a dependable
function contract keeps the result shape consistent so callers do not need to
guess. TypeScript adds static return-type checking later in Chapter 7; runtime
JavaScript remains responsible for actual input validation.

The returned value can be any JavaScript value:

- a primitive such as a number, string, boolean, `null`, or `undefined`;
- an object, array, function, `Map`, or `Set`;
- a promise representing later completion, developed in Chapter 6; or
- one object or array that groups several logical results.

```js
function eventMetrics(event) {
  const remaining = Math.max(0, event.capacity - event.registered);
  const percentFull = Math.round((event.registered / event.capacity) * 100);
  return { remaining, percentFull };
}

const { remaining, percentFull } = eventMetrics(events[0]);
```

A call returns exactly one value here: one object containing two named
properties. Destructuring at the call site extracts the two logical results.
Returning an array is appropriate when positions have stable meaning; an object
is usually clearer when the results have names.

Read `return` as a boundary crossing. Before it, values are local to the active
call. At `return`, the current call ends and its expression becomes the value of
the call at the place where it was written. If there is no expression, the
result is `undefined`; `console.log()` displays a value but does not return the
displayed value.

```js
function printStatus(status) {
  console.log(status);
}

const result = printStatus("open");
console.log(result);
```

Output:

```text
open
undefined
```

The first line is the side effect of logging. The second line shows the
function's return value. This difference is essential when composing functions:
printing a result is not the same as returning data for another calculation.

An early return ends the current call immediately. Guard clauses use this to
reject or finish a special case before the main path becomes deeply nested.

```js
function eventStatus(event) {
  const remaining = seatsRemaining(event);
  if (remaining === 0) return "full";
  if (remaining <= 10) return "almost full";
  return "open";
}
```

`return;` with no expression returns `undefined`. Falling off the end does the
same. A thrown exception is not a second kind of return value: it abruptly exits
the normal call path and searches outward for a matching `catch`.

## 5.3 Function calls take several important forms

Parentheses after a callable expression form a call, but the expression before
the parentheses affects `this`, construction, and dependency flow. Table 4.9
distinguishes the forms students will meet across this book.

**Table 4.9 - Common function call forms and their meaning**

| Call form | Example | What it means |
|---|---|---|
| Direct call | `seatsRemaining(event)` | Call a function value; module code normally has `this === undefined` |
| Method call | `registry.add(event)` | Call a property with `registry` as the receiver used for `this` |
| Constructor call | `new EventModel(data)` | Create an object, connect its prototype, and call a constructable function with that object as `this` |
| Callback invocation | `events.map(summarizeEvent)` | Another operation decides when and with which arguments to call the function |
| Indirect call | `report.call(registry, event)` | Call with an explicit `this`; `apply()` accepts the arguments in an array-like value |
| Bound call | `const reportHere = report.bind(registry)` | Create a new function with fixed `this` and optional leading arguments |
| Recursive call | `walk(node.children)` from inside `walk` | A function calls itself on a smaller problem; every unfinished call occupies a stack frame |
| Immediately invoked expression | `(function () { ... })()` | Create and call a function expression immediately; modules now replace many historical uses |

Do not use `new` with arrow functions; they are not constructors. Do not detach a
method that depends on `this` unless you preserve or replace the receiver. Section
11 develops these call-site rules after the call-stack and closure model is in
place.

## 5.4 Declarations, expressions, and arrow functions

JavaScript provides several function forms.

```js
function double(value) { return value * 2; }
const doubleAgain = function (value) { return value * 2; };
const doubleBriefly = (value) => value * 2;
```

They are not interchangeable in every advanced situation: `this`, construction,
and hoisting differ. For this chapter, use function declarations for named domain
operations and short arrow functions for callbacks such as array transformations.

A function should have a clear contract: accepted inputs, returned result,
possible error, and observable side effects. A **pure function** returns the same
result for the same inputs and does not change external state. Purity is not a
requirement for every operation, but calculation functions such as
`seatsRemaining()` are easier to reason about and test when they remain pure.

## 5.5 Scope answers where a name is available

JavaScript uses lexical scope: availability follows the nesting of source blocks
and functions. A binding declared with `let` or `const` inside `{ ... }` is not
available outside that block. A function can read bindings in surrounding scopes,
but callers cannot read its local bindings.

```js
const course = "Web Programming";

function describeEvent(event) {
  const remaining = seatsRemaining(event);
  return `${course}: ${event.title} has ${remaining} seats`;
}
```

Keep data local and pass needed inputs explicitly. Excessive global state makes
functions depend on invisible context and makes tests interfere with one another.

## 5.6 Side effects, pure calculations, and command-query separation

A function has a **side effect** when it changes observable state beyond its
returned value: logging, changing an object, writing a file, updating the DOM, or
sending a request. Side effects are necessary, but mixing them into every
calculation makes tests and reuse harder.

Prefer a calculation that returns data and a thin boundary function that performs
the effect. `summarizeEvents()` can return summary objects; a browser adapter can
render them. This is sometimes described as separating a **query**, which answers
a question, from a **command**, which changes state. JavaScript does not enforce
that design, but the distinction makes inputs, outputs, and failures easier to
explain.

---

# 6. Arrays model ordered collections

An array stores an ordered sequence of values in one object. Use an array when
position and iteration order are part of the data model: the first event in a
schedule, the next search result, or every category selected by a user. An
array is not merely “several variables.” It supplies one collection identity,
a `length` property, numeric index access, iteration, and methods that can search,
select, transform, copy, or mutate the sequence.

Indexes begin at zero. Figure 4.9 places each index directly above the value it
selects. With three elements, `length` is `3`, but the last valid index is `2`.
The general expression for the last index of a non-empty array is therefore
`array.length - 1`.

```js
const categories = ["technology", "arts", "community"];
categories[0];     // "technology"
categories[1];     // "arts"
categories[categories.length - 1]; // "community"
categories.length; // 3
```

<!-- figure:javascript-array-indexes -->

The brackets in `categories[1]` are an index access expression. JavaScript first
evaluates the expression between the brackets, obtains the property key `1`, and
then reads that property from the array. Reading `categories[3]` produces
`undefined`; it does not wrap to the beginning and it does not throw by itself.
That quiet result is why an off-by-one loop can continue until later code tries
to use a property of `undefined`.

`length` is one greater than the highest ordinary sequential index in a dense
array. The first item is index `0`, the second is `1`, and the last is
`array.length - 1`. Arrays can technically mix value types, but application data
is easier to validate when one array has one clear element shape, such as “event
objects.” Use `Array.isArray(value)` at an untrusted boundary because
`typeof value` reports `"object"` for both arrays and ordinary objects.

## 6.1 Dense arrays, missing elements, and intentional absence

A **dense array** has a value at every index from `0` through `length - 1`. A
**sparse array** contains a missing index, sometimes called a hole. A hole is not
the same observation as an index that explicitly stores `undefined`: both read
as `undefined`, but iteration methods may skip holes and `index in array`
distinguishes them.

```js
const sparse = ["technology", , "community"];
1 in sparse;       // false: index 1 is absent

const explicit = ["technology", undefined, "community"];
1 in explicit;     // true: index 1 exists and stores undefined
```

Ordinary application code should create dense arrays. Do not use `delete
categories[1]`; it leaves a hole without closing the sequence. Use a deliberate
copying or mutating operation according to the required contract.

The difference can be observed directly:

```js
const hole = ["A", , "C"];
const storedUndefined = ["A", undefined, "C"];
console.log(1 in hole, 1 in storedUndefined);
console.log(hole.map((value) => value ?? "?"));
console.log(storedUndefined.map((value) => value ?? "?"));
```

Output:

```text
false true
["A", <empty>, "C"]
["A", "?", "C"]
```

Several array iteration methods skip a hole because no element exists at that
index. An explicit `undefined` is an element and reaches the callback. Sparse
arrays are therefore a poor representation for “not yet known”; use an explicit
sentinel such as `null` or a separate status field when the application needs to
represent missing information.

## 6.2 Mutation and copying are different contracts

Some array methods change the existing array object. Others return a new array.
That distinction matters whenever another function or binding can observe the
original identity. Table 4.10 groups common methods by their effect rather than
asking students to memorize an alphabetical list.

**Table 4.10 - Common array operations, results, and mutation behavior**

| Operation | Main purpose | Return value | Changes the source array? |
|---|---|---|---|
| `push(value)` / `pop()` | Add/remove at the end | New length / removed value | Yes |
| `unshift(value)` / `shift()` | Add/remove at the beginning | New length / removed value | Yes; existing indexes move |
| `splice(start, count, ...items)` | Remove, replace, or insert within the array | Array of removed values | Yes |
| `sort(compare)` / `reverse()` | Reorder existing elements | The same array object | Yes |
| `slice(start, end)` | Copy a selected range; `end` is excluded | New array | No |
| `concat(...)` / `[...array]` | Make a shallow combined copy | New array | No |
| `toSpliced(...)` / `toSorted(compare)` / `toReversed()` | Copy with an edit or ordering change | New array | No |
| `with(index, value)` | Copy with one indexed replacement | New array | No |
| `at(index)` | Read by position; a negative index counts from the end | Element or `undefined` | No |
| `includes(value)` / `indexOf(value)` | Test membership / locate a value | Boolean / index or `-1` | No |
| `map(callback)` | Produce one result for every visited element | New array | No |
| `filter(callback)` | Keep elements whose callback is truthy | New array | No |
| `find(callback)` / `findIndex(callback)` | Locate the first matching value/index | Value or `undefined` / index or `-1` | No |
| `some(callback)` / `every(callback)` | Ask whether any/all elements pass | Boolean | No |
| `forEach(callback)` | Perform an effect for each visited element | `undefined` | No automatic source mutation |
| `flat(depth)` / `flatMap(callback)` | Flatten nested arrays / map once and flatten one level | New array | No |
| `reduce(callback, initial)` | Accumulate one result | Final accumulator | No automatic source mutation |

“Returns a new array” does not mean “deeply clones everything.” In
`const copy = [...events]`, the two arrays have different identities but their
corresponding event entries still refer to the same nested objects. Changing
`copy[0].registered` is therefore visible through `events[0]`. To replace one
event without modifying it, copy both levels that need independent identity:

```js
const revised = events.with(0, {
  ...events[0],
  registered: events[0].registered + 1,
});
```

## 6.3 Destructuring and spread make positions visible

Array destructuring connects positions to names. The rest element collects all
remaining values into a new array.

```js
const [firstCategory, secondCategory, ...otherCategories] = categories;
// firstCategory: "technology"
// secondCategory: "arts"
// otherCategories: ["community"]
```

Spread performs the opposite-looking operation in a new array literal: it
iterates a value and inserts its elements. `const all = [...core, ...optional]`
creates a new outer array. Both features are positional; object destructuring
in Section 7 is keyed by property name instead.

## 6.4 Transformations express intent

`filter()` selects elements, `map()` transforms each element, `find()` returns
the first matching element, and `some()` or `every()` answer boolean questions.

```js
const featuredTitles = events
  .filter((event) => event.featured)
  .map((event) => event.title);
```

The first callback returns a boolean; the second returns the new value for each
selected event. Both methods return new arrays. They do not deeply copy the
objects inside those arrays.

Figure 4.10 traces the pipeline. `filter()` may change the number of elements
but preserves the selected values. `map()` preserves the number of visited
elements but replaces each one with the callback result. The final array is a
collection of strings, not event objects.

<!-- figure:javascript-array-pipeline -->

The callback can receive `(element, index, array)`, but accept only the
parameters the calculation actually needs. The following two operations answer
different questions:

```js
const firstFullEvent = events.find((event) => event.registered >= event.capacity);
const fullEvents = events.filter((event) => event.registered >= event.capacity);
```

`find()` stops after the first match and returns one element or `undefined`.
`filter()` examines the collection and returns an array containing every match,
possibly an empty array. An empty array is truthy, so test its length when the
question is whether any results were selected.

Use `reduce()` when the operation is genuinely an accumulation and the accumulator
remains easy to name. A loop is preferable when it communicates the state change
more clearly to the intended reader.

```js
const totalCapacity = events.reduce(
  (total, event) => total + event.capacity,
  0,
);
```

The initial value `0` fixes the accumulator's intended type and defines the
result for an empty array. Omitting it makes the first element the accumulator
and causes an empty array to throw. A named loop is often clearer when the
accumulator contains several changing fields or when the body needs branching,
early exit, or detailed debugging evidence.

## 6.5 A practical array-manipulation walkthrough

The following sequence begins with one array and deliberately contrasts changes
to that array with operations that produce another array. Predict every line
before running it.

```js
const categories = ["technology", "arts", "community"];

categories.push("sports");
console.log(categories);
// ["technology", "arts", "community", "sports"]

const removed = categories.pop();
console.log(removed);    // "sports"
console.log(categories); // ["technology", "arts", "community"]

categories.splice(1, 1, "culture");
console.log(categories);
// ["technology", "culture", "community"]
```

`push()`, `pop()`, and `splice()` operate on the same array identity. `splice()`
starts at index `1`, removes one element, and inserts `"culture"` at that
position. Do not confuse it with `slice()`, which copies a range and does not
change its source.

When the source order or content must remain observable to another part of the
program, use a copying operation:

```js
const source = ["technology", "arts", "community"];
const replaced = source.with(1, "culture");
const alphabetic = source.toSorted((a, b) => a.localeCompare(b));

console.log(source);     // ["technology", "arts", "community"]
console.log(replaced);   // ["technology", "culture", "community"]
console.log(alphabetic); // ["arts", "community", "technology"]
```

Searching methods also have different result contracts. `includes()` returns a
boolean; `indexOf()` returns an index or `-1`; `find()` returns an element or
`undefined`; and `findIndex()` returns an index or `-1`. Test the documented
sentinel instead of relying on truthiness—index `0` is a valid match but is
falsy.

```js
categories.includes("culture");                 // true
categories.indexOf("culture");                  // 1
events.find((event) => event.registered === event.capacity)?.title;
// "Campus orchestra"
```

Figure 4.11 is an authentic browser capture of the tested evidence page in
`labs/week-04/language-evidence.html`. The three panels are produced from the
same functions verified by Node.js tests. Use it to compare loop traces,
function-result shapes, and array state before and after manipulation. The small
renderer uses the DOM only to display already-computed results; DOM programming
itself begins in Chapter 5.

<!-- media:week-04-language-evidence -->

---

# 7. Objects model named facts

An object literal groups properties that describe one entity.

```js
const event = {
  title: "Robotics night",
  capacity: 80,
  registered: 62,
};

event.title;
event["capacity"];
```

Use dot notation for a fixed property name and bracket notation when the name is
stored in a variable. The bracket expression is evaluated before lookup:

```js
const field = "capacity";
console.log(event.field);   // undefined: looks for a property literally named "field"
console.log(event[field]);  // 80: looks up the value of the field variable
```

The output is `undefined` on the first line and `80` on the second. This is a
common source of silent mistakes in dynamically generated forms and tables.
Prefer an explicit data shape and validate user-controlled keys before using
them to select or update properties.

Dot notation is concise when the property name is known in source code. Bracket
notation accepts an expression and is necessary for dynamic keys or names that
are not identifier syntax.

Reading a missing property normally produces `undefined`. Assigning a property
that does not yet exist creates it. These rules are convenient, but a misspelled
property such as `event.capcity` can therefore look like absent data rather than
an immediate syntax error. Validate required object shapes at boundaries and use
consistent names.

Destructuring extracts named properties, while object spread creates a shallow
copy with selected replacements.

```js
const { title, capacity } = event;
const updated = { ...event, registered: 63 };
```

## 7.1 Primitive copying and object identity

Primitive values are immutable. Object variables hold references to objects.

```js
const first = { registered: 62 };
const second = first;
second.registered = 63;
console.log(first.registered); // 63
```

Both bindings refer to the same object. Figure 4.12 contrasts that shared identity
with two separately copied number values. Spread creates a new outer object, but
nested objects remain shared unless copied deliberately.

<!-- figure:value-reference-identity -->

Optional chaining, as in `event.organizer?.email`, stops and produces `undefined`
when the value before `?.` is `null` or `undefined`. It does not validate that an
email is correct, and it should not hide a property that the program contract
requires.

## 7.2 Property existence, ownership, enumeration, and deletion are separate questions

An object may expose a property directly or inherit it through its prototype.
Those are different observations. Use the operation that matches the question:

```js
Object.hasOwn(event, "title"); // true when event itself owns title
"toString" in event;          // true because the prototype chain supplies it
event.subtitle === undefined; // true for an absent property or a stored undefined
```

`Object.hasOwn(object, key)` is the clearest ordinary test for an own property.
The `in` operator asks whether the key is available anywhere on the object or
its prototype chain. Reading and comparing with `undefined` cannot distinguish
absence from a property that deliberately stores `undefined`.

Enumeration also has a contract. `Object.keys(event)` returns the object's own,
enumerable string keys; `Object.values(event)` returns their values; and
`Object.entries(event)` returns `[key, value]` pairs that work naturally with
destructuring and `for...of`:

```js
for (const [key, value] of Object.entries(event)) {
  console.log(`${key}: ${value}`);
}
```

This loop does not promise a database schema or validate a received object. It
only visits the enumerable own properties that currently exist. When a fixed
shape is required, read and validate the named properties explicitly.

`delete event.subtitle` removes an own configurable property. It is not the same
as assigning `undefined`, which leaves the property present, and it should not be
used on array indexes because that creates a sparse array. `Object.freeze()`
prevents ordinary additions, removals, and assignments on one object, but the
freeze is shallow: nested objects remain mutable unless they are frozen too.
These operations are useful when their contracts are intentional; they are not
substitutes for designing a clear data model.

---

# 8. Errors are evidence, not verdicts

A syntax error means the source cannot be parsed as written. A reference error
often means a name is unavailable. A type error means an operation is unsuitable
for the received value. An assertion error means observed behavior disagreed with
a test expectation.

A logical error is different: the program runs but produces the wrong behavior,
such as reporting `18` occupied seats when the requirement asks for remaining
seats. Logical errors may produce no exception, so predictions, examples, and
tests matter. A stack trace is a sequence of active function calls reported with
an error; the first line in external library code is not necessarily the source
of the application defect.

Read an error from the first relevant frame of its stack, not only from the last
line. Record the error name, message, file, line, operation being attempted,
actual input, and expected contract. Figure 4.13 turns those observations into a
repeatable diagnosis path.

<!-- figure:javascript-debugging -->

Use a repeatable debugging record. Write the expected result before running the
program, record the actual result, locate the first operation where the two
diverge, and then test one explanation at a time. For example, if `"62" + 1`
prints `"621"`, inspect the input type before changing the arithmetic. Convert
the string at the boundary, validate the number, and rerun the same case. This
keeps a repair connected to evidence instead of relying on a guess.

Throw an `Error` object when a function cannot honor its contract.

```js
if (!Number.isFinite(event.capacity)) {
  throw new TypeError("Event capacity must be a finite number.");
}
```

Do not catch every error merely to suppress it. Catch an exception only where the
program can add context, recover, translate it into an appropriate boundary
response, or perform necessary cleanup. Otherwise allow it to remain visible
during development.

---

# 9. Small tests make behavior repeatable

A test supplies an input, observes a result, and compares it with an expectation.
Pure functions are especially testable because their return value depends on
explicit arguments rather than hidden page or network state.

```js
import test from "node:test";
import assert from "node:assert/strict";
import { seatsRemaining } from "./events.js";

test("calculates available seats", () => {
  const event = { capacity: 80, registered: 62 };
  assert.equal(seatsRemaining(event), 18);
});
```

`test(...)` registers a named case. The callback performs the case.
`assert.equal(actual, expected)` compares an observed value with the required
value using strict equality. When it fails, read the test name, actual value,
expected value, operator, and first relevant application frame. Do not change the
expected value merely to make the failure disappear; first decide whether the
implementation or the stated requirement is wrong.

Run the supplied Week 4 tests from the coursework repository root.

```text
npm test
```

A passing test is evidence for the tested examples, not proof that every possible
input is correct. Include normal cases, boundary cases, and invalid inputs. A test
name should state behavior, and a failure should make the disagreement easy to
locate.

For `seatsRemaining`, useful cases include an ordinary event, a sold-out event,
an event whose registration count exceeds capacity, and invalid nonnumeric
fields. The expected results might be `18`, `0`, `0`, and a clear exception.
Together they exercise the normal path, boundary, defensive rule, and contract
failure. Tests are executable examples of the requirement; they do not replace
the requirement itself.

---

# 10. Execution has preparation, calls, and returns

JavaScript does more than read a file one line at a time. Before evaluating a
script or module, the engine parses its source and checks whether the grammar is
valid. It then prepares bindings for the relevant scopes. During execution, each
function call receives an **execution context** containing its parameters, local
bindings, and connection to the surrounding lexical environment.

The **call stack** records which calls are active. The running script begins at
the bottom. Calling `summarizeEvents()` adds a frame; calling
`seatsRemaining()` from inside it adds another. A `return` removes the current
frame and sends its result to the previous one. Figure 4.14 shows this sequence.
Only the top frame executes at one instant in this synchronous example.

<!-- figure:javascript-call-stack-closure -->

This model explains a stack trace. The frames do not describe several errors;
they describe the route by which execution reached one reported failure. Start
with the first frame that belongs to your application, inspect its arguments and
locals, and then move outward only when the defect originates in a caller.

## 10.1 Declaration timing, hoisting, and the temporal dead zone

People sometimes say that declarations are "moved to the top." No source text is
physically moved. During scope preparation, JavaScript creates bindings before
the statements execute, but different declarations have different access rules.

**Table 4.11 - Declaration timing and the safe working rule**

| Declaration | Before its source declaration executes | Working rule |
|---|---|---|
| `const` | Binding exists but cannot be accessed; access throws `ReferenceError` | Declare before use and initialize once |
| `let` | Binding exists but cannot be accessed; access throws `ReferenceError` | Declare before use; reassign only when the algorithm requires it |
| Function declaration | Callable throughout its scope after successful parsing | Use for named domain operations |
| `var` | Binding exists with value `undefined`; function scoped | Read legacy code, but do not introduce it in course code |

The region from the start of a scope until a `let` or `const` declaration is
evaluated is called the **temporal dead zone (TDZ)**. The name describes an
access restriction, not elapsed clock time.

```js
console.log(status); // ReferenceError: cannot access before initialization
const status = "open";
```

Declaring a new binding with the same name inside a nested scope is
**shadowing**. It is legal when the meanings are truly local, but repeated
shadowing makes traces harder to read. Prefer distinct domain names when two
values have different roles.

## 10.2 Closures preserve lexical access

A function value carries access to the lexical environment in which it was
created. That combination is a **closure**. The preserved binding remains
available even after the outer function has returned.

```js
function createRegistrationCounter(initialCount = 0) {
  let count = initialCount;

  return function registerOne() {
    count += 1;
    return count;
  };
}

const register = createRegistrationCounter(62);
register(); // 63
register(); // 64
```

Each call to `createRegistrationCounter()` creates a separate `count` binding.
The returned function can update that binding, while code outside the closure
cannot assign it directly. Closures support private state, callbacks, event
handlers, and modules. They can also retain large objects longer than intended,
so long-lived closures should capture only the state they actually need.

---

# 11. Functions are values as well as procedures

JavaScript functions are objects and can be stored, returned, and supplied as
arguments. A **higher-order function** receives a function, returns one, or both.
Array methods such as `map()` are higher-order functions because they receive a
callback.

```js
function byRemainingSeats(left, right) {
  return seatsRemaining(left) - seatsRemaining(right);
}

const ordered = events.toSorted(byRemainingSeats);
```

The callback is passed as `byRemainingSeats`, without parentheses. Writing
`byRemainingSeats()` would call it immediately and pass its result instead.
`toSorted()` returns a new array; `sort()` changes the original array. Both use a
comparison function that must return a negative number, zero, or a positive
number. Returning only `true` or `false` does not define a complete ordering.

Default parameters apply when an argument is missing or explicitly
`undefined`. Rest parameters collect remaining arguments into an array.

```js
function totalRegistrations(...counts) {
  return counts.reduce((total, count) => total + count, 0);
}
```

Spread syntax looks similar but works at the call site: `totalRegistrations(...values)`
expands an iterable into separate arguments. Rest collects; spread expands.

## 11.1 Method calls and `this`

A function stored in an object property is commonly called a **method**. For an
ordinary method call, the value before the dot supplies `this`.

```js
const event = {
  title: "Robotics night",
  describe() {
    return `Event: ${this.title}`;
  },
};

event.describe(); // "Event: Robotics night"
```

`this` is determined by how an ordinary function is called, not by where its
source text appears. Detaching the method loses that call-site relationship.

```js
const describe = event.describe;
describe(); // TypeError in this module: this is undefined
```

Arrow functions do not create their own `this`; they close over the surrounding
one. That makes arrows useful for callbacks, but usually unsuitable for object
methods that need the receiving object. `call()`, `apply()`, and `bind()` can
select or permanently connect a `this` value, but explicit parameters are often
clearer for ordinary application calculations.

---

# 12. Objects delegate through prototypes

Every ordinary object has an internal prototype link to another object or to
`null`. When a requested property is absent from the object itself, JavaScript
continues the lookup through that **prototype chain**. Figure 4.15 shows lookup
as a sequence. The first matching property wins; reaching `null` produces
`undefined`.

<!-- figure:javascript-prototype-chain -->

```js
const eventMethods = {
  describe() {
    return `${this.title}: ${this.capacity} seats`;
  },
};

const event = Object.create(eventMethods);
event.title = "Robotics night";
event.capacity = 80;
event.describe();
```

`event` owns `title` and `capacity`; it inherits access to `describe`. Use
`Object.hasOwn(event, "title")` when the distinction between an own and inherited
property matters. Avoid trusting arbitrary inherited keys from unvalidated
input.

## 12.1 Classes provide familiar syntax over prototypes

The `class` syntax defines a constructor and prototype methods while preserving
JavaScript's prototype model.

```js
class CampusEvent {
  constructor({ title, capacity, registered = 0 }) {
    if (!title?.trim()) throw new TypeError("title is required");
    if (!Number.isFinite(capacity) || capacity <= 0) {
      throw new RangeError("capacity must be positive");
    }
    this.title = title.trim();
    this.capacity = capacity;
    this.registered = registered;
  }

  get remaining() {
    return Math.max(0, this.capacity - this.registered);
  }
}
```

Call a class with `new`. The constructor initializes one new instance; methods
are shared through the prototype. A getter such as `remaining` is read like a
property but runs code. Use a class when instances share behavior and must
maintain invariants. A plain object plus pure functions is often clearer for
records received from an API. Inheritance with `extends` can express a genuine
"is a" relationship, but composition is usually easier to change and test.

Private fields such as `#registrations` are enforced by the language and may be
useful for internal state. They are different from naming conventions that begin
with an underscore.

---

# 13. Choose a collection by the question it must answer

Arrays and objects are not the only standard collections. Choose from the
operations the program needs rather than from habit.

**Table 4.12 - Collection choices and their strongest use**

| Structure | Key or order model | Strong use | Important boundary |
|---|---|---|---|
| Array | Integer indexes in sequence | Ordered lists, transformation pipelines | Searching by arbitrary key is linear unless another index exists |
| Plain object | String or symbol property keys | A record with known field names | Inherits object behavior; validate external keys |
| `Map` | Keys of any value type, insertion ordered | Dynamic lookup table with frequent add, get, and delete | Convert deliberately before JSON serialization |
| `Set` | Unique values, insertion ordered | Membership and duplicate removal | Object uniqueness uses identity, not deep content equality |

```js
const eventByTitle = new Map(events.map((event) => [event.title, event]));
const categories = new Set(events.map((event) => event.category));

eventByTitle.get("Robotics night");
categories.has("technology");
```

`Map` and `Set` expose `size`, not `length`. Their keys and values are iterable,
so `for...of` and spread work with them. Objects expose enumerable own entries
through `Object.keys()`, `Object.values()`, and `Object.entries()`.

## 13.1 Iterables and iterators

An **iterable** can produce an iterator, normally through the well-known
`Symbol.iterator` method. Arrays, strings, maps, and sets are iterable. An
iterator's `next()` method returns objects shaped like `{ value, done }`.
Most application code should use `for...of`, spread, or collection methods
instead of operating an iterator manually, but the protocol explains why the
same syntax works across different collections.

Generators declared with `function*` can pause at `yield` and implement custom
iterables. They are useful for lazy sequences and advanced control flows, yet
they are not required for the first Campus Hub features.

---

# 14. Standard built-ins define common data boundaries

The standard library supplies reusable objects and functions. Knowing their
boundaries matters more than memorizing every method.

**Table 4.13 - Built-ins and their boundary questions**

| Facility | Typical work | Boundary question |
|---|---|---|
| `Number` and `Math` | Conversion, rounding, finite checks, numeric operations | Is binary floating-point precision acceptable? |
| `String` | Search, slice, replace, normalize, case conversion | Am I counting UTF-16 code units, code points, or user-perceived characters? |
| `Date` and `Intl` | Instants, formatting, locale-aware display | Which time zone and locale are intended? |
| `JSON` | Exchange text containing objects, arrays, numbers, strings, booleans, and null | Has the parsed structure been validated? |
| `RegExp` | Pattern-based searching and validation | Is the pattern anchored, readable, and safe for untrusted long input? |

## 14.1 Numbers are precise within stated limits

JavaScript `Number` uses IEEE 754 binary64 floating-point representation.
Consequently, some decimal fractions cannot be represented exactly:
`0.1 + 0.2 !== 0.3`. Compare measurements with a documented tolerance and store
money in integer minor units when that matches the domain. Integers are exact
only through `Number.MAX_SAFE_INTEGER`; `BigInt` supports larger integers but
cannot be mixed directly with `Number` arithmetic and is not represented by JSON.

`Math.round()`, `Math.floor()`, and `Math.ceil()` answer different questions.
`Math.random()` is suitable for demonstrations and ordinary sampling, not for
passwords, tokens, or security decisions; secure randomness comes from host
cryptographic APIs introduced with the relevant security boundary.

## 14.2 Text requires a Unicode model

JavaScript strings are sequences of UTF-16 code units. A visible character may
use more than one code unit, and some user-perceived characters combine several
Unicode code points. Therefore `text.length` is not always the number of symbols
a reader perceives. `[...text]` iterates code points and `Intl.Segmenter` can
segment user-perceived graphemes when the interface requires that meaning.

Normalize only for a stated purpose. Case conversion and sorting can depend on
language: use `localeCompare()` or `Intl.Collator` for user-facing order instead
of assuming code-unit order matches an alphabet.

## 14.3 Dates represent instants; presentation uses context

A `Date` stores a time value relative to the Unix epoch. Its display depends on
time-zone and locale decisions. Avoid parsing ambiguous strings such as
`"03/04/2027"`; use a documented interchange form and validate it. Use
`Intl.DateTimeFormat` to present a date for a user.

```js
const formatter = new Intl.DateTimeFormat("en-GB", {
  dateStyle: "long",
  timeZone: "Europe/Istanbul",
});
```

The forthcoming Temporal API is deliberately excluded from required code until
it is part of the supported course runtime and browser baseline. Date handling
must follow the tested platform, not a proposal article.

## 14.4 JSON is text at a trust boundary

JavaScript Object Notation (JSON) resembles object-literal syntax, but JSON is a
text data format. It does not contain functions, comments, `undefined`, symbols,
bigints, maps, sets, or cyclic object graphs.

```js
const text = JSON.stringify({ title: "Robotics night", capacity: 80 });
const data = JSON.parse(text);
```

Parsing proves that the text has valid JSON grammar. It does not prove that
`data.capacity` exists, is a number, or belongs to an authorized user. Validate
the resulting structure before domain logic. Treat `JSON.parse()` as a safer
data parser than `eval()`; never execute untrusted text as JavaScript.

## 14.5 Regular expressions describe text patterns

A regular expression can search, split, or validate strings.

```js
const courseCodePattern = /^[A-Z]{3}\d{3}$/;
courseCodePattern.test("CEN402"); // true
```

`^` and `$` anchor the whole input, `[A-Z]` selects one uppercase ASCII letter,
`{3}` repeats the preceding pattern three times, and `\d` matches a digit. A
pattern is not automatically a complete business rule. Keep patterns readable,
test rejection cases, and avoid nested ambiguous repetition that can consume
excessive processing time on hostile input.

---

# 15. Modules make dependencies explicit

The laboratory already uses `export` and `import`; these words define an
ECMAScript module boundary. A module has its own top-level scope and runs in
strict mode. It exposes only explicitly exported bindings.

```js
// events.js
export function seatsRemaining(event) {
  return Math.max(0, event.capacity - event.registered);
}

// events.test.js
import { seatsRemaining } from "./events.js";
```

The relative specifier begins with `./`, meaning the file is resolved relative
to the importing module. The extension is written explicitly in this course.
Imports are live read-only views of exported bindings; an importing module does
not receive permission to reassign an export.

Figure 4.16 shows a module graph. Arrows mean “imports from.” The test and browser
entry modules can both depend on `events.js`, while the domain module remains
independent of either interface.

<!-- figure:javascript-module-graph -->

In a browser, use `<script type="module" src="events.js"></script>`. Module
scripts are deferred by default and follow cross-origin rules. In Node.js, this
repository's `package.json` declares `"type": "module"`, so `.js` files use the
ECMAScript module system. Chapter 7 develops module architecture, packages,
dependency risk, bundling, and TypeScript; this chapter establishes the language
mechanism needed to understand those tools.

## 15.1 Strict mode rejects several error-prone behaviors

Modules are always strict. Among other effects, an ordinary function call has
`this === undefined`, assigning an undeclared identifier throws, and some silent
legacy failures become exceptions. Do not rely on accidental globals. The error
is evidence that a declaration or dependency is missing.

## 15.2 Memory is managed, but reachability still matters

JavaScript automatically reclaims objects that are no longer reachable. A
program cannot demand when garbage collection occurs. Global collections,
closures, event listeners, timers, and caches can keep objects reachable and
therefore retain memory. Release references when an owning feature ends and put
limits on caches. Performance work begins with measurement; do not replace clear
code with speculative micro-optimizations.

---

# 16. Language mastery prepares later browser layers

This chapter covers the language model used throughout the book. The remaining
browser chapters add separate responsibilities.

**Chapter 5** supplies the Document Object Model, browser events, form state, and
accessible rendering. These are host APIs operating on the page.

**Chapter 6** supplies promises, `async`/`await`, the event loop, `fetch`, storage,
cancellation, and resilient loading states. These govern work that completes
over time.

**Chapter 7** develops module architecture, npm dependencies, build tools,
source maps, linting, formatting, and TypeScript. These organize and check larger
programs.

This separation is a teaching dependency, not a claim that production programs
use one feature at a time. A real Campus Hub browser application uses language,
DOM, events, asynchronous APIs, and modules together. Learning each boundary
first makes failures easier to locate later.

---

# Guided laboratory - Model Campus Hub event availability

## Goal and evidence

Complete `labs/week-04/events.js` so event records can be validated, classified,
filtered, and summarized. Required evidence is a passing test run, the correct
browser summary, a clean Console, and a Git commit containing only the intended
Week 4 changes.

## Step 1 - Run each entry point and name its evidence

Before changing the Campus Hub logic, prove that you can distinguish the four
files introduced in Section 0.6.

1. Run `node labs/week-04/hello.js`. Record the two terminal lines. No browser
   request should be necessary.
2. Start `npm run serve:week04`, leave that server terminal running, and visit
   `http://localhost:8000/hello-browser.html`. Record the visible heading, the
   two Console messages, and successful Network rows for both
   `hello-browser.html` and `hello-browser.js`.
3. Visit `http://localhost:8000/`. Record the Campus Hub heading, the
   `events.js` request, and the current `#program-output` text.
4. In one sentence per file, explain why deleting that file would break only its
   corresponding path. This is a dependency explanation, not a filename quiz.

## Step 2 - Establish the baseline

From the personal coursework repository root, prove `package.json` is present,
run `npm test`, then run `npm run serve:week04`. Open
`http://localhost:8000/`. Keep the server terminal open and use a second terminal
for tests and Git commands.

## Step 3 - Read the event shape and indexes

Open `labs/week-04/events.js`. For each property, state its type and purpose.
Predict `80 - 62` before executing code. Draw the three-element array with
indexes `0`, `1`, and `2`, then label its `length` as `3`. Open Console and verify
the starter table. Confirm that `events[0].title` is `"Robotics night"` and that
`events[events.length - 1].title` is `"Sustainable gardens"`.

## Step 4 - Trace the language evidence page

Visit `http://localhost:8000/language-evidence.html`. For the loop panel, identify
which output came from `for...of`, counted `for`, `while`, and `do...while`. For
the function panel, identify the direct call, method call, callback invocation,
object return, default parameter, and rest parameter. For the array panel, mark
which results came from mutation and which came from copying operations. Then
open `language-examples.js` and connect each visible property to the exact source
statement that produced it. Run the language-evidence tests before continuing.

## Step 5 - Write one function at a time

Implement `seatsRemaining(event)`, then test it. Add `eventStatus(event)` with the
boundaries `full`, `almost full`, and `open`. Do not write all functions before
collecting evidence; one small failing-to-passing cycle localizes mistakes.

## Step 6 - Transform the collection

Implement `filterEvents(allEvents, category)` and
`summarizeEvents(allEvents)`. Preserve the input array. Before coding, state
whether each operation needs `find`, `filter`, `map`, or a loop and what result
shape it must return. Use names that describe domain meaning rather than
temporary mechanics.

## Step 7 - Validate the boundary

Reject missing or non-numeric capacity and registration values with a useful
`TypeError`. Observe one deliberate failure, read its stack, repair the input,
and rerun the tests.

## Step 8 - Build a keyed index

Implement `groupEventsByCategory(allEvents)`. Return a `Map` whose keys are
category names and whose values are new arrays containing the matching event
objects. Validate that the input is an array. Confirm that adding an event to one
group array does not change the original array's length.

## Step 9 - Build a closure with private state

Implement `createEventRegistry(initialEvents)`. Store events in a private `Map`
inside the factory function and return methods named `add(event)`,
`findByTitle(title)`, and `list()`. Validate each event through the existing
boundary function. Make `list()` return a new array so callers cannot replace the
registry's private collection.

## Step 10 - Compare output with code

Reload the browser. The completed reference result appears in Figure 4.17. Check
all three event titles, status words, and remaining-seat counts. A visual match is
not enough; the automated tests must also pass.

<!-- media:week-04-browser-output -->

## Step 11 - Commit evidence

Run `git status`, review `git diff`, then commit the completed Week 4 files with a
message that describes the behavior, such as `Complete event availability logic`.

Use Table 4.14 as the laboratory completion record. Each row requires observable
evidence rather than a statement that the task was attempted.

**Table 4.14 - Week 4 laboratory completion record**

| Check | Expected evidence |
|---|---|
| Repository root | `package.json` is visible before npm commands |
| Entry-point model | Terminal, minimal browser page, and Campus Hub page produce the predicted evidence |
| Array reasoning | Three values are traced at indexes 0-2 and the last index is identified as `length - 1` |
| Language evidence | Loop, function-call, return-shape, and array-manipulation outputs are connected to tested source statements |
| Automated tests | Normal, boundary, and invalid-input cases pass |
| Browser | Three correct event summaries replace the loading message |
| Console | No uncaught exception or failed module request |
| Data integrity | Filtering and summarizing do not mutate the source array |
| Keyed collection | Category groups and registry lookups use `Map` deliberately |
| Closure boundary | Registry state is reachable only through its returned operations |
| Git | One focused commit records the completed behavior |

---

# Exercises

## Foundation

### Exercise 1 - Values and types

State the type and value produced by `typeof 42`, `typeof "42"`, `typeof null`,
`Array.isArray([])`, and `typeof (() => 1)`.

### Exercise 2 - Binding or object change

Explain which operation fails and why: `const event = { capacity: 80 };`, then
`event.capacity = 90;`, then `event = { capacity: 100 };`.

### Exercise 3 - Strict comparison

Predict `0 === false`, `0 == false`, `"" || "Untitled"`, and
`"" ?? "Untitled"`. Explain the conversion or short-circuit rule.

### Exercise 4 - Trace a branch

For remaining-seat values `0`, `8`, and `18`, trace the `eventStatus` branch and
give the returned status.

## Application

### Exercise 5 - Write a total function

Write `occupancyPercent(event)` that returns a rounded percentage and rejects a
non-positive capacity. Explain the chosen error.

### Exercise 6 - Array pipeline

From the laboratory data, produce titles of featured events with more than 15
remaining seats. Do not mutate the source array.

### Exercise 7 - Scope diagnosis

Explain why a `const remaining` declared inside a function cannot be read after
the function returns. Show how returning it repairs the data flow.

### Exercise 8 - Identity diagnosis

Two bindings refer to the same event object. A change through one appears through
the other. Explain why and show a shallow-copy update.

## Challenge

### Exercise 9 - Boundary table

Design cases for `eventStatus`: ordinary open, exactly 10 seats, one seat, zero
seats, over-registration, and invalid numeric data. State the expected result.

### Exercise 10 - Debug a failing calculation

The Console shows `"8062"` after adding capacity and registrations obtained from
form fields. Diagnose the result and repair the calculation without relying on
implicit coercion.

### Exercise 11 - Choose loop or transformation

Choose between a loop, `filter()`, `map()`, and `find()` for four tasks: logging
every title, selecting technology events, constructing summary objects, and
locating the first full event. Explain each choice.

### Exercise 12 - Test quality

Critique a test that only calls `seatsRemaining()` with one ordinary valid event.
Propose a compact set that provides stronger evidence.

### Exercise 13 - Prove the environment before debugging code

A student says “JavaScript is broken.” Their terminal prompt shows
`C:\Users\Student>`, `dir package.json` reports that the file is absent, and
`npm run serve:week04` reports `ENOENT`. Explain what the evidence proves, what it
does not prove, and give the next three commands or actions in order.

### Exercise 14 - Separate source, command, and output

Classify each item as source code, a shell command, or runtime output:
`console.log(2 + 3);`, `node labs/week-04/hello.js`, and `5`. Explain why typing
the output line back into the shell is a category mistake.

### Exercise 15 - Trace browser script loading

The HTML page appears, but the Console has no greeting. Network shows the HTML
request with status 200 and `hello-brower.js` with status 404. Identify the most
likely defect, the exact evidence that supports the diagnosis, and the repair.

### Exercise 16 - Trace a closure

Call `createRegistrationCounter(5)` twice, producing `first` and `second`. Predict
the results of `first()`, `first()`, and `second()`. Explain which bindings each
returned function retains.

### Exercise 17 - Diagnose the temporal dead zone

Explain why `console.log(category); const category = "arts";` throws rather than
printing `undefined`. Contrast the behavior with legacy `var` without recommending
`var` for new code.

### Exercise 18 - Preserve a method receiver

An object method uses `this.title`. Explain why assigning the method to a new
variable and calling that variable fails in a module. Show two repairs: one using
an explicit parameter and one using `bind()`.

### Exercise 19 - Follow a prototype lookup

An object owns no `describe` property, but its prototype does. Trace the lookup.
Then add an own `describe` property and explain which function is called.

### Exercise 20 - Choose Array, Object, Map, or Set

Choose a collection for an ordered event schedule, one event record, a lookup by
event object identity, and unique category names. Defend each decision from the
required operations.

### Exercise 21 - Validate a JSON boundary

`JSON.parse('{"capacity":"80"}')` succeeds. Explain why this does not make the
capacity valid for arithmetic and write the next validation steps.

### Exercise 22 - Reason about Unicode length

Explain why a string's `.length` may differ from the number of symbols perceived
by a reader. State when code-unit length, code-point iteration, and grapheme
segmentation are appropriate.

### Exercise 23 - Draw a module graph

Draw arrows for `index.js` importing `events.js`, and `events.test.js` importing
the same module. Explain why `events.js` should not import either interface file.

### Exercise 24 - Repair accidental sorting mutation

A function calls `events.sort(compare)` and a later test observes a different
source order. Repair the function and explain the identity difference between
`sort()` and `toSorted()`.

### Exercise 25 - Place the concept in the right chapter

Classify each topic as core language in this chapter, DOM/event work in Chapter
5, asynchronous API work in Chapter 6, or module/tooling architecture in Chapter
7: closure, `querySelector`, `fetch`, prototype, `addEventListener`, npm package
selection, promise rejection, and TypeScript narrowing.

### Exercise 26 - Explain the four-file architecture

For `hello.js`, `hello-browser.html`, `hello-browser.js`, and `index.html`, state
the execution host, the action that starts it, its observable output, and its
direct JavaScript dependency. Then explain why `hello-browser.html` and
`index.html` are not redundant pages.

### Exercise 27 - Trace array indexes precisely

For `const values = [12, 18, 25];`, give `values.length`, the first index, the
last valid index, `values[1]`, and `values[3]`. Write a counted loop that visits
exactly the three existing values and explain why `<= values.length` is wrong.

### Exercise 28 - Choose mutation or copying deliberately

An instructor must display events in title order without changing the order
stored in `events`. Choose between `sort()` and `toSorted()`, write the operation,
and explain which array identity each observer sees. Then explain whether nested
event objects were cloned.

### Exercise 29 - Distinguish a hole from stored `undefined`

Compare `["a", , "c"]` and `["a", undefined, "c"]`. Predict the value of index
`1`, the result of `1 in array`, and the behavior expected from `map()` at that
index. Explain why ordinary course data should remain dense.

### Exercise 30 - Read one array pipeline as data flow

Given three events, two of which are featured, trace
`events.filter((event) => event.featured).map((event) => event.title)`. State the
element type and maximum length after each stage, whether either stage changes
the source array, and why the result objects would still be shared if the second
callback returned event objects instead of titles.

### Exercise 31 - Select and trace every basic loop form

Choose among `for...of`, counted `for`, `while`, and `do...while` for these
requirements: visit every event value; print each event with its index; retry
while a condition remains false; and perform one attempt before testing. For
each choice, name the state, condition, progress step, and exit argument.

### Exercise 32 - Diagnose an infinite and an off-by-one loop

Explain both defects in `for (let index = 0; index <= events.length; index -= 1)`.
Write the corrected header and state the first invalid array access produced by
the comparison defect if the update defect were repaired separately.

### Exercise 33 - Explain `var` without recommending it

Predict the output and scope of `var status` declared inside an `if` block within
a function. Then compare reading `var status`, `let status`, and `const status`
before their declaration lines. Explain why “hoisting moves the line” is only a
mental model.

### Exercise 34 - Design input and return contracts

Write `eventMetrics(event, precision = 0)` so it returns one object containing
`remaining` and `percentFull`. Validate the event and precision. Show calls with
the default and an explicit precision, then destructure the returned object.
Explain why two separate return statements cannot return two values from one call.

### Exercise 35 - Classify function call forms

Classify each as direct, method, constructor, callback, indirect, bound,
recursive, or immediately invoked: `fn(x)`, `obj.fn(x)`, `new Model(x)`,
`items.map(fn)`, `fn.call(obj, x)`, `fn.bind(obj)`, a call to `walk()` inside
`walk()`, and `(function () {})()`. State which forms establish `this` from a
receiver or explicit binding.

### Exercise 36 - Manipulate an array under two identity contracts

Starting with `const categories = ["technology", "arts", "community"]`, replace
`"arts"` with `"culture"` first by mutating the existing array and then by
creating a new array. Add and remove an end value, locate `"community"`, and
produce an alphabetic copy. State the source identity and return value after
each operation.

---

# Worked answers

## Answer 1

The results are `"number"`, `"string"`, `"object"`, `true`, and `"function"`.
The `null` result is a historical `typeof` behavior, not evidence that null has
ordinary object properties. `Array.isArray()` is the intentional array check.

## Answer 2

Changing `event.capacity` succeeds because the object is mutable. Assigning a
new object to `event` fails because `const` prevents rebinding. The misconception
is that `const` recursively freezes the value; it protects the binding.

## Answer 3

`0 === false` is false because the types differ. `0 == false` is true after loose
equality conversion. `"" || "Untitled"` returns `"Untitled"` because the empty
string is falsy. `"" ?? "Untitled"` returns the empty string because it is
neither null nor undefined. Use `??` when an empty string is valid data.

## Answer 4

Zero enters the first branch and returns `"full"`. Eight fails the zero test but
satisfies `<= 10`, returning `"almost full"`. Eighteen reaches the final branch
and returns `"open"`. Branch order makes the boundary behavior explicit.

## Answer 5

```js
function occupancyPercent(event) {
  if (!Number.isFinite(event.capacity) || event.capacity <= 0) {
    throw new RangeError("Capacity must be a positive finite number.");
  }
  if (!Number.isFinite(event.registered)) {
    throw new TypeError("Registered must be a finite number.");
  }
  return Math.round((event.registered / event.capacity) * 100);
}
```

The range error identifies a numeric value outside the accepted domain; the type
error identifies unsuitable numeric data. A project may standardize differently,
but the contract and tests must agree.

## Answer 6

```js
const titles = events
  .filter((event) => event.featured && seatsRemaining(event) > 15)
  .map((event) => event.title);
```

Both methods return new arrays. The existing event objects remain shared, but
this pipeline reads rather than mutates them.

## Answer 7

The local binding belongs to the function's lexical scope and is unavailable to
the caller. Return the value and bind the call result:

```js
function remainingFor(event) {
  const remaining = event.capacity - event.registered;
  return remaining;
}
const remaining = remainingFor(event);
```

## Answer 8

Assignment copies the object reference, not a separate object. Use
`const updated = { ...original, registered: 63 };` to create a new outer object.
This is shallow: nested objects would still be shared and require deliberate
copying when independent mutation is necessary.

## Answer 9

Expect `open` for 18, `almost full` for exactly 10 and for 1, and `full` for zero.
The supplied implementation clamps over-registration to zero and therefore also
returns `full`. Non-numeric data must throw `TypeError`. This set covers both
branch boundaries and the validation contract.

## Answer 10

Form values are strings, so `+` concatenates them. Convert and validate first:

```js
const capacity = Number(capacityInput.value);
const registered = Number(registeredInput.value);
if (!Number.isFinite(capacity) || !Number.isFinite(registered)) {
  throw new TypeError("Capacity and registrations must be numbers.");
}
const total = capacity + registered;
```

## Answer 11

Use `for...of` for logging because the purpose is a side effect for every value;
`filter()` for selecting technology events; `map()` for constructing one summary
per event; and `find()` for the first full event. A loop could implement all four,
but the named methods communicate the result shape directly.

## Answer 12

One ordinary case misses zero, over-registration, boundary values, missing
properties, strings, and non-finite numbers. A compact stronger suite includes an
ordinary subtraction, exactly full, over-registered clamping, each status
boundary, and invalid inputs that must throw. Tests should verify both returned
values and the promised error type.

## Answer 13

The evidence proves that npm searched `C:\Users\Student` and did not find the
project manifest there. It does not prove that Node.js, npm, or the JavaScript
source is defective. First open the authorized coursework folder in VS Code or
run `cd` with its exact path. Second run `dir package.json` and stop unless the
file is listed. Third run `npm run serve:week04` from that verified root. The
reasoning follows the boundary named by `ENOENT`: a missing path in the current
directory, not a language failure.

## Answer 14

`console.log(2 + 3);` is JavaScript source code stored in a `.js` file.
`node labs/week-04/hello.js` is a shell command that asks Node.js to execute a
named file. `5` is runtime output produced after the expression is evaluated.
Typing `5` into a shell treats evidence as though it were a command name; the
shell then searches for a program named `5`, which is unrelated to the original
calculation.

## Answer 15

The spelling `hello-brower.js` is missing the `s` in `browser`. Status 200 for the
HTML proves that the server and document request worked. Status 404 for the
script proves that the URL requested by `src` did not match an available file,
so no JavaScript source was delivered for execution. Change the HTML attribute
to `src="hello-browser.js"`, save, reload, and verify a 200 script response before
checking the Console message.

## Answer 16

The results are `6`, `7`, and `6`. Both calls through `first` retain the same
`count` binding created by the first factory call. `second` retains a different
binding created by the second call. A closure preserves lexical access; it does
not create one global counter shared by every factory call.

## Temporal dead zone - Answer 17

The `const` binding exists during scope preparation but remains inaccessible in
the temporal dead zone until its declaration is evaluated. Access therefore
throws `ReferenceError`. A `var` binding would already contain `undefined`, but
that behavior can hide ordering defects and `var` is function scoped. Declare
the `const` before its first use.

## Answer 18

An ordinary method obtains `this` from the call site. After detachment,
`describe()` has no receiving object, and strict module code supplies
`undefined`. An explicit data-flow repair is
`const describe = (value) => event.describe.call(value); describe(event);`.
A receiver-preserving repair is `const describe = event.describe.bind(event);`.
Prefer an explicit parameter for domain calculations when object receiver
semantics add no value.

## Answer 19

JavaScript first checks the object's own properties. Finding no `describe`, it
follows the internal prototype link and finds the method there. After an own
`describe` property is added, lookup stops at the object and calls that function;
the own property shadows the inherited property without deleting it.

## Answer 20

Use an array for the ordered schedule because position and iteration order
matter. Use a plain object for one event record with stable named fields. Use a
`Map` when event objects themselves are keys because object property keys cannot
preserve arbitrary object identity in the same direct way. Use a `Set` for unique
category names because membership and duplicate removal are its purpose.

## Answer 21

Parsing validates JSON grammar only. The property remains a string. First verify
that the parsed value is a non-null object and owns `capacity`; then decide
whether the contract accepts numeric strings. If it does, reject an empty string,
convert with `Number()`, and require `Number.isFinite(capacity)` plus the domain
range. If the contract requires a JSON number, reject the string directly.

## Answer 22

`.length` counts UTF-16 code units, and one Unicode code point can require two.
Combining marks and emoji sequences can also join several code points into one
perceived grapheme. Code-unit length is appropriate for low-level string
positions defined that way; `[...text]` supports code-point iteration; an
`Intl.Segmenter` with grapheme granularity is appropriate when the interface
must count user-perceived characters.

## Answer 23

Both arrows point toward `events.js`: `index.js -> events.js` and
`events.test.js -> events.js`. The domain module contains calculations shared by
the browser entry and tests. Importing either interface back into the domain
module would create unnecessary coupling and may produce a cycle. Dependency
direction should point from interface and verification code toward the reusable
domain boundary.

## Answer 24

Use `const ordered = events.toSorted(compare);`. `sort()` rearranges the same
array object and returns that object, so every holder observes the new order.
`toSorted()` creates a new array with the ordered references, leaving the source
array order unchanged. Nested event objects remain shared in both arrays.

## Chapter placement - Answer 25

Closure and prototype are core language concepts in this chapter.
`querySelector` and `addEventListener` belong to DOM and event programming in
Chapter 5. The Chapter 6 topics are `fetch` and promise rejection. npm package
selection and TypeScript narrowing belong to module and tooling architecture in
Chapter 7. The classification follows responsibility: language
semantics, browser document interaction, time-dependent host work, or project
organization and static checking.

## Four-file architecture - Answer 26

`hello.js` is started by the Node.js command and writes to the terminal.
`hello-browser.html` is requested by its browser URL, displays the minimal
orientation document, and requests `hello-browser.js`. That JavaScript file runs
in the browser and writes to Developer Tools > Console. `index.html` is requested
at the laboratory root, displays the Campus Hub interface, and loads `events.js`
as a module. The two HTML files are not redundant: one isolates the browser's
HTML-to-script loading path with two messages; the other supplies the integrated
laboratory interface and a visible output target for reusable event logic.

## Array indexes - Answer 27

The length is `3`; the first index is `0`; the last valid index is `2`, which is
`values.length - 1`; `values[1]` is `18`; and `values[3]` is `undefined`.

```js
for (let index = 0; index < values.length; index += 1) {
  console.log(values[index]);
}
```

The condition uses `<` because length counts elements while indexing begins at
zero. `index <= values.length` permits `index === 3`, one position beyond the
last element.

## Mutation or copying - Answer 28

Use `const ordered = events.toSorted((a, b) =>
a.title.localeCompare(b.title));`. `ordered` is a new array identity in title
order, while every observer of `events` retains the original order. `sort()`
would reorder and return the existing `events` array. Neither operation deeply
clones the event objects; corresponding entries in the two arrays can still
refer to the same objects.

## Sparse and explicit elements - Answer 29

Both index reads produce `undefined`. For the sparse array, `1 in array` is
false and `map()` skips the missing index, leaving a hole in the result. For the
explicit array, the `in` result is true and `map()` calls the callback with
`undefined`. Dense arrays give every position a deliberate value, making
iteration, validation, serialization, and tests less surprising.

## Array pipeline - Answer 30

The source contains three event objects. `filter()` visits them and returns at
most three event objects; under the stated data it returns two. `map()` then
visits those two objects and returns exactly two strings. Neither method changes
the source array. If `map()` returned each event object instead, the outer result
array would be new but its elements would still be references to the existing
objects, so later object mutation could be observed through both arrays.

## Loop selection - Answer 31

Use `for...of` to visit event values: the iterator supplies progress and exits
after the final value. Use counted `for` when the index must be printed: initialize
at zero, continue while the index is less than length, and increment once per
iteration. Use `while` for condition-governed retry when zero attempts may be
valid; the body must change the state read by the condition. Use `do...while`
when one attempt is required before the first test. The syntax differs, but every
choice still needs a reason it terminates.

## Loop defects - Answer 32

`<=` allows `index === events.length`, which is beyond the last valid index.
`index -= 1` moves away from termination after starting at zero, so the condition
remains true while the index becomes negative. The corrected header is
`for (let index = 0; index < events.length; index += 1)`. If only the update were
repaired, the first invalid access would be `events[events.length]`.

## `var` behavior - Answer 33

The `var` binding belongs to the containing function and remains readable after
the `if` block. During function-environment creation it is initialized to
`undefined`; its assignment occurs only when execution reaches the initializer.
An early `var` read therefore produces `undefined`, while early `let` and `const`
reads throw `ReferenceError` because the bindings are in their temporal dead
zone. “Moving the line” is a teaching model: the engine creates environment
records and bindings; it does not edit or reorder the source file.

## Input and return contracts - Answer 34

```js
function eventMetrics(event, precision = 0) {
  if (!event || !Number.isFinite(event.capacity) || event.capacity <= 0 ||
      !Number.isFinite(event.registered)) {
    throw new TypeError("Event requires positive capacity and numeric registration.");
  }
  if (!Number.isInteger(precision) || precision < 0 || precision > 4) {
    throw new RangeError("Precision must be an integer from 0 through 4.");
  }
  const remaining = Math.max(0, event.capacity - event.registered);
  const percentFull = Number(
    ((event.registered / event.capacity) * 100).toFixed(precision),
  );
  return { remaining, percentFull };
}

const ordinary = eventMetrics(events[0]);
const precise = eventMetrics(events[0], 1);
const { remaining, percentFull } = precise;
```

Each call crosses the function boundary once and therefore returns one value.
The object groups two named logical results. The first executed `return` ends the
call; a later return statement is reached only on a different control-flow path.

## Call forms - Answer 35

`fn(x)` is direct; `obj.fn(x)` is a method call; `new Model(x)` is a constructor
call; `items.map(fn)` causes callback invocation; `fn.call(obj, x)` is indirect
with explicit `this`; `fn.bind(obj)` creates a bound function whose later call
uses that receiver; the inner `walk()` is recursive; and `(function () {})()` is
an immediately invoked function expression. Method, `call`/`apply`, bound, and
constructor forms deliberately establish `this`. Direct module calls normally
have `this === undefined`; callback receivers depend on the API and should not be
guessed.

## Array identity contracts - Answer 36

`categories.splice(1, 1, "culture")` mutates the existing identity and returns
an array containing the removed `"arts"`. Starting again from the original,
`const replaced = categories.with(1, "culture")` returns a new array and leaves
the source unchanged. `push("sports")` mutates and returns the new length;
`pop()` mutates and returns `"sports"`; `indexOf("community")` returns `2` or
`-1` when absent; and `toSorted((a, b) => a.localeCompare(b))` returns a new
alphabetic array. None of these outer-array copies deeply clones nested objects.

---

# Debugging clinic

## Symptom 1 - `ReferenceError: remaining is not defined`

Locate the first application frame and inspect the spelling and lexical scope.
The name may be declared inside another block or function. Repair the data flow
with a parameter or return value rather than creating an unexplained global.

## Symptom 2 - `TypeError` mentions reading a property of undefined

Trace the expression left of the property access. An array lookup may not have
found an item, or a function may not have returned a value. Verify the producer
before adding optional chaining; `?.` can hide a violated required-data contract.

## Symptom 3 - The calculation concatenates digits

Inspect each input with `typeof`. Convert at the input boundary, validate the
converted number, and keep domain functions numeric. Do not scatter conversions
through later calculations.

## Symptom 4 - A test changed another test's data

Look for shared mutable objects or arrays. Construct fresh fixtures per test or
copy the changed level. Test isolation is a design property, not a matter of test
execution order.

---

# Retrieval quiz

1. What is the difference between ECMAScript and a browser API?
2. What does an expression produce?
3. When should a binding use `let` rather than `const`?
4. Why can a property of a `const` object change?
5. Why is `typeof null` not a sufficient null test?
6. What is the difference between `===` and `==`?
7. When is `??` safer than `||`?
8. What must change during a loop to support termination?
9. What happens when a function reaches its end without `return`?
10. Where is a function parameter binding available?
11. Why does `map()` not guarantee deep immutability?
12. What is the difference between dot and bracket property access?
13. Why can two bindings observe the same object mutation?
14. When should a function throw rather than invent a result?
15. What do normal, boundary, and invalid-input tests contribute?
16. What evidence proves that Node.js is available in the current terminal?
17. Why must `package.json` be visible before an npm project command?
18. What is the difference between saving a file and running it?
19. Why can an HTML page appear even when its JavaScript request fails?
20. Which browser panel proves whether `hello-browser.js` returned status 200 or 404?
21. What does the call stack record?
22. What is a closure?
23. Why does an arrow function not replace every ordinary function?
24. How does prototype property lookup stop?
25. When is `Map` a clearer choice than a plain object?
26. What is the difference between `sort()` and `toSorted()`?
27. What does successful `JSON.parse()` prove, and what does it not prove?
28. Why can `.length` misrepresent user-perceived text length?
29. What does an `import` declaration add to a module graph?
30. Why are DOM, asynchronous APIs, and tooling developed in later chapters?
31. Why are `hello.js` and `hello-browser.js` both useful even when their first calculations are similar?
32. For an array of length four, what are the first and last valid indexes?
33. What is the difference between `find()` and `filter()` when nothing matches?
34. Why can a copied array still expose mutation of a nested event object?
35. What distinguishes a sparse hole from an element whose value is `undefined`?
36. Why does `var` remain visible outside an `if` block inside the same function?
37. Which loop form guarantees that its body executes at least once?
38. What happens when a function is called with fewer or more arguments than named parameters?
39. How can one function call return several logically named results?
40. Which array operations in the walkthrough preserve the source array identity and contents?

## Quiz answers and misconception notes

1. ECMAScript defines the language; a browser API is supplied by the browser host.
2. An expression evaluates to a value; a statement controls or performs execution.
3. Use `let` when the algorithm deliberately reassigns that binding.
4. `const` prevents rebinding, not mutation of the referenced object.
5. It returns the historical string `"object"`; use `value === null`.
6. Strict equality compares without coercive type conversion; loose equality may convert.
7. Use `??` when falsy values such as `0`, `false`, or `""` remain valid.
8. State relevant to the condition must progress toward termination.
9. The call returns `undefined`.
10. A parameter is local to that function call's scope.
11. It creates a new array but may retain references to the same nested objects.
12. Dot notation uses a source-level property name; brackets evaluate a key expression.
13. Both contain references to one object identity.
14. Throw when the input violates a contract and no honest domain result exists.
15. They check ordinary behavior, decision edges, and rejection of invalid contracts.
16. `node --version` must print the expected version in that terminal; an installer file alone is not runtime evidence.
17. npm reads that manifest for named scripts and project metadata; absence usually means the terminal is in the wrong directory.
18. Saving writes editor contents to disk; running asks a runtime to read and execute the saved source.
19. The HTML and JavaScript are separate requests; the first can succeed while the second returns 404 or contains an error.
20. The Network panel records the request URL and Hypertext Transfer Protocol (HTTP) status; the Console reports execution messages and errors.
21. It records active calls and the route by which execution reached the current frame.
22. It is a function together with continued access to the lexical environment where it was created.
23. An arrow captures surrounding `this` and cannot serve as a constructor; ordinary functions receive call-site `this` and can have prototype behavior.
24. Lookup stops at the first matching own or inherited property, or at a `null` prototype when no match exists.
25. Use `Map` for dynamic keyed data, especially when keys are not strings or when frequent keyed insertion and deletion are central.
26. `sort()` mutates and returns the same array; `toSorted()` returns a newly ordered array.
27. It proves valid JSON grammar. It does not prove the parsed value has the required shape, types, range, or authorization.
28. It counts UTF-16 code units; visible graphemes may contain multiple code units and code points.
29. It adds a directed dependency from the importing module to the exporting module.
30. They add distinct host and project responsibilities. Learning their boundaries after core language semantics makes integrated failures traceable.
31. The first isolates Node.js and terminal execution; the second proves browser-host execution after an HTML document requests it.
32. The first index is `0` and the last is `3`, expressed generally as `length - 1`.
33. `find()` returns the first value or `undefined`; `filter()` always returns an array, which may be empty.
34. Spread and copying array methods create a new outer array but preserve references to nested objects unless those objects are copied too.
35. A hole has no property at that index and some methods skip it; an explicit element exists and stores the value `undefined`.
36. `var` is scoped to the containing function or script, not to an ordinary block.
37. `do...while` tests after the body, so the first iteration occurs before the first condition check.
38. Missing parameters receive `undefined` unless defaults apply; extra arguments are evaluated but remain unnamed unless rest parameters or `arguments` read them.
39. Return one object or array that groups the results, then destructure it at the call site.
40. `with()`, `toSorted()`, `slice()`, spread, and the other copying methods return new arrays; the source remains unchanged, although nested objects may still be shared.

---

# Session summary

- JavaScript is the course's primary programming language; hosts supply additional APIs.
- Values have types, while bindings give values names within lexical scopes.
- Prefer `const`; use `let` for deliberate reassignment, and understand `var` when maintaining legacy function-scoped code.
- Strict equality and explicit conversion keep data boundaries visible.
- Branches choose paths; `for...of`, `for`, `while`, and `do...while` express different repetition questions and still require progress toward an exit.
- Function contracts distinguish parameters from arguments, normal returns from exceptions, and direct, method, callback, constructor, indirect, bound, recursive, and immediate calls.
- Arrays represent ordered collections; objects represent named properties.
- Object assignment shares identity, while spread creates only a shallow copy.
- Active function calls form a stack; closures retain access to lexical bindings.
- Ordinary method calls receive `this` from the call site, while arrows capture it.
- Prototype delegation underlies objects and class syntax.
- Arrays, objects, maps, and sets answer different collection questions.
- JSON, Unicode text, dates, regular expressions, and numbers each have explicit boundaries.
- ECMAScript modules make dependencies and top-level scope visible.
- Errors and failing assertions are structured evidence.
- Small automated tests make expectations repeatable but prove only tested behavior.

## Glossary

Table 4.15 defines the chapter's working vocabulary. These definitions are
deliberately concise; the numbered sections provide the mechanisms and examples.

**Table 4.15 - Session 4 glossary**

| Term | Working definition |
|---|---|
| Argument | A value supplied at a function call site. |
| Array | An indexed, ordered object commonly used as a collection. |
| Binding | An association between an identifier and a value. |
| Boolean | The primitive logical type containing `true` and `false`. |
| Branch | One possible path selected by control flow. |
| Callback | A function supplied to another operation to be called later or for each value. |
| Call stack | The ordered record of function calls that have started and not yet returned. |
| Class | Syntax for constructing objects whose methods are shared through a prototype. |
| Closure | A function together with continued access to its defining lexical environment. |
| Coercion | Conversion performed by language rules, sometimes implicitly. |
| ECMAScript | The standardized language specification implemented as JavaScript. |
| Expression | Source code that evaluates to a value. |
| Function | A callable object that packages behavior behind parameters and a result. |
| Hoisting | The observable consequence of declarations being processed during environment creation before ordinary statement evaluation. |
| Mutation | A change to an existing object's state. |
| Iterable | A value that can produce an iterator, enabling `for...of` and spread. |
| JSON | A text data format for a defined subset of values; parsed data still requires validation. |
| Map | An insertion-ordered keyed collection whose keys may be values of any type. |
| Module | A source unit with private top-level scope and explicit imports and exports. |
| Identifier | A legal source-code name used for a binding, property, or other named construct. |
| Literal | A value written directly in source code, such as `18` or `"open"`. |
| Object | A value with identity and keyed properties. |
| Parameter | A local binding declared by a function for an incoming argument. |
| Primitive | An immutable non-object value such as a string, number, or boolean. |
| Prototype | An object consulted when a property is absent from the receiving object. |
| Set | An insertion-ordered collection of unique values. |
| Scope | The region of source code in which a binding is available. |
| Statement | Source code that performs or controls an execution step. |
| Test assertion | A comparison between observed and expected behavior. |
| Runtime | Software and host facilities that execute program instructions. |
| Return value | The single JavaScript value delivered when a function call completes normally; it is `undefined` when no expression is returned. |
| Source code | Human-authored program text stored in files. |
| Terminal | A text interface for running shell commands and reading their output. |
| Temporal dead zone | The part of a scope where a `let` or `const` binding exists but cannot yet be accessed. |
| `this` | A call-dependent value supplied to an ordinary function, commonly the receiver in a method call. |
| `var` | A legacy-compatible function- or script-scoped binding form initialized to `undefined` during environment creation. |

## Primary references and further reading

1. Ecma International, [ECMAScript 2026 Language Specification](https://tc39.es/ecma262/2026/). Use it as the normative authority for language semantics.
2. MDN, [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide). Use its approachable chapters for a second explanation and reference links.
3. MDN, [JavaScript fundamentals curriculum](https://developer.mozilla.org/en-US/curriculum/core/javascript-fundamentals/). Use its outcomes to audit beginner coverage and identify the later DOM and asynchronous layers.
4. MDN, [Indexed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections). Use it to compare indexing, array methods, sparse arrays, and typed-array boundaries.
5. MDN, [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript). Use it to revisit the relationship among HTML, CSS, JavaScript, and browser APIs.
6. Node.js, [Official download page](https://nodejs.org/en/download). Use it to obtain the latest supported patch release rather than copying a stale installer link.
7. Visual Studio Code, [Getting started](https://code.visualstudio.com/docs/getstarted/overview). Use it for current installation, workspace, and editor-interface guidance.
8. Node.js, [Test runner documentation](https://nodejs.org/docs/latest-v26.x/api/test.html). Use it for the tested command and test lifecycle.
9. Node.js, [Strict assertion documentation](https://nodejs.org/docs/latest-v26.x/api/assert.html). Use it to interpret equality failures and diffs.
10. University of Washington CSE 154, [Web Programming](https://courses.cs.washington.edu/courses/cse154/). Use its language, DOM, service, and database sequence as a comparison for course pacing.
11. Harvard CS50, [HTML, CSS, JavaScript](https://cs50.harvard.edu/college/2026/fall/weeks/html/). Use it as a compact comparison for variables, control flow, and events after prior programming foundations.
12. University of Helsinki, [Full Stack Open: JavaScript](https://fullstackopen.com/en/part1/java_script/). Use it as an exercise-rich bridge toward React after completing this chapter's foundations.
13. Marijn Haverbeke, [Eloquent JavaScript, 4th edition](https://eloquentjavascript.net/). Use Chapters 1-6 for additional language practice.
14. Axel Rauschmayer, [Exploring JavaScript](https://exploringjs.com/js/). Use it as an optional precise language companion after the first reading.
15. MDN, [Loops and iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration). Use it to compare `for`, `while`, `do...while`, `for...of`, and `for...in` against the operation being expressed.
16. MDN, [`var` statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var). Use it to verify function scope, initialization, redeclaration, and global-script behavior in legacy code.
17. MDN, [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions). Use it for parameter forms, return behavior, first-class function values, and advanced callable boundaries.
18. MDN, [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array). Use it to check current mutating, copying, iterative, searching, and ordering methods.

## What changes often?

Core value, control-flow, function, array, and object semantics are stable.
New ECMAScript editions add capabilities, Node.js download versions, diagnostics,
and test-runner features evolve, and browser or editor interfaces change. Always
use the latest available Node.js 26 LTS patch compatible with the course engine
constraint. Technical review date: **20 November 2026**.

## Instructor teaching guide

### Suggested twelve-to-fourteen-hour sequence

1. Tool roles, installation verification, folders, and terminals, 45 minutes.
2. First Node.js and browser programs with evidence, 45 minutes.
3. Runtime boundary, values, bindings, and expressions, 55 minutes.
4. Operators, equality, conversion, branches, and trace tables, 60 minutes.
5. `const`, `let`, legacy `var`, declaration timing, and scope comparison, 55 minutes.
6. `for...of`, counted `for`, `while`, `do...while`, exit reasoning, and loop tracing, 75 minutes.
7. Parameters, defaults, rest, destructuring, return shapes, call forms, and scope, 90 minutes.
8. Arrays, practical manipulation, identity, copying, searching, and transformations, 85 minutes.
9. Errors, tests, and debugging demonstration, 35 minutes.
10. Call stack, temporal dead zone, closures, and first-class functions, 65 minutes.
11. `this`, prototypes, and classes, 65 minutes.
12. Maps, sets, iteration, JSON, Unicode, dates, and regular expressions, 80 minutes.
13. Modules, strict mode, memory, and the Chapters 5-7 boundary, 50 minutes.
14. Guided laboratory, mastery extension, and evidence review, 150 minutes.

### Demonstrations that expose misconceptions

- Run `typeof document` in browser and Node.js to separate language from host.
- Reassign a `const`, then mutate a property of a `const` object.
- Read a `var` before assignment, compare it with the temporal dead zone, and then show why an `if` block does not contain `var`.
- Compare `0`, `"0"`, `false`, an empty string, and an empty array under strict comparison and conditions.
- Step through `eventStatus()` at 0, 10, and 11 seats.
- Trace the same three-value collection through `for...of`, counted `for`, `while`, and `do...while`; require a termination argument for each.
- Call one function directly, as a method, as a callback, and through `call()`; compare arguments, `this`, and return shape.
- Copy an array with spread, mutate a nested object, and observe shallow sharing.
- Break one assertion and read actual, expected, operator, and stack evidence.
- Call two closure factories and show that their captured bindings are independent.
- Detach a method, observe its lost receiver, and compare an explicit parameter with `bind()`.
- Trace an own-property miss through a prototype and then shadow the property.
- Compare `sort()` and `toSorted()` while another binding observes the source array.
- Parse valid JSON containing an invalid domain type and require a second validation step.

### Assessment and inclusion

Accept a trace table, spoken walkthrough, or debugger-step recording as formative
evidence when these demonstrate the same reasoning. Provide code as text rather
than images, allow additional time for syntax entry, and grade contract reasoning
separately from typing speed. A complete submission must still pass the same
behavioral tests and explain one failure repair.
