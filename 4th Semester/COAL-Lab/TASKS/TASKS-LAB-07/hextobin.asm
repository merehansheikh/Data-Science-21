.model small
.stack 100h
.386

.data
    display_message db "Type a HEX digit: $"
    typo db 10,13, "Illegal hex digit $"
    binary db 10, 13,"In binary it is: $"
    new_line db 10, 13, "$"
    
.code

    main proc 

        mov ax, @data
        mov ds, ax

        ;initializing the counter to 4 (for hex)
        start: mov cx ,0
        mov bx, 0000

        ;getting the message
        mov dx, offset display_message
        mov ah, 09
        int 21H

        input:
            
            mov ah,01
            int 21H

            ;checking for the new line character
            cmp al, 0Dh
            je further

            cmp al, 0
            jl invalid
            cmp al, 46H
            jnle invalid

            cmp al, 39h
            jnle ALPHA
            jmp NUM

            check : inc cx

        cmp cx, 4
        jl input
        jmp further
            
        ALPHA:
            shl bx ,4

            sub al, 37H
            or bl, al


            jmp check
            jmp further

        NUM:
            shl bx, 4

            sub al, 30h
            or bl, Al

            jmp check
            jmp further

        further:

        ;show the message
        mov dx, offset binary
        mov ah, 09
        int 21H

        call bin

        jmp exit

        ; display the invalid message
        invalid:
            mov dx, offset typo
            mov ah, 09
            int 21H

            jmp start

    exit:
        mov ah, 4ch
        int 21H


    main endp


    bin proc
    
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

    ret
    bin endp



end main