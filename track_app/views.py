from django.shortcuts import render
import requests

def track(request):
    phone_info = {}
    error = None
    if request.method == 'POST':
        api_key = '3cfd0b313037471f7b95d257242d3514'  # Replace with your Numverify API key
        phone_number = request.POST.get('phone_number')

        # API request to Numverify
        url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"
        response = requests.get(url)
        data = response.json()

        # Check if the phone number is valid and get the details
        if data['valid']:
            phone_info = {
                "Country": data.get('country_name', 'N/A'),
                "Location": data.get('location', 'N/A'),
                "Carrier": data.get('carrier', 'N/A'),
                "Line": data.get('line_type', 'N/A'),
            }
        else:
            error = "Invalid phone number. Please try again."

    return render(request, 'track.html', {'phone_info': phone_info, 'error': error})
