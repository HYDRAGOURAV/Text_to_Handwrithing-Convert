import pywhatkit as pw 
# You can also Get The input from User 
text = """
Artificial intelligence is the intelligence of machines or software, as opposed to the intelligence of humans or animals. It is a field of study in computer science that develops and studies intelligent machines. Such machines may be called AI.
"""

pw.text_to_handwriting(text, "demo.png", [0, 0, 138])  # color code 
print("END")

#  you cal also change color code 

