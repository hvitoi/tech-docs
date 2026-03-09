# %%
import re

re.search(r"-(prod|staging|test)$", "br-prod")


# %%

slack_link = "https://company.slack.com/archives/C123ABC/p1234567890123456"
match: re.Match[str] = re.search(r"/archives/([^/]+)/p(\d+)", slack_link)

if not match:
    raise Exception(f"Could not extract thread info from: {slack_link}")

channel_id = match.group(1)
ts = match.group(2)
thread_ts = f"{ts[:10]}.{ts[10:]}"  #  1234567890123456 -> 1234567890.123456

if not channel_id or not thread_ts:
    raise Exception(f"Could not extract thread info from: {slack_link}")
# return "C0AHXKUJJ6S", "1772532939.905959"
# # return channel_id, thread_ts
# # If a match is not found, returns None
