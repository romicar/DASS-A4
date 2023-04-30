import unittest as UT
from king import King
import village


class TesterForKingMove(UT.TestCase):

    def setUp(self):
        self.king = King([0, 0])
        self.V = village.createVillage(1)

# tests for all Kings direction movements
    def test_AllDirections(self):

        # # tests for LEFT direction movements
        direction = 'left'

        currentPos = [0, 0]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [0, 0]
        self.assertEqual(finalPos, expectedPos, f"{direction} move failed")

        currentPos = [3, 7]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [3, 6]
        self.assertEqual(finalPos, expectedPos, f"{direction} move failed")

        currentPos = [17, 30]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [17, 29]
        self.assertEqual(finalPos, expectedPos, f"{direction} move failed")

        # # tests for UP direction movements
        direction = 'up'

        currentPos = [0, 0]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [0, 0]
        self.assertEqual(finalPos, expectedPos, f"{direction} move failed")

        currentPos = [12, 15]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [11, 15]
        self.assertEqual(finalPos, expectedPos, f"{direction} move failed")

        currentPos = [17, 35]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [16, 35]
        self.assertEqual(finalPos, expectedPos, f"{direction} move failed")

        # # tests for DOWN direction movements
        direction = 'down'

        currentPos = [0, 0]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [1, 0]
        self.assertEqual(finalPos, expectedPos, f"{direction} move failed")

        currentPos = [17, 0]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [17, 0]
        self.assertEqual(finalPos, expectedPos, f"{direction} move failed")

        currentPos = [11, 15]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [12, 15]
        self.assertEqual(finalPos, expectedPos, f"{direction} move failed")

        # # tests for RIGHT direction movements
        direction = 'right'

        currentPos = [17, 35]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [17, 35]
        self.assertEqual(finalPos, expectedPos, f"{direction} move failed")

        currentPos = [0, 0]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [0, 1]
        self.assertEqual(finalPos, expectedPos, f"{direction} move failed")

        currentPos = [10, 12]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [10, 13]
        self.assertEqual(finalPos, expectedPos, f"{direction} move failed")

    # # tests for Kings movements in case of high speed of King
    def test_HighSpeed(self):
        self.king.speed = 100
        currentSpeed = self.king.speed

        # # tests for Kings LEFT movements in case of high speed of King
        direction = 'left'
        currentPos = [0, 35]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [0, 0]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of speed excess")

        currentPos = [9, 9]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [9, 0]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of speed excess")

        currentPos = [0, 0]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [0, 0]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of speed excess")

        # # tests for Kings UP movements in case of high speed of King
        direction = 'up'

        currentPos = [17, 35]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [0, 35]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of speed excess")

        currentPos = [1, 12]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [0, 12]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of speed excess")

        currentPos = [0, 0]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [0, 0]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of speed excess")

        # # tests for Kings DOWN movements in case of high speed of King
        direction = 'down'

        currentPos = [17, 35]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [17, 35]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of speed excess")

        currentPos = [15, 22]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [17, 22]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of speed excess")

        currentPos = [0, 0]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [17, 0]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of speed excess")

        # # tests for RIGHT Kings movements in case of high speed of King
        direction = 'right'
        currentPos = [12, 35]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [12, 35]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of speed excess")

        currentPos = [12, 30]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [12, 35]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of speed excess")

        currentPos = [0, 0]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [0, 35]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of speed excess")

    def test_KingMoves(self):
        self.king.speed = 20
        currentSpeed = self.king.speed

        self.V.map[1][5] = 1  # for wall
        barrier = 'wall'

        # for left
        direction = 'left'
        currentPos = [1, 15]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [1, 6]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of {barrier} collision")

        # for right
        direction = 'right'
        currentPos = [1, 0]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [1, 4]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of {barrier} collision")

        # for up
        direction = 'up'
        currentPos = [7, 5]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [2, 5]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of {barrier} collision")

        # for down
        direction = 'down'
        currentPos = [0, 5]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [0, 5]
        self.assertEqual(finalPos, expectedPos,
                         f"{direction} move failed because of {barrier} collision")

        # now checking for townhall, hut, cannon and wizard by looping through 3 to 6

        for i in range(3, 7):
            self.V.map[1][5] = i

            # for left
            direction = 'left'
            currentPos = [1, 15]
            self.king.position = currentPos
            self.king.move(direction, self.V)
            finalPos = self.king.position
            expectedPos = [1, 6]
            self.assertEqual(finalPos, expectedPos,
                             f"{direction} move failed because of collision")

            # for right
            direction = 'right'
            currentPos = [1, 0]
            self.king.position = currentPos
            self.king.move(direction, self.V)
            finalPos = self.king.position
            expectedPos = [1, 4]
            self.assertEqual(finalPos, expectedPos,
                             f"{direction} move failed because of collision")

            # for up
            direction = 'up'
            currentPos = [7, 5]
            self.king.position = currentPos
            self.king.move(direction, self.V)
            finalPos = self.king.position
            expectedPos = [2, 5]
            self.assertEqual(finalPos, expectedPos,
                             f"{direction} move failed because of collision")

            # for down
            direction = 'down'
            currentPos = [0, 5]
            self.king.position = currentPos
            self.king.move(direction, self.V)
            finalPos = self.king.position
            expectedPos = [0, 5]
            self.assertEqual(finalPos, expectedPos,
                             f"{direction} move failed because of collision")

        # now check for spawns
        self.V.map[1][5] = 0
        self.V.map[2][3] = 2

        # for left
        direction = 'left'
        currentPos = [2, 15]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [2, 0]
        self.assertEqual(finalPos, expectedPos, f"{direction} move fails")

        # for right
        direction = 'right'
        currentPos = [2, 0]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [2, 20]
        self.assertEqual(finalPos, expectedPos, f"{direction} move fails")

        # for up
        direction = 'up'
        currentPos = [5, 3]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [0, 3]
        self.assertEqual(finalPos, expectedPos, f"{direction} move fails")

        # for down
        direction = 'down'
        currentPos = [0, 3]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [17, 3]
        self.assertEqual(finalPos, expectedPos, f"{direction} move fails")

    def test_KingAlive(self):
        self.king.alive = False
        isAlive = self.king.alive

        # for left
        direction = 'left'
        currentPos = [2, 15]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [2, 15]
        self.assertEqual(finalPos, expectedPos, f"King alive fails")

        # for right
        direction = 'right'
        currentPos = [2, 0]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [2, 0]
        self.assertEqual(finalPos, expectedPos, f"King alive fails")

        # for up
        direction = 'up'
        currentPos = [5, 3]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [5, 3]
        self.assertEqual(finalPos, expectedPos, f"King alive fails")

        # for down
        direction = 'down'
        currentPos = [17, 7]
        self.king.position = currentPos
        self.king.move(direction, self.V)
        finalPos = self.king.position
        expectedPos = [17, 7]
        self.assertEqual(finalPos, expectedPos, f"King alive fails")


if __name__ == '__main__':
    hello = UT.main(exit=False)
    myfile = open("output.txt", "w")
    if hello.result.wasSuccessful():
        print(True, file=myfile)
    else:
        print(False, file=myfile)
