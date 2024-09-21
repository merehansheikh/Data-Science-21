.model small
.stack 100h
.386

.data
msg1 db "Enter the 1st value in Hex: $"
msg2 db "Enter the 2nd value in Hex: $"
invalid db "Invalid input, enter again: $"
new_line db 10, 13, "$"

.code

main proc

    mov ax, @data
    mov ds, ax

    mov dx, offset msg1
    mov ah, 09
    int 21H

    call hex_in
    ; mov 

    mov dx, offset new_line
    mov ah,09
    int 21H

    mov dx, offset msg2
    mov ah, 09
    int 21H

    mov dx, bx

    call hex_in

    add bx, dx

    mov dx, offset new_line
    mov ah,09
    int 21H

    jc print_one
    jmp hehe



    print_one:
        mov dl, 31H
        mov ah, 02
        int 21H


    hehe:
    ; mov AH, 09
    ; int 21H


    mov cl, 4

    again:
        rol bx, 4

        mov al, bl
        and al , 0Fh
        add al, 30h

        cmp al, 39h
        jle display_

        add al , 7H
        mov dl, Al
        mov ah,02
        int 21H

        dec cl
        ; int 21H

        jnz again
        jmp exit

    display_:
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

    hex_in proc

        start: mov cx, 4
        mov bx, 0000

        while_:
            
            mov ah,01
            int 21H

            cmp al, 30h
            jl invalid_response


            cmp al, 39h
            jle num
            

            cmp al, 41H
            jl invalid_response

            cmp al, 'F'
            jg invalid_response

            jmp ALPHA

            dec cx
            jnz while_
            jmp end_while
            


        ALPHA:
            shl bx ,4

            sub al, 37H
            or bl, al


            dec cx
            jnz while_
            jmp end_while

        NUM:
            shl bx, 4

            sub al, 30h
            or bl, Al


            dec cx
            jnz while_
            jmp end_while

        
        end_while: ret
        invalid_response: 
            mov dx, offset invalid
            mov ah, 09
            int 21H
            jmp start
    hex_in endp

end main

