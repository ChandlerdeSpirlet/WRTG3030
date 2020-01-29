import sys
import json
from ansible.module_utils.basic import AnsibleModule

def writeToFile(status):
    file = open("/Users/chandlerdespirlet/Desktop/CUSTOM_status.txt", "w+")
    if (status):
        file.write("The desired string IS present in the file.")
    else:
        file.write("The desired string IS NOT present in the file.")
    file.close()

def run_module():
    fields = {
        "FilePath": {"type": "str", "required": "yes"},
        "SearchWord": {"type": "str", "required": "yes"},
        "isPresent": {"type": "int", "default": 0}
    }
    module = AnsibleModule(argument_spec=fields)
    path = module.params["FilePath"]
    wordToFind = module.params["SearchWord"]
    present = module.params["isPresent"]
    searchfile = open(path, "r")
    for line in searchfile:
        for word in line.split():
            if wordToFind in word:
                present += 1
                break
    searchfile.close()
    writeToFile(present)
    module.params.update({"isPresent": present})
    module.exit_json(changed=True, meta=module.params)

def main():
    run_module()

if __name__ == '__main__':
    main()