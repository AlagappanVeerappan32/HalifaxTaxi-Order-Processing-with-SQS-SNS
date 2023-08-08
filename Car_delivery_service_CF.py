import json
import boto3
import random


# initilzing the services
sns_client = boto3.client('sns')
dynamodb = boto3.client('dynamodb')

# method used to send the messages to the SNS topic.
def publish_message_to_sns(message):
    
    topic_arn = 'arn:aws:sns:us-east-1:637592602151:HalifaxTaxi-Payload'
    
    # publishing the message to the topic
    try:
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message
        )
        print("Message published successfully!")
        return response
    except Exception as e:
        raise e

# getting the random values from the Dynamo DB
def generate_order_message():
    
    try:
        # table name
        table_name = 'HalifaxTaxi'
        # scaning the whole table
        response = dynamodb.scan(TableName=table_name)
        items = response['Items']
        # checking if the table as any item or not
        if not items:
            print("No items found in the table.")
        else:
            # Randomly select three different rows
            selected_rows = random.sample(items, 3)
            
            # Access one random value for each field from the selected rows
            clientAddress = random.choice([row['client']['S'] for row in selected_rows])
            carType = random.choice([row['car']['S'] for row in selected_rows])
            carAccessory = random.choice([row['addon']['S'] for row in selected_rows])

        # message to deliver 
        message_to_deliver = f"Hey, I would like to rent a {carType} with {carAccessory}. Please drop the car at {clientAddress}. Thank you, Have a nice day!"
        
        return message_to_deliver
        
    except ValueError as ve:
        # Handle the missing values exception
        print(f"ValueError occurred: {ve}")
        raise ve
    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")
        raise e
        

def lambda_handler(event, context):
    try:
        # calling the methods
        message_to_deliver = generate_order_message()
        publish_response = publish_message_to_sns(message_to_deliver)
        
        return {
            "statusCode": 200,
            "body": "Order message sent successfully!"
        }
        
    except Exception as e:
        # Handle any exceptions occurred during the process
        error_message = f"An error occurred: {e}"
        return {
            "statusCode": 500,
            "body": error_message
        }