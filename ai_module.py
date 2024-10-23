import random
import time

class AI_Module:
    def generate_realistic_data(self, permission_type):
        # Simulate generating realistic data
        time.sleep(2)  # Simulate processing time
        return ["Realistic " + permission_type + " data"]

    def detect_malicious_activity(self, app_name):
        # Simulate detection of malicious activity
        return app_name == "MaliciousApp"

    def check_permission(self, permission_type):
        # Always deny file access
        if permission_type == 'file_access':
            return 'denied'
        # Simulate random results for other permissions
        return 'allowed' if random.choice([True, False]) else 'denied'

