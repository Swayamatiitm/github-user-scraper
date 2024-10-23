import random

class VirtualRAM:
    def __init__(self):
        self.call_logs = [
            "Call from 123-456-7890 to 987-654-3210 at 10:00 AM",
            "Call from 234-567-8901 to 876-543-2109 at 11:00 AM",
            "Call from 345-678-9012 to 765-432-1098 at 12:00 PM",
            "Call from 456-789-0123 to 654-321-0987 at 1:00 PM"
        ]
        self.messages = [
            "Message from 123-456-7890: Hi, how are you?",
            "Message from 234-567-8901: Meeting at 3 PM.",
            "Message from 345-678-9012: Don't forget the report!",
            "Message from 456-789-0123: Let's catch up soon."
        ]
    
    def get_dummy_data(self, permission_type):
        if permission_type == 'call_logs':
            return [random.choice(self.call_logs) for _ in range(2)]  # Get 2 random call logs
        elif permission_type == 'messages':
            return [random.choice(self.messages) for _ in range(2)]  # Get 2 random messages
        return []
