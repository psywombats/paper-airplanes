# WARNING! This file is generated! Do not edit!

define c = Character('Celia', show_two_window=True, color="#dfdfdf")
define t = Character('Toma', show_two_window=True, color="#dfdfdf")
define m = Character('Meadow', show_two_window=True, color="#dfdfdf")
define k = Character('Kenta', show_two_window=True, color="#dfdfdf")
define who = Character('???', show_two_window=True, color="#dfdfdf")
define n = Character('Nyu', show_two_window=True, color="#dfdfdf")


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

label c01_downstairs_badend:

    I'm a little curious about what's happening downstairs...
    I don't think it would hurt to go and see what is going on.
    After a good solid three minutes of debating with myself, I mustered up as much courage as I could and moved my breakfast tray to the side. 
    With a deep breath, I slid out from my blanket, letting my feet hit the ground.
    n "Nyu!"
    I looked over to Nyu, who was giving me quite the stern look from her glossy eyes.
    c "I'm just a little curious Nyu. I won't be gone for too long, alright?"
    n "Nyu..."
    I gave her a quick reassuring smile as I unhooked my bag of IV and carried it gently in my arms.
    Usually, I would go "mobile" by putting my IV into a small vial, but I didn’t want to waste any time.
    Leaving Nyu by her lonesome, I walked over to the door and hesitantly opened it.
    If I had to be honest with myself... {w=3.0} I was a little nervous.
    Many people come to this hospital for a variety of different purposes, ranging from casual checks ups to drastic emergencies.
    If I head down there, I might see something horrible…
    A broken leg…
    A dislocated shoulder…
    Or maybe even a black eye…
    ...Or blood.
    A cold shiver of fear ran up and down my spine at the thought of what I might see.
    I shook my head, pushing the negative and fearful thoughts out.
    I will only be there for a moment, take a glance of the situation, and then leave before anyone can notice me.
    With a confident nod, I took a proud step out of my room.
    I looked down the hallway before taking another step, noticing that the nurse’s station not to far from my room is rather empty.
    Using this to my advantage, I stealthily ran towards the elevator. 
    It would be a lot more troublesome to take the stairs.
    The other doctors and nurses would have a higher chance of noticing me if I took the stairs, and they would instantly notice me thanks to the incident four years ago.
    Once I reached the elevator, I quickly pressed the button five times in desperation while looking both to the left and right, making sure not to get myself caught..
    I took a step back and impatiently waited for the elevator. 
    As I waited, I suddenly heard two low voices - most likely two men - shouting. 
    Their voices were mixed with the rapid sounds of stomping footsteps.
    I gasped softly in worry, trying to find a place to hide.
    mans_voice "Did... see... poor kid?!"
    I froze in place at one of the voice's words. 
    A child... Could this be about the noise downstairs?
    What happened? {w=2.0} Why does the man sound like he is in such a panic?
    Because of how loud their footsteps were, I couldn't hear everything they were saying.
    other_voice "His entire... blown off! This... is getting... hand!"
    \"Blown off?\" {w=4.0} Something from that child was blown off?
    Why? {w=2.0} And by what?
    Wha... What is going on beyond the walls of the hospital...?!
    mans_voice "We need to... Silver... there!"
    other_man "You're right, there... much blood...!!"
    What...? {w=1.0} Blood...?
    Suddenly, my heart began to pound as if trying to escape my body and run far away from the frightening words.
    c "..."
    c "...Ngh..."
    My body became tight; I found myself frozen in place.
    My eyes strained to stay open as I stood there, motionless aside from my throbbing heart. 
    Something isn't right.
    The panicked voices of the men started to blend with their footsteps, fading away into an abyss, where I couldn't hear anything.
    My chest... hurts...! {w=1.0} I-I'm scared…
    What's going on?
    My knee trembled, ready to lose their strength as my heartbeat rang in my ears like the lasting notes from a base drum.
    Each breath I took stabbed my body; waves of pain flowed through my body endlessly.
    It hurts... {w=4.0} So much…
    Slowly, my blood began to turn cold... 
    My heartbeat stopped as a momentous sound rung in my ears.
    My legs now felt numb as I let out a soft sigh.
    My eyelids suddenly became heavy, closing against my will and blocking me out of the vivid world I was in only moments ago…
    The next thing I knew, everything became still...

    .:. Bad Ending
    return

