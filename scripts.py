import os
import django
import csv
from datetime import datetime
from decimal import Decimal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce_site.settings")
django.setup()


from ordermanagment.models import orders  # ✅ Use correct model name and import

from decimal import Decimal, InvalidOperation

def safe_decimal(value):
    try:
        return Decimal(value.strip()) if value and value.strip() else Decimal('0')
    except (InvalidOperation, ValueError, AttributeError):
        return Decimal('0')


def safe_date(value, fmt='%Y-%m-%d'):
    try:
        if value and value.strip().upper() != 'NULL':
            return datetime.strptime(value.strip(), fmt)
    except (ValueError, TypeError):
        pass
    return None

with open('ordermanagment/Results.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try: 
            order = orders(
                order_id= row.get('order_id') or 'Unknown',
                customer_id= row.get('customer_id') or 'Unknown',
                customer_name=row['customer_name'],
                order_name=row['order_name'],
                total_amount=safe_decimal(row.get('total_amount')),
                financial_status=row['financial_status'],
                fulfillment_status=row['fulfillment_status'],
                vendor_names=row['vendor_names'],
                payment_gateway=row['payment_gateway'],
                phone_number=row['phone_number'],
                tracking_id=row['tracking_id'],
                note=row['note'],
                address=row['address'],
                parcel_status=row['parcel_status'],
                created_at=safe_date(row.get('created_at')),
                rcollection=safe_decimal(row['rcollection']),
                latestdate=safe_date(row.get('latestdate')),
                seller_earning=safe_decimal(row['seller_earning']),
                gov_earning=safe_decimal(row['gov_earning']),
                rdcharge=safe_decimal(row['rdcharge']),
                remarks=row['remarks'],
                latestupdateofpercel=row['latestupdateofpercel'],
                shippment_charges=safe_decimal(row['shippment_charges']),
                reverse_amount=safe_decimal(row['reverse_amount']),
                seller_payable=safe_decimal(row['seller_payable']),
                govaly_earning_per_order=safe_decimal(row['govaly_earning_per_order']),
                reverse_reason=row['reverse_reason'],
                govaly_paid=(row.get('govaly_paid', '').lower() in ['true', '1', 'yes']),
            )
            order.save()
            print(f"Order {order.order_id} saved successfully.")
        except Exception as e:
            print(f"Error saving order {row['order_id']}: {e}")    
