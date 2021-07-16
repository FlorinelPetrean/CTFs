
BITS 64:
    mov rdi, 1
    mov rbx, `first`
    push rbx
    mov rsi, rsp
    mov rax, 1
    syscall