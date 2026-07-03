# aiva/aiva_memory.py
from tinydb import TinyDB, Query
from datetime import datetime
import os

class AivaMemory:
    def __init__(self, db_path='aiva_memory.json'):
        self.db = TinyDB(db_path)
        self.log_table = self.db.table('conversations')
        self.state_table = self.db.table('state')
        self.current_state = self.state_table.all()[0] if self.state_table.all() else {}

    def record_message(self, speaker, message):
        entry = {
            'speaker': speaker,
            'message': message,
            'timestamp': datetime.now().isoformat(),
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.log_table.insert(entry)
        return entry

    def get_log(self):
        return [(msg['speaker'], msg['message']) for msg in self.log_table.all()]

    def get_recent_messages(self, speaker=None, limit=20):
        all_msgs = self.log_table.all()
        if speaker:
            filtered = [m for m in all_msgs if m.get('speaker') == speaker]
            return filtered[-limit:]
        return all_msgs[-limit:]

    def get_last(self):
        all_msgs = self.log_table.all()
        if all_msgs:
            last = all_msgs[-1]
            return (last['speaker'], last['message'])
        return None

    def count_conversations(self):
        return len(self.log_table.all())

    def get_memory_summary(self):
        return {
            'total_conversations': self.count_conversations(),
            'database_size': os.path.getsize('aiva_memory.json') if os.path.exists('aiva_memory.json') else 0
        }
