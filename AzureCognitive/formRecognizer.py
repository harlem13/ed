from azure.ai.formrecognizer import FormRecognizerClient
from azure.core.credentials import AzureKeyCredential

# Replace with your own values
endpoint = "https://enerjiinstanceformrecogtrials.cognitiveservices.azure.com/"
key = "c4ec2e7130854a7b94f9de1f684d4904"
pdf_url = "Invoices/invSample1.pdf"

# Authenticate the client
credential = AzureKeyCredential(key)
client = FormRecognizerClient(endpoint, credential)

# Call the API to extract data from the PDF document
try:
    with open(pdf_url, "rb") as f:
        poller = client.begin_recognize_invoices(f, locale="en-US")
    result = poller.result()
except Exception as e:
    print("Document Open Error: {0}".format(e))

# Print the extracted data
try:
    # Print the extracted data
    for invoice in result:
        print(invoice.fields)
        print("Invoice details:")
        invoice_id = invoice.fields.get("InvoiceId")
        if invoice_id:
            print(f"Invoice ID: {invoice_id.value}")
        invoice_date = invoice.fields.get("InvoiceDate")
        if invoice_date:
            print(f"Invoice Date: {invoice_date.value}")
        invoice_due_date = invoice.fields.get("BillingAddress")
        if invoice_due_date:
            print(f"Due Date: {invoice_due_date.value}")
        total_amount = invoice.fields.get("InvoiceTotal")
        if total_amount:
            print(f"Total Amount: {total_amount.value}")
            print("Total Amount Confidence: {}".format(total_amount.confidence))
        currency = invoice.fields.get("Currency")
        if currency:
            print(f"Currency: {currency.value}")
        seller_name = invoice.fields.get("VendorName")
        if seller_name:
            print(f"Seller Name: {seller_name.value}")
        seller_address = invoice.fields.get("SellerAddress")
        if seller_address:
            print(f"Seller Address: {seller_address.value}")

except Exception as e:
    print("An error occurred:")
    print(e)