use std::{env, path::PathBuf, process::Command};

fn main() {
    generate_qstr_bindings();
    generate_micropython_bindings();
    #[cfg(test)]
    add_test_dependencies();
}

/// Generates Rust module that exports QSTR constants used in firmware.
fn generate_qstr_bindings() {
    let out_path = env::var("OUT_DIR").unwrap();
    let target = env::var("TARGET").unwrap();

    // Tell cargo to invalidate the built crate whenever the header changes.
    println!("cargo:rerun-if-changed=qstr.h");

    bindgen::Builder::default()
        .header("qstr.h")
        // Build the Qstr enum as a newtype so we can define method on it.
        .default_enum_style(bindgen::EnumVariation::NewType { is_bitfield: false })
        // Pass in correct include paths.
        .clang_args(&[
            "-I",
            if target == "thumbv7em-none-eabihf" {
                "../../build/firmware"
            } else {
                "../../build/unix"
            },
        ])
        // Customize the standard types.
        .use_core()
        .ctypes_prefix("cty")
        .size_t_is_usize(true)
        // Tell cargo to invalidate the built crate whenever any of the
        // included header files change.
        .parse_callbacks(Box::new(bindgen::CargoCallbacks))
        .generate()
        .expect("Unable to generate Rust QSTR bindings")
        .write_to_file(PathBuf::from(out_path).join("qstr.rs"))
        .unwrap();
}

fn generate_micropython_bindings() {
    let out_path = env::var("OUT_DIR").unwrap();
    let target = env::var("TARGET").unwrap();

    // Tell cargo to invalidate the built crate whenever the header changes.
    println!("cargo:rerun-if-changed=micropython.h");

    let mut bindings = bindgen::Builder::default()
        .header("micropython.h")
        // obj
        .new_type_alias("mp_obj_t")
        .allowlist_type("mp_obj_type_t")
        .allowlist_type("mp_obj_base_t")
        .allowlist_function("mp_obj_new_int")
        .allowlist_function("mp_obj_new_int_from_ll")
        .allowlist_function("mp_obj_new_int_from_ull")
        .allowlist_function("mp_obj_new_bytes")
        .allowlist_function("mp_obj_new_str")
        .allowlist_function("mp_obj_get_int_maybe")
        .allowlist_function("mp_obj_is_true")
        .allowlist_function("mp_call_function_n_kw")
        .allowlist_function("trezor_obj_get_ll_checked")
        .allowlist_function("trezor_obj_get_ull_checked")
        // buffer
        .allowlist_function("mp_get_buffer")
        .allowlist_var("MP_BUFFER_READ")
        .allowlist_var("MP_BUFFER_WRITE")
        .allowlist_var("MP_BUFFER_RW")
        // dict
        .allowlist_type("mp_obj_dict_t")
        .allowlist_function("mp_obj_new_dict")
        .allowlist_function("mp_obj_dict_store")
        .allowlist_var("mp_type_dict")
        // fun
        .allowlist_type("mp_obj_fun_builtin_fixed_t")
        .allowlist_var("mp_type_fun_builtin_1")
        .allowlist_var("mp_type_fun_builtin_2")
        .allowlist_var("mp_type_fun_builtin_3")
        // gc
        .allowlist_function("gc_alloc")
        // iter
        .allowlist_type("mp_obj_iter_buf_t")
        .allowlist_function("mp_getiter")
        .allowlist_function("mp_iternext")
        // list
        .allowlist_type("mp_obj_list_t")
        .allowlist_function("mp_obj_new_list")
        .allowlist_function("mp_obj_list_append")
        .allowlist_var("mp_type_list")
        // map
        .allowlist_type("mp_map_elem_t")
        .allowlist_type("mp_map_lookup_kind_t")
        .allowlist_function("mp_map_init")
        .allowlist_function("mp_map_init_fixed_table")
        .allowlist_function("mp_map_lookup")
        // runtime
        .allowlist_function("mp_raise_ValueError")
        // typ
        .allowlist_var("mp_type_type");

    // Don't add impls that hinder safety guarantees.
    bindings = bindings.no_copy("_mp_map_t");

    // Pass in correct include paths and defines.
    if target == "thumbv7em-none-eabihf" {
        bindings = bindings.clang_args(&[
            "-I../firmware",
            "-I../trezorhal",
            "-I../../build/firmware",
            "-I../../vendor/micropython",
            "-I../../vendor/micropython/lib/stm32lib/STM32F4xx_HAL_Driver/Inc",
            "-I../../vendor/micropython/lib/stm32lib/CMSIS/STM32F4xx/Include",
            "-I../../vendor/micropython/lib/cmsis/inc",
            "-DTREZOR_MODEL=T",
            "-DSTM32F405xx",
            "-DUSE_HAL_DRIVER",
            "-DSTM32_HAL_H=<stm32f4xx.h>",
        ]);
        // Append gcc-arm-none-eabi's include path.
        let sysroot = Command::new("arm-none-eabi-gcc")
            .arg("-print-sysroot")
            .output()
            .expect("arm-none-eabi-gcc failed to execute");
        if !sysroot.status.success() {
            panic!("arm-none-eabi-gcc failed");
        }
        bindings = bindings.clang_arg(format!(
            "-I{}/include",
            String::from_utf8(sysroot.stdout)
                .expect("arm-none-eabi-gcc returned invalid output")
                .trim()
        ));
    } else {
        bindings = bindings.clang_args(&[
            "-I../unix",
            "-I../../build/unix",
            "-I../../vendor/micropython",
        ]);
    }

    bindings
        // Customize the standard types.
        .use_core()
        .ctypes_prefix("cty")
        .size_t_is_usize(true)
        // Tell cargo to invalidate the built crate whenever any of the
        // included header files change.
        .parse_callbacks(Box::new(bindgen::CargoCallbacks))
        // Write the bindings to a file in the OUR_DIR.
        .generate()
        .expect("Unable to generate Rust Micropython bindings")
        .write_to_file(PathBuf::from(out_path).join("micropython.rs"))
        .unwrap();
}

#[cfg(test)]
fn add_test_dependencies() {
    cc::Build::new()
        .object("../../build/unix/vendor/micropython/py/obj.o")
        .compile("micropython");
}
