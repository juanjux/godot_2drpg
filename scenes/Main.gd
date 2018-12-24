extends Node

export (PackedScene) var Mob

var score

func _ready():
	randomize()
	
func _process(delta):
	if Input.is_key_pressed(KEY_Q) or Input.is_key_pressed(KEY_ESCAPE):
		exit_game()

func game_over():
	$ScoreTimer.stop()
	$MobTimer.stop()
	$HUD.show_game_over()
	
func new_game():
	score = 0
	$Player.start($StartPosition.position)
	
func exit_game():
	get_tree().quit()
