import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="CostCalculator", methods=["GET", "POST"])
def CostCalculator(req: func.HttpRequest) -> func.HttpResponse:

    try:
        num1 = req.params.get("num1")
        num2 = req.params.get("num2")

        if num1 is None or num2 is None:
            data = req.get_json()
            num1 = data.get("num1")
            num2 = data.get("num2")

        num1 = float(num1)
        num2 = float(num2)

        total = num1 + num2

        return func.HttpResponse(
            f'{{"num1": {num1}, "num2": {num2}, "sum": {total}}}',
            status_code=200,
            mimetype="application/json"
        )

    except Exception:
        return func.HttpResponse(
            '{"error": "Please provide num1 and num2"}',
            status_code=400,
            mimetype="application/json"
        )