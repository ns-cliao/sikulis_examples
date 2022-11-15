#url = 'https://www.memozor.com/memory-games/for-kids/minecraft'
url = 'https://www.memozor.com/memory-games/for-kids/frozen-2'

PathChrome = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
interval = 0.3
similar_rate = 0.9

game_level_4_3 = "1668507148800.png"
game_level_4_4 = "1668506699341.png"
game_level = game_level_4_4


# ===== open browser =====
App.open(PathChrome)
App.focus('Matching game for kids')


# ===== open new tab  =====
if exists("1668517399077.png"):
  click("1668517399077.png")
elif exists("1668517380862.png"):
  click("1668517380862.png") 
click("1668420015498.png")
paste(url)
type(Key.ENTER)


# ===== scroll down =====
type(Key.HOME)
for x in range(10):
    type(Key.DOWN)
    sleep(interval)


# ===== click btn =====

if exists(game_level):
  click(game_level)
if exists("1668420516225.png"):
  click("1668420516225.png")
if exists("1668433396574.png"):
  click("1668433467888.png")


# ===== round-1: find all cards =====
cards = findAllList("1668507589135.png")
count = len(cards)
print "cards count = ", count


# ===== round-2: click cards to open =====
open_cards = []
idx = 0

for x in cards:
    x.click() # click to open card
    sleep(interval)
    o = capture(x) # capture image of opened card
    open_cards.append(o)
    print idx, o
    idx=idx+1
    sleep(interval)


# ===== round-3: find same card (loop) =====
clicked_cards = []

for x in range(count):
    if x in clicked_cards:
        continue

    print "loop ", x
    pattern = Pattern(open_cards[x]).similar(similar_rate)
    match = None
    match_idx = -1  
        
    for y in range(count):
        if x==y or y in clicked_cards:
            continue

        # find same card by pattern
        finder = Finder(open_cards[y])
        finder.find(pattern) 
        
        while finder.hasNext():
            f = finder.next()
            print "  match: ", y, f.score

            # find item with highest score
            if match is None or f.score > match.score:
                match = f
                match_idx = y

    # click/open same cards if matched
    if match is None:
        print "  no match: "
    else:
        print "  best match: ", match_idx, match.score
        clicked_cards.append(x)
        clicked_cards.append(match_idx)

        a = Region(cards[x].x, cards[x].y, cards[x].w, cards[x].h)
        a.click()
        sleep(interval)

        b = Region(cards[match_idx].x, cards[match_idx].y, cards[match_idx].w, cards[match_idx].h)
        b.click()
        sleep(interval)

print "clicked_cards = ", len(clicked_cards), clicked_cards


