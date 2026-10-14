# Getting Started with Anaconda

A quick-reference guide for installing Anaconda and managing Python environments and packages with `conda`.

## Table of Contents

- [What Is Conda?](#what-is-conda)
- [Installation and Setup](#installation-and-setup)
- [Managing Conda Itself](#managing-conda-itself)
- [Managing Environments](#managing-environments)
- [Managing Packages](#managing-packages)
- [Channels](#channels)
- [Using pip Inside a Conda Environment](#using-pip-inside-a-conda-environment)
- [Sharing and Reproducing Environments](#sharing-and-reproducing-environments)
- [Cleaning Up and Configuration](#cleaning-up-and-configuration)
- [Troubleshooting](#troubleshooting)
- [Command Cheat Sheet](#command-cheat-sheet)
- [Further Reading](#further-reading)

## What Is Conda?

[Conda](https://github.com/conda/conda) is an open-source, cross-platform, language-agnostic package manager **and** environment manager. It runs on Windows, macOS, and Linux. It was created for Python, but it can install and manage software written in other languages too (R, C/C++, Java, and more).

- **Package manager:** finds, installs, and updates packages together with their dependencies.
- **Environment manager:** creates separate, isolated installations so different projects can use different Python and package versions without conflicts. An environment can be thought of as a completely separate installation.

### Anaconda, Miniconda, and Miniforge

| Distribution | What you get |
| ------------ | ------------ |
| **Anaconda Distribution** | `conda` plus a large set of pre-installed data-science packages and tools (e.g. Anaconda Navigator). Large download. |
| **Miniconda** | `conda` plus Python and a minimal set of packages. Small download; you install everything else yourself. |
| **Miniforge** | Like Miniconda, but community-maintained and configured to use the `conda-forge` channel by default. |

> **Note:** Anaconda's default channels are subject to Anaconda's terms of service, which may require a paid license for some organizations. Check the [Anaconda website](https://www.anaconda.com/) for current terms, or consider Miniforge / `conda-forge` if this applies to you.

## Installation and Setup

1. Download and install Anaconda from the [official website](https://www.anaconda.com/download). (Prefer a lighter install? Use Miniconda or Miniforge instead; the commands below are the same.)

2. Activate it. Replace `~/anaconda3` with the directory where you installed Anaconda:

   ```bash
   source ~/anaconda3/bin/activate
   conda init
   ```

   `conda init` adds startup code to your shell configuration. To target a specific shell, pass its name, e.g. `conda init zsh` or `conda init bash`. On Windows, use **Anaconda Prompt** (or `conda init powershell`).

3. Restart your terminal. The prompt should now show the active environment:

   ```bash
   (base) max@223ubuntu:~/workspace/machineLearning$
   ```

4. Verify the installation:

   ```bash
   conda --version
   conda info
   ```

> **Tip:** To leave the current environment (and return to the plain shell if you are in `base`), run:
>
> ```bash
> conda deactivate
> ```

> **Tip:** If you don't want `base` activated every time you open a terminal:
>
> ```bash
> conda config --set auto_activate_base false
> ```
>
> (On newer versions the option is `auto_activate`.) Then run `conda activate` whenever you need it.

## Managing Conda Itself

Keep conda up to date. Always update it from the `base` environment:

```bash
conda update --name base conda
```

Install a specific conda version:

```bash
conda install --name base conda=<version>
```

## Managing Environments

> **Best practice:** Avoid installing project packages into `base`. Create a dedicated environment per project.

### Create an environment

```bash
conda create --name envName python=3.11
```

Create an environment and install packages in one step:

```bash
conda create --name envName python=3.11 numpy pandas
```

Create an environment at a specific path instead of the default location:

```bash
conda create --prefix ./envs/myenv python=3.11
```

### List all environments

```bash
conda env list
```

The active environment is marked with `*`.

### Switch to an environment

```bash
conda activate envName
```

The prompt changes from `(base)` to `(envName)`. Activating puts the environment's `bin` directory at the front of your `PATH`, so its `python` and tools take priority.

### Clone an environment

```bash
conda create --name newEnv --clone envName
```

### Rename an environment

```bash
conda rename --name oldName newName
```

On older conda versions, clone the environment and remove the old one instead.

### Remove an environment

```bash
conda env remove --name envName
```

## Managing Packages

> Make sure the target environment is activated first, or add `--name envName` to the command.

### Search for a package

```bash
conda search packageName
```

### Install a package

```bash
conda install packageName
```

Install several packages at once (recommended, so the solver can resolve them together):

```bash
conda install numpy pandas matplotlib
```

Install a specific version:

```bash
conda install packageName=1.2.3
```

Install from a specific channel:

```bash
conda install --channel conda-forge packageName
```

Install into another environment without activating it:

```bash
conda install --name envName packageName
```

### List installed packages

```bash
conda list
```

Filter by name (regular expressions are supported):

```bash
conda list numpy
```

### Update packages

```bash
conda update packageName          # one package
conda update --all                # every package in the environment
```

### Remove a package

```bash
conda remove --name envName packageName
```

## Channels

Channels are the locations (on [anaconda.org](https://anaconda.org)) where conda looks for packages. Common ones:

- `defaults`: packages maintained by Anaconda.
- `conda-forge`: a large, community-driven channel.

View, add, and prioritize channels:

```bash
conda config --show channels
conda config --add channels conda-forge
conda config --set channel_priority strict
```

> **Tip:** Mixing channels can cause dependency conflicts. Pick one primary channel and set `channel_priority strict` for more predictable results.

## Using pip Inside a Conda Environment

Prefer `conda install` whenever a package is available. If a package is only on PyPI:

1. Install `pip` into the environment first: `conda install pip`
2. Activate the environment, then run `pip install packageName`

> **Tip:** Install conda packages first and pip packages last. Re-running `conda install` after `pip install` can overwrite or break pip-installed packages.

## Sharing and Reproducing Environments

Export the active environment to a YAML file:

```bash
conda env export > environment.yml
```

To share across operating systems, export only the packages you explicitly installed:

```bash
conda env export --from-history > environment.yml
```

Recreate an environment from that file:

```bash
conda env create --file environment.yml
```

Update an existing environment from the file:

```bash
conda env update --name envName --file environment.yml --prune
```

A minimal `environment.yml` looks like this:

```yaml
name: myenv
channels:
  - conda-forge
dependencies:
  - python=3.11
  - numpy
  - pandas
  - pip
  - pip:
      - some-pypi-only-package
```

## Cleaning Up and Configuration

Remove cached package tarballs and unused packages to free disk space:

```bash
conda clean --all
```

View your current configuration:

```bash
conda config --show
conda info
```

## Troubleshooting

| Problem | Things to try |
| ------- | ------------- |
| `conda: command not found` | Run `source ~/anaconda3/bin/activate` then `conda init`, and restart the terminal. Check that the install path is correct. |
| Environment not activating in a script | Run `conda init` for your shell, or use `conda run --name envName command`. |
| "Solving environment" takes very long or fails | Install fewer packages at once, use a single channel, update conda (`conda update --name base conda`), or create a fresh environment. |
| Package conflicts after mixing pip and conda | Recreate the environment; install conda packages first, pip packages last. |
| Wrong Python is used | Run `which python` (Linux/macOS) or `where python` (Windows) and confirm the right environment is active. |

## Command Cheat Sheet

| Task                     | Command                                          |
| ------------------------ | ------------------------------------------------ |
| Activate base            | `source ~/anaconda3/bin/activate`                |
| Initialize shell         | `conda init`                                     |
| Check version            | `conda --version`                                |
| Update conda             | `conda update --name base conda`                 |
| Deactivate environment   | `conda deactivate`                               |
| Create environment       | `conda create --name envName python=3.11`        |
| List environments        | `conda env list`                                 |
| Switch environment       | `conda activate envName`                         |
| Clone environment        | `conda create --name newEnv --clone envName`     |
| Remove environment       | `conda env remove --name envName`                |
| Search package           | `conda search packageName`                       |
| Install package          | `conda install packageName`                      |
| Update package           | `conda update packageName`                       |
| List packages            | `conda list`                                     |
| Remove package           | `conda remove --name envName packageName`        |
| Export environment       | `conda env export > environment.yml`             |
| Create from file         | `conda env create --file environment.yml`        |
| Clean cache              | `conda clean --all`                              |

## Further Reading

- [conda on GitHub](https://github.com/conda/conda)
- [Official conda documentation](https://docs.conda.io)
- [Anaconda Distribution](https://www.anaconda.com/download)
- [conda-forge](https://conda-forge.org)
