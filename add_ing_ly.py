text=input("Enter a String:")
if text.endswith("ing"):
    text=text + "ly"
else:
    text=text + "ing"
print("Modified string:",text)
