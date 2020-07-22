#![no_std]

use core::panic::PanicInfo;

extern {
    // libc
    pub fn printf(format: *const u8, ...) -> i32;
    // common.c
    pub fn __fatal_error(expr: *const u8, msg: *const u8, file: *const u8, line: i32, func: *const u8);
}

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    unsafe {
        __fatal_error(b"" as *const u8, b"RUST PANIC" as *const u8, b"" as *const u8, 0, b"" as *const u8);
    }
    loop {}
}

#[no_mangle]
pub extern "C" fn rust_function() {
    unsafe {
        printf(b"Hello from Rust!\n" as *const u8);
    }
}
