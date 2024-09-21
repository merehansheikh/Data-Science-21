
.model small
.stack 100h
.data 
msg1 db "Enter the char in Upper Case: $"
msg2 db 10, 13, "Your entered char is: $ "
msg3 db 10, 13, "You entered the wrong character!$"


.code

main proc

    mov ax,@data
    mov ds, ax

    ;get the message and show it
    mov dx, offset msg1
    mov ah,09
    int 21H

    ;taking the input as a character
    mov ah,01
    int 21H



    ;if char >= A and char <= Z

    cmp Al, "A"
    jnge END_IF

    cmp Al, "Z"
    jnle END_IF


    ;get the second message
    mov dx, offset msg2
    mov ah,09
    int 21H


    mov dl, Al
    mov ah,02
    int 21H

    jmp exit


    END_IF:
        ;get the third message
        mov dx, offset msg3
        mov ah,09
        int 21H

    exit:
    mov ah,4ch
    int 21H

main endp
    end main