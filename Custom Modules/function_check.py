from os import system
import sys
import json
from ansible.module_utils.basic import AnsibleModule

def run_automation():
    system("ansible-playbook checkWord.yml getWordCount.yml temperature.yml")

def buildFile(path):
    run_automation()
    checkWord = open("/Users/chandlerdespirlet/Desktop/CUSTOM_status.txt", "r")
    for line in checkWord:
        checkWordLine = line
    checkWord.close()
    tempValues  = []
    temperatureStatus = open("/Users/chandlerdespirlet/Desktop/TemperatureStatus.txt", "r")
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
        file.write(item)
    file.close()
    
def run_module():
    fields = {
        "outFile": {"type": "str", "required": "yes"},
        "output": {"type": "str", "default": "No test file analyzed!"}
    }
    module = AnsibleModule(argument_spec=fields)
    path = module.params["outFile"]
    buildFile(path)
    system("python /Users/chandlerdespirlet/TestEnv/WRTG/custom_auth.py")
    finalFile = open("/Users/chandlerdespirlet/Desktop/custom_sample_data.txt", "r")
    badOuts = []
    for line in finalFile:
        if (line != ''):
            badOuts.append(line)
    if (len(badOuts) == 0):
        module.params.update({"output": "All tests passed successfully!"})
    else:
        finalError = ''
        for item in badOuts:
            if (len(badOuts) == 1):
                finalError = finalError
            else: 
                finalError += (item + ", ")
        module.params.update({"update": finalError})
    finalFile.close()
    module.exit_json(changed=True, meta=module.params)

def main():
    run_module()

if __name__ == '__main__':
    main()