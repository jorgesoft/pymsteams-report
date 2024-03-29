import pymsteams

def sendTeams(reportHook, date, services):
    #channel URL
    teamsURL = reportHook
    myTeamsMessage = pymsteams.connectorcard(teamsURL)
    myTeamsMessage.title("Test Report")
    myTeamsMessage.text("Test run at " + str(date))
    #section with the up services
    myMessageSection = pymsteams.cardsection()
    myMessageSection.activityTitle("Up Services")
    myMessageSection.activityText("Service name and response code: ")
    for up in services:
        myMessageSection.addFact(up, "200")
    myTeamsMessage.addSection(myMessageSection)
    myTeamsMessage.send()