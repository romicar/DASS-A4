import unittest as UT
from buildings import Hut, Wall, TownHall, WizardTower, Cannon
from king import King
import village

# checks for all king attacks
# checks for damage
# checks for alive/dead
# checks for destroyed targets
class TesterForKingAttack(UT.TestCase):
    
    def test_basic_attack(self):
        self.V = village.createVillage(1)
        self.hut = self.V.hut_objs[(6,22)]
        self.king = King([1,1])
        self.townhall = self.V.town_hall_obj
        self.wizardtower = self.V.wizard_tower_objs[(17, 27)]
        self.cannon = self.V.cannon_objs[(12,13)]
        self.wall = self.V.wall_objs[(15,20)]
        all=[self.hut,self.wall,self.cannon,self.wizardtower,self.townhall]
        for i in all:
            self.king.attack_target(i,0)
            self.assertEqual(i.health, i.max_health)
        for i in all:
            self.king.attack_target(i,1)
            self.assertEqual(i.health, i.max_health-1)
        for i in all:
            self.king.attack_target(i,2)
            self.assertEqual(i.health, i.max_health-3)
        for i in all:
            self.king.attack_target(i,3)
            self.assertEqual(i.health, i.max_health-6)
        for i in all:
            self.king.attack_target(i,4)
            self.assertEqual(i.health, i.max_health-10)
        self.king.alive=False
        for i in all:
            self.king.attack_target(i,5)
            self.assertEqual(i.health, i.max_health-10)    
        for i in all:
            self.king.attack_target(i,10000)
            self.assertEqual(i.health, i.max_health-10)
        self.king.alive=True
        for i in all:
            self.king.attack_target(i,i.max_health-11)
            self.assertEqual(i.health, 1)
        for i in all:
            self.assertEqual(i.destroyed, False)
        for i in all:
            self.king.attack_target(i,10000)
            self.assertEqual(i.health, 0)
            self.assertEqual(i.destroyed, True)

if __name__ == '__main__':
    hello = UT.main(exit=False)
    myfile = open("output_bonus.txt", "w")
    ans = hello.result.wasSuccessful()
    if (ans==False):
        print(False, file=myfile)
    else:
        print(True, file=myfile)
        