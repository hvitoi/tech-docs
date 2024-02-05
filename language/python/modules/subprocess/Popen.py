import subprocess

p = subprocess.Popen(
    "dmidecode -s system-product-name",
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
stdout, stderr = p.communicate()
