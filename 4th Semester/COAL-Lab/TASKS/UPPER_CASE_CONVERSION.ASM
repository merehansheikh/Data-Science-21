.model small
.stack 100h

.data
    cr equ 0dh ; equ used as =, it means to assign the variable that value
    lf equ 0ah

msg1 db "Enter a lower case letter: $"
msg2 db cr, lf, "In upper case it is: "" ; odh, oah is the new line character (10, 13)
char db ?, '$' ;storing something in it
.code

main proc
    mov AX,@data
    mov DS, AX

    ; get the first message and display it
    lea dx, msg1
    mov ah,09
    int 21H

    ;get the input from prompt
    mov ah,01
    int 21H
    sub al, 20h
    mov char ,al

    ;get the second message on the new line
    lea dx, msg2
    mov ah,09
    int 21H

    mov ah,4ch
    int 21H

main endp

end main