#![no_std]

use core::panic::PanicInfo;
use cty;

extern {
    // common.c
    pub fn __fatal_error(expr: *const u8, msg: *const u8, file: *const u8, line: i32, func: *const u8);

    pub fn display_init();
    pub fn display_refresh();
    pub fn display_print(text: *const u8, textlen: cty::c_int);
    pub fn display_backlight(val: cty::c_int) -> cty::c_int;
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
    let cstr = b"Hello from Rust!\n";
    unsafe {
        display_backlight(255);
        display_print(cstr as *const u8, 12);
        display_refresh();
    }
}