label start:

    [NVL format]
    Somewhere in the vast world of Mion, above where Ion sleeps, there is a meadow.
    The meadow has a secret that only those with the curse may know. {w=4.0} Not even the dark lord who watches over them, Kxon, knows where this meadow lies.
    The meadow is surrounded by tall, healthy, and green alder trees beneath a bright blue sky, creating a peaceful tranquility.
    It is a meadow filled with flowers that virtually cover the green grass. {w=4.0} The lovely flowers vary from yellow carnations, cosmos, irises, jasmines, lilies, orchids, to white roses.
    In this meadow, flower petals dance elegantly in the gentle spring breeze, never learning of the cold and harsh touch of winter.
    The tall alder trees protect the flowers at their base from the small drops of rain, causing the green grass to shine in the dew of the water.
    Amidst this beauteous scenery, {w=2.0} there is a young mother and her daughter, calmly making flower crowns while listening to the soothing lullabies from the wind.
    The mother has long beautiful blond hair that could light up the night sky, complemented with a pair of zircon colored eyes.
    The daughter is a spitting image of her.
    "\"Tell me, dear...\""
    ...began the mother as her fingers stopped tying the silky stems of flowers together.
    "\"What is the most painful thing that exists in this world?\""
    The daughter looked up from her imperfect flower crown, caught off guard by her mother's sudden question.
    "\"Um... I'm not sure, Mama. What is it?\""
    The daughter replied, unsure of where the conversation was going.
    The mother chuckled softly - a hint of sadness hidden in it - and placed her flower crown beside her.
    "\"Our curse.|""
    The mother muttered under her breath, barely whispering.
    She suddenly stood up, causing her daughter to tilt her head to the side.
    "\"Hm? {w=3.0} Are you going somewhere, Mama?\""
    The daughter asked, as her hands holding the flower crown slowly descended to her lap.
    The mother said nothing, a sad smile upon her face, as she turned her back towards her daughter and began to walk forward.
    She had no where in particular she wanted to go.
    She just knew that it was time for her departure.
    "\"W-Wait, Mama!\""
    The daughter called out, as she tried to stand up. {w=2.0} But her legs did not want to move, leaving her immobile on the ground.
    Without turning around, the mother continues to walk forward.
    She can't look back.
    They won't allow her to.
    This is how it was meant to be.
    "\"You still yet to understand the sadness of your ancestors... {w=4.0} Choose your actions wisely, my dear.\""
    The mother spoke in a momentum tone, a light brighter than the sun sparkling between the gaps of trees.
    "\"Mama, wait! {w=1.0} Please wait for me! I-I can't move!\""
    The daughter cried out, confusion and fear stirring up inside her.
    Before her, her mother was slowly going away.
    As confused as the daughter was, she had a feeling that... {w=2.0} she wouldn't be able to see her mother ever again if she goes.
    The poor child began to cry, reaching her small slender fingers towards her mother's back - hoping that in some way her mother would stop.
    But her mother continued to walk forward, towards the light, ignoring her daughter's cries.
    The girl's tears, the ones that she had tried so hard to keep in, began to seep out of her eyes as her vision began to blur, causing the sight of her mother to slowly blend with the colors of the meadow.
    The poor girl was too young to understand any of her Mother's words.
    All she wanted was for her mother to turn around with a smile and apologize, claiming that everything she did was nothing more than a joke.
    The child reached out as far as she could towards her Mother's back, crying out -
    [ADV format]
    who "Mama!"
    who "Ah...!"
    who "...That dream again..."
    who "...That's right... {w=4.0} It's just a dream..."
    [NVL format]
    A long sigh escaped from my lips as sweat tickled my skin while sliding down my jaw.
    Needing to calm myself, I listened to the soft ticking of the clock and the gentle beeping of the heart monitor.
    How long have I awoken to that same dream? {w=2.0} Possibly for three or four years now...
    Although, now that I think about it, that was the first time that mother had said something to me before she left.
    Before, it used to be nothing more than a simple "goodbye" and leave the child me in the dream.
    Maybe if I fall back to sleep, I can catch up to her and ask what she meant?
    ...No, dreams don't work like that.
    Dreams - at least the ones you have while you're asleep - are meant to fulfill the strongest desires from your heart, right?
    My desire may not be to have my mother leave me, but rather to keep her with me...
    However, the same dream has been replaying in my mind each night for four years. 
    I can predict every single word that will be uttered due to the redundancy of it.
    But even so, I still have no knowledge of why my mother leaves me in the dream.
    Although, I know why she left in real life... {w=3.0} It is the same reason why I live in a hospital.
    Suddenly feeling myself slowly drifting back to sleep, I let out another sigh - much longer than the first - as I wipe off the sweat on my face.
    As much as I wanted to fall into a deep slumber once again, I had a full day ahead of me.
    A day where it should never be wasted.
    I slowly push my body up with my elbows, my eyes lazily fluttering open.
    My eyelids felt heavy and my arms didn't have much feeling in them, but I somehow managed.
    Once I was propped up with my torso limply slouching over my legs, I glanced over to the clock. {w=2.0} It's seven in the morning.
    I woke up right on time as always. {w=1.0} Maybe I really do have an alarm clock embedded in my body that wakes me up.
    I arched my back a little, feeling the tension in my body disappear and began to rub my eyes, yawning in the process.
    I looked over to the right, where the only true window in my room hid behind the thick white curtains.
    It looks like the weather will be nice today, based on the bright light coming out from the bottom of the curtains.
    This room is often cloaked in darkness until the dawn. And even once the sun is out, not a single ray of sunlight penetrates through the curtains.
    To be more precise, room 302 on the third floor of the west wing in the Creed Hospital is where I reside.
    It is the second largest room in the entire hospital, the largest being the delivery room.
    It's a nice room overall, nicely decorated with furniture and large space, but I wish I didn't have so much.
    I shouldn't be the only one who gets all the nice stuff. There are other children who are younger than me that reside in this hospital, after all.
    In fact, I wish I didn't even have any of these extra furniture. {w=1.0} I would trade it all for nothing more than a different colored room and a simple chair next to my bed, with the vase of flowers on the window sill.
    Something like this is probably only me, but when you enter a hospital room, it doesn't feel very welcoming.
    When you enter, the room seems to emit a sad and cold atmosphere, thanks to the gray and gloomy color palette. {w=1.0} The first thing you see is the window and its curtains, which then makes you look at the color of the wall.
    The moment you do, all of the furniture vanishes, as if it was covered by an invisible cloak or disappeared into thin air.
    Recoloring the entire hospital would be nice; it would give each room its unique color of choice.
    Let's see... My room would probably look nice if it was colored... {w=1.0} Green.
    Yes, green is a nice cheerful color! It's one of my favorites!
    But I suppose having every single hospital room recolored with such a bright color palette might give the visitors a slight spasm.
    And that wouldn't be very good. {w=1.0} That would be horrible.
    [ADV Format]
    who "Nyu!"
    Suddenly, a high pitched voice squeaked to my left, snapping me back to reality.
    I looked over to the left and saw my friend and pet, Nyu, land on my bed.
    Using her small and stubby little arms and legs, she managed to wobble over my direction, her small glossy black eyes shining in excitement, and her cute little button nose twitching.
    I smiled at Nyu as she stopped right next to me, a slight look of exhaustion on her face.
    who "Good morning, Nyu. Did you sleep well?"
    n "Nyui!"
    I giggled at her reply, petting her soft pink and white fur.
    Nyu purred in reply to my touch, her ears twitching happily.
    Once she was satisfied with me petting her, Nyu pulled her body away from me and began to rummage through her small bag that is meant to hold emergency medicines for me.
    who "What are you doing, Nyu? Did you hide something in there?"
    Nyu ignored my questions as she continued to look around in her small bag.
    After a moment of silence and rummaging, Nyu pulled out a small note card and practically thrust it at me.
    I hesitantly took the card from Nyu's paws, smiling nervously at Nyu's forward behavior.
    Looking down at the card, I noticed that it appeared to be blank.
    I glanced over to Nyu, not knowing why she had given this to me.
    n "Nyu!"
    Nyu pointed at the card with confidence, huffing excitedly.
    I glanced back to the card, wondering what secrets it had.
    I began to twirl the card around, eyeing each corner of it for clues when I notice three letters on the back.
    who "\"H.B.C"\...?"
    I tilted my head in confusion at the three mysterious letters.
    I had a feeling that they meant something, but as I was still groggy from my sleep, I couldn't interpret the meaning.
    Was it some sort of secret code? {w} A code that could release Nyu's true form of ultimate fluffiness?!
    ...No, of course not. {w=1.0} That would be ridiculous.
    Exciting, but ridiculous.
    After a moment, I gasped softly in realization. 
    Today is my fourteenth birthday.
    On instinct at the realization, my shoulders slumped, as if trying to dampen the mood.
    Today is also the fourteenth anniversary of my Mother's death.
    She had died the very same day, if not the exact moment, I was born.
    Today is a day of joy, and yet it is also a day of sadness.
    A majority of my friends mainly remembered today as Mother's death...
    With a soft sigh, I quickly shook my head at the thought of "sadness", not wanting to ruin my birthday.
    I'm sure my mother wouldn't have wanted me to be sad on such a special day.
    The \"H.B.C\" must stand for \"Happy Birthday Celia.\" {w} They are the three letters that Nyu could manage to write.
    I looked over to Nyu and smiled.
    c "Thank you for the present, Nyu! {w=1.0} Your handwriting has really improved!"
    n "Nyu!"
    Nyu triumphantly placed her paws on where her hips would be, her ears twitching happily.
    I giggled at Nyu's response, gently petting her head.
    Suddenly, my stomach growled at me, demanding for food.
    Nyu squeaked in surprise at the sudden growl, jerking backwards.
    I giggled at Nyu's tumble from my stomach and looked over to the clock again. 
    It's 7:25.
    c "Oh dear, it's almost 7:30 already? {w=1.0} She's running a little late, isn't she?"
    I heard Nyu squeak in reply, agreeing with me.
    Right as the clock struck 7:26, my personal nurse, Meadow, opened the door, carrying a tray of food.
    m "Good morning, Miss Celia! {w=2.0} Good morning to you as well, Nyu!"
    I raised an eyebrow at Meadow's greeting, surprised at what she has called me.
    That was the first time she had called me \"Miss Celia\".
    c "Good morning, Miss Meadow!"
    Meadow blinked several times in surprise as she stopped beside the bed, a surprised look on her face.
    m "Huh? {w=3.0} {i}Miss{/i} Meadow?"
    I couldn't help but chuckle nervously at Meadow's response. 
    Did she not notice how she called me \"Miss Celia\"?
    c "Well, you called me \"Miss Celia\"". {w} I'm assuming that this is a new name game?"
    Meadow blinked in surprise before laughing at my explanation, placing the tray of food on my lap.
    m "No, no, it's not a name game!"
    m "I've been ordered to call you \"Miss Celia\" as a symbol of your 14th birthday. You're practically a young lady now!"
    I puffed out my cheeks in slight disapproval at her \"orders\", feeling like it was a bit unnecessary.
    Meadow giggled at my reaction and pinched my cheeks, causing me to smile a little.
    m "Come on, no need to be like that! Orders are orders, Celia. There is nothing I can do."
    I smiled sadly in understanding as Meadow let go of my cheeks.
    I looked down to my lap, where the glorious sight of my breakfast lay on top of the tray.
    Mixed with the bitter smell of ketchup, crisp bread and salted butter, the smell of the freshly cooked eggs and rice began to waft its way towards my nose, causing my stomach to growl once again but louder this time.
    Meadow couldn't help but laugh at the sound of my growling stomach.
    m "Wow, that was a loud one! You must be really hungry today, huh?"
    c "Hehe... Well, yes. {w=1.0} After all, you were six minutes later than usual."
    m "Ah, I'm sorry about that. I overslept this morning."
    I couldn't help but laugh a little at her excuse. 
    I see she is quite honest as usual.
    After laughing, I began to eat my food as Meadow took the clipboard from the end of my bed and wrote down the complicated numbers on the heart monitor.
    The morning has always been my favorite part of the day.
    Perhaps it's because I get to drink a nice cup of honey milk.
    Sweet silky honey melted in the smooth texture of hot milk...
    Here in the hospital, milk is only actually available in the morning.
    If you miss your chance now, you don't get to drink milk for the entire day.
    It's a strange rule for some - especially me, as I love milk.
    Suddenly, I heard a loud and stressed disarray of voices coming from the other side of the door.
    Surprised by the sound of the voices, I slowly stopped eating as Meadow turned her attention towards the door.
    c "Huh? {w=2.0} What's going on out there?"
    m "Sounds like a victim from an accident..." 
    m "But your room is almost soundproof, so the fact that we can hear them is..."
    Meadow's words trailed off as she stared intently at the door.
    Meadow placed her clipboard back onto my bed, a stern expression forming on her face.
    m "You stay here, Miss Celia. Whatever you do, do not leave your room."
    I blinked in surprise at Meadow's order, rather confused by her words.
    Stay in my room...?
    I always stay in my room and can't even leave it unsupervised... 
    So why would today be any different?
    Before I could open my mouth to ask Meadow why she had told me to stay in my room when it was such a common thing for me, she swiftly turned around and left, the door closing gently behind her.
    I stare at the door in surprise and confusion, Meadow's chocolate brown hair fluttering out of my view.
    c "... {w=1.0} Something isn't right..."
    n "Nyu?"
    I could hear the panicked voices coming from the hallway and the emergency room on the first floor, where many of the victims are transported to the west wing for surgical purposes.
    Vehicle accidents aren't common in this town, but when they occur the staff knows what to do and is always calm about the procedure.
    If they are making so much noise from three floors down, this isn't an average accident victim.
    ...
    Hm, what should I do?

    menu:
        "Stay in the room":
            jump c01_room

        "Go downstairs":
            jump c01_badend

