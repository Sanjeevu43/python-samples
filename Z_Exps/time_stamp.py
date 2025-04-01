import datetime

message = "This is my message."
timestamp = datetime.datetime.now().isoformat()  # ISO 8601 format (YYYY-MM-DDTHH:MM:SS.ffffff)
timestamped_message = f"{message} - {timestamp}"
print(timestamped_message)

print(int(datetime.datetime.now().year))

x = None
y = None
z = x | y | "Hai"
print(z)
