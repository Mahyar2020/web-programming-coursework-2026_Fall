# Session 4 - JavaScript from First Principles

JavaScript turns the static Campus Hub page into a program. This chapter begins
before the first line of code. It assumes that you may never have installed a
programming runtime, opened a project folder, used a terminal, or interpreted an
error message. We will prepare the computer, run one deliberately small program
in Node.js, run another in a browser, and learn how to tell source code from its
output. Only then will we introduce values, names, decisions, repetition,
functions, arrays, objects, errors, and tests.

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
6. use `const` and `let` according to whether a binding must be reassigned;
7. trace expressions, statements, branches, loops, and function calls;
8. explain strict equality, truthiness, conversion, `null`, and `undefined`;
9. design functions with explicit inputs, return values, and useful errors;
10. transform arrays without accidentally changing source data;
11. explain the difference between rebinding a name and mutating an object;
12. diagnose syntax, reference, type, and assertion failures from evidence; and
13. write and run small automated tests with Node.js.

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
| Node.js 24 Long-Term Support (LTS) | Execute JavaScript and course tools | `node --version` prints a value beginning with `v24.` |
| npm | Run commands defined by the project | `npm --version` prints a version number |
| Browser | Run client-side code and expose Developer Tools | The Console accepts `2 + 3` and displays `5` |
| Git | Record and inspect changes | `git --version` prints a version number |

The course is tested with the latest available patch release in the Node.js 24
Long-Term Support (LTS) line. “LTS” means that the release line receives a longer
period of maintenance than a short-lived current release. Use the newest 24.x
patch offered by the official Node.js download page; do not search for an old
patch number copied from a screenshot.

## 0.2 Install Node.js on Windows, step by step

If `node --version` already reports `v24.x.x`, continue to Section 0.4. Otherwise,
use the following sequence.

1. Open a browser and visit the official download page at
   `https://nodejs.org/en/download`.
2. Select the latest **LTS** release in the 24.x line and the Windows Installer
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
same: a new terminal must report Node.js 24 and a working npm command.

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

### Why are these two files separate?

The two files answer different questions. `hello-browser.html` is the document
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

Read the two files as a small contract:

| File | Responsibility | What you can observe |
|---|---|---|
| `hello-browser.html` | Supplies the document structure and requests the script | The page heading and the `<script src="hello-browser.js">` element |
| `hello-browser.js` | Runs JavaScript instructions in the browser host | The two messages in Developer Tools > Console |

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

The Console is a developer evidence panel, not part of the visible web page.
Changing page content uses the DOM and begins in Chapter 5. For now, logging is a
controlled way to observe values without adding another new concept.

## 0.7 Read the first failures instead of starting over

An error message is a report about an attempted operation. Read it before
changing anything. Table 4.4 maps common observations to the first useful check.

**Table 4.4 - First-run symptoms, meanings, and next checks**

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

Figure 4.4 separates the language from two environments that can execute it.
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

Table 4.5 collects the value categories used in this chapter. The examples are
values, while the final column explains the boundary that matters in programs.

**Table 4.5 - JavaScript values introduced in this chapter**

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
`if` branch. Figure 4.5 traces tokens through evaluation and assignment.

<!-- figure:javascript-evaluation -->

Evaluation works from smaller expressions toward a result. In
`capacity - registered`, JavaScript first reads the two operand values and then
applies subtraction. Parentheses make grouping explicit. Prefer
`(registered / capacity) * 100` to relying on a reader to remember every
precedence rule. Parentheses do not turn a value into a function call unless they
follow a callable expression.

## 2.2 `const` and `let`

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
Do not use `var` in new course code; its function scope and hoisting rules obscure
the block-scoped model students need first.

`const` does not freeze an object:

```js
const event = { registered: 62 };
event.registered = 63; // mutation is allowed
// event = {};         // rebinding would fail
```

The binding remains connected to the same object; a property inside that object
changed. Figure 4.8 later makes this distinction visible.

## 2.3 Strings and template literals

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

Figure 4.6 is a decision flow, not three independent tests. Once one condition
succeeds, execution skips the remaining branches and continues after the chain.

The expression inside `if (...)` is the condition. The braces delimit a block.
Indentation does not control execution, but it exposes the block structure to
human readers and should match the braces. Trace a branch by writing the current
input, the boolean result of each condition actually reached, the selected
branch, and the value after the chain. This prevents guessing from the final line
alone.

<!-- figure:javascript-control-flow -->

## 4.1 Loops repeat with a changing state

Use `for...of` when you need each value in an iterable collection.

```js
for (const event of events) {
  console.log(event.title);
}
```

On each iteration, `event` is bound to the next array value. The body runs once
for that value. With three events, the body runs three times. The loop itself
does not create a new array; it performs the statements in its body.

A counted loop exposes initialization, continuation condition, and update in one
header.

```js
for (let index = 0; index < events.length; index += 1) {
  console.log(index, events[index].title);
}
```

