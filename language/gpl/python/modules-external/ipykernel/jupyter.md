# Jupyter Notebooks

- Combines markdown and python code to create notebooks while running python interactively
- Notebooks can be created either as `.ipynb` (standard notebooks) or as `.py` (using the `# %%` annotation)

## Kernel

- The `IPython kernel` (`ipykernel` package) is the Python execution backend for Jupyter
- To work with Jupyter Notebooks you need an environment with the jupyter package setup (such as the `Anaconda` environment)

```shell
pip install ipykernel
```

## Vscode

- On VScode, the extension `ms-toolsai.jupyter` is required
- `Ctrl + Enter` to run the cell
- `.py` annotations
  - `# %%`: python code
  - `# %% [markdown]`: markdown
