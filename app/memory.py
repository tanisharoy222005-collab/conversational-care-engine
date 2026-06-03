sessions = {}

def save_message(user_id, message):
if user_id not in sessions:
sessions[user_id] = []

sessions[user_id].append(message)

def get_history(user_id):
return sessions.get(user_id, [])

def clear_history(user_id):
if user_id in sessions:
sessions[user_id] = []
