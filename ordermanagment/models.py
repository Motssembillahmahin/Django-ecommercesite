from django.db import models

# Create your models here.
from django.db import models

class orders(models.Model):
    order_id = models.BigIntegerField(null=True)
    customer_id = models.BigIntegerField(null=True)
    
    # Customer name and order name should be CharField, not DecimalField
    customer_name = models.CharField(null=True, max_length=100)  # Assuming it's a string
    order_name = models.CharField(null=True, max_length=50)  # Assuming it's a string

    # For decimal values like total amount, financial status, and seller earnings
    total_amount = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    financial_status = models.CharField(null=True, max_length=50)  # Assuming it's a status string
    fulfillment_status = models.CharField(null=True, max_length=50)  # Assuming it's a status string
    
    # Vendor names, payment gateway, phone number, tracking ID should be CharField
    vendor_names = models.CharField(null=True, max_length=50)  # Assuming it's a string or comma-separated list
    payment_gateway = models.CharField(null=True, max_length=150)  # Assuming it's a string
    phone_number = models.CharField(null=True, max_length=20)  # Assuming it's a phone number in string format
    tracking_id = models.CharField(null=True,max_length=50)  # Assuming it's a string

    # Other fields
    note = models.TextField(null=True)  # Assuming it's a text field
    address = models.TextField(null=True)
    parcel_status = models.JSONField(null=True)  # Ensure it's a JSON field
    created_at = models.DateTimeField(null= True, auto_now_add=True)
    
    # Numeric fields with decimal precision
    rcollection = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    latestdate = models.DateField(null=True)  # Assuming it's a date field
    seller_earning = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    gov_earning = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    rdcharge = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    
    # Remarks as JSONField, and others as TextField
    remarks = models.JSONField(null=True)  # Missing parentheses were added here
    latestupdateofpercel = models.TextField(null=True)

    # Additional numeric fields for monetary values
    shippment_charges = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    reverse_amount = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    seller_payable = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    govaly_earning_per_order = models.DecimalField(null=True, max_digits=10, decimal_places=2)

    # Text fields
    reverse_reason = models.TextField(null=True)

    # Boolean field for status
    govaly_paid = models.BooleanField(null=True, default=False)
    liveparcelstatus = models.TextField(null=True)

    def __str__(self):
        return f"Order {self.order_name} by {self.customer_name} with {self.vendor_names}"


    