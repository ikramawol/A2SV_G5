class Robot:

    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1
        self.direction = "East"
        self.position = [0,0]
        self.perimeter = 2*(width + height - 2)
        self.move = 0

    def step(self, num: int) -> None:
        self.move += num
        self.move %= self.perimeter

        if self.move > self.perimeter//2 + self.width:
            self.direction = "South"
            self.position = [0, self.height - (self.move - (self.perimeter // 2) - self.width)]

        elif self.move > self.perimeter//2:
            self.direction = "West"
            self.position = [self.width - (self.move - (self.perimeter//2)), self.height]

        elif self.move > self.width:
            self.direction = "North"
            self.position = [self.width, self.move - self.width]

        elif not self.move:
            self.direction = "South"
            self.position = [0,0]

        else:
            self.direction = "East"
            self.position = [self.move, 0] 
            
    def getPos(self) -> List[int]:
        return self.position

    def getDir(self) -> str:
        return self.direction


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()