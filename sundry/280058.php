<?php

function slugify(string $input): string { 
    // همه را کوچک کن
    $str = strtolower($input);

    // حذف علائم نگارشی (به جز فاصله و حروف و اعداد)
    $str = preg_replace('/[^a-z0-9\s]/', '', $str);

    // حذف فاصله‌های اضافی
    $str = preg_replace('/\s+/', ' ', $str);

    // ادغام iran server (حتی اگر فاصله‌ها زیاد باشد)
    $str = preg_replace('/iran\s+server/', 'iranserver', $str);

    // حذف فاصله‌های ابتدا و انتها
    $str = trim($str);

    // جایگزینی فاصله با خط تیره
    $str = str_replace(' ', '-', $str);

    return $str;
}
