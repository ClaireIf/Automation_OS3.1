import os
os.system('py.test test_usbcheck_restartStability.py test_WiFi_restartStability.py test_usbcheck_updateStability.py test_WiFi_updateStability.py--html=./StabilityResult.html')