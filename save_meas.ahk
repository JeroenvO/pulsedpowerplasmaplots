; This script was created using Pulover's Macro Creator
; to record mouseclicks. 
; www.macrocreator.com
; Exported to AHK and updated. 

; Automatic capture of waveforms 
; Jeroen van Oorschot 2018

#NoEnv
SetWorkingDir %A_ScriptDir%
CoordMode, Mouse, Window
SendMode Input
#SingleInstance Force
SetTitleMatchMode 2
#WinActivateForce
SetControlDelay 1000
SetWinDelay 100
SetKeyDelay 200
SetMouseDelay 200
SetBatchLines -1

HideTrayTip() {
	Menu Tray, NoIcon
	Sleep 200  ; It may be necessary to adjust this sleep.
	Menu Tray, Icon
}

WaitReady() {
	Loop
	{
		; Wait for mouse cursor to become normal (not waiting)
		if (A_index == 10)
		{
			MsgBox, 1, , Error! Timeout! Continue?.
			IfMsgBox, Cancel
				Return 1
			Return 0
		}
		if (A_Cursor == "Wait")
		{
			Sleep, 750
		}
		else
			return 0
	}
}

F7::
TrayTip, AHK EasyScope clicker, Started script!, 1
Loop
{	
	; Ask base filename
	InputBox, filename, Give file name, file name prepend
	if (ErrorLevel)
	{
		MsgBox, CANCEL was pressed.
		Return
	}
	
	Sleep, 500
	Loop, 24 ; store 24 waveforms
	{
		Sleep, 200
		indexzero := A_index-1
		TrayTip, AHK EasyScope clicker, Iteration %indexzero%
		
		; check single run
		Sleep, 200
		Click, 316, 67 Left, Down
		Click, 316, 67 Left, Up
		Sleep, 1000
		Click, 498, 107 Left, Down
		Click, 498, 107 Left, Up
		Sleep, 500
		if (WaitReady())
			Return
		Send, {Escape}
		Sleep, 500
		
		; Refresh scope
		Click, 269, 384 Left, Down
		Click, 269, 384 Left, Up
		Sleep, 500
		if (WaitReady())
			Return
		Sleep, 100
		
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
		Sleep, 100
		Send, {Home}
		Send, {Delete}
		Send, %filename%
		Send, {_}
		Send, %indexzero%
		Sleep, 100
		Send, {Enter}
		Sleep, 100
		
		HideTrayTip()
	}
	
	; Refresh scope
	Click, 269, 384 Left, Down
	Click, 269, 384 Left, Up
	Sleep, 200
	
	MsgBox, 1, , Finished measurement %A_index%. Restart?, 100
	IfMsgBox, Timeout
		Return ; i.e. Assume "No" if it timed out.
	IfMsgBox, Cancel
		Return ; i.e. Assume "No" if it timed out.
	; Otherwise, continue:
}

F8::ExitApp

F12::Pause