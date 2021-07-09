# snake-game
Learning the pygame module and refreshing my knowledge on classes in python through recreating Snake with a working GUI (additional game options, menus, and a store with customizable items).

## Bugs
- background music isn't restarting when failing and restarting
- update() resets the snake position every time the screen refreshes 
- spamming wasd as a 3 block snake too fast causes death but this shouldn't be possible
- make it so speed changes only happen after the next match (eventually just put it in the reset() function, but rn it updates too often)
    - right now, changes to speed only apply after going to main menu....
- resizable window
- game_over() and check_fail() runs every time?
- decreasing cell size does not shrink everything else like it used to...
- pressing resume should bring up pause page with game in the background
- change what pressing escape does in options screen (right now it just goes back to prev page)
- just hovering over main menu button activates it (sometimes)
- since move() is always being triggered through update() with its else statement(usually unles fruit is on its head), move() always triggers the - check_fail()/ game_over() function causing the snake to spawn over and over again
- going the opposite way as the first key press causes game_over() (however, this shouldn't be possible)
- countdown 3-2-1 when resuming after pausing
- pressing down left when going right kills you sometimes and other similar combinations
- score at game over screen


## Ideas
- Resolution slider (cell_size * cell_number x cell_size * cell_number) 
- snake speed slider (ms_speed from 25-250)
- shop
- new color block snakes
- new backgrounds
- new bg music
- make tiles smaller (maybe?) so snake animation look cleaner
- separate classes into different files to make work space more manageable
- game over screen
- make game paused after going back to game from options
- When hovering, change button color (lighter)

Base Snake game assets and code from clear-code-projects