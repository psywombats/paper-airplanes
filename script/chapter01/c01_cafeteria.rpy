label c01_cafeteria:

    The second floor of the main building was known to be the loudest in the entire hospital, perhaps even louder than the emergency rooms in the west wing.
    This floor was filled with small children happily playing games with one another, not caring about the wounds or illness they had.
    Smiling at the sounds of the children's laughter, Toma and I walked down the hallway, taking a right halfway down the hall.
    Opening the glass doors, we entered the large room, the heavenly aroma of different types of foods wafting to our noses.
    It was two in the afternoon, so the cafeteria was still rather crowded with residents or visitors alike.
    t "Go ahead and pick a table for us. I'll bring the food over once it's done."
    c "Oh, alright. {w=1.0} I think I'll have..."

    menu:
        "The usual":
            $lunch_usual += 1
            c "The usual, please."
            
        "The lunch special":
            $lunch_special += 1
            c "I want to have the lunch special today."

    t "Coming right up!"
    Toma turned and walked towards the counter where the food was being sold, lining up in the fourth line.
    I turned around, facing the many tables that were already occupied, leaving only a small selection free.
    Of course, all of the seats right next to the tall windows were taken, the occupants fawning over the scenery.
    I smiled at the sight of the happy residents, glad that they were enjoying the scenery.
    I began to walk towards the back of the cafeteria, where a table laid lonesome by itself.
    Many people disliked sitting at this area due to the lack of light. {w=1.0} However, I found it to be more reason to sit there.
    Perhaps it was just me, but I had always enjoyed sitting in a low light area. {w=1.0} The strong heat coming off of the lightbulbs and the bright light shining had always bothered me.
    Once I reached the lonesome table, I pulled out a chair and sat down, facing the rest of the cafeteria.

    if $white_book == 1:
        I placed my book down in front of me, staring blankly at the white colored cover.
        A little girl, unfortunately cursed by something so beautiful and fragile as a flower...
        A sad tale, but I had found comfort in it. {w} Perhaps it was because of the \"curse\" the little girl had?
        The curse that had fallen upon my mother and me versus the curse that fell on the fictional child... {w=4.0} So different and yet so similar.
        A gentle sigh escaped my lips, turning into a soft hum halfway.

    if $green_book == 1:
        Innocent children, waking up one morning to find their parents and close relatives gone...
        I couldn't help but feel sorry for them.
        Their ages varied from eight to eighteen, all with their own powers and unique personalities.
        What would I do if Meadow had vanished, I wonder...
        Meadow is like a mother and yet an older sister to me. {w=2.0} I wouldn't know what to do if she was gone...

    if $yellow_book == 1:
        A human girl, half human and half Bulakka.
        I can only imagine that she has been bullied a lot in her past...
        And yet, she tries really hard to move forward from her past, joining her funny uncle in his drama club.
        The girl is so strong... {w=1.0} I don't think I would ever have the strength to continue if people had picked on me.
        I struggle enough already... If I was ever being picked on, I wouldn't be able to...
        I gasped softly in surprise, realizing how depressing my thoughts had become.
        I shook my head violently, trying to desperately to keep the sad thoughts away.
        If only forever...

    if $direct_cafeteria == 1:
        As I waited patiently for Toma to arrive with our food, I began to hum a little tone to myself.
        The melody was off key and the tone was horrible.
        I giggled a little to myself at my horrible humming skills, finding it fun nonetheless.

    t "Hey, here's the food."
    I lifted my head up in surprise. Toma's perky voice snapped me to reality.
    Toma smiled brightly as he held two trays, placing the one on his right hand down in front of the empty seat in front of me.

    if $white_book == 1:
        I quickly removed the book from the table, setting it on my lap as the tray on Toma's left hand is set down in front of me.

    if $green_book == 1:
        I quickly removed the book from the table, setting it on my lap as the tray on Toma's left hand is set down in front of me.

    if $yellow_book == 1:
        I quickly removed the book from the table, setting it on my lap as the tray on Toma's left hand is set down in front of me.

    if $lunch_usual == 1:
        The meal consisted of a small serving of white rice and thin slices of juicy, tender beef.
        A small plate of various vegetables accompanied my food, along with a small teacup filled with honey lemon tea.

    if $lunch_usual == 1:
        The meal consisted of a small bowl of thin noodles, bathed in a salty broth and topped with eggs and green onions.
        Two small pieces of toasted bread lay on top of a plate next to the bowl and a small cup of honey-lemon tea.

    Toma's tray that he held in his right hand consisted of a medium sized bowl that was filled to the brim with salty and chicken-scented broth and thick layers of noodles filling on top of each other underneath the salty soup.
    He also had a small plate of sugar coated doughnuts. {w=1.0} It was right next to a tall cup of tan liquid, most likely coffee.
    Toma has quite the sweet tooth. Even though he most likely plans on buying flan once we’re done eating, he loves to eat the sugar coated donuts.
    Toma placed the tray down in front of his seat in front of me, happily taking a seat.
    c "Thank you for the food! May Ion bless it with his powers and keep us pure."
    t "True words of wisdom! Now, let's eat!"
    Smiling at the small, but surely fulfilling entree, I picked up the cutlery next to me and began to eat the slices of beef with the rice.
    After a few bites of the beef and rice, Toma suddenly made a loud cry of satisfaction, his face flustered in bliss.
    t "WOOO! {w=1.0} Man, this food is ab-{i}soup{/i}-lutely food-tastic!"
    I quickly covered my mouth with the back of my right hand, muffling my laughter as the pairs of eyes from everyone in the room turned towards us.
    Toma didn't mind their confused looks, who continuously making cries of satisfaction.
    c "Toma, stop it! {w=1.0} You're making too much noise!"
    t "Aw, come on! {w=2.0} The kids outside are making more noise than I am!"
    c "True, but right now, you are the loudest person in the room!"
    Toma laughed, rubbing the back of his head in slight embarrassment.
    Once Toma had calmed down, everyone returned to their normal conversations while eating the food of their choice.
    Toma's soup was gone shortly after, leaving him only his cup of coffee and doughnuts.
    As I continued to slowly eat the rest of my main food, Toma began to talk about his work.
    t "So recently, we found this plant called a \"buhana\" near the Green Sea Harbor in the northwest island of Morford. {w=1.0} Someone had accidently brought it along with them after their trip to the capital there."
    c "I see... {w=3.0} Did you get any new data from it?"
    t "Well, to help you... {w=4.0} Sadly not."
    t "However, I did gather a lot of information that led to another plant which is like a flower in some sense. {w=1.0} It just might be our ticket to the curse."
    t "Supposedly, it's a flower called an \"aquaba.\" It's a flower that stores a strange liquid in the head, and only blooms once every full moon."
    t "As for its location..."
    Toma fell silent, intensely thinking about something.
    After about two minutes, Toma groaned and slammed his right fist onto the table, causing my food to shake.
    c "Hey, Toma it's okay. {w=1.0} You're working hard enough already, don't over do it."
    t "No I'm not. {w=2.0} All I'm doing is sitting around and researching plants."
    t "I'm not working hard enough, and the fact that you aren't cured yet is proof of that."
    c "W-Well, four years isn't very long! I think that you're doing a good job!"
    Toma ignored my words, letting his head rest on his left hand, his eyes glaring in shame at the sugar coated doughnuts.
    Toma was always hard on himself, blaming himself for the fact that I was still in the hospital.
    I wish that he wasn't like this. {w=4.0} If he isn't careful, he too might someday be in this hospital.
    c "Toma, you just need to be patient."
    c "I'm really grateful that you're working so hard for my wellbeing, but please... {w=4.0} Take care of yourself, alright?"
    t "... {w=4.0} It's funny how someone of your condition can say that so freely."
    Toma didn't say a word after that, nibbling on his food.
    The air surrounding us had become stiffening and uncomfortable; glances shot our direction from the others.
    He is becoming more and more like a father with each passing day...
    [Transition]
    Toma's usual self returned by the time we finished eating. After having a cup of flan with me, we began to walk back towards my room.
    My IV had run out, causing my body to feel weak and my eyelids tired.
    t "Man, when are they going to let Fail Flan go? {w=1.0} It was a complete accident anyway."
    c "Ehehe... Well, it's going to be a while for the chefs to forgive us for making that mess."
    t "Psh, they're just really grudgy."
    c "Think about it from their perspective, Toma. {w=1.0} We were running around with open cups of flan, and spilt it all over the ground!"
    c "Last time I checked, caramel is very hard to clean up."
    t "Hm... {w=2.0} That's true."
    c "But that’s what makes their flan super good! {w=1.0} Even if it is from a vending machine."
    Toma nodded happily, a certain loving sparkle in his eyes.
    t "You can say that again! {w=1.0} If it weren't so expensive, I'd go for another cup right now with extra caramel!"
    c "Mm, that does sound nice..."
    t "Right?!"
    t "Flan is the miracle food that is able to cure anyone's sadness!"
    c "Flan is the miracle food!"
    Toma and I laughed as my door became visible to us.
    Speaker "Toma Brith, you are needed in the office. {w=1.0} Toma Brith, you are needed in the office."
    t "Aw man, it's that time already? I didn't even notice how late it was!"
    I giggled at Toma's flustered reaction, finding his definition of late amusing.
    Toma's break time can go as long as five hours every other day; he is released from the office at 11:25 and has to return by 4:30.
    Toma often used those hours to sleep and occasionally to stop by to see me like today. {w} But that is mostly when he had the treat of obtaining his pay.
    t "Sorry to cut short Celia, but I gotta dash."
    c "It's fine, just take care of yourself!"
    t "Heh, I'll try."
    t "Oh, and uh, hey... {w=4.0} Back there... {w=1.0} I really didn't mean it."
    c "I know, it’s okay. {w=1.0} Now go on, or you’ll get in trouble!"
    t "...{w=3.0} Thanks for putting up with me."
    I smiled at Toma's words, feeling the genuine gratitude behind them as he turned around and began to jog forward.
    I stopped in front of my door, watching Toma jog off into the distance before taking a sharp left turn, where an elevator awaited him.
    I smiled in relief at Toma's safe trip, glad that he didn't fall or trip while jogging.
    I placed my hand on the doorknob, and began to turn when a loud slam snapped my attention to the area behind me.
    To my surprise, down the hall, a young boy about my age held onto a doorknob for dear life as he struggled to stand.
    His raven-black hair covered his eyes as he looked around, his head turned to my direction.
    I blinked in surprise when his emerald green eyes met mine; they sent a shiver down my spine.
    I held my book close to my chin on instinct, considering it as a small barrier between he and I.
    c "Ah, um... {w} H-Hello."
    I stuttered, feeling his eyes glaring daggers at me, making me rather nervous.
    The boy said nothing as he turned around, his feet clumsily tripping on each other while he began to walk forward.
    My eyes slowly drifted towards his shoulders, causing another shiver to run down my spine at the flapping left sleeve.
    Where one would usually find a left arm, that boy had nothing.
    I recalled Toma's words about the accident victim losing something valuable. {w=1.0} That boy must be the new resident then!
    My face lit up at the realization. {w=1.0} There was a new resident who was about the same age as me!
    A chance to make a new friend!
    ??? "Where do you think you're going?"
    I flinched at the voice, instantly recognising it to be Meadow's.
    I turned around and saw Meadow marching forward, a serious and slightly surprised look on her face.
    c "Oh, hello Meadow!"
    m "Miss Celia, please get inside your room."
    I blinked in surprise as Meadow marched right past me, quickening her pace as the boy staggered to the right wall, using his right arm as a support.
    Meadow grabbed the boy's shoulders, causing him to flinch and instantly start shaking her off.
    m "Sir, you shouldn't be walking around like this. {w=1.0} Let's go back to your room, alright?"
    Meadow instructed in a calming manner. {w=1.0} However, the boy didn't listen and continued to shake Meadow off.
    I fidgeted where I stood, a concerned look on my face as I wondered if I should help Meadow calm the boy down.
    The boy suddenly stopped shaking Meadow off, his body becoming limp and almost falling to the ground, {w=1.0} but thanks to Meadow's strong grip, she was able to help him stand.
    It appeared that he had fainted, which was normal for an accident victim.
    c "H-Here, let me help Meadow."
    I took a few steps forward, wanting to help when Meadow looked calmly over at me and smiled.
    m "Thank you dear, but I've got everything under control."
    m "You went out with Toma today, right? {w=1.0} Go on inside and rest."
    c "Ah, but..."
    m "It's fine, go on now Miss Celia."
    I watched Meadow wrap her arms around the boy, easily carrying the boy by the waist into his room.
    I pressed my lips together and obediently entered my room.

    jump c01_end
