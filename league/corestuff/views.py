import random
from django.http import JsonResponse
from django.shortcuts import render

from .data.why_did_i_lose import (
    CAUSES,
    KEY_EVENTS,
    MENTAL_DAMAGE,
    RIOT_EXPLANATIONS,
    RARE_OUTPUTS,
)


def home(request):
    return render(request, "corestuff/home.html")


def why_did_i_lose_page(request):
    return render(request, "corestuff/why_did_i_lose.html")


def why_did_i_lose_api(request):
    data = {
        "cause": random.choice(CAUSES),
        "key_event": random.choice(KEY_EVENTS),
        "mental_damage": random.choice(MENTAL_DAMAGE),
        "riot_explanation": random.choice(RIOT_EXPLANATIONS),
        "rare": random.choice(RARE_OUTPUTS) if random.random() < 0.03 else None,
    }
    return JsonResponse(data)






# Tilt Meter Page
def tilt_meter_page(request):
    return render(request, 'corestuff/tilt_meter.html')



import random
from django.http import JsonResponse
from django.shortcuts import render

def tilt_meter_api(request):
    levels = [
        "Calm 😐 (lying to yourself)",
        "Mildly Annoyed 😏 (maybe a tiny scream in the shower)",
        "Tilted 🤬 (keyboard might die tonight)",
        "Raging 🔥 (your soul leaves your body temporarily)",
        "Apocalyptic 💀🔥 (summoning the gods of frustration)",
        "Absolute Chaos 🩸💀 (uninstall.exe initiated)",
        "Void of Sanity 🕳️ (you question your existence)",
    ]

    memes = [
        "go to the dark side, CHOOSE TEEMO NEXT GAME 😈",
        "Your top laner died 12 times before 10 minutes",
        "The jungler said 'I’ll gank mid' and didn’t",
        "Enemy Yasuo crits more than your heart can handle",
        "Your support stole your healing minions… intentionally",
        "Riot buffed Teemo again just to hurt you",
        "Your team refuses to surrender because 'we can still win' (you can’t)",
        "You miss one skillshot and the universe laughs",
        "Your mouse might explode 💥",
        "You start whispering to minions 🫣",
        "The League servers personally mock you 💻 (she sacodavo)",
    ]
    
    emojis = ["🤯","💀","🔥","🩸","🥵","😈","🕳️"]

    calm_rares = [
        "You feel eerily calm… like the eye of the storm 🌪️",
        "The universe says: 'Breathe, young summoner' 🧘",
        "For a moment, peace. Then chaos resumes…",
    ]

    legendary_rares = [
        "You realize it’s YOUR fault… yet you still blame the jungle 😤",
        "Your mouse broke mid-laning phase and you still can’t blame Teemo 💀",
        "The Tilt Gods have personally judged you ⚡🩸",
        "You hit 9000 tilt and the League client whispers 'try again'… forever"
    ]

    tilt_calm = [
        "Breathe in… Breathe out… The tilt subsides… for now.",
        "A moment of clarity amidst the chaos of Summoner's Rift.",
        "at this point you might actually understand that league is not for you.",
    ]

    blame_targets = [
        "The Jungler (obviously)", "The 0/10 Yasuo Power Spike", "Riot's Spaghetti Code", 
        "Lag (even though ping is 20ms)", "Main Character Syndrome ADCs", "Packet Loss",
        "The Support who 'secured' the kill", "Your own keyboard's layout"
    ]
        
    prescriptions = [
        "Go outside and touch actual grass.", "Drink a glass of water and stare at a wall.",
        "Uninstall for 24 hours.", "Play a game where you can't lose, like Stardew Valley.",
        "Apologize to your mouse for the clicking.", "Queue up again immediately (Bad idea).",
        "Take a deep breath, think about your future, then queue again.",
        "Never play this game ever again (recommended). :)"
    ]

    # Randomly pick tilt level + meme + emoji
    level = random.choice(levels)
    perscription = random.choice(prescriptions)
    blame = random.choice(blame_targets)
    meme = random.choice(memes)
    emoji = random.choice(emojis)
    tilt_score = random.randint(100, 9000)

    # Rank Outlook logic
    if tilt_score > 7000: outlook = "Demoted to Iron IV"
    elif tilt_score > 4000: outlook = "Hardstuck Emerald"
    else: outlook = "Potential Pro Player"

    # Determine rare text
    rare_text = ""
    roll = random.random()
    if roll < 0.01:  # 1% chance legendary
        rare_text = random.choice(legendary_rares)
    elif roll < 0.03:  # 2% chance calm rare
        rare_text = random.choice(calm_rares)
        tilt_score = random.randint(-10, 10)
        level = random.choice(tilt_calm)

    return JsonResponse({
        "level": level,
        "meme": meme,
        "emoji": emoji,
        "tilt_score": tilt_score,
        "rare": rare_text,
        "perscription": perscription,
        "blame": blame,
        "outlook": outlook
    })