label c01_library:

    c "I want to go to the library today! It has been so long since I have visited there, so it would be nice to see it again!"
    t "Haha! If you're not drawing your horrible portraits of Nyu, you're always reading a book. {w=1.0} Quite the nerd as usual."
    I gasped at Toma's words, slightly offended and shocked by his opinion.
    c "I beg your pardon, Toma!"
    c "There is absolutely nothing wrong with reading! {w=1.0} Besides, my drawings of Nyu are not horrible!"
    Toma chuckled at my reaction, patting my head all the while.
    t "Hahaha, come on, don't be that way! {w=1.0} I'm only teasing you!"
    I puffed out my cheeks as his hand slipped off my head, smiling cheekily at my reaction.
    It didn't matter who, Toma always had a way to push the buttons of anyone he meets.
    In order to stay on that person's good side, he'll say that he was only teasing them. 
    However, he seems to only pat my head when clarifying his way of teasing.
    t "Come on, let's go."
    I smiled and nodded, the two of us walking side by side as Toma began to tell me stories of his adventure away from the hospital.
    [Transition/In the library]
    I stretched my arms in the air in delight, taking in the lovely scenery of bookshelves carrying the many different types of literature inside of them.
    The library rarely sees any visitors, so it is the perfect place to forget your troubles and dive into a new world.
    Along with the small signs of plant life on the window and the faint sky-blue colored walls, time quickly passes here. It is the true sanctuary for those wanting to escape reality.
    At the moment, my favorite section is science fiction.
    c "Ah...! The library! So many books to explore!"
    t "More like so many books to snore..."
    I gave Toma a sharp look at his remark, causing him to laugh nervously.
    t "Hey, don't give me that look! {w=1.0} I'm just kidding~!"
    I puffed out my left cheek, showing that I wasn't going to let Toma off the hook so easily with his remark.
    Toma laughed a little as he walked forward, smiling nervously at me as he pointed somewhere in the distance.
    t "A-Anyways, I'm pretty sure that this place has gotten a fantasy aisle recently. {w=1.0} Want to check it out?"
    c "Huh? Fantasy?!"
    t "Yeah, fantasy. {w=1.0} Come on, it's this way."
    Toma took the lead and began to walk towards the left corner of the library, the sounds of our footsteps bouncing off the walls and echoing in our ears.
    The smell of books and flowers filled the air, forming a comfortable and soothing atmosphere.
    {Bookshelf}
    t "If folklore and legends are over here then... {w=2.0} Here we are! Fantasy."
    Toma placed his hands behind his head in victory and stepped to the side as I walked forward, entering the narrow aisle between the bookshelves.
    c "Amazing...! You really know your way around the library, Toma!"
    Despite the library's simple but calming interior, the bookshelves and books themselves all look fairly similar, forcing visitors to be at a complete loss about which book to get.
    t "Ah, well... {w=3.0} That's not really true."
    t "The bookshelf right next to us is all about folklore and legends dating all the way back to Ion's time. {w=1.0} I'll be the first to know about anything new around this general area."
    I giggled as Toma made a heart with his hands, pointing it towards the direction of a bookshelf nearby.
    This was the one thing I had always found amusing with Toma.
    He loves anything about Mion's past era, including the "Old World" era, where our world was at its most hideous state.
    Aside from capital scholars, no one knows the stories from back then {w=1.0} but even for them, all they can do is come up with small and simple theories.
    c "Hehe, well, thank you for letting me know!"
    t "No problem."
    t "I'll go and get us the table, so you go on ahead and pick out a book."
    c "Alright, thank you!"
    Toma nodded at my words, stuffing his hands into his lab coat pockets, and turned around, walking towards my favorite table.
    I turned towards the bookshelf and scanned the selection it had to offer for me.
    Each book was a key to a portal; {w=1.0} one that would take me away from Mion and into the world of the book.
    Impatient and wanting to explore the new worlds, I quickly grabbed three random books that had my three favorite colors as covers.
    One was white, another was green, and the last was yellow.
    With a happy smile, I held the books close to my chest and began to walk towards Toma who was sitting in the comfortable chairs with his head hanging limply from his shoulders.
    As I inched closer and closer to him, he began to snore loudly, like the growling threats of a bear.
    I smiled at his behavior, shaking my head in disapproval.
    c "Come now Toma, don't pretend to fall asleep and snore like that."
    c "Do something proactive and read a book yourself."
    t "Ugh, but I've read all the books that interest me!"
    t "This place has a surprisingly low number of books in regards to legends. {w=1.0} You would think that the library would import new ancient books that are actually important instead of those boring and inappropriate romance novels."
    I giggled nervously at Toma's words, understanding his frustration with the library's priorities.
    c "Well, there is no stopping the librarian from getting what she wants."
    t "Ah... {w=4.0} Haha, that's what you think..."
    I blinked in confusion at Toma's words and his now flushed face.
    t "Well, whatever. Maybe I'll just read one of your books."
    I looked down at my arms as Toma pointed at the three spines facing him.
    c "Oh, alright! Which one do you want?"
    t "Doesn't matter, I'll just take one of the books you won't be reading."
    Toma slumped down in his seat and pushed the seat across from him, telling me to sit there as it was my usual spot.
    I took a seat, placing the three books I had selected randomly in a row in front of Toma and me.
    Hm... Which book should I read?

    menu:
        "The white book":
            $white_book += 1
            c "I'll read the white book."
            t "Alright, then I'll read the green one."
            The two of us slid the books we had claimed close to us as Toma moved the yellow book near the end of the table.

        "The green book":
            $green_book += 1
            c "I'll read the green book."
            t "Alright, then I'll read the yellow one."
            The two of us slid the books we had claimed close to us as Toma moved the white book near the end of the table.

        "The yellow book":
            $yellow_book += 1
            c "I'll read the yellow book."
            t "Alright, then I'll read the green one."
            The two of us slid the books we had claimed close to us as Toma moved the white book near the end of the table.
   
    Toma instantly opened up the cover and began to read, his head resting on his left hand as his eyes slowly scanned the words.
    While Toma read his book in the most indifferent way possible, I looked over to the right of me, where the window we had sat next to glowed its normal radiance of pure sunlight.
    There, right in front of the window, was a field of white.
    But not of snow. {w=1.0} It was a field of daisies.
    Normally, such a plain flower wouldn't be so beautiful, {w=1.0} but the sight of a field of white petals gently swaying in the wind, glowing in the rays of the sun, makes them much more appealing than normal.
    On windy spring days, the petals would break off of the main stem, and join the wind in its reckless dancing.
    On wet rainy days, the daisies continued to glow a soft white color above them, as if the rain was supplying them with a new layer.
    It was because of those daisies... {w=3.0} That I have grown to love this spot most in the entire library.
    The thought of a simple flower being able to outshine its plain appearance soothes me.
    With a small smile, I looked down at my book, opened the cover and began to read.
    [Transition]
    t "...Celia."
    t "... Hey, Celia!"
    t "...Celia!"
    c "Hm?"
    I looked up to hear Toma's voice repeatedly calling my name.
    c "Oh my, I'm sorry Toma! {w=1.0} Were you saying something?"
    A small smile appeared on Toma's face as he tilted his head slightly to the side, raising an eyebrow as he continued to hold his head up with his left hand.
    t "Well, I'm pretty sure you haven't noticed it, but a bear barged into the room."
    c "Huh?! A bear?!"
    t "Hey, not so loud! {w=1.0} It's still in here."
    My body stiffened at Toma's warning, and I pressed my lips together to ensure that not a single sound was to escape.
    A terrifying idea entered my mind, causing me to slowly glance around my surroundings.
    I was too nervous to look behind me; the book in tightened in my hands.
    My heart began to race with apprehension, sweat forming on the back of my neck.
    If a bear was truly in here... {w=3.0} It could eat the books!
    No, wait... {w=2.0} Bears can't eat books, right?
    who "RAWR!"
    c "Eek!"
    I jumped in my seat, the books I was holding onto so tightly falling onto my lap.
    Laughter filled the library as I panted, calming my racing heart.
    t "Oh good Ion, that was... Hahaha!"
    c "T-Toma...!"
    t "Hahaha...! {w=4.0} I'm sorry, I... I couldn't help it!"
    I puffed out my cheeks in frustration, smacking Toma's hands gently with my book.
    c "You should know better than anyone not to do that!"
    t "Yeah, yeah, you're right. {w=2.0} Again, sorry."
    t "Anyway, the real bear here is your stomach."
    t "While you were reading, your stomach was growling away. {w=1.0} At first, I really did think that there was a bear in here.
    c "Ah... {w=4.0} Now that you mention it, I do feel rather hungry."
    Toma stood up from his chair, chuckling softly as he grabbed the book he was reading as well as the extra one.
    t "Well, how about the two of us grab something to eat?"
    c "Hm?"
    t "Your old man gave me my pay today, so I can buy you something in the cafeteria."
    t "I can even buy you some flan!"
    I smiled at the word "flan", happily standing up from my seat with the book close to my chest.
    Toma and I walked towards the entrance of the library, stopping at the checkout counter where the librarian - who is also a nurse - waited.
    t "Can you return these for me?"
    The librarian smiled and nodded.
    librarian "Of course, sir."
    The librarian took the books from Toma, and then turned her attention to me, eyeing the book I had.
    c "O-Oh... I would like to check out this one please."
    The librarian smiled politely, her dimples showing as she tucked a loose strand of her long red hair back.
    librarian "But of course, Miss Celia."
    I gave my book to the librarian, a nervous smile forming as the words \"Miss Celia\" echoed in my ears.
    Even the librarian was ordered to call me by that name.
    A stiffening silence fell over Toma and I as we patiently watched the Librarian swiftly checking out the book.
    With a loud thump from the check out stamp that printed the date of return on a little sheet, the librarian offered the book back to me.
    Librarian "I apologize for the wait. Here you are Miss Celia."
    My body flinched as she called me by that name once again, hesitantly taking the book back.
    t "...Alright then. {w=1.0} Let's have lunch, Celia."
    c "... {w=6.0} Yes, let's do that."
    Toma opened the door for me as I passed through, my head held high with a strained smile on my face.
    [Transition]
    As Toma and I walked down the hallway of the fifth floor, right below where the library was stationed, Toma took the book from my hands and opened the cover in curiosity.
    t "So, is this book any good?"
    c "Ah, well... I suppose so."
    t "What's it about?"

    if $white_book == 1:
        c "Well, it seems to be about a little girl who is cursed with a strange white flower, {w=1.0} but because she likes the flower so much, she tries to sell it to the other villagers."
        c "However, no one would buy it from her, because of the curse..."
        t "Huh... {w=4.0} Now I understand why you like it."
        c "Well, what about you? {w=1.0} Did you not like the book you were reading?"
        t "Yeah, mine was all about this group of kids taking care of each other after all the adults on the island vanished."
        c "Oh my, so it was a survival type of story?"
        t "I guess. {w=2.0} Unlike you, Celia, I just read books to pass time. Not as a way of entertainment."

    if $green_book == 1:
        c "Well, it seems to be about a bunch of children taking care of one another after all the adults in the island vanished. {w} Thankfully, a ship from the city found the island and offered to take the children there to look for their parents."
        c "As for the rest of the story, I haven't gotten that far yet."
        t "Huh... {w=4.0} I didn't know you were into survival."
        c "Eheh... {w=2.0} W-Well, it's not my favorite scenario, but I can't stop reading!"
        c "But what about you? {w=1.0} Did you not like the book you were reading?"
        t "Yeah, mine was all about this highschool girl who was half Bulakka overcoming her past by joining a drama program at her school."
        c "Really?! {w=1.0} That sounds interesting. Why didn't you get it?"
        t "Haha, well it wasn't my thing. {w=2.0} Unlike you, Celia, I just read books to pass time, not as a way of entertainment."

    if $yellow_book == 1:
        c "Well, it seems to be about a girl in highschool who is half human and half Bulakka. {w} She has a really sad past, and to move on from it, she joins a drama club that her uncle runs."
        c "I stopped on the sixth chapter, so I don't know anything else from that point."
        t "Sheesh, talk about girly. {w=1.0} I understand why you like it."
        c "Ehehe well, what about you? {w=1.0} Did you not like the book you were reading?"
        t "Yeah, mine was all about this group of kids taking care of each other after all the adults on the island vanished."
        c "Oh my, so it was a survival type of story?"
        t "I guess. {w=2.0} Unlike you, Celia, I just read books to pass time. Not as a way of entertainment."

    I smiled gently at Toma's words. As he began to stretch his arms up into the air, a comforting silence filled the long hallway.
    c "... {w=6.0} Toma?"
    t "Mm?"
    c "...Why do you not call me \"Miss Celia\" like the others?"
    t "... {w=5.0} It doesn't fit you, really."
    t "And to be quite honest, I know that it would make you more uncomfortable than you already are."
    c "Hehe, that's true..."
    c "...Thank you, Toma."
    t "Pfft, you should be thanking me for a total of four years worth of friendship."
    c "Hehe, that's true. {w=2.0} Thank you for everything, including being my friend."
    t "What? {w=0.5} I'm not your best friend yet?"
    c "Hehe, I think Ivy is still my best friend."
    t "Oh, ouch! {w=0.5} Your words stab me!"
    The two of us began to laugh, my soft giggling drowning in Toma's gentle chuckles.
    I always felt at peace when I was with Toma. {w=1.0} He seemed to have always find the right way to cheer me up, even when nothing was bothering me at all.
    The two of us began to rush towards an elevator that had opened; two elderly women in matching dresses slowly exiting them.
    t "Hello."
    c "Good afternoon!"
    The women gave Toma and I a short nod, wide smiles forming on their aged and wrinkled faces.
    Then, we entered the elevator moments before its cold metal doors slid close.
    I pushed the button to the second floor, feeling the smooth and chilly metal spread along my finger.
    I took a step back where Toma stood and watched the numbers slowly decrease.
    c "...Oh Toma, I have a question."
    c "Do you know about anything with regards to the new third floor resident? {w} They just entered the hospital early this morning."
    t "Oh... {w=7.0} That."
    Toma stared at the slowly changing numbers, not glancing over to me as a suspenseful silence filled the confined space.
    It seemed to me as if... {w=2.0} Toma was thinking intensely about something.
    t "... {w=4.0} It was a wreck."
    c "Oh, so it was just another accident victim?"
    t "Not exactly."
    t "The person lost something valuable to them, and needs to be supervised. {w=1.0} It is, after all, the reason they are a third floor resident."
    c "Oh, I see..."
    The suspenseful silence filled the small space once again as I returned my attention to the slow elevator numbers, slightly unsatisfied.
    Meadow and Toma's stories match, which is a good thing, but it doesn't really give me all the answers I wanted.
    Why was there such a commotion when it happened?
    What did they lose?
    Why doesn't Meadow want me to meet with this new resident?
    Nothing makes sense...
    With a sweet chime, the elevator doors opened, allowing the two of us to step out.

    jump c01_cafeteria

