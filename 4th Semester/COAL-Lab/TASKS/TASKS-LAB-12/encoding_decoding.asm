
.model small
.stack 100h
.386

.data

    ed db 65 dup(0) 
        db 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'


    de db 65 dup(0) 
        db 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', "A"

    new_line  db 10, 13, "$" ;new line character

    str1 db 25 dup(0)
    ; str2 d
    encode db 50 dup(0)
    

.code

; main ;description
main PROC

    mov ax, @data
    mov ds, ax

    mov si, offset str1
    ; mov bx, offset str1


    mov cx, 00


    aa : 
    mov ah, 01
    int 21h

    cmp al, 0Dh ; new line
    je exit
    
    mov [si] , al

    inc si
    inc cx
    jmp aa

    exit: 
    push cx
    call print_encoded
    pop cx


    mov dx, offset new_line
    mov ah, 09
    int 21H

    call print_dec

    mov ah, 4ch
    int 21h



    
main ENDP

;descriptio
print_encoded PROC
    mov bx, offset ed
    mov si, offset str1
    mov di, offset encode

    ; mov al, [si]

    loop1:

        mov al, [si]
        xlat
        mov [di], al
        ; add al, 30h
        mov dl, al
        mov ah,02
        int 21h

    inc di
    inc si
    dec cx
    jnz loop1

    ret

print_encoded ENDP


;description
print_dec PROC

    mov bx, offset de
    mov si ,offset encode

    loop2:
        mov al, [si]
        xlat
        ; mov dl ,30h
        mov dl ,al
        mov ah, 02
        int 21h

    inc si
    dec cx

    jnz loop2
    ret
    
print_dec ENDP


end main