def chat_translator_api(request):
    user_text = request.GET.get('text', '').lower()
    
    database = {
        "jungler": [
            "MY JUNGLER IS PLAYING WITH A STEERING WHEEL. I'M CONVINCED.",
            "JUNGLE GAP SO BIG IT HAS ITS OWN POSTAL CODE. GG.",
            "DID YOU DOWNLOAD THE GAME JUST TO WATCH THE BUFFS SPAWN?",
            "I'D FLAME YOU BUT BURNING TRASH IS BAD FOR THE ENVIRONMENT.",
            "REPORT JG FOR ASSISTING ENEMY TEAM BY EXISTING.",
            "BRO IS FARMING GROMP WHILE THE NEXUS IS EXPLODING. PEAK CINEMA.",
            "IS YOUR MINIMAP DLC? DO I NEED TO PAY FOR YOU TO SEE THE GANK?",
            "YOU HAVE THE MAP AWARENESS OF A FOLDING CHAIR.",
            "I'VE SEEN BETTER PATHING IN A ROOMBA WITH A DEAD BATTERY.",
            "PLEASE VISIT THE NEAREST PRACTICE TOOL AND NEVER LEAVE."
        ],
        "support": [
            "MY SUPPORT IS A SECRET AGENT FOR THE ENEMY TEAM. 100%.",
            "NICE LUX SUPPORT. 0 WARDS, 0 IMPACT, 100% EGO. UNINSTALL.",
            "WHY ARE YOU STANDING BEHIND ME? ARE YOU MY BACKPACK?",
            "IF YOU MISS ONE MORE HOOK I AM TURNING INTO A GHOST AND RUNNING MID.",
            "PLEASE SELL YOUR SUPPORT ITEM AND BUY SOME BRAIN CELLS.",
            "0 WARDS AT 20 MINS. IS YOUR '4' KEY BROKEN OR JUST YOUR BRAIN?",
            "STOP STEALING THE WAVE YOU PARASITE. GO TO ANOTHER LANE.",
            "I'D CALL YOU DOG WATER BUT DOGS ARE ACTUALLY USEFUL.",
            "YOU ARE THE REASON I HAVE TRUST ISSUES IN REAL LIFE.",
            "GIVE ME A CANNON MINION, IT HAS MORE PRESENCE IN LANE THAN YOU."
        ],
        "adc": [
            "MY ADC HAS THE REACTION TIME OF A STATUE. LOG OFF.",
            "STOP FRONTLINING LIKE YOU'RE A TANK YOU ABSOLUTE POTATO.",
            "100 CS AT 30 MINS. ARE YOU CLICKING THE MINIONS OR JUST WAVING AT THEM?",
            "I'D RATHER HAVE A BOTS IN MY LANE. AT LEAST THEY KITE.",
            "YOU ARE THE MAIN CHARACTER OF A TRAGEDY. STOP DYING.",
            "IS YOUR RIGHT-CLICK BROKEN OR ARE YOU JUST COMMITTED TO THE FED?",
            "QUIT THE GAME. SAVE THE OXYGEN FOR SOMEONE WHO CAN KITE.",
            "YOU BOUGHT A KRAKEN SLAYER BUT YOU CAN'T EVEN SLAY A CRAB.",
            "OUR ADC IS LITERALLY A GOLD DELIVERY SERVICE. FAST AND RELIABLE.",
            "I'D FLAME YOUR MECHANICS BUT YOU DON'T HAVE ANY."
        ],
        "mid": [
            "MID GAP IS LITERALLY APOCALYPTIC. THE WORLD IS ENDING.",
            "STOP ROAMING. EVERY TIME YOU LEAVE, THE ENEMY GETS A TRIPLE KILL.",
            "YOU'RE GETTING SOLO KILLED BY A YASUO WHO IS 0/10. HOW??",
            "MID IS JUST A HIGHWAY FOR THE ENEMY TEAM AT THIS POINT.",
            "I'VE SEEN AI INTERMEDIATE BOTS WITH MORE LANE PRESSURE.",
            "PLEASE STOP 'LIMIT TESTING'. WE ALL KNOW YOUR LIMIT IS IRON 4.",
            "YOUR KDA LOOKS LIKE A PHONE NUMBER. STOP CALLING THE ENEMY.",
            "YOU'RE MISSING SO MANY SKILLSHOTS YOU'RE ACCIDENTALLY AIMING AT ME.",
            "IS YOUR KEYBOARD MISSING THE 'R' KEY OR ARE YOU JUST SAVING IT FOR NEXT GAME?",
            "I WOULD ASK YOU TO HELP BUT YOU'D PROBABLY JUST ACCIDENTALLY FEED."
        ],
        "top": [
            "TOP IS A 1v1 AND YOU ARE CURRENTLY LOSING TO THE TURRET.",
            "NICE TELEPORT. YOU REALLY HELPED THAT MINION DIE FASTER.",
            "STOP PUSHING WITHOUT WARDS. YOU ARE A BUFFET FOR THEIR JUNGLER.",
            "OUR TOP LANER IS PLAYING SINGLE-PLAYER LEAGUE WHILE WE LOSE.",
            "I FORGOT WE HAD A TOP LANE UNTIL I SAW THE ENEMY WAS 10/0.",
            "ARE YOU PLAYING ON A TOUCHPAD? THAT WOULD EXPLAIN THE TILT.",
            "PLEASE TYPE 'FF' SO WE CAN ALL GO HOME AND CRY.",
            "YOU'RE BUILDING TANK BUT DYING FASTER THAN THE CASTER MINIONS.",
            "I'D SAY YOU'RE THROWING BUT YOU HAVE TO BE IN THE GAME TO THROW.",
            "GO BACK TO CO-OP VS AI. EVEN THE BOTS ARE WORRIED ABOUT YOU."
        ],
        "generic_rage": [
            "I AM NOT TOXIC. I AM A TRUTH-TELLER IN A WORLD OF GRIEFERS.",
            "MY TEAMS ARE THE REASON RIOT ADDED THE 'MUTE ALL' BUTTON.",
            "I'M RUNNING IT DOWN. NOT BECAUSE I'M MAD, BUT BECAUSE YOU DESERVE IT.",
            "IS THIS A SOCIAL EXPERIMENT? AM I BEING PRANKED BY 4 BOTS?",
            "I WOULD UNINSTALL BUT I WANT TO SEE HOW MUCH WORSE THIS GETS.",
            "MY MENTAL IS GONE. IT LEFT THE ROOM. IT'S IN ANOTHER ZIP CODE.",
            "I'M NOT EVEN MAD ANYMORE. I'M JUST IMPRESSED BY YOUR INCOMPETENCE.",
            "THIS GAME IS A PSYOP DESIGNED TO DESTROY MY WILL TO LIVE.",
            "IF I HAD A NICKEL FOR EVERY BRAIN CELL IN THIS LOBBY, I'D HAVE ZERO CENTS.",
            "I'M GOING TO BECOME A VILLAIN AFTER THIS MATCH. THANKS TEAM.",
            "YOU GUYS ARE THE REASON TEEMO WAS CREATED. TO PUNISH US ALL.",
            "I'VE HAD MORE FUN AT THE DENTIST THAN IN THIS 20 MINUTE VOMIT-FEST.",
            "IS YOUR MONITOR ON OR ARE YOU JUST LISTENING TO THE AUDIO?",
            "PLEASE LOOK UP 'HOW TO PLAY LEAGUE' ON YOUTUBE. START WITH THE BASICS.",
            "THIS ISN'T A GAME. IT'S A 40-MINUTE HOSTAGE SITUATION.",
            "I'M NOT AFK. I'M JUST CELEBRATING YOUR FAILURE FROM THE FOUNTAIN.",
            "EVERY TIME YOU PING ME, AN ANGEL LOSES ITS WINGS AND I LOSE MY SANITY.",
            "I'D ASK YOU TO FF BUT I KNOW YOU LOVE SUFFERING AS MUCH AS YOU LOVE FEEDING.",
            "I'M REPORTING MYSELF FOR PLAYING WITH YOU PEOPLE.",
            "LITERALLY MENTAL BOOM. REEEEEEEEEEEEEEE.",
            # ... (I will fill the rest with unhinged dark humor) ...
            "YOUR GAMEPLAY IS A STAIN ON THE HISTORY OF ESPORTS.",
            "I'VE SEEN BRONZE PLAYERS WITH MORE DIGNITY THAN THIS TEAM.",
            "STOP TYPING AND START CLICKING. THOUGH CLICKING CLEARLY ISN'T YOUR FORTE.",
            "I'D RATHER EAT A DENIM JACKET THAN PLAY ANOTHER MINUTE WITH YOU.",
            "IS YOUR HOUSE ON FIRE? BECAUSE THAT'S THE ONLY EXCUSE FOR THIS PLAY.",
            "YOU'RE NOT JUST BAD. YOU'RE ARTISTICALLY BAD. IT'S ALMOST BEAUTIFUL.",
            "I'M GOING TO PLAY STARDEW VALLEY AFTER THIS. I NEED TO FEEL PURE AGAIN.",
            "I HOPE YOUR INTERNET CUTS OUT. FOR YOUR OWN SAKE.",
            "YOU ARE THE REASON THE DODGE PENALTY WAS INVENTED.",
            "I'M TYPING THIS WITH MY TEARS. THEY TASTE LIKE LP LOSS.",
            "OUR CHANCES OF WINNING ARE LOWER THAN MY SELF-ESTEEM.",
            "GO PLAY TETRIS. YOU CAN'T FEED THE BLOCKS THERE.",
            "I'D SAY YOU'RE GIVING THE ENEMY A WIN, BUT YOU'RE GIVING THEM THE WHOLE SEASON.",
            "YOU'RE LIKE A MINION, BUT AT LEAST MINIONS GIVE GOLD WHEN THEY DIE... WAIT.",
            "I'M NOT ANGRY. I'M DISAPPOINTED. LIKE YOUR PARENTS PROBABLY ARE.",
            "IF FEEDING WAS AN OLYMPIC SPORT, YOU'D HAVE MORE GOLD THAN PHELPS.",
            "I'VE SEEN BETTER MICRO FROM A MICROWAVE.",
            "STOP PINGING THE JUNGLER. HE CAN'T GANK YOUR STUPIDITY.",
            "THIS MATCH IS GOING IN MY VILLAIN ORIGIN STORY.",
            "PLEASE CLICK THE RED 'X' IN THE CORNER. DO IT FOR THE COMMUNITY.",
            "I'M LITERALLY ASCENDING TO A NEW LEVEL OF RAGE. I CAN SEE THE MATRIX.",
            "YOU ARE THE FINAL BOSS OF THE IRON DIVISION.",
            "I'D FLAME YOUR MOM BUT SHE'S PROBABLY DISAPPOINTED ENOUGH.",
            "YOUR MACRO IS JUST WATCHING THE SCREEN UNTIL YOU DIE.",
            "IS THIS THE 'BRING YOUR TODDLER TO WORK' DAY FOR LEAGUE?",
            "I'M NOT SURRENDERING. I WANT YOU TO STAY IN THIS HELL WITH ME.",
            "YOU'RE PLAYING LIKE YOU'RE UNDERWATER. WITHOUT A DIVING SUIT.",
            "I'D OFFER ADVICE BUT YOU CLEARLY DON'T SPEAK 'WINNER'.",
            "EVERY TIME YOU DIE, A RIOT EMPLOYEE GETS A BONUS.",
            "YOU ARE THE REASON I HAVE A THERAPIST ON SPEED DIAL."
        ]
    }

    # Combined all for a true "100" feel
    all_generic = database["generic_rage"]
    
    # Logic to pick category
    selected_list = all_generic
    for key in database:
        if key in user_text:
            selected_list = database[key]
            break

    return JsonResponse({"toxic": random.choice(selected_list)})