label c01_nowhere:

    c "I don't have anywhere particular in mind. {w=1.0} I just want to walk around and stretch my legs."
    t "Huh? Seriously? {w=1.0} That's kind of boring, isn't it?"
    I giggled a little as I threw my arms up into the air.
    c "But it has been a while since I've walked around! {w=1.0} And the two of us can chat while walking!"
    Toma raised an eyebrow at my explanation, a mischievous look in his eyes as his lips curled up into a smile.
    t "Oh~? {w=2.0} You missed talking with me did you?"
    c "Hehe, I know you certainly have!"
    Toma threw his head back as he laughed, knowing the truth behind my words.
    t "You got that right. {w=1.0} It's boring working hour after hour with no one to talk to, except for a strict man occasionally.
    I giggled at Toma's words, and the two of us began to walk.
    With no specific location, we were able to go freely as we pleased. Nothing chaining us down.
    The feeling of freedom, one that only residents of the third floor in the west wing could have, is simply amazing.
    Of course, almost every other resident was given more freedom than I was. {w=1.0} I could only walk around like this if I was being supervised by someone eligible.
    t "Hey, you're 14 now, right?"
    I gasped softly in surprise as I smiled pleasingly at Toma.
    c "You remembered my birthday!"
    Toma scoffed, as if offended.
    t "Hey, come on now! You gotta give me more credit than that! {w=2.0} The two of us always celebrate your birthday! So of course I would remember."
    I covered my mouth with the back of my right hand, suppressing my laughter at Toma's reaction.
    c "You're right, I apologize."
    Toma and I have been friends for four years now, going all the way back to when I was 9 1/2 and when he was 12.
    As a way of making me happy, Toma had dragged me around the whole hospital on my tenth birthday, buying me flan for the first time.
    The two of us had never tried it back then, and started to grow a burning passion for its sweet flavor and silky smooth texture.
    t "Man, you're a little lady now. {w=2.0} And I mean that literally."
    Toma placed a hand on top of my head and his other hand on top of his own head, as if measuring the distance between us.
    I giggled, swatting away his hand from my head.
    c "I think being five feet is reasonably tall for my body type and figure!"
    t "Haha, no it's not! {w=1.0} You should at least be five three by now!"
    I blinked in surprise at Toma’s information.
    c "Really? Well then what about you? {w=1.0} You're five eight right now, so shouldn't you be six feet?"
    Toma stiffened at my words for a split second before laughing nervously.
    t "It's different for guys."
    c "Huh?"
    t "Well you see, it's all about -"
    who "Out of the way, kids!"
    Interrupting Toma, a loud raspy voice cried out to us as the sound of wheels gradually got louder.
    I looked ahead, where a couple of elderly men and women began to rush towards us in wheelchairs, their faces set in concentration.
    I squeaked in surprise as Toma dragged me to the side along with himself, mere seconds before the leading elderly woman ran me over.
    I blinked in surprise as the wind from the wheelchairs blew over Toma and I, causing our clothes to sway in the same direction.
    t "Hey! {w=1.0} I thought the nurses told you all not to do any more wheelchair races!"
    An elderly man, who was in the back of the group of racing elders, turned his wheelchair around to face us while the others laughed and argued.
    elderly_a "Wahahaha! {w=1.0} You youngsters think you can order us around?! My, has the youth fallen."
    t "Heh heh, well the nurses and us helpers are taking care of you, you know? {w=1.0} If you can't realise that, then is it the wise who have fallen."
    elderly_a "Quite the sassy little thing as always, eh Toma?"
    t "Heh, you better believe it old man."
    This caught the rest of the elders attention, causing an elderly woman near the back of the group to turn and face as like the elderly man.
    elderly_b "So rude to your elders! {w=1.0} We know that you are trying to impress your little girlfriend by acting tough, but please do so with a little more manners!"
    t "H-Huh?! {w=4.0} G-Girlfriend?! W-What gave you that idea?!"
    The elders began to laugh, their raspy voices cackling.
    I looked over to Toma, whose face was burning bright red with embarrassment. 
    I smiled at little at Toma's expression, finding it confusing that he was acting strangely.
    t "Y-You got the wrong idea! {w=4.0} Celia and I... W-We aren't...!"
    c "What are you talking about Toma? I am your girl friend, aren't I?"
    t "HUH?!"
    Toma jumped at my words, the tips of his ears turning as red as a cherry.
    For some reason, the elders \"ooh\"ed and \"ahh\"ed at the scene before them, some of the elderly woman giggling like children.
    c "Well, I am a girl and your friend, correct? {w=1.0} So, I'm your girl friend!"
    Toma's red face turned pale in seconds, as his once gaping mouth closed shut.
    t "Ah, that's right. {w=1.0} That's very true."
    The elders began to laugh once again, those who didn't need a wheelchair standing up and patting Toma on the back.
    I smiled warmly at the scene, finding it comforting but very confusing as well.
    elderly_a "Well, how about another round gang?"
    The elderly cheered in delight, wobbling over to their wheelchairs in delight.
    I smiled brightly at the sight, turning to Toma and tugged on one of his white sleeves.
    c "Hey Toma, can I race with them too? I want to go wheelchair racing!"
    t "Huh? {w=3.0} Oh, uh, sorry Celia but you can't."
    c "Aw, why not?"
    t "Well, you're just so slow they'll beat you before you even start pushing the wheels!"
    c "Huh?! That's not very nice!"
    t "Hahah! {w=1.0} Hey, don't look so mad!"
    t "They most likely don't have any extra wheelchairs with them. {w=1.0} Maybe next time, okay?"
    c "Hmm... Alright."
    I waved goodbye to the elderly as Toma and I began to continue walk around.
    [Transition]
    Toma and I walked across the wing, entering the third floor of the main building.
    The third floor was used as some sort of relaxation center, where a majority of hospital residents and their visitors hung out in.
    Despite the rather large number around, the area was quiet and had a relaxing atmosphere.
    Toma and I stopped walking for a bit, examining the area. 
    People of different ages were sitting down, all chatting happily about whatever they wanted.
    I smiled at the sight of a little girl, talking happily with her mother and father.
    Despite the little girl's mother's wearing a hospital gown, the family looked so happy together.
    As I continued to look around the room, I noticed a young man wearing bandages on his head, smiling sheepishly as he spoke to an older woman. {w=1.0} Most likely his mother.
    I began to remember about the commotion from this morning, the new resident of the third floor...
    I never found out who they were or how they ended up there.
    Sure, Meadow told me some information, but it doesn’t really answer the many questions I had in my head.
    I turned my attention to the nurses' station in the left corner, where nurses were smiling gently at the sight of all the happy patients.
    I smiled at them as a few noticed me, and began to walk over to them.
    The head nurse of the station, a friendly woman with long black hair tied into a bun, noticed me walking towards her and gave a warm smile.
    c "Good afternoon!"
    nurse "Well, good afternoon. {w=1.0} It's rare to see you two together!"
    I looked over my shoulder and saw Toma standing right next to me, his hands tied behind his head. 
    Without even noticing, he had followed me to the nurses station.
    It was only natural, seeing as how he could never leave me by myself. {w=5.0} But for some reason, I felt a little upset about it.
    t "Well, today's special."
    nurse "Oh?"
    t "It's Celia's birthday today! {w=1.0} I thought it'd be nice to celebrate by having lunch together."
    I looked at Toma in surprise.
    We’re going to eat lunch together? {w=2.0} That means we get to eat flan today~!
    The nurse began to giggle in a mischievous way, the other nurses in the station smiling brightly at us.
    nurse "My, how kind of you Toma~!"
    t "H-Hey! {w=2.0} What's with that look you're giving me?"
    The nurse didn't reply, as she and the others began to giggle.
    Toma sighed while scratching his head in nervousness.
    t "Come on, first the old folks now you guys? {w=4.0} Seriously, it's not like that..."
    I looked over to Toma in confusion, our eyes locking which caused him to flinch.
    Toma looked away as his face reddened slightly, causing the nurses giggling to arise.
    nurse "Anyway, what can we help you with?"
    c "Oh, right!"
    c "There was some sort of commotion earlier this morning, down in the emergency rooms. {w=1.0} Meadow had told me that the third floor received a new resident."
    c "And, well, I was wondering what happened to them."
    The nurses fell silent, their once smiling faces transforming into ones that showed discomfort.
    I waited patiently for an answer, watching the nurses exchange nervous glances with one another.
    t "... {w=5.0} A wreck."
    I turned my attention to Toma, who had returned to normal, his eyes closed as if he was recalling something.
    c "A wreck?"
    Toma nodded, opening his eyes and instantly locked with the nurses in front of him.
    I looked over to the nurse’s, just in time to see them begin to nod - agreeing with Toma's claim.
    c "Oh, so it was just another accident victim?"
    t "Not exactly."
    t "The person lost something valuable to them, and needs to be supervised. {w=2.0} It is, after all, the reason they are a third floor resident."
    c "Oh, I see..."
    I looked down at my feet and wiggled my bare toes.
    Meadow and Toma’s stories match, which is a good thing, but it still doesn’t really give me all the answers I wanted.
    Why was there such a commotion when it happened?
    Why doesn’t Meadow want me to meet with this new resident?
    Nothing makes sense...
    And what did they lose?
    A body part? {w=0.5} Something of a momento? {w=1.0} Or maybe... Someone important to them...
    My heart instantly went out to them at the mere thought of losing someone, the familiar feeling of loneliness dwelling inside me.
    c "How awful... {w=6.0} I wish I could have helped them out in some way."
    t "It's not your fault for their loss, Celia. {w=2.0} There was nothing anyone could have done."
    My body tensed at Toma curt words.
    There was truth in what he said, but I couldn't help but think otherwise.
    Couldn't there have been something, {i}anything{/i} that someone could have done? {w=4.0} Anything at all?
    Humans have the ability to choose what fate they want to have, and my mother was proof of that in the beginning.
    The fact that there was nothing someone could have done to save the accident victim... {w=5.0} It hurts me.
    After another ten minutes or so, Toma's stomach began to growl.
    With the fun air from earlier now back, the two of us said goodbye to the nurses and made our way to the second floor of the main hospital where the cafeteria awaited us.

    jump c01_cafeteria

