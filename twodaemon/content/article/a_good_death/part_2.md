*A good death is one which costs the player no more than they expected and which the player believes to 
be their fault.*

Welcome to the second part of A Good Death, some thoughts on the topic of death and failure in challenge-based 
gaming. In part one we defined a good death as seen above, then discussed the two axes of frustration: 
perceived unfairness and relative loss. Now, in part two, we will discuss implementing the solutions to 
the axes: **fairness** and **acceptable loss**.

### Fairness...

...is making sure that the player understands their death to be due to their own failure, at least in 
part. Since dying without understanding is unfair, it follows that we can make it fairer by telling the 
player how we're about to kill them. Then trying to kill them, obviously. Surviving is still their own problem.

This means you need to **telegraph** and you need to be **consistent**. Every enemy attack should speak of survival 
as clearly as it speaks of death, every trap should trace out the danger it represents for all the world to 
see. Assuming they look, of course - not only do things become fair, but a new opportunity for challenge 
appears, the challenge of correctly interpreting the warnings. Testing the player's perception, planning 
and learning, not just their reflexes. 

Note that the consistency is necessary for telegraphing to be effective - if you send many signals but 
change what they mean the player can't actually read the warnings accurately and therefore nothing is being 
conveyed. 

Clover Studio's last hurrah, *God Hand*, understands the rules of telegraphing and consistency through and 
through. A brutally (and comically) vicious game of hand-to-hand combat, God Hand will throw many, many 
punches during the course of the game. In response to this, you have a few options: You can step left or 
right, you can dodge where you stand, you can backflip away and you can hit your opponent in the face.

There are different limitations to each of these, different attacks they can or cannot deal with and 
different situations to which each should be applied - with the exception of the last, which should be 
applied liberally wherever it will fit. It's that sort of game, really. 

When the punches (and kicks, grabs, flying charges, teleporting demons, sparkly death bolts...) are 
coming thick and fast, one thing pushes the game from frustrating to glorious: every strike can be 
predicted by the wind-up, with a little practice, and types of attacks look similar across many foes. 
Oh, some enemies will use feints or tricks, but there's nothing you cannot learn and then react to, 
nothing undodgeable or unbeatable. And when you fight and you watch and you learn and then you dance 
through a mad melee in a blur of perfect evasion and precision retaliation, well, then you earn the game's title.

![God Hand](/static/images/a_good_death/GodHand.png "I don't think you brought enough mooks.")

Moving on from the simplest telegraphing of a strike to the more cautious environmental warnings, From 
Software's *Dark Souls* shows us the way with a lift. One lift of many, with one significant difference and 
a swathe of supporting ones. 

You see, this lift kills you. 

Specifically it cranks steadily up to the next floor, hesitates a short moment, then slams vertically into 
the spikes lining the top of the lift shaft. Charming, really. 

No lift before this one has been dangerous in any way, in fact they've all been extremely helpful - an 
example of breaking consistency in order to avoid the player becoming complacent. To make sure the lift 
is fair despite not being consistent, many kinds of telegraphed warning are provided. 

- The lift is found in Sen's Fortress, a trap-filled labyrinth which would make Indiana Jones put down his 
whip and go back to lecturing. That's our first clue. 
- The second are the visible chains of the lift's pulley, which can be seen even when the lift has risen out 
of sight and as they pull, stop, *pull*, stop, reverse. The room is even large enough that it is unlikely 
the player will not see the lift rising at some point.
- For a third, the truly paranoid (i.e., anyone who got this far) can look up the lift shaft and see the spikes. 
- Finally - but probably the first clue seen - the lift looks like this:

![Dark Souls - Doom Lift](/static/images/a_good_death/DarkSoulsLift.png "My, but that is a lot of blood.")

Players still die to this but it is impossible not to be aware that they were *warned*, which means realising 
that it was their fault and, therefore, that the lift was fair.

**Telegraph** that which your players cannot have learned, and be **consistent** so you don't have to spell everything out. 

### Acceptable loss...

...is when the losses incurred by death align with the player's expectations. In part I we discussed the tendency 
for players to mentally **checkpoint**, constructing for themselves an idea of where they should return when they die. 
Our problem becomes making sure that the reload point and the player's checkpoints align. 

There are two main approaches: either your game's load points are subservient to the player's checkpoints or the 
player's checkpoints are shaped by the game's design.

The former is common, usually with an autosaving mechanism of some kind. At its simplest games just scatter an 
autosave at the start of every level, or at every loading boundary, or every five minutes. Depending on the game 
just saving at the beginning can obviously be the best approach - Super Hexagon, Ridiculous Fishing and the like 
would make little sense with a mid-run save point. These are all short-burst challenge games, though. Anything 
longer form needs a smarter solution.

