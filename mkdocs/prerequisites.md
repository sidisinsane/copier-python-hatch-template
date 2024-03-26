---
weight: 0
---
# Prerequisites

<p>
<a title="Git" href="https://git-scm.com/">
    <img alt="Git" src="https://img.shields.io/badge/Git-1f2328?logo=git">
</a>
<a title="Asdf" href="https://asdf-vm.com/">
    <img alt="Asdf" src="https://img.shields.io/badge/Asdf-4e443c">
</a>
<a title="Python Version" href="https://www.python.org/">
    <img alt="Python Version" src="https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/sidisinsane/copier-python-hatch-template/main/pyproject.toml&logo=python&logoColor=white&label=Python">
</a>
<a title="Copier" href="https://copier.readthedocs.io/en/stable/">
    <img alt="Copier" src="https://img.shields.io/badge/Copier-4b5563">
</a>
<a title="Hatch" href="https://github.com/pypa/hatch">
    <img alt="Hatch" src="https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg">
</a>
<a title="GitHub" href="https://github.com/">
    <img alt="GitHub" src="https://img.shields.io/badge/GitHub-1f2328?logo=github">
</a>
</p>

## Git

[Git](https://git-scm.com/) is a free and open source distributed version control system.

### Install

| OS    | Package Manager | Command                       |
|-------|-----------------|-------------------------------|
| linux | Aptitude        | `apt install git`             |
| linux | DNF             | `dnf install git`             |
| linux | Pacman          | `pacman -S git`               |
| linux | Zypper          | `zypper install git`          |
| macOS | Homebrew        | `brew install coreutils git`  |
| macOS | Spack           | `spack install coreutils git` |

!!! note
    Check if `git` is already installed by running `git -v` before installing.

## Asdf

[Asdf](https://asdf-vm.com/) is a multiple runtime version manager.

### Install Asdf

[Visit the asdf getting started page](https://asdf-vm.com/guide/getting-started.html) for detailed instructions.

## Python 3

[Python](https://www.python.org/) is an interpreted, object-oriented, high-level programming language with dynamic semantics.

### Install Asdf Python Plugin

```shell
asdf plugin add python
```

??? note
    To list all **installed** plugins run `asdf plugin list`.
    To list all **available** plugins run `asdf plugin list all`.

### Install Python Version

```shell
asdf install python latest
```

or

```shell
asdf install python 3.12.2
```

??? note
    To list all **installed** python versions run `asdf list python`.
    To list all **available** python versions run `asdf list all python`.

### Set a Default Python Version

```shell
asdf global python latest
```

or

```shell
asdf global python 3.12.2
```

### Set a Python Version for Your Project

```shell
cd PATH/TO/PROJECT && asdf local python latest
```

or

```shell
cd PATH/TO/PROJECT && asdf local python 3.12.2
```

??? note
    The local Python version will be set in a `.tool-versions` file within the current directory.
    `.tool-versions`
    ```text
    python 3.12.2
    ```

## Copier

[Copier](https://copier.readthedocs.io/en/stable/) is a library and CLI app for rendering project templates.

### Install Copier

???+ note "Requirement"

    If you haven't already, install `pipx` first: `pip install --user pipx`.

```shell
pipx install copier
```

### Inject Copier Templates Extensions

```shell
pipx inject copier copier-templates-extensions
```

## Hatch

[Hatch](https://hatch.pypa.io/latest/) is a modern, [PEP 621](https://peps.python.org/pep-0621/) compliant, extensible Python project manager.

### Install Hatch

```shell
pipx install hatch
```

### Configure Hatch

Store virtual environments in a directory named `.hatch` in each project directory.

```shell
hatch config set dirs.env.virtual .hatch
```

??? note

    This adds the following to the configuration:
    ```toml
    [dirs.env]
    virtual = ".hatch"
    ```
    The [Configuration for Hatch](https://hatch.pypa.io/latest/config/hatch/) is stored in a `config.toml` file at i.e. `~/Library/Application Support/hatch` on macOS.

## GitHub

You will need a [GitHub](https://github.com/) account for the [GitHub Actions workflow](https://docs.github.com/en/actions/using-workflows).
