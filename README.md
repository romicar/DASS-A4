# Assignment 4 
Added unit tests for the codebase provided in `Assignment3`
> Romica Raisinghani (2021101053)

## DESCRIPTION OF `test.py`


* Created a `TesterForKing` class to check the functionality of the `King.move()` method

* `test_AllDirections()` method checks for the `left`, `right`, `up` and `down` movements of the King

* `test_HighSpeed()` method sets the Kings spped to high (here 100) and check for the `left`, `right`, `up` and `down` movements of the King by making sure that it reaches appropriate position after the moves made as per the speed

* > `test_KingMoves()` method creates barriers like `wall`, `townhall`, `hut`, `cannon` and `wizard` by appropriately checking the collision if possible by the `left`, `right`, `up` and `down` movements of the King

*  > `test_KingMoves()` method also checks the King's movement if a spawn is present. In this case, the should be no collision and test is made for `left`, `right`, `up` and `down` movements of the King

## DESCRIPTION OF `test_bonus.py`

* Created a `TesterForKingAttack` class to check the functionality 

* `test_basic_attack()` method checks for the `king.attack_target()` method

* If the king is dead, the health of the targets would remain same after the attack by the king

* First health is intact(attack=0), then health reduces by 1(attack 1), then health reduces by 3(attack=2), then health reduces by 10(attack=4)

* If the attack is of value=i, then the health of the target would reduce by i

* If the attack value is greater than the current health of the target, then the health of target becomes zero



