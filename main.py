"""
Verteilte Anwendungen Gruppe 07 
Aufgabenblatt 02
1. Aufgabe


Members:
Mauriz Weymann, Sascha Heinze, Sinan Ertogrul, Mark Unger

Avengers Quiz mit Anmeldung / Registrierung
"""
import Quiz
import Register


#User login or registration
name = Register.collectcredentials()

#Start Quiz 
Register.update_user(name, Quiz.Game())

#return Highscores
Register.all_user_scores()


#register.collectcredentials()
# newscore = Quiz.Game()
# score = score + newscore