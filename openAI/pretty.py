import csv
import json

csv_data = """Title,Issue Number,Used Price Range (Low End),Used Price Range (High End),Summary
Marvel Team-Up Spider-Man and the Watcher,127,$1.00,$12.00,"This issue features Spider-Man teaming up with The Watcher in a special Christmas-themed adventure. They face off against yet another formidable foe. Throughout the snowy scenes, the story weaves elements of holiday spirit and action, showcasing Spider-Man's agility and resilience as well as The Watcher's mysterious oversight."
"""

reader = csv.DictReader(csv_data.splitlines())
data = list(reader)

json_data = json.dumps(data, indent=4)

print(json_data)


test = {'id': 'chatcmpl-9bLGKteUsnRzqFHk5zw6FP2aWjtAH', 'object': 'chat.completion', 'created': 1718686896, 'model': 'gpt-4o-2024-05-13', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': '```csv\nTitle,Issue Number\nCaptain America,247\n```'}, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 801, 'completion_tokens': 14, 'total_tokens': 815}, 'system_fingerprint': 'fp_9cb5d38cf7'}
test_csv = test['choices'][0]['message']['content']

# Clean data
test_csv = test_csv.replace('```csv\n', '').replace('\n```', '')

lines = test_csv.split('\n')

# open a CSV file to write to
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for line in lines:
        # split each line into fields and write it to the CSV file
        writer.writerow(line.split(','))