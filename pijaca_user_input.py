class Pijaca:

    def __init__(self, user_name, ime_pijace, zing_coefficient, emotion, weather, share_status):
        self.user_name = user_name.lower()
        self.ime_pijace = ime_pijace.lower()
        self.zing_coefficient = int(zing_coefficient)
        self.emotion = int(emotion)
        self.weather = int(weather)
        self.share_status = share_status.lower()

    @classmethod
    def from_input(cls):
        return cls(
            input("Kako ti je ime?\n"),
            input("Kaj je pijaca, ki jo trenutno pijes?\n(nic ni veljaven odgovor ;) )\n"),
            input(
                "Kako kulska je pijaca, ki jo pijes na lestvici od 1 > 10?\n(10 = totalno kulska\n 1 = bolj tako tako)\n"),
            input("Kako se pocutis danes na lestvici od 1 > 10?\n(10 = odlicno\n 1 = bolj tako tako)\n"),
            input("Kaksno je vreme pri tebi?\n(10 = zelo lepo\n 1 = slabo)\n"),
            input("Ali bi svojo pijaco delil/a s prijatelji?\n(Ja / Ne)\n"),
        )


oseba1 = Pijaca.from_input()

with open("user_input.txt", "w") as save_to_file:
    save_to_file.write(str(vars(oseba1)))