def patch_notes_api(request):
    notes = [
        # --- CHAMPIONS ---
        "Yasuo: Removed wind wall (developers accidentally pressed delete).",
        "Teemo: Now banned in 98% of households.",
        "Yuumi: Deleted. No explanation provided. Everyone is happier.",
        "Master Yi: Pressing Q now automatically uninstalls the game for the enemy team.",
        "Vayne: Every time you tumble into 5 people, your PC volume increases by 10%.",
        "Lee Sin: Now actually blind. Your screen goes black when you pick him.",
        "Shaco: Every time you go invisible, a random person in the world unfollows you.",
        "Draven: Now requires a credit card swipe for every axe caught.",
        "Malphite: Now literally does nothing. Even when he does something.",
        "Garen: Spin duration increased to 40 minutes. He just doesn't stop.",
        "Blitzcrank: Hooks now target your own teammates if you miss an enemy.",
        "Ryze: Reworked for the 492nd time. He is now a support champion that heals with blue mana.",
        "Aurelion Sol: Now accurately sized. He takes up the entire map. You cannot see the grass.",
        "Karthus: Pressing R now also turns off your opponent's Wi-Fi router.",
        "Singed: Poison trail now smells like disappointment. It lingers for 3 business days.",
        "Tryndamere: Too angry to die, but now too angry to live. He just screams at the shopkeeper.",
        "Aphelios: To simplify him, he now has 45 weapons and requires a PhD to auto-attack.",
        "Seraphine: Hovering her now forces everyone in the lobby to listen to K-Pop for 20 minutes.",
        "Zoe: Getting hit by a bubble now forces your computer to sleep for 2 hours.",
        "Urgot: Grinding someone with R now actually deletes their champion from their account.",

        # --- GAMEPLAY & MECHANICS ---
        "Jungle camps now flame you in the chat if you miss Smite.",
        "Flash: Now has a 50% chance to blink you into the enemy fountain.",
        "Shopkeeper: Now refuses to sell you items if your KDA is below 0.5.",
        "Baron Nashor: Now wears a top hat; gains 500% sass.",
        "Surrender Vote: Now requires only 1 'Yes' vote if the Jungler is 0/5.",
        "Minions: Now have a 5% chance to dodge your last hits and laugh.",
        "Turrets: Now focus players who have 'TTV' in their name first.",
        "Fog of War: Now filled with actual monsters that eat your wards.",
        "Health Potions: Now taste like pennies and provide 0 healing if you're tilted.",
        "Teleport: Using it on a minion now kills the minion out of spite.",
        "Bounty System: If you are 0/10, the enemy team gets a reward just for looking at you.",
        "Oracle Lens: Now reveals your deepest, darkest secrets to the lobby.",
        "Cloud Soul: Now just gives you a minor panic attack whenever you move fast.",
        "Elder Dragon: Executing an enemy now sends a 'Git Gud' email to their parents.",
        "Honeyfruit: Now contains 200mg of caffeine. Your champion develops a twitch.",
        "Scuttle Crab: Now has 4,000 HP and talks back to the Jungler.",
        "Inhibitors: Now grow back faster if they sense you are losing hope.",
        "Pings: The '?' ping now costs 10 Blue Essence per use to curb toxicity.",
        "Level 18: Reaching this level now triggers a mandatory 'Touch Grass' pop-up.",

        # --- PLAYER PSYCHOLOGY & CLIENT ---
        "Ranked Queue: Now requires a blood sacrifice and a stable mental state.",
        "Promotion Series: Now specifically pairs you with players who 'just want to have fun'.",
        "Honor Level 0: Your champion's voice lines are replaced by your mother's voice expressing disappointment.",
        "Client: Loading screen now lasts until you acknowledge that it's your fault you're Hardstuck.",
        "Chat Filter: Replacing 'KYS' with 'Keep yourself safe' was too nice; it now replaces it with 'I am a fragile little cupcake'.",
        "Matchmaking: Now balances teams by shoe size and level of existential dread.",
        "LeaverBuster: Instead of a ban, you are forced to play 10 games of Support for an Iron IV ADC.",
        "Skin Shards: Now only drop Emotes of champions you don't own.",
        "Death Recap: Now just says 'You died because you're bad' in 45 different languages.",
        "Friend Requests: Automatically blocked if the sender plays Shaco.",
        "Victory Screen: Now followed by a 30-minute lecture on why you actually played poorly.",
        "Defeat Screen: Now lasts forever. You cannot exit the game. This is your life now.",
        "LP Loss: Now scales with how much you typed in All-Chat.",
        "Autofill: Now only fills you into the role you hate the most.",
        "Vanguard Anti-Cheat: Now scans your kitchen to make sure you're eating your vegetables.",
        "End of Game Chat: Now mandatory for 5 minutes. You cannot leave until everyone has said something mean.",
        "Ranked Rewards: Silver players now receive a 'participation' sticker and a bill for server costs.",
        "Loading Screen: Tips now include advice like 'Maybe try a different hobby' and 'The sun is outside'.",
        "Profile Background: Now defaults to the champion that has killed you the most this week.",

        # --- ABSURD & DARK ---
        "Nexus: Now has 1 HP but heals every time someone types 'report' in chat.",
        "Smite: Now only works if you type a 500-word apology to the monster first.",
        "Wards: Now scream when they are destroyed.",
        "Junglers: Now receive 0 XP from camps unless they visit a lane to say something encouraging.",
        "All-Chat: Now translates everything to 'I am currently crying' for the losing team.",
        "Champion Select: If no one picks a tank, the game automatically installs DOTA 2.",
        "In-game Music: Replaced by the sound of a middle-aged man sighing heavily.",
        "Ping Spikes: Now perfectly timed with every skillshot you attempt.",
        "Blue Buff: Now belongs to the Mid laner by law. Stealing it results in an immediate ban.",
        "Red Buff: Now burns the user for 10 true damage because life is pain.",
        "The Rift: Now tilted at a 45-degree angle. Good luck pathing.",
        "Keyboard Support: Your 'W' key is disabled if you are playing a kiting champion.",
        "Mouse Sensitivity: Now fluctuates based on your heart rate.",
        "Ranked Borders: Now get smaller and uglier the more you lose.",
        "Gold Income: You now lose 1 gold per second if you haven't moved in 3 seconds.",
        "Items: Buying 6 Tears of the Goddess now grants the 'True Loser' achievement.",
        "Voice Chat: Now only works if you are whispering sweet nothings to your teammates.",
        "Minion Dematerializer: Now works on teammates. Use wisely.",
        "Rift Herald: Now dances on your corpse for an extra 10 seconds.",
        "Hextech Chests: Now have a 90% chance to contain a picture of Phreak smiling.",
        "Mastery Emotes: Now cost $4.99 per flash.",
        "AFK Detection: Now triggers if you haven't blamed the jungler for 5 minutes.",
        "League Partner Program: Now requires you to legally change your name to 'Riot' something.",
        "Final Patch Note: The game is now perfect. Any remaining issues are purely your fault.",
    ]
    return JsonResponse({"note": random.choice(notes)})

