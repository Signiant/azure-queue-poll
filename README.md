# azure-queue-poll
Polls an Azure storage queue for messages and writes to STOUT

## Config file format
````
{
	"account": "AZURE STORAGE ACCOUNT NAME", 
	"key": "AZURE STORAGE ACCOUNT KEY",
	"queue": "AZURE STORAGE QUEUE NAME"
}

````
Sample docker run command showing how to mount the config file into the container using a data volume on the local docker host
:
````
docker run -d --privileged=true \
              -v /my/local/folder/qbranch_config.json:/usr/src/app/qbranch_config.json \
              --name azure_queue_poll \
              signiant/azure-queue-poll
````
