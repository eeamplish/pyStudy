
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        print(f"{self.price}元的闹钟开始响")
        winsound.Beep(2000, 3000)


clock1 = Clock()
clock1.id = "001"
clock1.price = 199

clock2 = Clock()
clock2.id = "002"
clock2.price = 999

clock1.ring()