def should_i_queue_api(request):
    decisions = [
        # --- THE "STOP" CATEGORY (RED) ---
        {"status": "STOP", "msg": "No. Sleep. This ends badly.", "color": "red", "lp": "-19", "sanity": "Deceased"},
        {"status": "DANGER", "msg": "Absolutely not. Your mental is on life support.", "color": "red", "lp": "-25", "sanity": "Non-Existent"},
        {"status": "DANGER", "msg": "Your ISP called. They are cutting your internet for your own good.", "color": "red", "lp": "0 (AFK)", "sanity": "Gone"},
        {"status": "TERMINAL", "msg": "If you click play, I am calling your emergency contact.", "color": "red", "lp": "-30", "sanity": "Extinct"},
        {"status": "STOP", "msg": "Even the bots are worried about you right now.", "color": "red", "lp": "-15", "sanity": "Hallucinating"},
        {"status": "DANGER", "msg": "You are 1 game away from a villain origin story. Go to bed.", "color": "red", "lp": "-22", "sanity": "Corrupted"},
        {"status": "STOP", "msg": "Your keyboard is literally begging for a break.", "color": "red", "lp": "-20", "sanity": "Shattered"},
        {"status": "ABORT", "msg": "Look at your eyes in the mirror. You look like a Shaco main. Stop.", "color": "red", "lp": "-18", "sanity": "Ghost-like"},
        {"status": "STOP", "msg": "The enemy team thanks you for the free LP you're about to give them.", "color": "red", "lp": "-24", "sanity": "Gift-wrapped"},
        {"status": "WARNING", "msg": "Your current tilt is visible from space. Log off.", "color": "red", "lp": "-21", "sanity": "Radioactive"},
        {"status": "DANGER", "msg": "Clicking 'Play' right now is legally considered self-sabotage.", "color": "red", "lp": "-26", "sanity": "Hazardous"},
        {"status": "STOP", "msg": "Go drink water. The 'League Water' doesn't count.", "color": "red", "lp": "-19", "sanity": "Dehydrated"},
        {"status": "TERMINAL", "msg": "You aren't 'limit testing,' you are mental testing. And you failed.", "color": "red", "lp": "-28", "sanity": "0%"},
        {"status": "STOP", "msg": "Your teammates are already pre-emptively reporting you.", "color": "red", "lp": "-20", "sanity": "Blacklisted"},
        {"status": "DANGER", "msg": "Vanguard is trying to close your client to save your dignity.", "color": "red", "lp": "-22", "sanity": "Failing"},

        # --- THE "CAUTION" CATEGORY (YELLOW) ---
        {"status": "CAUTION", "msg": "Yes, but mute all instantly.", "color": "yellow", "lp": "+15 (Miracle)", "sanity": "Fragile"},
        {"status": "CAUTION", "msg": "Only if you play Yuumi and eat a sandwich simultaneously.", "color": "yellow", "lp": "+10", "sanity": "Vibing"},
        {"status": "RISKY", "msg": "The coins are in the air. Could be a win, will probably be a breakdown.", "color": "yellow", "lp": "-5", "sanity": "Shaky"},
        {"status": "CAUTION", "msg": "Play one more, but only if you promise not to type a single word.", "color": "yellow", "lp": "+12", "sanity": "Suppressed"},
        {"status": "RISKY", "msg": "Your luck is at 2%. Do you feel like a gambler?", "color": "yellow", "lp": "+20", "sanity": "Desperate"},
        {"status": "CAUTION", "msg": "One more. But if you die first blood, you have to uninstall.", "color": "yellow", "lp": "-15", "sanity": "On Edge"},
        {"status": "WARNING", "msg": "You're playing like a bot. At least a bot doesn't tilt.", "color": "yellow", "lp": "-10", "sanity": "Mechanical"},
        {"status": "CAUTION", "msg": "The LP gods are undecided. Proceed with extreme salt.", "color": "yellow", "lp": "+2", "sanity": "Neutral"},
        {"status": "RISKY", "msg": "You're chasing the 'one win' high. It’s a trap.", "color": "yellow", "lp": "-18", "sanity": "Addicted"},
        {"status": "CAUTION", "msg": "Yes, but if the jungler breathes wrong, you must ignore it.", "color": "yellow", "lp": "+14", "sanity": "Meditating"},
        {"status": "WARNING", "msg": "Your MMR is screaming. One more might kill it.", "color": "yellow", "lp": "-12", "sanity": "Critical"},
        {"status": "RISKY", "msg": "It's 3 AM. Nothing good happens on the Rift at 3 AM.", "color": "yellow", "lp": "-25", "sanity": "Sleepy"},
        {"status": "CAUTION", "msg": "Queue up, but expect your teammates to be actual raccoons.", "color": "yellow", "lp": "+5", "sanity": "Low"},
        {"status": "WARNING", "msg": "You are one '?' ping away from a permanent ban.", "color": "yellow", "lp": "-20", "sanity": "Combustible"},
        {"status": "RISKY", "msg": "Win this and you're a hero. Lose this and you're a meme.", "color": "yellow", "lp": "+25", "sanity": "Heroic?"},

        # --- THE "GO" CATEGORY (GREEN) ---
        {"status": "GO", "msg": "Yes. Redemption arc begins. (It won't.)", "color": "green", "lp": "-17", "sanity": "Stable (For 5 mins)"},
        {"status": "GO", "msg": "The enemy team looks even worse than you. Go get 'em.", "color": "green", "lp": "+18", "sanity": "Confident"},
        {"status": "SEND IT", "msg": "Full tilt or full glory. No in-between.", "color": "green", "lp": "+22", "sanity": "Manic"},
        {"status": "GO", "msg": "You're too deep in the hole to stop now. Dig faster.", "color": "green", "lp": "-10", "sanity": "Numb"},
        {"status": "GO", "msg": "Your mechanics are trash, but your spirit is... also trash. Go anyway.", "color": "green", "lp": "+15", "sanity": "Berserk"},
        {"status": "GO", "msg": "The LP isn't going to lose itself. Get back in there.", "color": "green", "lp": "-20", "sanity": "Committed"},
        {"status": "SEND IT", "msg": "Pick something weird. If you're going down, make it interesting.", "color": "green", "lp": "-30", "sanity": "Creative"},
        {"status": "GO", "msg": "You're due for a carry. Statistically. Maybe.", "color": "green", "lp": "+19", "sanity": "Hopeful"},
        {"status": "GO", "msg": "Your boss/teacher won't mind if you're a zombie tomorrow.", "color": "green", "lp": "+12", "sanity": "Delusional"},
        {"status": "SEND IT", "msg": "One more. The lose streak has to end somewhere, right?", "color": "green", "lp": "+16", "sanity": "Naive"},
        {"status": "GO", "msg": "Ranked is a circus and you are the star attraction. Enter the tent.", "color": "green", "lp": "+11", "sanity": "Jester-like"},
        {"status": "GO", "msg": "Your coffee is still warm. Your soul is not. Perfect for League.", "color": "green", "lp": "+14", "sanity": "Caffeinated"},
        {"status": "SEND IT", "msg": "You've already lost your mind. Might as well lose the LP too.", "color": "green", "lp": "-22", "sanity": "Ascended"},
        {"status": "GO", "msg": "The redemption arc is calling. It’s a wrong number, but answer anyway.", "color": "green", "lp": "+13", "sanity": "Confused"},
        {"status": "GO", "msg": "Just one more and then we'll tell everyone you're a pro.", "color": "green", "lp": "+20", "sanity": "Ego-boosted"},

        # --- EXTRA DARK ---
        {"status": "VOID", "msg": "The Void is calling. It says you're Hardstuck.", "color": "red", "lp": "-99", "sanity": "Vacuum"},
        {"status": "DANGER", "msg": "Your chair is planning an intervention.", "color": "red", "lp": "-19", "sanity": "Betrayed"},
        {"status": "STOP", "msg": "Do you remember what sunlight feels like? No? Then stop.", "color": "red", "lp": "-20", "sanity": "Vampiric"},
        {"status": "ABORT", "msg": "Even Riot's servers are trying to kick you off. Take the hint.", "color": "red", "lp": "-50", "sanity": "Unstable"},
        {"status": "GO", "msg": "Queue up. You haven't suffered enough today.", "color": "green", "lp": "-100", "sanity": "Masochistic"}
    ]
    return JsonResponse(random.choice(decisions))



