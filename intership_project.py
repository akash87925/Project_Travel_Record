class TravelRecord:
    def __init__(self, history_id, individual_name, destination, start_date, end_date):
        self.history_id = history_id
        self.individual_name = individual_name
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return (f"TravelRecord(history_id={self.history_id}, "
                f"individual_name={self.individual_name}, "
                f"destination={self.destination}, "
                f"start_date={self.start_date}, "
                f"end_date={self.end_date})")


class TravelHistoryTracker:
    def __init__(self):
        self.records = {}

    def create_record(self, history_id, individual_name, destination, start_date, end_date):
        if history_id in self.records:
            raise ValueError("Record with this history ID already exists.")
        self.records[history_id] = TravelRecord(history_id, individual_name, destination, start_date, end_date)

    def read_record(self, history_id):
        return self.records.get(history_id, "Record not found.")

    def update_record(self, history_id, individual_name=None, destination=None, start_date=None, end_date=None):
        if history_id not in self.records:
            raise ValueError("Record not found.")
        record = self.records[history_id]
        if individual_name is not None:
            record.individual_name = individual_name
        if destination is not None:
            record.destination = destination
        if start_date is not None:
            record.start_date = start_date
        if end_date is not None:
            record.end_date = end_date

    def delete_record(self, history_id):
        if history_id in self.records:
            del self.records[history_id]
        else:
            raise ValueError("Record not found.")

    def analyze_travel_behaviors(self):
        analysis = {}
        for record in self.records.values():
            if record.individual_name in analysis:
                analysis[record.individual_name]['trips'].append(record)
                analysis[record.individual_name]['count'] += 1
            else:
                analysis[record.individual_name] = {'trips': [record], 'count': 1}
        return analysis


# Example usage:
tracker = TravelHistoryTracker()
tracker.create_record(1, "Alice", "France", "2023-01-01", "2023-01-10")
tracker.create_record(2, "Bob", "Germany", "2023-02-05", "2023-02-15")
tracker.create_record(3, "Alice", "Spain", "2023-03-10", "2023-03-20")

print(tracker.read_record(1))
tracker.update_record(1, destination="Italy")
print(tracker.read_record(1))
tracker.delete_record(2)

print(tracker.analyze_travel_behaviors())
