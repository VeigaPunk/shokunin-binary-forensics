| mutant | class | line | function | leg(s) | edit | tree (base 7d380ce) | self-test | union |
|---|---|---|---|---|---|---|---|---|
| m001-cmp-strict_json-L77 | cmp | 77 | strict_json | C1_RECEIPTS,C1_REGISTRY,C1_VOTES | `in -> not in` | verdict-set | KILLED | KILLED |
| m002-cmp-base_readme-L144 | cmp | 144 | base_readme | C1_ONLY_C02 | `!= -> ==` | survived | KILLED | KILLED |
| m003-if-base_readme-L153 | if | 153 | base_readme | C1_ONLY_C02 | `negate BoolOp test` | message-only | KILLED | KILLED |
| m004-cmp-base_readme-L153 | cmp | 153 | base_readme | C1_ONLY_C02 | `== -> !=` | survived | KILLED | KILLED |
| m005-not-parse_sources-L162 | not | 162 | parse_sources | C1_SIDS,C1_SOURCES | `delete `not`` | verdict-set | KILLED | KILLED |
| m006-if-parse_sources-L165 | if | 165 | parse_sources | C1_SIDS,C1_SOURCES | `negate if test` | verdict-set | KILLED | KILLED |
| m007-cmp-parse_sources-L167 | cmp | 167 | parse_sources | C1_SIDS,C1_SOURCES | `== -> !=` | verdict-set | KILLED | KILLED |
| m008-cmp-parse_sources-L168 | cmp | 168 | parse_sources | C1_SIDS,C1_SOURCES | `in -> not in` | verdict-set | KILLED | KILLED |
| m009-not-check_registry-L182 | not | 182 | check_registry | C1_REGISTRY | `delete `not`` | verdict-set | KILLED | KILLED |
| m010-cmp-check_registry-L187 | cmp | 187 | check_registry | C1_REGISTRY | `!= -> ==` | verdict-set | KILLED | KILLED |
| m011-cmp-check_registry-L190 | cmp | 190 | check_registry | C1_REGISTRY | `!= -> ==` | survived | survived | SURVIVED |
| m012-cmp-na_reason_ok-L197 | cmp | 197 | na_reason_ok | C1_VOTES | `>= -> <` | verdict-set | KILLED | KILLED |
| m013-cmp-na_reason_ok-L197 | cmp | 197 | na_reason_ok | C1_VOTES | `is not -> is` | verdict-set | KILLED | KILLED |
| m014-not-check_votes-L203 | not | 203 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m015-not-check_votes-L211 | not | 211 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m016-not-check_votes-L214 | not | 214 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m017-if-check_votes-L214 | if | 214 | check_votes | C1_VOTES | `negate BoolOp test` | verdict-set | KILLED | KILLED |
| m018-cmp-check_votes-L214 | cmp | 214 | check_votes | C1_VOTES | `not in -> in` | verdict-set | KILLED | KILLED |
| m019-cmp-check_votes-L217 | cmp | 217 | check_votes | C1_VOTES | `in -> not in` | verdict-set | KILLED | KILLED |
| m020-cmp-check_votes-L220 | cmp | 220 | check_votes | C1_VOTES | `!= -> ==` | verdict-set | KILLED | KILLED |
| m021-cmp-check_votes-L222 | cmp | 222 | check_votes | C1_VOTES | `not in -> in` | verdict-set | KILLED | KILLED |
| m022-cmp-check_votes-L224 | cmp | 224 | check_votes | C1_VOTES | `!= -> ==` | verdict-set | KILLED | KILLED |
| m023-not-check_votes-L228 | not | 228 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m024-cmp-check_votes-L228 | cmp | 228 | check_votes | C1_VOTES | `>= -> <` | verdict-set | KILLED | KILLED |
| m025-cmp-check_votes-L232 | cmp | 232 | check_votes | C1_VOTES | `== -> !=` | verdict-set | KILLED | KILLED |
| m026-cmp-check_votes-L234 | cmp | 234 | check_votes | C1_VOTES | `!= -> ==` | verdict-set | KILLED | KILLED |
| m027-not-check_votes-L237 | not | 237 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m028-not-check_votes-L240 | not | 240 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m029-cmp-check_votes-L240 | cmp | 240 | check_votes | C1_VOTES | `== -> !=` | survived | survived | SURVIVED |
| m030-not-check_votes-L245 | not | 245 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m031-cmp-check_votes-L247 | cmp | 247 | check_votes | C1_VOTES | `in -> not in` | verdict-set | KILLED | KILLED |
| m032-not-check_votes-L252 | not | 252 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m033-not-check_votes-L254 | not | 254 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m034-if-check_votes-L257 | if | 257 | check_votes | C1_VOTES | `negate BoolOp test` | verdict-set | KILLED | KILLED |
| m035-cmp-check_votes-L257 | cmp | 257 | check_votes | C1_VOTES | `== -> !=` | verdict-set | KILLED | KILLED |
| m036-not-check_votes-L257 | not | 257 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m037-not-check_votes-L259 | not | 259 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m038-cmp-check_votes-L259 | cmp | 259 | check_votes | C1_VOTES | `== -> !=` | verdict-set | KILLED | KILLED |
| m039-cmp-check_votes-L262 | cmp | 262 | check_votes | C1_VOTES | `not in -> in` | verdict-set | KILLED | KILLED |
| m040-cmp-check_votes-L264 | cmp | 264 | check_votes | C1_VOTES | `not in -> in` | verdict-set | KILLED | KILLED |
| m041-if-check_votes-L266 | if | 266 | check_votes | C1_VOTES | `negate BoolOp test` | verdict-set | KILLED | KILLED |
| m042-cmp-check_votes-L266 | cmp | 266 | check_votes | C1_VOTES | `in -> not in` | verdict-set | KILLED | KILLED |
| m043-cmp-check_votes-L266 | cmp | 266 | check_votes | C1_VOTES | `in -> not in` | verdict-set | KILLED | KILLED |
| m044-cmp-check_votes-L271 | cmp | 271 | check_votes | C1_VOTES | `< -> >=` | verdict-set | KILLED | KILLED |
| m045-if-check_receipts-L280 | if | 280 | check_receipts | C1_RECEIPTS | `negate if test` | verdict-set | KILLED | KILLED |
| m046-cmp-check_receipts-L290 | cmp | 290 | check_receipts | C1_RECEIPTS | `!= -> ==` | verdict-set | KILLED | KILLED |
| m047-cmp-check_receipts-L292 | cmp | 292 | check_receipts | C1_RECEIPTS | `!= -> ==` | verdict-set | KILLED | KILLED |
| d-host | d-host | 295 | check_receipts | C1_RECEIPTS | `host allowlist sub-check removed (MutationR96 d-host)` | survived | survived | SURVIVED |
| m049-cmp-check_receipts-L295 | cmp | 295 | check_receipts | C1_RECEIPTS | `not in -> in` | verdict-set | KILLED | KILLED |
| m050-not-check_receipts-L298 | not | 298 | check_receipts | C1_RECEIPTS | `delete `not`` | verdict-set | KILLED | KILLED |
| m051-cmp-check_receipts-L301 | cmp | 301 | check_receipts | C1_RECEIPTS | `!= -> ==` | verdict-set | KILLED | KILLED |
| m052-cmp-check_receipts-L303 | cmp | 303 | check_receipts | C1_RECEIPTS | `in -> not in` | verdict-set | KILLED | KILLED |
| m053-cmp-check_receipts-L303 | cmp | 303 | check_receipts | C1_RECEIPTS | `in -> not in` | verdict-set | KILLED | KILLED |
| m054-not-check_receipts-L305 | not | 305 | check_receipts | C1_RECEIPTS | `delete `not`` | verdict-set | KILLED | KILLED |
| m055-not-check_receipts-L307 | not | 307 | check_receipts | C1_RECEIPTS | `delete `not`` | verdict-set | KILLED | KILLED |
| m056-cmp-check_sids-L328 | cmp | 328 | check_sids | C1_SIDS | `not in -> in` | verdict-set | KILLED | KILLED |
| m057-not-check_sids-L330 | not | 330 | check_sids | C1_SIDS | `delete `not`` | verdict-set | KILLED | KILLED |
| m058-if-check_sources-L341 | if | 341 | check_sources | C1_SOURCES | `negate BoolOp test` | verdict-set | KILLED | KILLED |
| m059-cmp-check_sources-L341 | cmp | 341 | check_sources | C1_SOURCES | `not in -> in` | survived | survived | SURVIVED |
| m060-cmp-check_sources-L345 | cmp | 345 | check_sources | C1_SOURCES | `in -> not in` | verdict-set | KILLED | KILLED |
| m061-cmp-check_sources-L345 | cmp | 345 | check_sources | C1_SOURCES | `< -> >=` | survived | survived | SURVIVED |
| m062-not-check_sources-L353 | not | 353 | check_sources | C1_SOURCES | `delete `not`` | message-only | KILLED | KILLED |
| m063-cmp-check_sources-L356 | cmp | 356 | check_sources | C1_SOURCES | `in -> not in` | message-only | KILLED | KILLED |
| m064-cmp-check_sources-L357 | cmp | 357 | check_sources | C1_SOURCES | `!= -> ==` | survived | survived | SURVIVED |
| m065-cmp-check_sources-L362 | cmp | 362 | check_sources | C1_SOURCES | `is -> is not` | message-only | KILLED | KILLED |
| m066-cmp-check_sources-L364 | cmp | 364 | check_sources | C1_SOURCES | `!= -> ==` | message-only | KILLED | KILLED |
| m067-not-check_sources-L368 | not | 368 | check_sources | C1_SOURCES | `delete `not`` | message-only | KILLED | KILLED |
| m068-cmp-check_sources-L371 | cmp | 371 | check_sources | C1_SOURCES | `!= -> ==` | message-only | KILLED | KILLED |
| m069-cmp-check_sources-L373 | cmp | 373 | check_sources | C1_SOURCES | `!= -> ==` | message-only | KILLED | KILLED |
| m070-cmp-check_sources-L375 | cmp | 375 | check_sources | C1_SOURCES | `!= -> ==` | message-only | KILLED | KILLED |
| m071-cmp-check_sources-L377 | cmp | 377 | check_sources | C1_SOURCES | `not in -> in` | message-only | KILLED | KILLED |
| m072-cmp-check_sources-L379 | cmp | 379 | check_sources | C1_SOURCES | `!= -> ==` | message-only | KILLED | KILLED |
| m073-cmp-check_sources-L380 | cmp | 380 | check_sources | C1_SOURCES | `!= -> ==` | verdict-set | KILLED | KILLED |
| m074-not-check_sources-L382 | not | 382 | check_sources | C1_SOURCES | `delete `not`` | verdict-set | KILLED | KILLED |
| m075-cmp-check_quotes-L386 | cmp | 386 | check_quotes | C1_QUOTES | `in -> not in` | verdict-set | KILLED | KILLED |
| m076-not-check_quotes-L387 | not | 387 | check_quotes | C1_QUOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m077-cmp-check_quotes-L392 | cmp | 392 | check_quotes | C1_QUOTES | `!= -> ==` | verdict-set | KILLED | KILLED |
| m078-cmp-check_quotes-L395 | cmp | 395 | check_quotes | C1_QUOTES | `not in -> in` | verdict-set | KILLED | KILLED |
| m079-if-check_embed_nonvacuous-L407 | if | 407 | check_embed_nonvacuous | C1_EMBED_NONVACUOUS | `negate BoolOp test` | survived | survived | SURVIVED |
| m080-not-check_embed_nonvacuous-L407 | not | 407 | check_embed_nonvacuous | C1_EMBED_NONVACUOUS | `delete `not`` | survived | KILLED | KILLED |
| m081-if-check_embed_nonvacuous-L411 | if | 411 | check_embed_nonvacuous | C1_EMBED_NONVACUOUS | `negate if test` | survived | KILLED | KILLED |
| m082-not-check_embed_nonvacuous-L413 | not | 413 | check_embed_nonvacuous | C1_EMBED_NONVACUOUS | `delete `not`` | verdict-set | KILLED | KILLED |
| m083-not-check_pycache-L422 | not | 422 | check_pycache | C1_PYCACHE | `delete `not`` | survived | KILLED | KILLED |
| m084-not-check_pycache-L426 | not | 426 | check_pycache | C1_PYCACHE | `delete `not`` | verdict-set | KILLED | KILLED |
| m085-if-check_admitted_union-L437 | if | 437 | check_admitted_union | C1_ADMITTED_UNION | `negate BoolOp test` | verdict-set | KILLED | KILLED |
| m086-cmp-check_admitted_union-L437 | cmp | 437 | check_admitted_union | C1_ADMITTED_UNION | `== -> !=` | verdict-set | KILLED | KILLED |
| m087-if-check_admitted_union-L443 | if | 443 | check_admitted_union | C1_ADMITTED_UNION | `negate if test` | survived | KILLED | KILLED |
| m088-if-check_admitted_union-L450 | if | 450 | check_admitted_union | C1_ADMITTED_UNION | `negate if test` | verdict-set | KILLED | KILLED |
| m089-cmp-check_admitted_union-L452 | cmp | 452 | check_admitted_union | C1_ADMITTED_UNION | `not in -> in` | verdict-set | KILLED | KILLED |
| m090-not-check_admitted_union-L455 | not | 455 | check_admitted_union | C1_ADMITTED_UNION | `delete `not`` | verdict-set | KILLED | KILLED |
| m091-cmp-evaluate-L465 | cmp | 465 | evaluate | C1_ROWS_TOTAL | `== -> !=` | verdict-set | KILLED | KILLED |
| m092-cmp-evaluate-L466 | cmp | 466 | evaluate | C1_ROWS_TOTAL | `== -> !=` | verdict-set | KILLED | KILLED |
| m093-cmp-evaluate-L467 | cmp | 467 | evaluate | C1_C02_HELD | `== -> !=` | verdict-set | KILLED | KILLED |
| m094-cmp-evaluate-L468 | cmp | 468 | evaluate | C1_C02_HELD | `== -> !=` | verdict-set | KILLED | KILLED |
| m095-cmp-evaluate-L470 | cmp | 470 | evaluate | C1_C02_CITES | `== -> !=` | verdict-set | KILLED | KILLED |
| m096-if-evaluate-L476 | if | 476 | evaluate | C1_ONLY_C02 | `negate if test` | survived | KILLED | KILLED |
| m097-if-evaluate-L478 | if | 478 | evaluate | C1_ONLY_C02 | `negate BoolOp test` | message-only | KILLED | KILLED |
| m098-cmp-evaluate-L478 | cmp | 478 | evaluate | C1_ONLY_C02 | `!= -> ==` | survived | KILLED | KILLED |
| m099-cmp-evaluate-L478 | cmp | 478 | evaluate | C1_ONLY_C02 | `!= -> ==` | message-only | KILLED | KILLED |
| m100-not-evaluate-L480 | not | 480 | evaluate | C1_ONLY_C02 | `delete `not`` | survived | KILLED | KILLED |
| m101-cmp-evaluate-L480 | cmp | 480 | evaluate | C1_ONLY_C02 | `is not -> is` | survived | KILLED | KILLED |
| m102-cmp-evaluate-L481 | cmp | 481 | evaluate | C1_ONLY_C02 | `!= -> ==` | verdict-set | KILLED | KILLED |
| m103-cmp-evaluate-L489 | cmp | 489 | evaluate | C1_ADMITTED | `== -> !=` | survived | KILLED | KILLED |
| m104-cmp-evaluate-L489 | cmp | 489 | evaluate | C1_ADMITTED | `< -> >=` | survived | KILLED | KILLED |
| m105-cmp-evaluate-L490 | cmp | 490 | evaluate | C1_ADMITTED | `== -> !=` | verdict-set | KILLED | KILLED |
| m106-if-evaluate-L506 | if | 506 | evaluate | C1_LINT | `negate if test` | verdict-set | KILLED | KILLED |
| m107-cmp-evaluate-L511 | cmp | 511 | evaluate | C1_LINT | `== -> !=` | verdict-set | KILLED | KILLED |
| m108-cmp-evaluate-L513 | cmp | 513 | evaluate | C1_EMBEDDED | `== -> !=` | survived | KILLED | KILLED |
| m109-cmp-evaluate-L513 | cmp | 513 | evaluate | C1_EMBEDDED | `== -> !=` | verdict-set | KILLED | KILLED |
| m110-cmp-evaluate-L514 | cmp | 514 | evaluate | C1_EMBEDDED | `in -> not in` | verdict-set | KILLED | KILLED |
| m111-not-evaluate-L515 | not | 515 | evaluate | C1_EMBEDDED | `delete `not`` | verdict-set | KILLED | KILLED |
| m112-if-evaluate-L534 | if | 534 | evaluate | C1_K_HELD_BACKED | `negate BoolOp test` | verdict-set | KILLED | KILLED |
| m113-cmp-evaluate-L534 | cmp | 534 | evaluate | C1_K_HELD_BACKED | `== -> !=` | verdict-set | KILLED | KILLED |
| m114-cmp-evaluate-L536 | cmp | 536 | evaluate | C1_K_HELD_BACKED | `== -> !=` | verdict-set | KILLED | KILLED |
| m115-if-_raw_line-L559 | if | 559 | _raw_line | C1_ONLY_C02 | `negate BoolOp test` | message-only | KILLED | KILLED |
| m116-cmp-_raw_line-L559 | cmp | 559 | _raw_line | C1_ONLY_C02 | `== -> !=` | message-only | KILLED | KILLED |
| m117-cmp-_raw_line-L559 | cmp | 559 | _raw_line | C1_ONLY_C02 | `== -> !=` | message-only | KILLED | KILLED |
