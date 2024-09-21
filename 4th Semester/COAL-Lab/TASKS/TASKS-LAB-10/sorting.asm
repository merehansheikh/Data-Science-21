.model small
.stack 100h
.386
.data
    array db 55,84,133,9Bh,7AH
    decimal db 'Data in Decimal Format: $'
    hex_decimal db 'Data in Hexa-Decimal Format: $'
    new_line db 10, 13, "$"
    space db ' $'
.code

main proc

    mov ax, @data
    mov ds, ax

    call sort_data
    

    mov dx, offset new_line
    mov ah, 09
    int 21h

    mov dx, offset hex_decimal
    mov ah, 09
    int 21h

    mov bl, 16
    call display_data

    mov dx, offset new_line
    mov ah, 09
    int 21h

    mov dx, offset decimal
    mov ah, 09
    int 21h

    mov bl, 10
    call display_data



    
    
    


    
    mov ah, 4ch
    int 21h




main endp

sort_data proc
    mov cl, 4
    while_outer_loop:
        mov ch, 5
        mov si, offset array
        mov bl, [si]
        while_inner_loop:
            cmp bl, [si]
            jbe continue
            xchg bl, [si]
            dec si
            mov [si], bl
            inc si


            continue:
                mov bl, [si]
                inc si
                dec ch
                jnz while_inner_loop
        
        dec cl
        jnz while_outer_loop
    
    ret
sort_data endp

display_data proc
    mov cl, 5
    mov si, offset array
    traverse_array:
        mov al, [si]
        mov ch, 0
        while_quo:
            mov ah, 0
            div bl
            push ax
            inc ch
            cmp al, 0
            je display_vals
 
            jmp while_quo
        
        display_vals:

            pop dx
            mov dl, dh
            cmp dl, 9
            jg add_37
            add dl, 30H
            jmp c
        
        add_37:
            add dl, 37H
        c:
            mov ah, 02
            int 21h
            dec ch
            jnz display_vals
        
        mov dx, offset space
        mov ah, 09
        int 21h
        
        inc si
        dec cl
        jnz traverse_array

    ret

        


display_data endp
end main