from os import makedirs
from os import path
import sys
import json
from ansible.module_utils.basic import AnsibleModule #Allows for Ansible syntax to be used.

def run_module():
    fields = {
        "directory": {"type": "str", "required": "yes"}
    }
    module = AnsibleModule(argument_spec=fields)
    file_direc = module.params["directory"]
    newpath = file_direc 
    if not path.exists(newpath):
        makedirs(newpath)
        module.exit_json(changed=True, meta=module.params)
    module.exit_json(changed=False, meta=module.params)

def main():
    run_module()

if __name__ == '__main__':
    main()