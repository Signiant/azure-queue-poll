#!/usr/bin/python
# qbranch.py 1.0
# Checks an Azure error queue
# Author: Mike Perttula

import json
import time
import argparse
from azure.storage import QueueService


def checkQueue(aName, aKey, aQueue):
    while 1:
        try:
            queue_service = QueueService(account_name=aName, account_key=aKey)
        except Exception as e:
            print "Could not connect to queue"
        else:
            try:
                queue_metadata = queue_service.get_queue_metadata(aQueue)
            except Exception as e:
                print "Could not find queue"

            else:
                try:
                    count = queue_metadata['x-ms-approximate-messages-count']
                    print aQueue + " queue is empty"
                    if int(count) > 0:
                        print "Messages in " + aQueue + " queue: " + count
                        messages = queue_service.get_messages(aQueue)
                        for message in messages:
                            print "Message " + message.message_id + " : " + message.message_text
                            queue_service.delete_message(aQueue, message.message_id, message.pop_receipt)
                except Exception as e:
                    print "Could not read queue " + str(e)
        time.sleep(15)


parser = argparse.ArgumentParser(prog='qbranch')
parser.add_argument('config', help="Queue config file")
args = parser.parse_args()

if args.config:
    with open(args.config) as configFile:
        config = json.load(configFile)
    checkQueue(config["account"], config["key"], config["queue"])
else:
    parser.print_help()
