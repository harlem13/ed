"""
The rossum_hook_request_handler is an obligatory main function that accepts
input and produces output of the rossum custom function hook.
:param payload: see https://api.elis.rossum.ai/docs/#annotation-content-event-data-format
:return: dict with files to be processed
"""
import json

def rossum_hook_request_handler(payload):
    if payload['event'] == 'email' and payload["action"] == "received":
        try:
            response = main(payload)
        except Exception as e:
            print("Serverless function exception: {0}".format(e))
            return payload["files"]
        return json.dumps(response)

"""
Try to pass values from email content to each of the documents to be processed.
:param payload: dict representing the payload
:return: dict with the API response
"""


def main(payload):
    incoming_files = payload["files"]
    modified_payload = payload
    email_sender = payload["headers"]["from"]
    extracted_value = email_sender
    i = 0
    for file in incoming_files:
        if extracted_value != []:

            if "values" not in file:
                file["values"] = []

            print(file)
            """print("Parsed values: {0}".format(extracted_value))"""
            file["values"].append({"id": "email:Sender", "value": extracted_value})
            print(file)
            incoming_files[i] = file
            i = i + 1

    print(incoming_files)
    modified_payload["files"] = incoming_files
    print(modified_payload)
    return modified_payload