label c01_room:

    Hmm... I really shouldn't disobey Meadow... I would probably be a nuisance for the people downstairs as well.
    And besides, knowing Meadow, she'd tell me at least the basic story of what happened.
    Nodding with determination, I returned my attention to my food and continued to eat.
    [Transition]
    The time is now 8:30, and Meadow still hadn't returned. {w=3.0} Something terrible really must have happened.
    I hope not too many people were hurt...
    Thankfully, the cries of panicked voices died down half an hour ago. {w=2.0} Everything must have gotten settled around then.
    n "Nyu! Nyu nyui, nyu nyu, nyui!"
    Nyu puffed out her cheeks in frustration as she weakly but indignantly stomped her little paw on the bed.
    Nyu and I decided to play a game of charades while we waited for time to pass by.
    Nyu naturally isn't very good at the game. {w=2.0} She can only do so much without a real pair of hands, so it is rather easy to tell what she is trying to say.
    c "Hehe, having trouble figuring out what to do next?"
    n "Nyuuu...!"
    I couldn't help but giggle at Nyu's frustrated response; I see that she is trying to act stubborn.
    As Nyu continued to ponder about what she should do, the door opened, catching my attention.
    c "Meadow!"
    m "Heh, I'm back! {w=1.0} Did you miss me?"
    I giggled at Meadows words as she walked towards me. Her normal bright smile plastered on her face.
    I turned as much of my body as I could toward her, slowly gathering courage to ask her about the commotion from earlier.
    c "So, Meadow... {w=4.0} I'm sorry, but I have been curious about it. What happened downstairs on the first floor? Was it just another accident victim?"
    Meadow's eyes widened slightly as she stared at me in silence.
    She looked at me as if she had no knowledge of what I was speaking about.
    Meadow closed her eyes, deep in thought.
    m "... {w=2.0} No, it wasn't."
    I blinked twice in slight confusion by Meadow's frank answer.
    c "Well... If it wasn't an accident victim, what happened?"
    m "... {w=4.0} Let's just say that it's a {b}rare{/b} case."
    \"A rare case..?\" {w=1.0} Even though I could tell that there was some hesitation in Meadow's words, I could hear the pure sincerity behind her explanation.
    ...However, I had a feeling that this was the best Meadow was willing to share with me at the moment.
    m "Anyway, because it is a rare case... {w=1.0} The victim will be staying up here on the third floor. He was hurt pretty badly, and so we will need to be monitored daily."
    c "Oh, I see..."
    I couldn't help but pity the poor soul.
    The third floor of the hospital was where the people who were greatly injured or couldn't take care of themselves had to stay. {w=1.0} Almost all of the residents on this floor are above the age of 55.
    c "Oh! I have an idea!"
    Meadow blinked in surprise at my sudden announcement.
    m "Hmm?"
    c "May I please welcome the new resident? {w} After being in such a horrible accident, they must be very scared and possibly even lonely-{nw}"
    m "Absolutely not."
    I flinched in surprise at Meadow's quick response, thrown off completely by her sudden serious expression.
    m "Miss Celia, I would prefer it if you did not go any where near the new resident."
    c "Eh...?"
    m "Do not go near any strangers you might see."
    I stare at Meadow in confusion and slight nervousness, my hands trembling slightly.
    c "...A-Alright..."
    Meadow smiled her usual smile.
    m "Good."
    Despite Meadow's new carefree smile, I couldn't help but sense a more serious and slightly terrifying atmosphere emitting from her.
    I don't even know what the new resident looks like, and Meadow is telling me not go anywhere near them.
    ...
    I can't help but become more and more curious about this new resident...
    [Transition]
    It is now 11:30 in the morning, half an hour before lunch time.
    Nyu and I had moved on to drawing portraits of each other. {w=1.0} And of course, she isn't very good at that either.
    c "And... {w=2.0} Done!"
    I giggled happily as I reveal the picture I had drawn of her.
    c "Well? What do you think?"
    n "Nyu..."
    Nyu shook her head in disapproval at my hard work, causing me to giggle nervously.
    c "Oh come on, it isn't that bad..."
    Nyu puffed out her cheeks, placing her stubby paws on her hips.
     It looks like she isn't going to change her opinion.
    I puffed out my own cheeks as I turn the paper back towards me to gaze at the picture.
    c "Well I think it looks good enough..."
    As I stared at my picture of Nyu, a sudden knock on the door caught my attention.
    c "Ah, come in!"
    The door opened and closed softly.
    who "Yo! Good morning, Celia."
    c "Oh, Toma! Good morning to you."
    n "Nyu!"
    Surprised by Toma's greeting, Nyu ears enlarged and she flew towards Toma's face, ramming into him.
    t "Whoa there, Nyu! Not the face!"
    I laughed a little as I watch Toma attempt to remove Nyu, who was tightly gripping his face.
    The struggle continued for a few minutes before Toma successfully removed Nyu from his face.
    t "Whew... Does Nyu have an interest in faces or something?"
    c "Hehe, that is probably the only way she knows how to greet people."
    t "I hope so, or else Nyu and I will be having a little bit of trouble getting along."
    I giggled at Toma's humorous behavior as Toma walked toward me, dropping Nyu on my lap.
    c "So Toma, what brings you here?"
    Toma smiled as he stuffed his hands into his lab coat pockets.
    t "Just wanted to see if you wanted to walk around and stretch your legs today."
    I gasped in pleasent surprise, clapping my hands together.
    c "Oh, that sounds nice! {w=1.0} I haven't gotten out of bed in a while."
    t "Cool! I'll put your device on mobile mode then."
    My \"device\"... {w} A strange name that Toma and I call my IV stand.
    I couldn't help but pout slightly at the word as I slid my legs off of the bed.
    Even if I needed to go to some place close by, I had to bring my IV bag everywhere with me. {w=1.0} I didn't mind it at first...
    I couldn't do a lot of things because of the bag weighing me down. {w=2.0} If I held it in one arm, it was too painful for me, the needle would move barely an inch and scrape my vein.
    But after meeting Toma, the needle that is usually hooked to the IV bag itself can now detach and hook up to a small vial that I can hold in one hand without hurting myself.
    But because of how small the vial is, my time out of my room is very limited.
    
    The moment I stepped out of my room, I stretched my arms as far as I could, a hum of delight escaping me.
    I giggled as Toma closed the door, his back facing me, and ran to the room across from me.
    t "Hey, Celia! {w=1.0} No running in a hospital, remember?"
    I took a sharp turn to the right, running towards Toma with a happy and carefree smile.
    c "Hehe, I'm sorry! I couldn't help myself."
    t "Well, obviously."
    I let out a short laugh at Toma's words, feeling a different presence behind them.
    c "It's such a nice day today! The hallway is rather warm, thanks to the sunlight! {w=1.0} Such a shame we can't go outside to the garden."
    Toma smiled sadly at me while rubbing the back of his head.
    t "You know the rules, Celia."
    Ever since my incident four years ago, I haven't had permission to step outside of the hospital. {w=2.0} Not that I was able to go very far back then, either...
    But the small things most people see in the outside world is what I miss the most. {w=1.0} Not being able to experience the time of the seasons can really put a damper on your mood.
    The things like the nice gentle breeze during the spring, the steaming hot sunlight dancing on your skin in the summer, the splendid sight of pure white snow nestled on the ground during winter, or the lovely colors of the leaves during autumn...
    I even miss the gentle concertos of the rain, elegantly playing music with what it touches and splashing cool water on any nearby human.
    I had truly enjoyed the simple things like that when I was younger.
    For me... {w=4.0} It proved that I was truly alive, living in this world and experiencing the continuously progressing time.
    I suppose the nice part about staying in the hospital everyday is that I get to stay nice and dry though.
    t "So Celia, what do you want to do? {w=1.0} Do you have anywhere in particular you want to go?"
    I blinked in surprise at Toma’s sudden question, not expecting him to ask so suddenly.
    c "Um, well..."

    menu:
        "The library":
            jump c01_library

        "The Cafeteria":
            $direct_cafeteria += 1

            c "Let's go to the cafeteria!"
            Toma let’s out a soft chuckle, most likely expecting me to say something that.
            t "Sounds good. {w=1.0} It's almost lunchtime anyway."
            I cheer happily at Toma’s acceptance and pulled his right hand.
            c "Hey, Toma! Let's go and have some flan today!"
            t "Do you even have to ask?!"
            Toma and I began to walk down the hallway as I tug at his arm happily like a child, happily talking with enthusiasm about the flan that the two of us had grown to love.
            The cafeteria was in the main hospital building on the second floor, which meant that we had to take one of the long narrow hallways.
            Those hallways, leading to either the main building or the west wing where those like myself who cannot escape fate stay, are the most beautiful.
            Windows that reached the ceiling, making everything in the outside visible, could take your breath away.
            The hospital courtyard just so happened to be right below those hallways, letting the people walking down the hallway see the tall dark green trees, marbled architecture like the fountain of Ion, and bright beautiful flowers.
            Visitors often stopped in the middle of the hallway, taking in the beautiful view.
            
            jump c01_cafeteria

        "Nowhere in particular":
            $direct_cafeteria += 1
            jump c01_nowhere

