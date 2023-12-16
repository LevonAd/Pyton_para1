class Nocia():
    Size = 15
    Smart = 10
    def smarter():
        Smart = Smart + 5
class Apple(Nocia):
    Size = 20
    Smart = 30

Iphon = Apple()
Iphon.smarter
print(Iphon.Smart)