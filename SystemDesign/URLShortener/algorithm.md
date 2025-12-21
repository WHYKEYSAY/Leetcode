# Algorithm: URL Shortener (Base62 Encoding)

This implementation uses a **Bijective Function** approach to map a unique Integer ID to a short string.

## Core Concept
1.  **Database ID**: Every URL stored in the system is assigned an auto-incrementing integer ID (primary key).
2.  **Base Conversion**: Convert that base-10 integer ID into a base-62 number.
    *   **Base62 Alphabet**: `0-9` (10 chars), `a-z` (26 chars), `A-Z` (26 chars). Total = 62.

## Steps

### Encoding (Long URL -> Short URL)
1.  Check if `LongURL` is already in the database.
2.  If yes, return existing ID.
3.  If no, assign a new valid ID (e.g., `100`).
4.  Convert `100` to Base62.
    *   Example: `100` -> `1C` (in Base62).
5.  Return `http://tinyurl.com/1C`.

### Decoding (Short URL -> Long URL)
1.  Extract the key from the short URL (e.g., `1C`).
2.  Convert `1C` from Base62 back to Base10 ID.
    *   `1 * 62^1 + C(38) * 62^0` = `62 + 38` = `100`.
3.  Look up ID `100` in the database and return the associated Long URL.

## Complexity
*   **Time Complexity**: 
    *   Encode: O(1) - The number of digits in the short URL is very small (e.g., 7 characters allows 3.5 trillion URLs).
    *   Decode: O(1).
*   **Space Complexity**: O(N) where N is the number of URLs encoded, to store the mapping.

## Why Base62?
*   It's URL-safe (no special characters like `+` or `/` used in Base64).
*   It's compact. A split of just 6 characters gives `62^6` ≈ 56.8 billion combinations.
