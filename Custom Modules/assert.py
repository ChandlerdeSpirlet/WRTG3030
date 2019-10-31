from os import system
import sys
import json
from ansible.module_utils.basic import AnsibleModule

def run_automation():
    system("ansible-playbook checkWord.yml getWordCount.yml temperature.yml")

def buildFile(path):
    checkWord = open("/Users/chandlerdespirlet/Desktop/CUSTOM_status.txt", "r")
    for line in checkWord:
        checkWordLine = line
    checkWord.close()
    tempValues  = []
    temperatureStatus = open("/Users/chandlerdespirlet/Desktop/CUSTOM_temp.txt", "r")
    for line in temperatureStatus:
        tempValues.append(line)
    temperatureStatus.close()
    wordCount = open("/Users/chandlerdespirlet/Desktop/count_output.txt", "r")
    for line in wordCount:
        wordCountText = line
    wordCount.close()
    
    file = open(path, "w+")
    file.write(checkWordLine + '\n' + wordCountText + '\n')
    for item in tempValues:
        file.write(item + '\n')
    file.close()
    
def run_module():
    fields = {
        "OutputFile": {"type": "str", "required": "yes"}
    }
    path = module.params["OutputFile"]
    run_automation()
    buildFile(path)
    module = AnsibleModule(argument_spec=fields)
    module.exit_json(changed=True, meta=module.params)

def main():
    run_module()

if __name__ == '__main__':
    main()