import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/kirmani.io/goto/public_html')

from goto import app as application
