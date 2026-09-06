# Prerequisites

This course starts from physics problems, not programming basics. The first lab
assumes you can write a short Python script, move around a terminal, use Git,
and edit files in an IDE (integrated development environment). If any of that is
unfamiliar, the material below closes the gap — do it **before the second
class**, not alongside it.

!!! info "How much time to allow"
    Allow roughly **5–10 hours** in total if all four areas are new to you, and
    an hour or two if you are only refreshing. Python is the one that matters
    most; the terminal, Git, and IDE sections are short.

## :material-language-python: Python

You should be comfortable with variables, lists and dictionaries, `for` loops,
`if` statements, writing and calling functions, and importing a module.

| Resource | Use it for |
| --- | --- |
| [W3Schools Python tutorial](https://www.w3schools.com/python/python_intro.asp) | Working through the language from the start, or looking up one topic |
| [Python 101](https://github.com/Python-Crash-Course/Python101) | Practising with real code once you know the syntax |

!!! tip "Read less, type more"
    Reading about a language is not the same as being able to use it. Type the
    examples out yourself rather than copying them, and change something in each
    one to see what breaks.

## :material-console: Terminal and command line

You will use a terminal to manage course materials, run training scripts, and
work on NSTC Core. You need to be able to move between directories, list and
inspect files, and copy, move, and delete them.

| Resource | Use it for |
| --- | --- |
| [The Linux command line for beginners](https://ubuntu.com/tutorials/command-line-for-beginners#5-moving-and-manipulating-files) | Navigation and file handling — sections 1–5 are the relevant part |

The commands worth knowing by the second class are `pwd`, `ls`, `cd`, `mkdir`,
`cp`, `mv`, `rm`, and `cat`.

!!! warning "`rm` does not ask twice"
    There is no recycle bin on the command line, and none on a compute cluster.
    Check what directory you are in with `pwd` before deleting anything.

## :material-git: Git and GitHub

Git is used for version control throughout the course, and course materials and
assignments are distributed through it. You need a **GitHub account**, and you
should be able to clone a repository, commit a change, and push it back.

| Resource | Use it for |
| --- | --- |
| [Hello World](https://docs.github.com/en/get-started/using-github/hello-world) | Creating an account and a repository, and making your first commit — about half an hour |

The commands worth knowing are `git clone`, `git status`, `git add`, `git
commit`, `git push`, and `git pull`.

!!! tip "Commit small and often"
    A commit is a checkpoint you can return to. Commit whenever something works,
    with a message saying what changed — not once at the end of the week.

## :material-code-braces: IDE

Any IDE will do, but the course demonstrations and screenshots use **Visual
Studio Code**, and the teaching assistants can help you with it most easily.

| Resource | Use it for |
| --- | --- |
| [VS Code introductory videos](https://code.visualstudio.com/docs/introvideos/basics) | Getting oriented in VS Code in about half an hour |
| [Jupyter notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) | **Running the course notebooks on your own machine** rather than in Colab |

Two extensions are worth installing at the same time: **Python** and **Jupyter**,
both published by Microsoft. Together they let you open and run a `.ipynb` file
directly in the editor.

!!! tip "If you want to run the notebooks locally"
    Nothing requires a local setup, but it is faster than Colab and gives you a
    real debugger. Follow the guide above, and point the kernel at the
    environment created by `uv sync` — see [Software setup](#software-setup) —
    so your package versions match the ones the course pins.

## :material-function-variant: Mathematics

Basic linear algebra, calculus, and probability are assumed. There is no
preparatory reading to do here — the relevant ideas are reintroduced as they come
up, starting with estimators and the bias–variance trade-off in Session 3.

## :material-package-variant-closed: Software setup

### Python environment with `uv`

We use [`uv`](https://docs.astral.sh/uv/) to install Python packages and keep
course environments reproducible.

Install it using the
[official instructions](https://docs.astral.sh/uv/getting-started/installation/),
or run:

=== "macOS and Linux"

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Windows PowerShell"

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

Open a new terminal and confirm the installation:

```bash
uv --version
```

After downloading course materials, create or update the project environment
and run Python with:

```bash
uv sync
uv run python your_script.py
```

`uv sync` installs the exact dependencies recorded by the course. You normally
do not need to activate the `.venv` directory manually. See the
[`uv` project guide](https://docs.astral.sh/uv/guides/projects/) for additional
commands.

## :material-clipboard-list-outline: Before the second class

1. Install [VS Code](https://code.visualstudio.com/), with the Python and Jupyter extensions.
2. Confirm you can open a terminal and run `python3 --version`.
3. Write and run one short Python script of your own — anything at all.
4. Create a [GitHub](https://github.com/) account and make one commit in a test repository.
5. Sign in to [Google Colab](https://colab.research.google.com/) and open a blank notebook.
6. Create a [Kaggle](https://www.kaggle.com/) account.

Accounts for course services and NSTC Core are handled separately, in the first
weeks of term — see the [Resources](resources.md) page for those.

!!! question "Still unsure whether you are ready?"
    Come to the first class anyway. The first week of class is an ungraded
    orientation, and everything covered in it can be caught up afterwards. If you are worried
    about the gap, say so early rather than late — email the
    [instructor or a teaching assistant](index.md#teaching-team).
