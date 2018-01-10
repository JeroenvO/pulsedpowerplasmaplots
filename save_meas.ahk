; This script was created using Pulover's Macro Creator
; to record mouseclicks. 
; www.macrocreator.com
; Exported to AHK and updated. 

; Automatic capture of 30 waveforms 
; Jeroen van Oorschot 2018

#NoEnv
SetWorkingDir %A_ScriptDir%
CoordMode, Mouse, Window
SendMode Input
#SingleInstance Force
SetTitleMatchMode 2
#WinActivateForce
SetControlDelay 100
SetWinDelay 100
SetKeyDelay 200
SetMouseDelay 200
SetBatchLines -1

F7::
Loop
{
	; Refresh scope
	Click, 269, 384 Left, Down
	Click, 269, 384 Left, Up
	Sleep, 200
	; Ask base filename
	InputBox, filename, Give file name, file name prepend
	Sleep, 100
	Loop, 20 
	{
		; Refresh scope
		Click, 269, 384 Left, Down
		Click, 269, 384 Left, Up
		Sleep, 3000
		; Save spectrum
		Click, 227, 144 Left, Down
		Click, 227, 144 Left, Up
		Sleep, 200
		; Select waveforms
		WinActivate, Select the Chan ahk_class #32770
		Sleep, 200
		Click, 58, 109 Left, Down
		Click, 58, 109 Left, Up
		Sleep, 200
		Click, 49, 131 Left, Down
		Click, 52, 129 Left, Up
		Sleep, 200
		Click, 135, 58 Left, Down
		Click, 135, 58 Left, Up
		Sleep, 200
		; Save as
		WinActivate, Save Wave Graph File ahk_class #32770
		Sleep, 200
		Send, {Home}
		Send, {Delete}
		Send, %filename%
		Send, {_}
		indexzero := A_index-1
		Send, %indexzero%
		Sleep, 200
		Send, {Enter}
		Sleep, 200
	}
	; Refresh scope
	Click, 269, 384 Left, Down
	Click, 269, 384 Left, Up
	Sleep, 200
	
	MsgBox, 1, , Finished measurement %A_index%. Restart?, 10
	IfMsgBox, Timeout
		Return ; i.e. Assume "No" if it timed out.
	IfMsgBox, Cancel
		Return ; i.e. Assume "No" if it timed out.
	; Otherwise, continue:
}

F8::ExitApp

F12::Pause
