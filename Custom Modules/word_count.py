import sys
import json
from ansible.module_utils.basic import AnsibleModule

def writeToFile(count, word):
    outputFile = open("/Users/chandlerdespirlet/Desktop/count_output.txt", "w+")
    outputFile.write("Word count for search word: " + word + " is " + count)
    outputFile.close()

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
    writeToFile(counter, wordToFind)
    module.params.update({"count": counter})
    module.exit_json(changed=True, meta=module.params)

def main():
    run_module()

if __name__ == '__main__':
    main()