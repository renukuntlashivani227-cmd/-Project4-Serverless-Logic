def lambda_handler(event, context):

    num1 = event["num1"]
    num2 = event["num2"]

    total = num1 + num2

    return {
        "sum": total
    }