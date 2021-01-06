#![no_std]
#![feature(alloc_error_handler)]

use core::panic::PanicInfo;
use cty;
use cstr_core::CStr;
use cstr_core::CString;
use cstr_core::c_char;
use alloc_cortex_m::CortexMHeap;
use core::alloc::Layout;

extern "C" {
    // common.c
    pub fn __fatal_error(
        expr: *const u8,
        msg: *const u8,
        file: *const u8,
        line: i32,
        func: *const u8,
    );

    pub fn display_init();
    pub fn display_refresh();
    pub fn display_print(text: *const u8, textlen: cty::c_int);
    pub fn display_backlight(val: cty::c_int) -> cty::c_int;
}

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    unsafe {
        __fatal_error(
            b"" as *const u8,
            b"RUST PANIC" as *const u8,
            b"" as *const u8,
            0,
            b"" as *const u8,
        );
    }
    loop {}
}

#[global_allocator]
static ALLOCATOR: CortexMHeap = CortexMHeap::empty();

#[alloc_error_handler]
fn oom(_: Layout) -> ! {
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

const INVALID_COORDS: &str = "Invalid coordinates";
const INVALID_SLICE: &str = "Invalid slice";

const DISPLAY_WIDTH: u16 = 240;
const DISPLAY_HEIGHT: u16 = 240;

fn rust_display_text(
    x: u16,
    y: u16,
    text: &CString,
    font: u16,
    fgcolor: u16,
    bgcolor: u16,
    offset: usize,
    length: usize,
) -> Result<(), &'static str> {
    if x >= DISPLAY_WIDTH || y >= DISPLAY_HEIGHT {
        return Err(INVALID_COORDS)
    }

    Ok(())
}