First `index` is initialized to zero. Before each iteration,
`index < events.length` is tested. After the body, `index += 1` increases the
index. Replacing `<` with `<=` would attempt one index beyond the last element
because the final valid index is `length - 1`.

Use a counted `for` loop when the index itself matters, and a `while` loop when
repetition is governed by a condition whose number of iterations is not known in
advance. Every loop needs a progress argument: identify what changes and why the
condition must eventually become false. `break` exits the nearest loop;
`continue` skips to its next iteration. Avoid `for...in` for array values because
it iterates enumerable property keys rather than expressing value iteration.

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

Figure 4.7 shows one call frame. The argument is connected to the parameter, the
body evaluates using local bindings, and the result returns to the call site.

<!-- figure:function-call-boundary -->

## 5.1 Declarations, expressions, and arrow functions

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

## 5.2 Scope answers where a name is available

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

---

# 6. Arrays model ordered collections

An array stores an ordered sequence. Indexes begin at zero.

```js
const categories = ["technology", "arts", "community"];
categories[0];     // "technology"
categories.length; // 3
```

Reading beyond the existing indexes produces `undefined`; it does not wrap or
throw automatically. Methods such as `push()` mutate an array. Spread syntax can
create a shallow copy: `const copy = [...categories]`.

`length` is one greater than the highest ordinary sequential index in a dense
array. The first item is index `0`, the second is `1`, and the last is
`array.length - 1`. Arrays can technically mix value types, but application data
is easier to validate when one array has one clear element shape, such as “event
objects.” Use `Array.isArray(value)` at an untrusted boundary because
`typeof value` reports `"object"` for both arrays and ordinary objects.

## 6.1 Transformations express intent

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

Use `reduce()` when the operation is genuinely an accumulation and the accumulator
remains easy to name. A loop is preferable when it communicates the state change
more clearly to the intended reader.

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

Both bindings refer to the same object. Figure 4.8 contrasts that shared identity
with two separately copied number values. Spread creates a new outer object, but
nested objects remain shared unless copied deliberately.

<!-- figure:value-reference-identity -->

Optional chaining, as in `event.organizer?.email`, stops and produces `undefined`
when the value before `?.` is `null` or `undefined`. It does not validate that an
email is correct, and it should not hide a property that the program contract
requires.

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
actual input, and expected contract. Figure 4.9 turns those observations into a
repeatable diagnosis path.

<!-- figure:javascript-debugging -->

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

---

# Guided laboratory - Model Campus Hub event availability

## Goal and evidence

Complete `labs/week-04/events.js` so event records can be validated, classified,
filtered, and summarized. Required evidence is a passing test run, the correct
browser summary, a clean Console, and a Git commit containing only the intended
Week 4 changes.

## Step 1 - Establish the baseline

From the personal coursework repository root, prove `package.json` is present,
run `npm test`, then run `npm run serve:week04`. Open
`http://localhost:8000/`. Keep the server terminal open and use a second terminal
for tests and Git commands.

## Step 2 - Read the event shape

Open `labs/week-04/events.js`. For each property, state its type and purpose.
Predict `80 - 62` before executing code. Open Console and verify the starter table.

## Step 3 - Write one function at a time

Implement `seatsRemaining(event)`, then test it. Add `eventStatus(event)` with the
boundaries `full`, `almost full`, and `open`. Do not write all functions before
collecting evidence; one small failing-to-passing cycle localizes mistakes.

## Step 4 - Transform the collection

Implement `filterEvents(allEvents, category)` and
`summarizeEvents(allEvents)`. Preserve the input array. Use names that describe
domain meaning rather than temporary mechanics.

## Step 5 - Validate the boundary

Reject missing or non-numeric capacity and registration values with a useful
`TypeError`. Observe one deliberate failure, read its stack, repair the input,
and rerun the tests.

## Step 6 - Compare output with code

Reload the browser. The completed reference result appears in Figure 4.10. Check
all three event titles, status words, and remaining-seat counts. A visual match is
not enough; the automated tests must also pass.

<!-- media:week-04-browser-output -->

## Step 7 - Commit evidence

Run `git status`, review `git diff`, then commit the completed Week 4 files with a
message that describes the behavior, such as `Complete event availability logic`.

Use Table 4.6 as the laboratory completion record. Each row requires observable
evidence rather than a statement that the task was attempted.

**Table 4.6 - Week 4 laboratory completion record**

| Check | Expected evidence |
|---|---|
| Repository root | `package.json` is visible before npm commands |
| Automated tests | Normal, boundary, and invalid-input cases pass |
| Browser | Three correct event summaries replace the loading message |
| Console | No uncaught exception or failed module request |
| Data integrity | Filtering and summarizing do not mutate the source array |
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

---

# Session summary

