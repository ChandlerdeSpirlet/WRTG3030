from os import system
import sys
import json
from ansible.module_utils.basic import AnsibleModule

def process_file(path):
    system("python /Users/chandlerdespirlet/Desktop/Temperature_Analysis.py -i 2")
    values = []
    file = open(path, "r")
    counter = 0
    for line in file:
        if (counter == 0):
            values.append(str(line[21:len(line) - 1]) + "F")
        if (counter == 1):
            values.append(str(line[21:len(line) - 1]) + "%")
        if (counter == 2):
            values.append(str(line[15:20]) + " " + str(line[23:24]) + " hours" + " " + str(line[25:27]) + " minutes")
        if (counter == 3):
            values.append(str(line[17:len(line) - 1]) + "F")
        if (counter == 4):
            values.append(str(line[17:len(line) - 1]) + "F")
        if (counter == 5):
            values.append(str(line[14:len(line) - 1]) + "%")
        if (counter == 6):
            values.append(str(line[14:len(line)]) + "%")
        counter += 1
    file.close()
    return values

def run_module():
    fields = {
        "script": {"type": "str", "required": "yes"},
        "avg_temp": {"type": "str", "default": "0.0"},
        "avg_humidity": {"type": "str", "default": "0"},
        "time_elapsed": {"type": "str", "default": "NULL"},
        "max_temp": {"type": "str", "default": "0.0"},
        "min_temp": {"type": "str", "default": "0.0"},
        "max_humidity": {"type": "str", "default": "0"},
        "min_humidity": {"type": "str", "default": "0"}
    }
    module = AnsibleModule(argument_spec=fields)
    path = module.params["script"]
    values = process_file(path)
    module.params.update({"avg_temp": values[0]})
    module.params.update({"avg_humidity": values[1]})
    module.params.update({"time_elapsed": values[2]})
    module.params.update({"max_temp": values[3]})
    module.params.update({"min_temp": values[4]})
    module.params.update({"max_humidity": values[5]})
    module.params.update({"min_humidity": values[6]})
    module.exit_json(changed=True, meta=module.params)

def main():
    run_module()

if __name__ == '__main__':
    main()