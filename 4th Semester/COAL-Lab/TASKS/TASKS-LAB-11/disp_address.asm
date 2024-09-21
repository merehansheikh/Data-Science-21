.model small
.stack 100h
.386
.data

    arr db 128 dup(69h)
    new_line db 10, 13, "$"
    
.code
main proc

    mov ax, @data
    mov ds, ax

    mov si, offset arr
    mov cl, 128

    while_arr:
        
        call dumping_display

        mov dx, offset new_line
        mov ah, 09
        int 21h
        cmp cl, 0
        jg while_arr

    mov ah, 4ch
    int 21h

main endp

display_address proc

    mov ch, 4
    while_display:
        rol bx, 4
        mov al, bl
        and al, 0Fh

        cmp al, 0AH
        jl add_30H
        add al, 37H
        jmp continue_

        add_30H:
            add al, 30H

        continue_:
            mov dl, al
            mov ah, 02
            int 21h

            dec ch
            jnz while_display
    
    ret
display_address endp

dumping_display proc
    mov bx, ds
    call display_address
    
    mov dl, ":"
    mov ah, 02
    int 21h
    
    mov bx, si
    call display_address
    
    
    
    mov dl, " "
    mov ah, 02
    int 21h

    mov dh, 0
    while_dump:
        mov ax, [si]
        push ax
        
        mov al, [si]
        
        rol al, 4
        mov [si], al
        mov bl, al
        and bl, 0Fh

        cmp bl, 0AH
        jl add_30h_
        add bl, 37H
        jmp e

        add_30h_:
            add bl, 30H

        e:
            mov dl, bl
            mov ah, 02
            int 21h
        
        mov al, [si]
        rol al, 4
        mov [si], al
        mov bl, al
        and bl, 0Fh

        cmp bl, 0AH
        jl add_30h_1
        add bl, 37H
        jmp e1

        add_30h_1:
            add bl, 30H

        e1:
            mov dl, bl
            mov ah, 02
            int 21h

        mov dl, " "
        mov ah, 02
        int 21h
        
        
        
        inc si
        inc dh
        dec cl
        cmp cl, 0
        je exit___
        cmp dh, 16
        je exit___
        jmp while_dump

    exit___:
        pop ax
        mov dl, al

        mov ah, 02
        int 21h
        dec dh
        jnz exit___
        ret
        


dumping_display endp

end main