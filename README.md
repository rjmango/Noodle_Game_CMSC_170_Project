# Noodle Shop Game - README

## Introduction
The Noodle Shop is a turn-based simulation game where players take on the role of a noodle shop owner, managing customer orders and ensuring proper noodle doneness. Customers have varying patience levels and preferences, requiring strategic decision-making and efficient time management. The game challenges players to optimize their workflow, balance cooking times, and serve customers before they leave unsatisfied.

## Purpose and Objectives
The game aims to provide an engaging and strategic simulation of running a noodle shop while improving players' multitasking and decision-making skills. The specific objectives include:
- Simulating a dynamic kitchen environment with turn-based mechanics.
- Encouraging players to strategize noodle cooking times and customer service.
- Introducing increasing difficulty levels for progressive challenge.
- Tracking player performance through scores and order accuracy.

## Features
- **Turn-Based Gameplay**: Players control actions per turn, including placing, cooking, and serving noodles.
- **Cooking Mechanics**: Noodles move through different cooking stages (Dipped → Extra Firm → Firm → Regular → Soft → Extra Soft → Overcooked), requiring precise timing.
- **Customer Patience System**: Customers arrive with varying patience levels, and orders must be completed before they leave.
- **Multi-Counter System**: Players manage multiple counters simultaneously, adjusting to different customer demands.
- **Difficulty Modes**: Adjustable difficulty with different customer quotas, counters, and service challenges.
- **Scoring and Progression**: Players earn scores based on successful orders, with high-score tracking and level progression.
- **Persistence through File Handling**: High scores and game progress are saved and loaded for replayability.

## Methodology
- **Game Design and Planning**: Define core mechanics, customer AI behavior, and difficulty scaling.
- **Development and Implementation**: Use a game engine (such as Unity or Python with Pygame) to create turn-based mechanics and UI elements.
- **Testing and Balancing**: Conduct playtesting to refine order pacing, difficulty levels, and scoring mechanics.
- **Optimization and Persistence**: Implement file handling for saving high scores and progress.
- **Deployment and User Feedback**: Release the game, gather feedback, and apply updates for better gameplay balance.

## Expected Output
- A fully functional turn-based simulation game with interactive cooking and customer service mechanics.
- A challenging and engaging experience where players must balance speed, accuracy, and strategy.
- A scoring and progression system that rewards efficiency and high performance.
- A replayable game with saved high scores and difficulty adjustments for varying skill levels.

## About the Gameplay
### Noodle Doneness Progression
Noodles follow this doneness progression when placed on a tray:
```
Dipped → Extra Firm → Firm → Regular → Soft → Extra Soft → Overcooked
```

### Counters
The noodle shop has at least 3 counters, depending on the difficulty you choose:
```
-----------        -----------        -----------
 Counter A         Counter B         Counter C
```
- **EASY**: 3 counters
- **MEDIUM**: 4 counters
- **HARD**: 5 counters

Your final score is multiplied based on difficulty:
- EASY: ×1
- MEDIUM: ×2
- HARD: ×3

### Tray System
The player's **TRAY** can hold up to **FIVE** noodle bowls at a time.

**Example Tray:**
```
Slot A: Empty
Slot B: Dipped
Slot C: Overcooked
Slot D: Firm
Slot E: Empty
```

## Game Mechanics
- Each turn, a customer may appear on an empty counter.
- The customer will display their requested **Noodle Doneness** and their **current Patience**.

**Example Counters:**
```
-----------        -----------        -----------
 Counter A         Counter B         Counter C
 Overcooked
 Patience: 5
```

### Actions Per Turn:
1. **PLACE** a noodle bowl into an empty tray slot.
   - Example:
   ```
   Enter an empty tray slot: A
   Tray:
   Slot A: Dipped
   Slot B: Empty
   Slot C: Empty
   Slot D: Empty
   Slot E: Empty
   ```

2. **WAIT** (skip a turn)
   - Noodles progress through doneness levels each turn.
   - Once noodles become **Overcooked**, they remain Overcooked.
   - All seated customers lose **one** patience per turn.
   - If patience reaches **zero**, the customer leaves, making the order unsuccessful.

3. **SERVE** a noodle bowl to a counter.
   - Example:
   ```
   Enter a tray slot: A
   Enter a counter slot: B
   Successful Order!
   ```

## Scoring & Streaks
- Each successful order is worth **35 points**.
- Consecutive successful orders add to a **streak multiplier (1.15 per streak)**.
- If an order fails or a customer leaves, the streak resets to **ZERO**.

**Example Score Display:**
```
Score: 35                           Streak: 1
Customers to Serve: 9    Successful Orders: 1
Total Customers: 10    Quota for the round: 5
```

## Win/Lose Conditions
- Each round has a **quota** of successful orders:
  - **EASY**: 50% of customers
  - **MEDIUM**: 75% of customers
  - **HARD**: 100% of customers
- If you meet the quota, the next round starts (with **five** more customers).
- If you fail to meet the quota, **Game Over**.

## Prerequisites
- Device with Windows installed.

## Game Setup
1. **Download** the game ZIP file.
2. **Extract** the files to a folder of your choice.
3. **Run** the executable file (`RUNME.bat` or `main.exe`).
4. **Enjoy** the game!

---
### Thank you for playing the Noodle Shop Game! 🍜