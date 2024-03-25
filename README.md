<h1 align="center">
    <br>
    <a title="Home" href="https://github.com/sidisinsane/copier-python-hatch-template">
        <img alt="Project Logo" src="mkdocs/images/logo.svg" width="200">
    </a>
    <br>
    Copier Python Hatch Template
    <br>
</h1>

<p align="center">
  <i align="center">A Copier template for Python projects managed by Hatch.</i>
</p>

<p align="center">
    <a title="License" href="https://github.com/sidisinsane/copier-python-hatch-template/blob/main/LICENSE">
        <img alt="License" src="https://img.shields.io/github/license/sidisinsane/copier-python-hatch-template">
    </a>
    <a title="CI Status" href="https://github.com/sidisinsane/copier-python-hatch-template/blob/main/.github/workflows/ci.yml">
        <img alt="CI Status" src="https://img.shields.io/github/actions/workflow/status/sidisinsane/copier-python-hatch-template/ci.yml?logo=github&label=ci">
    </a>
    <a title="CodeQL Status" href="https://github.com/sidisinsane/copier-python-hatch-template/blob/main/.github/workflows/codeql.yml">
        <img alt="CodeQL Status" src="https://img.shields.io/github/actions/workflow/status/sidisinsane/copier-python-hatch-template/codeql.yml?logo=github&label=codeql">
    </a>
    <a title="Deploy Status" href="https://github.com/sidisinsane/copier-python-hatch-template/blob/main/.github/workflows/deploy.yml">
        <img alt="Deploy Status" src="https://img.shields.io/github/actions/workflow/status/sidisinsane/copier-python-hatch-template/deploy.yml?logo=github&label=deploy">
    </a>
    <a title="Test Status" href="https://github.com/sidisinsane/copier-python-hatch-template/blob/main/.github/workflows/test.yml">
        <img alt="Test Status" src="https://img.shields.io/github/actions/workflow/status/sidisinsane/copier-python-hatch-template/test.yml?logo=github&label=test">
    </a>
</p>

<p align="center">
    <a title="Python Version" href="https://www.python.org/">
        <img alt="Python Version" src="https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/sidisinsane/copier-python-hatch-template/main/pyproject.toml&logo=python&logoColor=white&label=Python">
    </a>
    <a title="Copier" href="https://copier.readthedocs.io/en/stable/">
        <img alt="Copier" src="https://img.shields.io/badge/Copier-4b5563">
    </a>
    <a title="Hatch" href="https://github.com/pypa/hatch">
        <img alt="Hatch" src="https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg">
    </a>
    <a title="Material for MkDocs" href="https://squidfunk.github.io/mkdocs-material/">
        <img alt="Material for MkDocs" src="https://img.shields.io/badge/Material_for_MkDocs-526CFE?logo=MaterialForMkDocs&logoColor=white">
    </a>
    <a title="Pytest" href="https://pytest.org/">
        <img alt="Pytest" src="https://img.shields.io/badge/Pytest-0a9edc?logo=pytest&amp;logoColor=white&labelColor=4b5563">
    </a>
    <a title="Markdownlint" href="https://github.com/DavidAnson/markdownlint">
        <img alt="Markdownlint" src="https://img.shields.io/badge/Markdownlint-000000?logo=markdown&amp;logoColor=white&labelColor=4b5563">
    </a>
    <a title="Commitlint" href="https://commitlint.js.org/">
        <img alt="Commitlint" src="https://img.shields.io/badge/Commitlint-3451b2?logo=commitlint&amp;logoColor=white&labelColor=4b5563">
    </a>
    <a title="Ruff" href="https://docs.astral.sh/ruff/">
        <img alt="Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json">
    </a>
    <a title="Bandit" href="https://github.com/PyCQA/bandit">
        <img alt="Bandit" src="https://img.shields.io/badge/Bandit-4b5563">
    </a>
    <a title="Mypy" href="https://mypy-lang.org/">
        <img alt="Mypy" src="https://img.shields.io/badge/Mypy-4b5563">
    </a>
</p>

---

## Prerequisites

### Copier

[Copier](https://copier.readthedocs.io/en/stable/) is a library and CLI app for rendering project templates.

#### Install Copier

> [!IMPORTANT]
> If you haven't already, install `pipx` first: `pip install --user pipx`.

```shell
pipx install copier
```

#### Inject Copier Templates Extensions

```shell
pipx inject copier copier-templates-extensions
```

### Hatch

[Hatch](https://hatch.pypa.io/latest/) is a modern, [PEP 621](https://peps.python.org/pep-0621/) compliant, extensible Python project manager.

#### Install Hatch

```shell
pipx install hatch
```

#### Configure Hatch

Store virtual environments in a directory named `.hatch` in each project directory.

```shell
hatch config set dirs.env.virtual .hatch
```

> [!NOTE]
> This adds the following to the configuration:
>
> ```toml
> [dirs.env]
> virtual = ".hatch"
> ```
>
> The [Configuration for Hatch](https://hatch.pypa.io/latest/config/hatch/) is stored in a `config.toml` file at i.e. `~/Library/Application Support/hatch` on macOS.

## Usage

### Generate a Project

```shell
copier copy --trust https://github.com/sidisinsane/copier-python-hatch-template.git PATH/TO/DESTINATION
```

or

```shell
copier copy --trust gh:sidisinsane/copier-python-hatch-template PATH/TO/DESTINATION
```

> [!NOTE]
> You can also clone the project template using `git clone https://github.com/sidisinsane/copier-python-hatch-template.git`, modify it and generate a project the locally cloned repo.
>
> ```shell
> copier copy --trust PATH/TO/CLONED/PROJECT/TEMPLATE PATH/TO/DESTINATION
> ```

## Aftermath

### Create Virtual Environment

```shell
cd PATH/TO/DESTINATION && hatch env create
```

> [!NOTE]  
> You can locate environments by running `hatch env find`.

### Install Pre-Commit Hooks

```shell
git init && hatch run dev:pre-commit-install
```

> [!NOTE]  
> After you have created a new empty GitHub project, you are ready to make your initial commit.
>
> ```shell
> git add .
> git commit -m "initial commit"
> git branch -M main
> git remote add origin <https://github.com/REPO_NAMESPACE/REPO_NAME.git>
> git push -u origin main
> ```

See the [documentation](https://sidisinsane.github.io/copier-python-hatch-template/) for more details.
