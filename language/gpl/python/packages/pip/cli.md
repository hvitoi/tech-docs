# pip cli

## list

- The packages shown are coupled to the pip binary ran
- If you ran the pip binary from your venv you will probably have several project dependencies
- If you the the pip binary from the system-wide installed you will have few dependencies, usually the packages "pip", "wheel" and "packaging"

```shell
pip list
```

## show

- Show information about a package, including where it is installed and its dependencies

```shell
pip show "pip"
```

## install

```shell
# install a package globally
pip install numpy
pip install "numpy[standard]" # specify version

# upgrade package to the newest version (install or upgrade it)
pip install --upgrade pip # -U upgrade pip itself

# install from a directory
git clone https://github.com/squidfunk/mkdocs-material.git
pip install -e mkdocs-material

# install from requirements file
pip install -r requirements.txt
pip install --no-cache-dir --upgrade -r /code/requirements.txt # Do not save downloaded packages into pip's local cache directory (usually ~/.cache/pip). Doesn't make sense in production environment, in which you won't reuse the cache. Also also saves disk space
```

## freeze

- Lists all the dependencies and creates a `requirements.txt` file
- This file contains the direct dependencies required
- To install them all run `pip install -r requirements.txt`
- Requirements file does not store the hash of the dependencies, so it might potentially be unsafe

```shell
pip freeze
```

```txt
mkdocs==1.5.2
mkdocs-material==9.1.21
mkdocs-redirects==1.2.1
```
