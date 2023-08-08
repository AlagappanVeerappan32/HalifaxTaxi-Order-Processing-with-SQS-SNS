import json
import boto3

# initilzing the services
sqs_client = boto3.client("sqs")
sns_client = boto3.client("sns")

# getting the url of the queue.
def get_queue_url(queue_name):
    try:
        # Get the queue URL using the queue name
        response = sqs_client.get_queue_url(QueueName=queue_name)
        queue_url = response["QueueUrl"]
        return queue_url

    except Exception as e:
        print(f"Error while fetching queue URL: {e}")
        raise e

# Now we will publish the message to sns topic where email is subscribed.
def process_sqs_message(message_content):
    try:
        topic_arn = "arn:aws:sns:us-east-1:637592602151:HalifaxTaxiCF"

        # Publish the message_content to the SNS topic
        response = sns_client.publish(TopicArn=topic_arn, Message=message_content)

        print("Message published to SNS successfully:", response)

    except Exception as e:
        print(f"Error while processing the SQS message: {e}")
        raise e


def lambda_handler(event, context):

    # getting queue name and url
    queue_name = "HalifaxTaxiPayloadCF"
    queue_url = get_queue_url(queue_name)
    print(queue_url)

    try:
        while True:
            # Polling messages from the SQS queue
            response = sqs_client.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=10, 
            )

            print(response)
            # check message is present in response or not
            if "Messages" in response:
                # Process the received messages
                for message in response["Messages"]:
                    # print(message)

                    message_content = message["Body"]
                    # print(message_content)

                    sqs_message = json.loads(message_content)

                    order_message = sqs_message["Message"]
                    print(order_message)

                    # Process the message content
                    process_sqs_message(order_message)
                    print("message has sent to the user")

                    # Delete the processed message from the queue
                    sqs_client.delete_message(
                        QueueUrl=queue_url, ReceiptHandle=message["ReceiptHandle"]
                    )
            else:
                print("No messages found in the queue.")
                break

    except Exception as e:
        print(f"An error occurred: {e}")
        raise e
