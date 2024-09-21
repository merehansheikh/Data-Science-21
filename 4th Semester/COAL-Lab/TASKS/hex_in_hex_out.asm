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

    ;displaying new line
    mov DX, offset new_line
    mov AH, 09
    int 21H



    mov cl, 4

    again:
        rol bx, 4

        mov al, bl
        and al , 0Fh
        add al, 30h

        cmp al, 39h
        jle display

        add al , 7H
        mov dl, Al
        mov ah,02
        int 21H

        dec cl
        ; int 21H

        jnz again
        jmp exit

    display:
        mov dl ,al
        mov ah, 02
        int 21H

        dec cl
        jnz again

    exit:
        mov ah,4ch
        int 21H
    int 21H

main endp
    end main