- JavaScript is the course's primary programming language; hosts supply additional APIs.
- Values have types, while bindings give values names within lexical scopes.
- Prefer `const`; use `let` for deliberate reassignment.
- Strict equality and explicit conversion keep data boundaries visible.
- Branches choose paths, loops repeat with progress, and functions define contracts.
- Arrays represent ordered collections; objects represent named properties.
- Object assignment shares identity, while spread creates only a shallow copy.
- Errors and failing assertions are structured evidence.
- Small automated tests make expectations repeatable but prove only tested behavior.

## Glossary

Table 4.7 defines the chapter's working vocabulary. These definitions are
deliberately concise; the numbered sections provide the mechanisms and examples.

**Table 4.7 - Session 4 glossary**

| Term | Working definition |
|---|---|
| Argument | A value supplied at a function call site. |
| Array | An indexed, ordered object commonly used as a collection. |
| Binding | An association between an identifier and a value. |
| Boolean | The primitive logical type containing `true` and `false`. |
| Branch | One possible path selected by control flow. |
| Callback | A function supplied to another operation to be called later or for each value. |
| Coercion | Conversion performed by language rules, sometimes implicitly. |
| ECMAScript | The standardized language specification implemented as JavaScript. |
| Expression | Source code that evaluates to a value. |
| Function | A callable object that packages behavior behind parameters and a result. |
| Mutation | A change to an existing object's state. |
| Identifier | A legal source-code name used for a binding, property, or other named construct. |
| Literal | A value written directly in source code, such as `18` or `"open"`. |
| Object | A value with identity and keyed properties. |
| Parameter | A local binding declared by a function for an incoming argument. |
| Primitive | An immutable non-object value such as a string, number, or boolean. |
| Scope | The region of source code in which a binding is available. |
| Statement | Source code that performs or controls an execution step. |
| Test assertion | A comparison between observed and expected behavior. |
| Runtime | Software and host facilities that execute program instructions. |
| Source code | Human-authored program text stored in files. |
| Terminal | A text interface for running shell commands and reading their output. |

## Primary references and further reading

1. Ecma International, [ECMAScript 2026 Language Specification](https://tc39.es/ecma262/2026/). Use it as the normative authority for language semantics.
2. MDN, [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide). Use its approachable chapters for a second explanation and reference links.
3. MDN, [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript). Use it to revisit the relationship among HTML, CSS, JavaScript, and browser APIs.
4. Node.js, [Official download page](https://nodejs.org/en/download). Use it to obtain the latest supported patch release rather than copying a stale installer link.
5. Visual Studio Code, [Getting started](https://code.visualstudio.com/docs/getstarted/overview). Use it for current installation, workspace, and editor-interface guidance.
6. Node.js, [Test runner documentation](https://nodejs.org/docs/latest-v24.x/api/test.html). Use it for the tested command and test lifecycle.
7. Node.js, [Strict assertion documentation](https://nodejs.org/docs/latest-v24.x/api/assert.html). Use it to interpret equality failures and diffs.
8. Marijn Haverbeke, [Eloquent JavaScript, 4th edition](https://eloquentjavascript.net/). Use Chapters 1-6 for additional language practice.
9. Axel Rauschmayer, [Exploring JavaScript](https://exploringjs.com/js/). Use it as an optional precise language companion after the first reading.

## What changes often?

Core value, control-flow, function, array, and object semantics are stable.
New ECMAScript editions add capabilities, Node.js download versions, diagnostics,
and test-runner features evolve, and browser or editor interfaces change. Always
use the latest available Node.js 24 LTS patch compatible with the course engine
constraint. Technical review date: **21 October 2026**.

## Instructor teaching guide

### Suggested eight-hour sequence

1. Tool roles, installation verification, folders, and terminals, 45 minutes.
2. First Node.js and browser programs with evidence, 45 minutes.
3. Runtime boundary, values, bindings, and expressions, 55 minutes.
4. Operators, equality, conversion, branches, and trace tables, 60 minutes.
5. Loops, functions, returns, and scope, 60 minutes.
6. Arrays, objects, identity, and transformations, 60 minutes.
7. Errors, tests, and debugging demonstration, 35 minutes.
8. Guided laboratory and evidence review, 120 minutes.

### Demonstrations that expose misconceptions

- Run `typeof document` in browser and Node.js to separate language from host.
- Reassign a `const`, then mutate a property of a `const` object.
- Compare `0`, `"0"`, `false`, an empty string, and an empty array under strict comparison and conditions.
- Step through `eventStatus()` at 0, 10, and 11 seats.
- Copy an array with spread, mutate a nested object, and observe shallow sharing.
- Break one assertion and read actual, expected, operator, and stack evidence.

### Assessment and inclusion

Accept a trace table, spoken walkthrough, or debugger-step recording as formative
evidence when these demonstrate the same reasoning. Provide code as text rather
than images, allow additional time for syntax entry, and grade contract reasoning
separately from typing speed. A complete submission must still pass the same
behavioral tests and explain one failure repair.
