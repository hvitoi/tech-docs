#!/usr/bin/env python
import subprocess
import json
import sys

# output = subprocess.check_output(
#     "wpctl status",
#     shell=True,
#     encoding='utf-8',
# )

# # remove the ascii tree characters and return a list of lines
# lines = output.replace("├", "").replace("─", "").replace(
#     "│", "").replace("└", "").splitlines()


# sys.stdout.write(str(output))
# # get the index of the Sinks line as a starting point
# sinks_index = None
# for index, line in enumerate(lines):
#     if "Sinks:" in line:
#         sinks_index = index
#         break

# # start by getting the lines after "Sinks:" and before the next blank line and store them in a list
# sinks = []
# for line in lines[sinks_index + 1:]:
#     if not line.strip():
#         break
#     sinks.append(line.strip())

# # remove the "[vol:" from the end of the sink name
# for index, sink in enumerate(sinks):
#     sinks[index] = sink.split("[vol:")[0].strip()

# # strip the * from the default sink and instead append "- Default" to the end. Looks neater in the wofi list this way.
# for index, sink in enumerate(sinks):
#     if sink.startswith("*"):
#         sinks[index] = sink.strip().replace("*", "").strip() + " - Default"

# # make the dictionary in this format {'sink_id': <int>, 'sink_name': <str>}
# sinks_dict = [
#     {
#         "sink_id": int(sink.split(".")[0]),
#         "sink_name": sink.split(".")[1].strip()
#     }
#     for sink in sinks
# ]


# sys.stdout.write(json.dumps(sinks_dict))


sinks_json = subprocess.check_output(
    "pactl -f json list sinks",
    shell=True,
    encoding="utf-8",
)
sinks = json.loads(sinks_json)


sinks_processed = [
    sink["index"] for sink in sinks for sink in sinks if sink["index"] == 39
]

sys.stdout.write(json.dumps(sinks_processed))
