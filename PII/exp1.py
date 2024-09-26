from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

text = 'My Name is Sanjeevu and my phone number is 7760912912'

analyzer = AnalyzerEngine()
result = analyzer.analyze(text=text,entities=["PHONE_NUMBER","NAME"], language='en')
print(result)