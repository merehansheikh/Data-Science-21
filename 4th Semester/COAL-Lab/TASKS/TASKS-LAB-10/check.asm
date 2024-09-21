

.model small
.stack 100h
.386
.data

array1 db 16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1
decimal db "The number in decimal is: $"
new_line  db 10, 13, "$" ;new line character


.code

main proc

    mov ax, @data
    mov ds, ax

    mov si, offset array1

    

    mov cl, 16
    mov bx, 0000
    first :
        mov ch, 15
        mov si, offset array1
        second:

            mov bl, [si + 1]
            cmp bl, [si]
            jg swap
            jmp sec


            swap: 
            xchg bl, [si+1]
            mov [si + 1], bl

            sec: 
            inc si
            dec ch
            jnz second
            

        dec cl
        jnz first

        call printing_array

mov ah, 4ch
int 21h

main endp

printing_array proc

    mov si, offset array1
    mov cx, 16

    prin_loop: 
        mov ax, [si]
        push cx
        call decimal_out
        pop cx

        inc si
        dec cx
        jnz prin_loop

    ret

printing_array endp

; print proc:




decimal_out proc

        ; mov dx, offset new_line
        ; mov ah, 09
        ; int 21H
        ; mov dx, offset decimal
        ; mov ah, 09
        ; int 21H


    mov ax, bx
    mov BX, 10
    while_quo_0:

        mov dx, 0
        div bx
        add dx, 30H
        push dx

        cmp ax, 0
        jne while_quo_0

    mov cx, 4
    display_while :
        pop dx
        mov ah, 02
        int 21h
        dec cx
        jnz display_while

    exe_dec : ret
    decimal_out endp

end main