from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .models import GameScore
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'corestuff/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'corestuff/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
from django.contrib.auth.decorators import login_required



@login_required
def save_score_api(request):
    score_val = request.POST.get('score')
    if score_val:
        GameScore.objects.create(user=request.user, score=score_val)
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"}, status=400)

def reaction_test_page(request):
    # Fetch top 10 unique high scores
    leaderboard = GameScore.objects.select_related('user').order_by('-score')[:10]
    return render(request, "corestuff/reaction_test.html", {"leaderboard": leaderboard})


@login_required
def save_score_api(request):
    if request.method == 'POST':
        score_val = request.POST.get('score')
        if score_val:
            new_score = int(score_val)
            # 1. Get the existing score for this user (if any)
            user_score_obj, created = GameScore.objects.get_or_create(
                user=request.user, 
                defaults={'score': new_score}
            )

            # 2. If it wasn't just created, check if the new score is actually higher
            if not created:
                if new_score > user_score_obj.score:
                    user_score_obj.score = new_score
                    user_score_obj.save()
                    return JsonResponse({"status": "success", "message": "New High Score!"})
                else:
                    return JsonResponse({"status": "success", "message": "Score saved, but not a personal best."})
            
            return JsonResponse({"status": "success", "message": "New High Score!"})

    return JsonResponse({"status": "error"}, status=400)

