import random

def ai_decision(ai_counters, ai_tray, aiVals, quota, aiStreak):
    """ AI makes decisions based on customer patience and noodle doneness."""
    
    # Step 1: Check if AI can serve any customers
    for counter, (preference, patience) in ai_counters.items():
        for slot, (occupied, doneness) in ai_tray.items():
            if occupied and doneness == preference:
                serve_noodles(slot, counter, ai_tray, ai_counters, aiVals, quota, aiStreak)
                return f"AI serves noodles from slot {slot} to counter {counter}."
    
    # Step 2: Check if AI needs to place new noodle bowls
    if any(not occupied for slot, (occupied, _) in ai_tray.items()):
        empty_slots = [slot for slot, (occupied, _) in ai_tray.items() if not occupied]
        chosen_slot = random.choice(empty_slots)
        place_noodles(chosen_slot, ai_tray)
        return f"AI places a new bowl in slot {chosen_slot}."
    
    # Step 3: Default action is to wait and allow noodles to cook
    # print("AI waits this turn.")
    wait_turn()
    return "AI Waits"

def serve_noodles(slot, counter, trays, counters, vals, quota, streak):
    if trays[slot][1] == counters[counter][0]:                                  # Checks if customer preference is equal to the doneness of noodle served
        vals["served"] += 1 													# Adds one to successful order count
        vals["score"] += int(35 + 0.15*streak["current"])                       # Adds score rounded down to nearest integer. Score dedpends on the streak
        streak["current"] += 1
        if streak["current"] > streak["longest"]:
            streak["longest"] = streak["current"]                               # Updates the maximum streak
    else:
        if vals["score"] > 10:													# Score cannot be negative
            vals["score"] -= 10													# Subtracts score when order unsuccesful
        streak["current"] = 0 													# Resets streak
    
    trays[slot] = [0,0]										                    # Resets the default value for the selected tray
    counters[counter] = [0,""]									                # Resets the default value for the selected counter

def place_noodles(slot, trays):
    trays[slot][0] = 1 			                                                # Update status from 0/empty to 1/occupied

def wait_turn():
    # Do nothing
    return