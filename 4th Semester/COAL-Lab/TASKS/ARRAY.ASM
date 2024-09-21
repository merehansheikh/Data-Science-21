.model small
.stack 100h

.data   ; defining the data

char_str db "The binary is: $"
new_line db 10, 13, "$" ; new line character
ones db "The number of ones: $"

.code
main proc
	
	mov AX, @data
	mov DS, AX
	
	mov AH,01 ; taking the input
	int 21H
	mov BL, AL
	
	mov CL , 8 ; for the counter
	mov CH, 30H ; for the count of the number of ones in the input
	
	mov DX, offset char_str
	mov AH, 09 ; display the character string
	int 21H
	
	again: 
		SHL BL, 1 ; shift left bits
		
		JC ONE ; jump if carry is set
		
		mov DL, 30H ; store 0 in DL
		mov AH, 02 ; output 0
		int 21H
		JMP LOOP1 ;jumping to the loop
		
		ONE:
			mov DL, 31H ; store 1 in DL (for outputing)
			inc CH ;increment the CH counter by one
			mov AH, 02 ; output 1
			int 21H 
		
		LOOP1:
			dec CL ; decrement the CL counter by one
			JNZ again
	
	mov DX, offset new_line ; display the new_line
	mov AH, 09
	int 21H
	
	mov DX, offset ones ; display the ones string
	mov AH, 09
	int 21H
	
	mov DL, CH ; shift the count of ones in CH
	mov AH,02
	int 21H
	
	mov AH, 4CH ; to terminate the program
	int 21H



main endp
end main