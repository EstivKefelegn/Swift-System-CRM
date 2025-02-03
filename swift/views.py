from django.shortcuts import render, redirect
# from . import swiftForm
from django.contrib import messages
from .models import SWIFTAccountDetail

# Create your views here.
def success_page(request):
    return render(request, "Confirm.html")


def swiftAccountDetail(request):
    if request.method == 'POST':
        # Get form data
        business_name = request.POST.get('business_name')
        business_address = request.POST.get('business_address')
        country_of_operation = request.POST.get('country_of_operation')
        account_number = request.POST.get('account_number')
        swift_service_requested = request.POST.get('swift_service_requested')
        other_service_description = request.POST.get('other_service_description')
        primary_contact_name = request.POST.get('primary_contact_name')
        contact_email = request.POST.get('contact_email')
        contact_phone = request.POST.get('contact_phone')
        country_of_incorporation = request.POST.get('country_of_incorporation')
        legal_entity_identifier = request.POST.get('legal_entity_identifier')
        kyc_aml_documents = request.FILES.get('kyc_aml_documents')
        authorized_signatory_name = request.POST.get('authorized_signatory_name')
        additional_notes = request.POST.get('additional_notes')

        # Create a new SWIFTAccountDetail record
        swift_account = SWIFTAccountDetail(
            business_name=business_name,
            business_address=business_address,
            country_of_operation=country_of_operation,
            account_number=account_number,
            swift_service_requested=swift_service_requested,
            other_service_description=other_service_description if swift_service_requested == 'OTHER' else None,
            primary_contact_name=primary_contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
            country_of_incorporation=country_of_incorporation,
            legal_entity_identifier=legal_entity_identifier,
            kyc_aml_documents=kyc_aml_documents,
            authorized_signatory_name=authorized_signatory_name,
            additional_notes=additional_notes,
        )
        swift_account.save()

        messages.success(request, "Account details submitted successfully.")
        return redirect('success_page')  # Redirect to a success page or back to the form
    
    return render(request, 'index.html')

