# GHOST

## Objective
The objective of GHOST is to force the other player to spell out a complete word. Each player can choose one letter per turn, provided that the letter can lead to a valid word. If the player feels that the other has created a full word, they can then challenge, winning the game if they are correct.

The game has a built in AI that, at request, will provide you which letter to enter such that you are guarenteed to win the round.

## Controls -- Special Characters
#### Enter these characters during your turn to call special commands

! -- Challenge the other player. If the word is a full word, that player is eliminated from the game. The next round then begins.

help -- Print possible letters you can enter such that there are still posibilities for words.

clear -- Clear the current string, restart the round

? -- Use the CPU to determine which letters you can plug in such that you will always win.

## Notes
This game has only been completed in that the AI and the basic structure of the game are functional. There are still some edge cases and minor bugs that can lead to a crash in the program, so more testing is needed before it can be a finalized product.