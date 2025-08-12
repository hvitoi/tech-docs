# %%
# It's used when working with unmanaged resources (like file streams).
# Ensures that the resource is gracefully closed even if exceptions are thrown
# It's syntactic sugar for try/finally blocks.

# The expression must be an object that supports the "context management protocol"
# The "context management protocol" has the methods __enter__() and __exit__()

# %%
# ---- File open ----
with open("file.txt") as file_content:
    for line in file_content:
        print(line)

# same as:
file_content = open("file.txt")
for line in file_content:
    print(line)

# %%
# ---- HTTP request ---
import httpx

with httpx.Client() as client:
    response = client.get("https://httpbin.org/get")
    print("Status:", response.status_code)
    print("Body:", response.json())
