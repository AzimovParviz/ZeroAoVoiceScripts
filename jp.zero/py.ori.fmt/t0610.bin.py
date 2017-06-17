﻿from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0610.bin",                # FileName
        "t0610",                    # MapName
        "t0610",                    # Location
        0x006A,                     # MapIndex
        "ed7301",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 106, 0, 0, 0, 1],
    )

    BuildStringList((
        "t0610",                  # 0
        "bt0600",                 # 1
        "bt0600",                 # 2
        "bt0600",                 # 3
        "bt0600",                 # 4
        "bt0600",                 # 5
        "bt0600",                 # 6
        "bt0600",                 # 7
        "bt0600",                 # 8
    ))

    ATBonus("ATBonus_370", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_1BA3", 10,  7,   0,   7,   9,   6,   9)
    Sepith("Sepith_1B9B", 0,   17,  5,   0,   12,  10,  12)
    Sepith("Sepith_1B8B", 13,  0,   7,   14,  0,   4,   9)
    Sepith("Sepith_1B93", 7,   7,   0,   0,   9,   15,  9)

    MonsterBattlePostion("MonsterBattlePostion_3B0", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_434", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_438", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_43C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_440", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_444", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_448", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_44C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 8, 14, 180)

    # monster count: 16

    BattleInfo(
        "BattleInfo_450", 0x0000, 23, 6, 45, 6, 1, 40, 0, "bt0600", "Sepith_1BA3", 65, 35, 0, 0,
        (
            ("ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4C0", 0x0000, 23, 6, 45, 6, 1, 25, 0, "bt0600", "Sepith_1B9B", 65, 35, 0, 0,
        (
            ("ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            ("ms60800.dat", "ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5A0", 0x0000, 23, 6, 45, 6, 1, 50, 0, "bt0600", "Sepith_1B8B", 65, 35, 0, 0,
        (
            ("ms61701.dat", "ms61701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            ("ms61701.dat", "ms61701.dat", "ms61701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_530", 0x0000, 23, 6, 45, 6, 1, 25, 0, "bt0600", "Sepith_1B93", 65, 35, 0, 0,
        (
            ("ms65801.dat", "ms65801.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            ("ms65801.dat", "ms65801.dat", "ms65801.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_610", 0x0400, 23, 6, 45, 6, 1, 40, 0, "bt0600", "Sepith_1BA3", 65, 35, 0, 0,
        (
            ("ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_680", 0x0400, 23, 6, 45, 6, 1, 25, 0, "bt0600", "Sepith_1B9B", 65, 35, 0, 0,
        (
            ("ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            ("ms60800.dat", "ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_760", 0x0400, 23, 6, 45, 6, 1, 50, 0, "bt0600", "Sepith_1B8B", 65, 35, 0, 0,
        (
            ("ms61701.dat", "ms61701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            ("ms61701.dat", "ms61701.dat", "ms61701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6F0", 0x0400, 23, 6, 45, 6, 1, 25, 0, "bt0600", "Sepith_1B93", 65, 35, 0, 0,
        (
            ("ms65801.dat", "ms65801.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            ("ms65801.dat", "ms65801.dat", "ms65801.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3D0", "MonsterBattlePostion_430", "ed7400", "ed7403", "ATBonus_370"),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch64850.itc",               # 10
        "monster/ch64851.itc",               # 11
        "monster/ch60850.itc",               # 12
        "monster/ch60850.itc",               # 13
        "monster/ch65850.itc",               # 14
        "monster/ch65851.itc",               # 15
        "monster/ch61750.itc",               # 16
        "monster/ch61750.itc",               # 17
    ))

    DeclMonster(12730,   15260,   50,      0x1010000,    "BattleInfo_450", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(45860,   30110,   7550,    0x1010000,    "BattleInfo_4C0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(83400,   26570,   10500,   0x1010000,    "BattleInfo_5A0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-94420,  25490,   50,      0x1010000,    "BattleInfo_530", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-73900,  25580,   -2950,   0x1010000,    "BattleInfo_450", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(60600,   23080,   1550,    0x1010000,    "BattleInfo_4C0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(37780,   6050,    1550,    0x1010000,    "BattleInfo_530", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(26470,   1850,    1550,    0x1010000,    "BattleInfo_5A0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(12730,   15260,   50,      0x1810000,    "BattleInfo_610", 1490, 16,  0xFFFF, 0,  1)
    DeclMonster(45860,   30110,   7550,    0x1810000,    "BattleInfo_680", 1491, 18,  0xFFFF, 2,  3)
    DeclMonster(83400,   26570,   10500,   0x1810000,    "BattleInfo_760", 1492, 22,  0xFFFF, 6,  7)
    DeclMonster(-94420,  25490,   50,      0x1810000,    "BattleInfo_6F0", 1493, 20,  0xFFFF, 4,  5)
    DeclMonster(-73900,  25580,   -2950,   0x1810000,    "BattleInfo_610", 1494, 16,  0xFFFF, 0,  1)
    DeclMonster(60600,   23080,   1550,    0x1810000,    "BattleInfo_680", 1495, 18,  0xFFFF, 2,  3)
    DeclMonster(37780,   6050,    1550,    0x1810000,    "BattleInfo_6F0", 1496, 20,  0xFFFF, 4,  5)
    DeclMonster(26470,   1850,    1550,    0x1810000,    "BattleInfo_760", 1497, 22,  0xFFFF, 6,  7)

    DeclActor(85540,   10500,   27550,   1200,    85540,   11500,   27550,   0x007C, 0,  3,  0x0000)
    DeclActor(25000,   1500,    -4000,   1200,    25000,   2500,    -4000,   0x007C, 0,  4,  0x0000)
    DeclActor(-88000,  50,      15000,   1200,    -88000,  1050,    15000,   0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_854",          # 00, 0
        "Function_1_933",          # 01, 1
        "Function_2_E14",          # 02, 2
        "Function_3_EDD",          # 03, 3
        "Function_4_FF7",          # 04, 4
        "Function_5_1144",         # 05, 5
        "Function_6_1241",         # 06, 6
        "Function_7_16B4",         # 07, 7
        "Function_8_1AEC",         # 08, 8
    ))


    def Function_0_854(): pass

    label("Function_0_854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_862")
    Jump("loc_932")

    label("loc_862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_932")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A7")
    ClearChrFlags(0x10, 0x80)

    label("loc_8A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B6")
    ClearChrFlags(0x11, 0x80)

    label("loc_8B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C5")
    ClearChrFlags(0x12, 0x80)

    label("loc_8C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D4")
    ClearChrFlags(0x13, 0x80)

    label("loc_8D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E3")
    ClearChrFlags(0x14, 0x80)

    label("loc_8E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F2")
    ClearChrFlags(0x15, 0x80)

    label("loc_8F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_901")
    ClearChrFlags(0x16, 0x80)

    label("loc_901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_910")
    ClearChrFlags(0x17, 0x80)

    label("loc_910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_932")
    Event(0, 6)

    label("loc_932")

    Return()

    # Function_0_854 end

    def Function_1_933(): pass

    label("Function_1_933")

    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D66")
    OP_70(0x0, 0x0)
    Jump("loc_D6A")

    label("loc_D66")

    OP_70(0x0, 0x1E)

    label("loc_D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7D")
    OP_70(0x1, 0x0)
    Jump("loc_D81")

    label("loc_D7D")

    OP_70(0x1, 0x1E)

    label("loc_D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D94")
    OP_70(0x2, 0x0)
    Jump("loc_D98")

    label("loc_D94")

    OP_70(0x2, 0x1E)

    label("loc_D98")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DB7")
    OP_1B(0x0, 0x0, 0x8)

    label("loc_DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E10")
    Event(0, 7)

    label("loc_E10")

    Call(0, 2)
    Return()

    # Function_1_933 end

    def Function_2_E14(): pass

    label("Function_2_E14")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E3A")
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0x14, 0x80)
    Jump("loc_E6F")

    label("loc_E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_E4D")
    ClearChrFlags(0xC, 0x8)
    Jump("loc_E6F")

    label("loc_E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E65")
    ClearChrFlags(0x14, 0x80)

    label("loc_E65")

    Jump("loc_E6F")

    label("loc_E6A")

    ClearChrFlags(0xC, 0x8)

    label("loc_E6F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EA7")
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x10, 0x80)
    Jump("loc_EDC")

    label("loc_EA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_EBA")
    ClearChrFlags(0x8, 0x8)
    Jump("loc_EDC")

    label("loc_EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_ED7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED2")
    ClearChrFlags(0x10, 0x80)

    label("loc_ED2")

    Jump("loc_EDC")

    label("loc_ED7")

    ClearChrFlags(0x8, 0x8)

    label("loc_EDC")

    Return()

    # Function_2_E14 end

    def Function_3_EDD(): pass

    label("Function_3_EDD")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC0")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x0, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 100)
    AddSepith(0x1, 100)
    AddSepith(0x2, 100)
    AddSepith(0x3, 100)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×１００\x01\x07\x02",

            "#57I水のセピス×１００\x01\x07\x02",

            "#58I火のセピス×１００\x01\x07\x02",

            "#59I風のセピス×１００\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x114, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_FE5")

    label("loc_FC0")


    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_FE5")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_EDD end

    def Function_4_FF7(): pass

    label("Function_4_FF7")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F3")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x6F, 1)"), scpexpr(EXPR_END)), "loc_107C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x114, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_10EE")

    label("loc_107C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x6F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x6F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_10EE")

    Jump("loc_1138")

    label("loc_10F3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1138")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_FF7 end

    def Function_5_1144(): pass

    label("Function_5_1144")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120A")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x2, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x4, 100)
    AddSepith(0x5, 100)
    AddSepith(0x6, 100)

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I時のセピス×１００\x01\x07\x02",

            "#61I空のセピス×１００\x01\x07\x02",

            "#62I幻のセピス×１００\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x114, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_122F")

    label("loc_120A")


    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_122F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1144 end

    def Function_6_1241(): pass

    label("Function_6_1241")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    OP_68(92500, 2400, 60350, 0)
    MoveCamera(38, 31, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(45700, 0)
    SetChrPos(0x101, 1810, 50, 2520, 45)
    SetChrPos(0x102, 2200, 50, 840, 45)
    SetChrPos(0x103, -170, 50, 1890, 45)
    SetChrPos(0x104, 500, 0, 290, 45)
    Sleep(500)
    SetCameraDistance(43630, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(70700, 1000, 38130, 0)
    MoveCamera(29, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(39380, 0)
    OP_68(31200, 1000, 7200, 7000)
    OP_0D()
    OP_6F(0x1)
    Fade(500)
    OP_68(18510, 1000, 20080, 0)
    MoveCamera(76, 33, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(28950, 0)
    OP_68(2520, 1000, 2740, 7000)
    OP_0D()
    OP_6F(0x1)
    Fade(500)
    OP_68(1370, 1000, 1460, 0)
    MoveCamera(86, 32, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21360, 0)
    OP_0D()

    #C0008
    ChrTalk(
        0x101,
        (
            "#5P#0001Fここがマインツ鉱山の廃坑か……\x02\x03",

            "#0005Fでも、廃坑にしては\x01",
            "あまり古い印象は受けないな。\x02\x03",

            "一応、導力灯も\x01",
            "整備されてるみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#11P#0100F時々魔獣が発生するそうだから、\x01",
            "その対策なんでしょう。\x02\x03",

            "見た感じ、資材置き場なんかには\x01",
            "まだ使われているみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x104,
        (
            "#12P#0300F薄暗くて雰囲気のある\x01",
            "場所じゃねぇか。\x02\x03",

            "#0304F肝試しには最適かもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#5P#0006Fのんきなことを\x01",
            "言ってるな……\x02\x03",

            "#0001F念の為言っとくけど、\x01",
            "仕事で来てるんだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        "#12P#0309Fへへ、分かってるって。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#6P#0203F……奥からかなりの数の\x01",
            "魔獣の気配を感じます。\x02\x03",

            "#0200Fかなり入り組んだ構造に\x01",
            "なっているようですし、\x01",
            "慎重に進むべきかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#5P#0001Fそうだな……\x01",
            "迷わないように気を付けよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -580, 0, -580, 45)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Sleep(500)
    OP_29(0x1C, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_6_1241 end

    def Function_7_16B4(): pass

    label("Function_7_16B4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(13580, 550, 13530, 0)
    MoveCamera(44, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22340, 0)
    SetChrPos(0x101, 12000, 50, 15200, 180)
    SetChrPos(0x102, 13300, 50, 15200, 180)
    SetChrPos(0x103, 12000, 50, 16500, 180)
    SetChrPos(0x104, 13300, 50, 16500, 180)
    SetCameraDistance(21340, 3000)

    def lambda_1742():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1742)

    def lambda_175C():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_175C)

    def lambda_1776():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1776)

    def lambda_1790():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1790)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_17C4():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17C4)

    def lambda_17D1():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17D1)

    def lambda_17DE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_17DE)

    def lambda_17EB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_17EB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0015
    ChrTalk(
        0x101,
        (
            "#6P#0000F……どうやらさっきの魔獣で\x01",
            "最後みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        (
            "#5P#0203Fええ、そのようです。\x02\x03",

            "#0200Fもう廃坑内には、\x01",
            "魔獣の気配を感じません。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        (
            "#11P#0306Fかぁ～、やっとかよ。\x02\x03",

            "この広い坑内を歩き回るのは\x01",
            "流石に骨が折れたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        (
            "#12P#0100Fふふ、お疲れさま。\x02\x03",

            "それじゃあロイド……\x01",
            "さっそく町長さんに\x01",
            "報告にいきましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#6P#0000Fああ、そうしようか。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x104,
        (
            "#11P#0306Fうー、もう歩きたくねー。\x02\x03",

            "#0309F……ロ～イド。\x01",
            "出口までおぶってくれよ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0021
    ChrTalk(
        0x101,
        (
            "#6P#0003Fお断りします。\x02\x03",

            "#0000Fふざけてないで\x01",
            "さっさと行くぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        "#11P#0306Fちぇー。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x1C, 0x1, 0x4)
    SetChrName("")
    SetMessageWindowPos(-1, 40, -1, -1)

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "自動で町長宅に戻りますか？\x07\x00",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【町長宅に戻る】\x01",      # 0
            "【やめる】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AD3")
    StopBGM(0xFA0)
    WaitBGM()
    NewScene("t0510", 0, 0, 0)
    IdleLoop()
    Jump("loc_1AEB")

    label("loc_1AD3")

    OP_1B(0x0, 0x0, 0x8)
    SetChrPos(0x0, 12000, 50, 15200, 180)
    EventEnd(0x5)

    label("loc_1AEB")

    Return()

    # Function_7_16B4 end

    def Function_8_1AEC(): pass

    label("Function_8_1AEC")

    EventBegin(0x1)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【町長宅に戻る】\x01",      # 0
            "【やめる】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B47")
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    NewScene("t0510", 0, 0, 0)
    IdleLoop()
    Jump("loc_1B5A")

    label("loc_1B47")

    SetChrPos(0x0, 1170, 50, 1170, 45)
    EventEnd(0x5)

    label("loc_1B5A")

    Return()

    # Function_8_1AEC end

    SaveToFile()

Try(main)
