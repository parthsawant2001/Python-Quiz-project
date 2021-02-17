class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
question_prompts = [
     "Who is president of USA?\n(a) Donald Trump\n(b) Narendra Modi\n(c) Vladimir Putin\n(d) Shah Rukh Khan\n",
     "Who is the richest person in the world?\n(a) Mukesh Ambani\n(b) Bill Gates\n(c) Elon Musk\n(d) Jeff Bezos\n",
     "Who invented the light bulb?\n(a) Issac Newton\n(b) Thomas Edison\n(c) Albert Einstein\n(d) Nikola Tesla\n",
]
questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "d"),
     Question(question_prompts[2], "b"),
]
def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))
run_quiz(questions)
