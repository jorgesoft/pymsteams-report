# pymsteams-report 2.0
## Python application to report URL status to MS Teams, running in a docker container

Test HTTP or HTTPS endpoints and report the results to a Microsoft Teams webhook

## How to use

Set up two webhooks in a MS Teams channel, one for All Ok report and one for errors

##### https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook 

Add the webhooks URL and the sites that you want to monitor in the [config.py](https://github.com/gorj3/pymsteams-report/blob/master/config.py)

```
# place weebHook links inbtween the ""
reportHook = ""
errorHook = ""

# example of list of services and URLs to send the get request test
services = {
  "Google" : "https://google.com",
  "NY State COVID-19" : "https://asdfa.jorgedemo.com"
  }
```

Build the docker image with this command 

```
docker build -t pymsteams-report .
```

And create a container with this command 

```
docker run -it --rm --name running-pymsteams-report pymsteams-report
```

## Required libraries:
pymsteams - https://pypi.org/project/pymsteams/

###### pip install pymsteams

How to set up a webhook: https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/connectors-using