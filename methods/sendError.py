import pymsteams

def sendError(errorHook, service, date, error):
    #channel URL
    teamsURL = errorHook
    myTeamsMessage = pymsteams.connectorcard(teamsURL)
    myTeamsMessage.title("TEST REPORT ERROR FOR " + str(service))
    myTeamsMessage.text("Test run at " + str(date))
    #section with the up services
    myMessageSection = pymsteams.cardsection()
    myMessageSection.activityTitle(service)
    myMessageSection.activityText(str(error))
    myTeamsMessage.addSection(myMessageSection)
    myTeamsMessage.send()