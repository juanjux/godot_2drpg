extends CanvasLayer

signal start_game
	
func show_game_over():
	$StartButton.show()

func _on_StartButton_pressed():
	$StartButton.hide()
	emit_signal("start_game")