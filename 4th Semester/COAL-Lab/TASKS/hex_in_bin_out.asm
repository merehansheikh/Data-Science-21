.model small
.stack 100h
.386

.data
msg1 db "Enter the value in Hex: $"
new_line db 10, 13, "$"

.code

main proc

    mov ax, @data
    mov ds, ax

    mov dx, offset msg1
    mov ah, 09
    int 21H

    mov cx, 4
    mov bx, 0000

    while_:
        
        mov ah,01
        int 21H

        cmp al, 39h
        jnle ALPHA
        jmp NUM

        dec cx
        jnz while_
        jmp end_while
        


    ALPHA:
        shl bx ,4

        sub al, 37H
        or bl, al


        dec cx
        jnz while_

    NUM:
        shl bx, 4

        sub al, 30h
        or bl, Al


        dec cx
        jnz while_

    ;
    mov dx, offset new_line
    mov ah,09
    int 21H
    end_while: 

    mov dx, offset new_line
    mov ah, 09
    int 21H
    ;shifting if the register

    shl bl, 3

    
    mov cx, 16

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
        dec cx
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