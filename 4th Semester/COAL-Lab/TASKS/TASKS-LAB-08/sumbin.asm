

.model small
.stack 100h
.386 

.data
msg1 db "Enter the 1st number in binary: $"
msg2 db "Enter the 2nd number in binary: $"
invalid db "Please enter a valid binary: $"

; var dw ?
char_str db "The number after addition is: $"
new_line  db 10, 13, "$" ;new line character


.code


main proc 
    mov ax, @data
    mov ds, ax


    ;taking the inoput
    mov dx, offset msg1
    mov ah, 09
    int 21H

    call bin_input ;getting the first
    ; pop Dx

    mov dx, offset new_line
    mov ah, 09
    int 21H
    mov dx, offset msg2
    mov ah, 09
    int 21H

    mov dx, bx

    call bin_input ;getting the 2nd

    add bx, dx
    ; mov bx, dx

    mov CL , 8 ;for the counter

    mov DX, offset new_line
    mov AH, 09
    int 21H


    mov dx, offset char_str
    mov ah,09
    int 21H

    ror bh, 1
    jc print_one
    jmp again

    print_one:
        mov DL, 31H
        mov AH, 02
        int 21H
        jmp again
    



    again: 

        rol Bl, 1

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

    

        ; mov DX, offset new_line
        ; mov AH, 09
        ; int 21H

    ; print_one
    mov ah,4ch
    int 21H
    

main endp

    bin_input proc

        start: mov cl, 8
        mov bx, 0

        while_ :


            mov ah,01
            int 21H

            ;checking if the number is valid
            ; cmp al ,0DH
            ; jmp aa
            cmp al, 30H
            jl invalid_response
            cmp al, 31H
            jg invalid_response

            sub al ,30H

            shl bx, 1

            or bl, al

            dec cl

        jnz while_

    ; aa : push bx

    ret 
    invalid_response:
        mov dx, offset invalid
        mov ah,09
        int 21H
        jmp start
    bin_input endp



    end main