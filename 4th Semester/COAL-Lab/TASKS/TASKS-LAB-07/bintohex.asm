.model small
.stack 100h
.386

.data
    display_message db "Type a binary number upto 16 digits $"
    typo db 10,13, "Illegal BINARY digit $"
    hex_dis db 10, 13,"In HEX it is: $"
    new_line db 10, 13, "$"
    
.code

    main proc 

        mov ax, @data
        mov ds, ax

        start: mov cx, 0
        mov bx, 0000

        mov dx, offset display_message
        mov ah, 09
        int 21H


        input :

            mov ah,01
            int 21H

            ;checking for the new line character
            cmp al, 0Dh
            je further

            cmp al, 30H
            jl invalid
            cmp al, 31H
            jnle invalid

            sub al ,30H
            shl bx, 1

            or bl, al

            inc cx

        cmp cx, 16
        jl input
        jmp further

        further:

        ;show the message
        mov dx, offset hex_dis
        mov ah, 09
        int 21H

        call hex

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


    hex proc
    
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

    ret
    hex endp



end main