*Gunpoint* provides a noteworthy example of matching an autosave system to the design - it [autosaves every five 
seconds](http://www.pentadact.com/2012-03-22-gunpoints-save-system/) and offers you the previous three autosaves 
to choose from immediately when you die. As *Gunpoint* is essentially a stealth puzzle game with chance of sudden 
death, dying usually indicates either a critical planning flaw - in which case it'll be fatal next time, too, 
forcing a change in plans or level restart regardless - or a minor mistake in implementation which needn't be too 
heavily punished. 

![Gunpoint](/static/images/a_good_death/Gunpoint.png)

Instead of scattering our autosaves, we can try predicting where they should be. Humans have a tendency to 
checkpoint at breaks in game flow. This means cutscenes (before and after), bosses (also before and after) 
and other significant events. It also means changes in environment; in particular traversing doors is a common 
trigger for mental checkpoints. A good boost to this strategy can be achieved with a lot of playtesting and 
analysis of their play, most famously used to the extreme by Valve.

Providing a manual save system is neither a solution nor a problem, incidentally, and instead is an addition 
heavily dependent on the overall design of the game. Manual saves let the player define their own game 
sections, possibly breaking something intended as a larger experience into smaller sections through repeat 
saves. This isn't necessarily an issue, it just depends on the game's design. That said, if you're relying on 
a manual save to create acceptable loss, relying on the player to remember to save regularly, you either have 
a non-real-time game or not as much control over your design as you might want.

On the other hand I also suggested shaping the player's checkpoints according to the game's design earlier. 
Put simply (and it isn't simple) you have save points or autosaves which are designed not just to force the 
player to checkpoint, but also to get them to *stop checkpointing on anything else*.

The earlier *Resident Evil* games had a neat trick for this, requiring the expenditure of a finite number 
of ink ribbons to save. When saving is a commodity the player becomes very aware of their last investment. 
That said, a fine balance is necessary - if the player ever actually runs out that's not going to result 
in an acceptable death at *all*, but having too many ruins the effect.

The best example of shaping player checkpointing I've yet seen can be found in *Dark Souls*, and specifically 
in its iconic Bonfires. I could write an entire article on challenge-related design in *Dark Souls*, but the 
Bonfires may be my favourite.

Their appearance fits with the game's aesthetic but stands upright and visible, and the game rarely hides them. 
First marking one as reached involves lighting it with a press of a button and a unique lighting animation, 
cementing the success of advancing further in the game.  Once lit, warm and comforting flames curl upwards 
from the base - an effect used nowhere else, since offensive fire effects are faster and far more aggressive. 
Actually using them as a checkpoint even involves your character sitting down at them and resting. Their 
entire design is geared towards having the player checkpoint there and only there. They're fundamentally 
just save points, but I've yet to see a better save point.

![Dark Souls - Bonfire](/static/images/a_good_death/DarkSoulsBonfire.png "I feel safer already.")

### Personally...

...I like to play *Monster Hunter 3 Ultimate*. Monster Hunter is a game of planning, learning and attrition, 
a few hunters attempting to wear out and bring down a seemingly unstoppable mass of muscle and bone. 
My first proper hunt in Monster Hunter was a Barroth - an oversized T-rex with a club tail and a tough 
bony spade-like ridge for a forehead. 

The battle takes forty full minutes of my constant attention. I have no potions, precious little health, my 
stamina failing me. He limps, much of his strength lost, many attacks ending in lumbering falls.  Earlier he 
raged and I could do little but strive to dodge and survive but now even that fire is gone.

He seemed unstoppable, invincible and powerful, but I'm learning.

When he lashes out I dance aside, when he pauses I strike where he cannot reach, when he shakes great masses 
of mud to delay me I step in to cut at his vulnerable belly. We're both nearing our end.

He charges, great ridged head lowered. I step in, roll left, turn to raise my sword for the final blow - 
and have time enough to realise my mistake before a flicked tail smashes me into a defeated backwards slide. 

Forty minutes and a great pile of potions, whetstones, rations and resources, everything I have lost, and all 
I feel is exhilaration. I earned every step of that battle. The loss of that much time and effort would be 
inconceivable to many games, but that was a hunt, its separation from the safe camp clearly defined, and I had 
failed it - an **acceptable** price, a reasonable one, stated up-front.  My defeat was my own mistake, the 
flick of a tail which always flicks in that direction on that attack, a mistake I had made and learned to 
avoid but still, in the end, forgot. A **fair end**, without a doubt. 

A Barroth is, by the standards of the game, a very weak monster - but that battle is still one of my most fondly 
remembered. 

![Monster Hunter 3 Ultimate - Barroth](/static/images/a_good_death/MH3UBarroth.png)

Death is frustrating when players lose more than they expect and feel that they have been cheated out of their 
fair earnings, and this loss can be made **acceptable** by either understanding or defining what they expect to lose.
Death is frustrating when players feel that they have no control over their loss, and can be made **fair** by informing 
the player about the threat of death both before and after, such that they either perceive the threat or recognise 
their mistake after the fact.

A good death is one which costs the player no more than they expected and which the player believes to be their fault. 
