import telebot
from jira import JIRA
import re

def SendToTelegram(send_message):
   TOKEN  = '638688644:AAHL4FlM0InqWhi6WQCG4V1PVsiPO_w2fag'
   tb = telebot.TeleBot(TOKEN)
   tb.send_message(-314248112,send_message)
def GetVersion(pach_tofile):
   w= 'version'
   with open(pach_tofile,'r' ) as f:
        for line in f:
          if w  in line:
            reg = re.compile('[^0-9v.-]')
            version = reg.sub('', line)
   return version
def Jira():
    # set works server
    if __name__ == "__main__":

       options = {

       'server': 'https://dev.intecracy.com/jira/',

       'verify': False,

       'rest_api_version': '2'
    }
    wfnb = []
    ibwfbn = []
    version = GetVersion('/home/xmelayx/telebot/vetsion')
# login & passwd basic_auth
    jira = JIRA(options, basic_auth=('Aziot', '!QAZ2wsx'))
    # variables of project
    issue_project_wfnb = jira.search_issues('project=NECTAIN and status=RESOLVED and type=Bug and cf[11970] = "Waiting for next build" ' , maxResults=10000)
    issue_project_ibwfbn = jira.search_issues('project=NECTAIN and status=RESOLVED and type=Bug  and  cf[11970] = "In build, build number set"' , maxResults=10000)
#    issue_wfnb_field = jira.search_issues(' cf[11970] = "Waiting for next build" ')
# set build number | change build status from 'Waiting for next build' to 'In build, build number set'
    for issue_wfnb in issue_project_wfnb:
        wfnb.append(issue_wfnb)
        issue_wfnb.update(fields={"customfield_11371":[version]})
        issue_wfnb.update(fields={'customfield_11970': {'value':'In build, build number set'}})
    message_wfnb = ' '.join(map(str,wfnb))
# change build number | change build status from 'In build, waiting for build number' to 'In build, build number set'
    for issue_ibwfbn in  issue_project_ibwfbn:
        ibwfbn.append(issue_ibwfbn)
        issue_ibwfbn.update(fields={"customfield_11371":[version]})#
        issue_ibwfbn.update(fields={'customfield_11970': {'value':'In build, build number set'}})
    message_ibwfbn = ' '.join(map(str,ibwfbn))
    Create_message_to_send(message_ibwfbn, message_wfnb, version)

# Create and send message
def Create_message_to_send(issue_message_ibwfbn ,issue_message_wfnb, version):
    message_to_send_wfnb = ("Issue how to change build status from Waiting for next build to In build, build number set"+'\n'
                            + issue_message_wfnb+'\n'
                            + "Update to version"+ version) 
    message_to_send_ibwfbn = ("Issue how to change build status from In build, waiting for build number to In build, build number set"+"\n"
                              + issue_message_ibwfbn+"\n"
                              + "Update to version "+ version)
    print message_to_send_wfnb
    if issue_message_wfnb:
       SendToTelegram(message_to_send_wfnb) 
    if issue_message_ibwfbn:
       SendToTelegram(message_to_send_ibwfbn) 
Jira()

