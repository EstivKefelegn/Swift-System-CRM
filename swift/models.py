from django.db import models

# Create your models here.
from django.db import models

class SWIFTAccountDetail(models.Model):
    
    
    
    PAYMENT_INITIATION = 'MT103'
    FUND_TRANSFER = 'MT202'
    FOREIGN_EXCHANGE = 'FX'
    SECURITIES_SETTLEMENT = 'SEC'
    OTHER = 'OTHER'
    
    
    
    SWIFT_SERVICE_CHOICES = [
        (PAYMENT_INITIATION, 'Payment Initiation (SWIFT MT103)'),
        (FUND_TRANSFER, 'Fund Transfer Services (SWIFT MT202)'),
        (FOREIGN_EXCHANGE, 'Foreign Exchange Transactions'),
        (SECURITIES_SETTLEMENT, 'Securities Settlements'),
        (OTHER, 'Other'),
    ]
    
    
    business_name = models.CharField(max_length=255)
    business_address = models.TextField()
    country_of_operation = models.CharField(max_length=100)
    
    account_number = models.CharField(max_length=34, help_text="Account Number")
    
    swift_service_requested = models.CharField(
        max_length=10,
        choices=SWIFT_SERVICE_CHOICES,
        default=PAYMENT_INITIATION
    )
    other_service_description = models.CharField(max_length=255, blank=True, null=True, help_text="Describe if 'Other' service is selected")

    # Contact Information
    primary_contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)

    # Security & Compliance
    country_of_incorporation = models.CharField(max_length=100)
    legal_entity_identifier = models.CharField(max_length=20, blank=True, null=True, help_text="Optional LEI for compliance")
    kyc_aml_documents = models.FileField(upload_to='kyc_documents/', blank=True, null=True, help_text="Upload KYC/AML document")

    # Additional Information
    authorized_signatory_name = models.CharField(max_length=255)
    additional_notes = models.TextField(blank=True, null=True)

    # System Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
        default='Pending'
    )

    def __str__(self):
        return f"{self.business_name} - {self.account_number}"
