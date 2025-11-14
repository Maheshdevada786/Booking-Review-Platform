import os
import django
from django.template.loader import get_template

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookingReview_Community.settings')
django.setup()

try:
    tmpl = get_template('booking_form.html')
    print('Template compiled OK:', tmpl)
except Exception as e:
    import traceback
    traceback.print_exc()
    print('ERROR:', e)
