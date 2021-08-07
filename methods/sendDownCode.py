import pymsteams

def sendDownCode(errorHook, service, date, status):
    #channel URL
    teamsURL = errorHook
    myTeamsMessage = pymsteams.connectorcard(teamsURL)
    myTeamsMessage.title("TEST REPORT CODE {} in {}".format(status, service))
    myTeamsMessage.text("Test run at " + str(date))
    #section with the up services
    myMessageSection = pymsteams.cardsection()
    myMessageSection.activityTitle(service)
    myMessageSection.activityText(str(status))
    myTeamsMessage.addSection(myMessageSection)
    myTeamsMessage.send()