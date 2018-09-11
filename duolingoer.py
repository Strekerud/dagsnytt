import duolingo

def printProgress():
    lingo  = duolingo.Duolingo('Strekerud')
    lingo_emil = duolingo.Duolingo('beezlebob')
    lingo_bone = duolingo.Duolingo('tandberg')
    lingo_masha = duolingo.Duolingo('Masha672543')
    lingo_sigurd = duolingo.Duolingo('sigurlu')

    language_progress = lingo.get_language_progress('ru')
    streak_info = lingo.get_streak_info()

    #print "Next level in " + str(language_progress['level_left']) + " experience"

    tenths_done = int((float(language_progress['level_progress']) / language_progress['level_points']) * 10)
    
    print "----------------------------"
    print "=== DUOLINGO STATS ==="
    print "My current streak: " + str(language_progress['streak'])
    print "Masha's streak: " + str(lingo_masha.get_language_progress('nb')['streak']) + "  (lvl: " + str(lingo_masha.get_language_progress('nb')['level']) + ")"
    print "Emil's streak: " + str(lingo_emil.get_language_progress('fr')['streak']) + "  (lvl: " + str(lingo_emil.get_language_progress('fr')['level']) + ")"
    print "Bones's streak: " + str(lingo_bone.get_language_progress('de')['streak']) + "  (lvl: " + str(lingo_bone.get_language_progress('de')['level']) + ")"
    print "Sigurd's streak: " + str(lingo_sigurd.get_language_progress('dn')['streak']) + "  (lvl: " + str(lingo_sigurd.get_language_progress('dn')['level']) + ")"
    print "Level: " + str(language_progress['level'])
    print "Level progress: [",
    for _ in range(tenths_done):
        print "#",
    for _ in range(tenths_done, 10):
        print "-",
    print "] (" + str(language_progress['level_progress']) + "/" + str(language_progress['level_points']) + ")"
    if streak_info['streak_extended_today']:
        print "Daily XP requirement IS MET."
    else:
        print "Daily XP requirement NOT MET. Fix it, Kristoffer."
    print "----------------------------"
