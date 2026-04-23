# %%
from subprocess import run, CompletedProcess

res: CompletedProcess = run("ls -la", shell=True)

res.stdout
