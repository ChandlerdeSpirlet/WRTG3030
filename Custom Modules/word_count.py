import sys
import json
from ansible.module_utils.basic import AnsibleModule

def run_module():
    fields = {
        "FilePath": {"type": "str", "required": "yes"},
        "SearchWord": {"type": "str", "required": "yes"},
        "count": {"type": "int", "default": -1}
    }
    module = AnsibleModule(argument_spec=fields)
    path = module.params["FilePath"]
    wordToFind = module.params["SearchWord"]
    searchfile = open(path, "r")
    counter = 0
    for line in searchfile:
        for word in line.split():
            if wordToFind in word:
                counter += 1
    searchfile.close()
    module.params.update({"count": counter})
    module.exit_json(changed=True, meta=module.params)

def main():
    run_module()

if __name__ == '__main__':
    main()