from .models import Comment

login_required(login_url='login')
def community_wall(request):
    if request.method == "POST":
        content = request.POST.get("comment_text")
        if content:
            Comment.objects.create(user=request.user, text=content)
            return redirect('community_wall')

    comments = Comment.objects.all()[:50] # Show last 50
    return render(request, 'corestuff/community.html', {'comments': comments})

import requests

import random
import requests
from django.shortcuts import render
import os
from django.conf import settings
import json
import random
import requests
from django.shortcuts import render

def champion_roller(request):
    # 1. Initialize empty lists as fallbacks
    boots_list = []
    legendary_list = []
    champ_list = ["Garen"] # Default fallback champion

    try:
        # Fetch Data
        champ_url = "https://ddragon.leagueoflegends.com/cdn/14.1.1/data/en_US/champion.json"
        item_url = "https://ddragon.leagueoflegends.com/cdn/14.1.1/data/en_US/item.json"
        
        champ_res = requests.get(champ_url).json()
        item_res = requests.get(item_url).json()
        
        # 2. Extract Data safely
        champ_data = champ_res.get('data', {})
        item_data = item_res.get('data', {})
        
        if champ_data:
            champ_list = list(champ_data.keys())

        for tid, info in item_data.items():
            gold = info.get('gold', {}).get('total', 0)
            purchasable = info.get('gold', {}).get('purchasable')
            tags = info.get('tags', [])
            maps = info.get('maps', {})

            if purchasable:
                # Logic for Boots
                if "Boots" in tags and gold >= 900:
                    boots_list.append({"id": tid, "name": info.get('name')})
                # Logic for Legendaries
                elif gold >= 2300 and maps.get('11'):
                    legendary_list.append({"id": tid, "name": info.get('name')})

    except Exception as e:
        print(f"Error fetching Riot Data: {e}")
        # Fallback values if API is down
        boots_list = [{"id": "3006", "name": "Berserker's Greaves"}]
        legendary_list = [{"id": "3089", "name": "Rabadon's Deathcap"}]

    # 3. Final Context
    context = {
        "champ_json": json.dumps(champ_list),
        "boots_json": json.dumps(boots_list),
        "legendary_json": json.dumps(legendary_list),
        "role_json": json.dumps(["TOP", "JUNGLE", "MID", "ADC", "SUPPORT"]),
        "summoners_standard": json.dumps(["SummonerFlash", "SummonerDot", "SummonerHaste", "SummonerHeal", "SummonerExhaust", "SummonerBarrier", "SummonerBoost", "SummonerTeleport"]),
        "summoner_smite": "SummonerSmite"
    }
    return render(request, 'corestuff/roller.html', context)

def quiz_view(request):
    # Fetching inside the view ensures 'champs' is always defined when the page loads
    url = "https://ddragon.leagueoflegends.com/cdn/14.1.1/data/en_US/champion.json"
    data = requests.get(url).json()
    champs = data['data']

    return render(request, 'corestuff/quiz.html', {
        'full_champ_data': champs
    })