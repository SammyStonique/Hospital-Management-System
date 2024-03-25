import uuid
from .models import *


#Function to generate incrementing invoice numbers
def invoice_number_gen(company_id):
        txn_type = "INV"
        company_uuid = uuid.UUID(company_id)
        last_invoice = Journal.objects.filter(company=company_uuid, txn_type=txn_type).order_by('journal_no').last()
        if not last_invoice:
            return "INV00001"
        invoice_no = last_invoice.journal_no
        invoice_int = int(invoice_no.split('INV')[-1])
        new_invoice_int = invoice_int + 1
        new_invoice_no = 'INV'+ str(new_invoice_int).zfill(5)
        
        return new_invoice_no