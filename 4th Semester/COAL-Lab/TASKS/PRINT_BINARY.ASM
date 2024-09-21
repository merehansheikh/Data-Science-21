.model small
.stack 100h

.data   ;defining the data

char_str db "The binary is: $"
new_line db 10, 13, "$" ;new line character
ones db "The number of ones: $"

.code
main proc

mov AX, @data
mov DS, AX

mov AH,01 ;taking the input
int 21H
mov BL, AL

mov CL , 8 ;for the counter
mov CH, 30H ; for the count of the number of ones in the input

mov DX, offset char_str
mov AH, 09
int 21H

again: 
    SHL BL, 1

    jc ONE

    mov DL, 30H
    mov AH, 02
    int 21H
    jmp loop1



ONE:
    mov DL, 31H
    inc CH
    mov AH, 02
    int 21H

loop1:
    dec CL
    jnz again

    mov DX, offset new_line
    mov AH, 09
    int 21H

    mov DX, offset ones
    mov AH, 09
    int 21H

    mov DL, CH
    mov AH,02
    int 21H

mov AH,4ch
int 21H



main endp
end main