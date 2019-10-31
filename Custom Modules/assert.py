from os import system
import sys
import json
from ansible.module_utils.basic import AnsibleModule

def run_automation():
    system("ansible-playbook checkWord.yml getWordCount.yml temperature.yml")

def buildFile():
    checkWord = open("/Users/chandlerdespirlet/Desktop/CUSTOM_status.txt", "r")
    for line in checkWord:
        checkWordLine = line
    checkWord.close()
    
    file = open("/Users/chandlerdespirlet/Desktop/Custom_Check.txt", "w+")
