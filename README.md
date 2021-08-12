# pymsteams-report 2.0
Python application to report URL status to MS Teams, running in a docker container, and using [pymsteams](https://pypi.org/project/pymsteams/)

## How to use

1. Use this document to set up two webhooks in a MS Teams channel, one for All Ok report and one for errors

https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook 
 
2. Create a Dockerhub token (https://docs.docker.com/docker-hub/access-tokens/), and save the token and username as secrets `DOCKERHUB_TOKEN` and `DOCKERHUB_USERNAME`

3. Create a secret for error webhook `ERRORHOOK` and save the URL with this format: 
```
errorHook = "<hook-url>"
```

4. Create a secret for all ok webhook `REPORTHOOK` and save the URL with this format: 
```
reportHook = "<hook-url>"
```
5. GitHub actions will build the container image for each push or pull request to main branch

## Build the image locally

Add the webhooks URL and the sites that you want to monitor in the [config.py](https://github.com/gorj3/pymsteams-report/blob/master/config.py) file. 
You can also edit the timers here.

```
# place weebHook links inbtween the ""
reportHook = "<hook-url>"
errorHook = "<hook-url>"

# example of list of services and URLs to send the get request test
services = {
  "Google" : "https://google.com",
  "NY State COVID-19" : "https://react.jorgedemo.com"
  }

#time to repeat the test
timer = 60

#time to wait for response
wait_time = 60
```

Build the docker image with this command 

```
docker build -t pymsteams-report .
```

And create a container with this command  

```
docker run -d --rm --name running-pymsteams-report pymsteams-report
```

## Outputs

If all sites responded with a 200 code (OK), the All OK webhooks recieves a report

![allok](https://s3.amazonaws.com/jorgesilva.pro/content/allok.PNG)

If one site times out or respondes with a code different than 200, the error webhook recieves a report

![error](https://s3.amazonaws.com/jorgesilva.pro/content/error.PNG)