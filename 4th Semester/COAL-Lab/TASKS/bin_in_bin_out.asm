

.model small
.stack 100h
.386 

.data
msg1 db "Enter the digit in binary: $"

; var dw ?
char_str db "The number after multiplication by 2 is: $"
new_line  db 10, 13, "$" ;new line character


.code


main proc 
    mov ax, @data
    mov ds, ax

    ; mov var , offset va

    ;taking the inoput
    mov dx, offset msg1
    mov ah, 09
    int 21H

    mov cx, 16
    mov bx, 0000

    while_ :


        mov ah,01
        int 21H

        sub al ,30H
        ; mov bx, ax
        shl bx, 1

        or bl, al

        dec cx

        jnz while_

    ; shift the bx register by 2
    shl bx ,2

    mov CL , 16 ;for the counter
    ; mov CH, 30H ; for the count of the number of ones in the input

    mov DX, offset new_line
    mov AH, 09
    int 21H


    mov dx, offset char_str
    mov ah,09
    int 21H

    again: 

        SHL BX, 1

        jc ONE

        mov DL, 30H
        mov AH, 02
        int 21H
        jmp loop1



    ONE:
        mov DL, 31H
        mov AH, 02
        int 21H

    loop1:
        dec CL
        jnz again

        mov DX, offset new_line
        mov AH, 09
        int 21H

        ; mov DX, offset ones
        ; mov AH, 09
        ; int 21H


    mov ah,4ch
    int 21H
    

main endp

    end main