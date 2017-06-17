﻿from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r3000.bin",                # FileName
        "r3000",                    # MapName
        "r3000",                    # Location
        0x0065,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -74000, 0, 0, 0, 0, 1, 101, 0, 1, 0, 2],
    )

    BuildStringList((
        "r3000",                  # 0
        "MapThread",              # 1
        "br3000",                 # 2
        "br3000",                 # 3
        "br3000",                 # 4
        "br3000",                 # 5
        "アルモリカ古道",         # 6
        "太陽の砦方面",           # 7
    ))

    ATBonus("ATBonus_380", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_1953", 8,   16,  0,   10,  5,   3,   0)
    Sepith("Sepith_195B", 0,   0,   6,   17,  6,   6,   6)
    Sepith("Sepith_1963", 10,  6,   2,   0,   8,   8,   8)
    Sepith("Sepith_196B", 7,   7,   7,   7,   7,   7,   7)

    MonsterBattlePostion("MonsterBattlePostion_3E0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_444", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_448", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_44C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_450", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_454", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_458", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 2, 13, 180)

    # monster count: 11

    BattleInfo(
        "BattleInfo_6B8", 0x0000, 25, 6, 60, 8, 1, 20, 0, "br3000", "Sepith_1953", 30, 40, 20, 10,
        (
            ("ms69500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3E0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
            ("ms69500.dat", "ms69500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
            ("ms69500.dat", "ms63400.dat", "ms69500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3E0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
            ("ms69500.dat", "ms64100.dat", "ms64100.dat", "ms64100.dat", 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
        )
    )

    BattleInfo(
        "BattleInfo_5F0", 0x0000, 25, 6, 60, 8, 1, 40, 0, "br3000", "Sepith_195B", 30, 40, 20, 10,
        (
            ("ms63400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3E0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
            ("ms63400.dat", "ms63400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
            ("ms63400.dat", "ms63400.dat", "ms63400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3E0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
            ("ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
        )
    )

    BattleInfo(
        "BattleInfo_528", 0x0000, 25, 6, 60, 8, 1, 10, 0, "br3000", "Sepith_1963", 30, 40, 20, 10,
        (
            ("ms63500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3E0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
            ("ms63500.dat", "ms63500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
            ("ms63500.dat", "ms63400.dat", "ms63500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3E0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
            ("ms63500.dat", "ms63500.dat", "ms63400.dat", "ms63500.dat", 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
        )
    )

    BattleInfo(
        "BattleInfo_460", 0x0000, 25, 6, 60, 8, 1, 40, 0, "br3000", "Sepith_196B", 30, 40, 20, 10,
        (
            ("ms66800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3E0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
            ("ms66800.dat", "ms66800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
            ("ms66800.dat", "ms69500.dat", "ms66800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3E0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
            ("ms66800.dat", "ms69500.dat", "ms66800.dat", "ms69500.dat", 0, 0, 0, 0, "MonsterBattlePostion_3C0", "MonsterBattlePostion_440", "ed7400", "ed7403", "ATBonus_380"),
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
        "monster/ch66850.itc",               # 10
        "monster/ch66851.itc",               # 11
        "monster/ch63550.itc",               # 12
        "monster/ch63550.itc",               # 13
        "monster/ch63450.itc",               # 14
        "monster/ch63450.itc",               # 15
        "monster/ch69550.itc",               # 16
        "monster/ch69550.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-48110,  -430,    0,       0x1010000,    "BattleInfo_6B8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-29990,  22710,   0,       0x1010000,    "BattleInfo_5F0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-20090,  26140,   0,       0x1010000,    "BattleInfo_528", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(8940,    -4260,   0,       0x1010000,    "BattleInfo_460", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(29230,   4880,    0,       0x1010000,    "BattleInfo_528", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(2630,    24090,   4000,    0x1010000,    "BattleInfo_5F0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-7500,   31850,   4000,    0x1010000,    "BattleInfo_6B8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(27140,   28810,   4000,    0x1010000,    "BattleInfo_460", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-23760,  -27800,  -2000,   0x1010000,    "BattleInfo_5F0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-14830,  -14300,  -3000,   0x1010000,    "BattleInfo_528", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4380,    -14740,  -2000,   0x1010000,    "BattleInfo_6B8", 0,   22,  0xFFFF, 6,  7)

    DeclActor(-23340,  100,     30500,   1200,    -23340,  1100,    30500,   0x007C, 0,  3,  0x0000)
    DeclActor(-830,    -3100,   -5690,   1200,    -830,    -2100,   -5690,   0x007C, 0,  4,  0x0000)
    DeclActor(34670,   2100,    23450,   1200,    34670,   3100,    23450,   0x007C, 0,  5,  0x0000)
    DeclActor(-4050,   4100,    34680,   1200,    -4050,   5100,    34680,   0x007C, 0,  6,  0x0000)
    DeclActor(-2350,   -2650,   -10000,  1200,    -2350,   -1650,   -10000,  0x007C, 0,  7,  0x0000)
    DeclActor(-21620,  -3000,   -14210,  1200,    -28130,  -4990,   -12180,  0x007C, 0,  9,  0x0000)

    PlaceName(-95.0, 0.0, -2.0, 0x0000, 0x0000, "アルモリカ古道")
    PlaceName(102.0, 0.0, -18.0, 0x0000, 0x0000, "太陽の砦方面")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_808",          # 00, 0
        "Function_1_8F3",          # 01, 1
        "Function_2_912",          # 02, 2
        "Function_3_D93",          # 03, 3
        "Function_4_EE0",          # 04, 4
        "Function_5_102D",         # 05, 5
        "Function_6_117A",         # 06, 6
        "Function_7_12C7",         # 07, 7
        "Function_8_1414",         # 08, 8
        "Function_9_1857",         # 09, 9
    ))


    def Function_0_808(): pass

    label("Function_0_808")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_886")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_838")
    Sleep(20000)
    Jump("loc_83B")

    label("loc_838")

    Sleep(40000)

    label("loc_83B")

    SetScenarioFlags(0xBA, 1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0xBB8)
    Sleep(2000)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_8C6")

    label("loc_886")

    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)

    label("loc_8C6")

    Sound(131, 1, 100, 0)
    Sleep(10000)
    Sleep(10000)
    Sleep(10000)
    Sleep(10000)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0xBB8)
    StopEffect(0x0, 0x2)
    Sleep(1000)
    OP_24(0x83)
    ClearScenarioFlags(0xBA, 1)
    Jump("Function_0_808")

    label("loc_8F2")

    Return()

    # Function_0_808 end

    def Function_1_8F3(): pass

    label("Function_1_8F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_911")
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_911")

    Return()

    # Function_1_8F3 end

    def Function_2_912(): pass

    label("Function_2_912")

    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC1")
    OP_70(0x0, 0x0)
    Jump("loc_CC5")

    label("loc_CC1")

    OP_70(0x0, 0x1E)

    label("loc_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD8")
    OP_70(0x1, 0x0)
    Jump("loc_CDC")

    label("loc_CD8")

    OP_70(0x1, 0x1E)

    label("loc_CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEF")
    OP_70(0x2, 0x0)
    Jump("loc_CF3")

    label("loc_CEF")

    OP_70(0x2, 0x1E)

    label("loc_CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D06")
    OP_70(0x3, 0x0)
    Jump("loc_D0A")

    label("loc_D06")

    OP_70(0x3, 0x1E)

    label("loc_D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1D")
    OP_70(0x4, 0x0)
    Jump("loc_D21")

    label("loc_D1D")

    OP_70(0x4, 0x1E)

    label("loc_D21")

    LoadEffect(0x0, "map/mpr3000.eff")
    BeginChrThread(0x8, 0, 0, 0)
    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -28130, -4990, -12180, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D92")
    OP_16(0x3, 0x1, 0x1, 0x0)

    label("loc_D92")

    Return()

    # Function_2_912 end

    def Function_3_D93(): pass

    label("Function_3_D93")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8F")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_E18")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x106, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_E8A")

    label("loc_E18")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E8A")

    Jump("loc_ED4")

    label("loc_E8F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
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

    label("loc_ED4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_D93 end

    def Function_4_EE0(): pass

    label("Function_4_EE0")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDC")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x78, 1)"), scpexpr(EXPR_END)), "loc_F65")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x78),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x106, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_FD7")

    label("loc_F65")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x78),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x78),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_FD7")

    Jump("loc_1021")

    label("loc_FDC")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_1021")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_EE0 end

    def Function_5_102D(): pass

    label("Function_5_102D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1129")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x38E, 1)"), scpexpr(EXPR_END)), "loc_10B2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x106, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_1124")

    label("loc_10B2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1124")

    Jump("loc_116E")

    label("loc_1129")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
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

    label("loc_116E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_102D end

    def Function_6_117A(): pass

    label("Function_6_117A")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1276")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_11FF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x106, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_1271")

    label("loc_11FF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1271")

    Jump("loc_12BB")

    label("loc_1276")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0012
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

    label("loc_12BB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_117A end

    def Function_7_12C7(): pass

    label("Function_7_12C7")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x106, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C3")
    Sound(14, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_134C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x106, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_13BE")

    label("loc_134C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_13BE")

    Jump("loc_1408")

    label("loc_13C3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0015
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

    label("loc_1408")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_12C7 end

    def Function_8_1414(): pass

    label("Function_8_1414")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_E0(0x1)
    StopEffect(0x8, 0x2)
    OP_68(-76840, 600, 2200, 0)
    MoveCamera(50, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20290, 0)
    SetChrPos(0x101, -77000, 0, 1250, 90)
    SetChrPos(0x102, -77500, 0, 2250, 90)
    SetChrPos(0x103, -78500, 0, 250, 90)
    SetChrPos(0x104, -79250, 0, 1250, 90)

    def lambda_14A1():
        OP_97(0xFE, 0x1770, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14A1)
    Sleep(50)

    def lambda_14BE():
        OP_97(0xFE, 0x1770, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14BE)
    Sleep(50)

    def lambda_14DB():
        OP_97(0xFE, 0x1770, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14DB)
    Sleep(50)

    def lambda_14F8():
        OP_97(0xFE, 0x1770, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14F8)
    OP_68(-70840, 600, 2200, 3000)
    FadeToBright(1000, 0)
    Sleep(2500)
    Fade(500)
    OP_68(-43580, 600, 10100, 0)
    MoveCamera(56, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(30240, 0)
    OP_68(-19260, 600, -26750, 10000)
    Sleep(9500)
    Fade(500)
    OP_68(-14980, 600, -4990, 0)
    MoveCamera(62, 28, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(91000, 0)
    SetCameraDistance(101750, 6000)
    OP_0D()
    PlaceName2(340, 200, "c_plac27", 0x0, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(-72110, 1200, 220, 0)
    MoveCamera(42, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15470, 0)
    OP_0D()

    #C0016
    ChrTalk(
        0x101,
        (
            "#6P#0005Fここが古戦場か……\x01",
            "遺跡らしきものが沢山あるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        (
            "#6P#0303F古戦場って言うくらいだ、\x01",
            "それこそ何か出てもおかしくねぇな。\x02\x03",

            "#0302Fそれこそ、敗残兵の霊とかが\x01",
            "現れたりしてな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x102, 0x104, 750)

    #C0018
    ChrTalk(
        0x102,
        "#5P#0105F……れ、霊っ？！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0019
    ChrTalk(
        0x103,
        "#12P#0205F……エリィさん？\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x2EE)

    #C0020
    ChrTalk(
        0x102,
        (
            "#5P#0113F……コホン。\x01",
            "な、なんでもないわ。\x02\x03",

            "#0108F……天気もかなり悪いし\x01",
            "魔獣も相当徘徊しているみたい。\x02\x03",

            "#0101F観光客が奥の方に\x01",
            "入り込んでしまっていたら……\x01",
            "あまり時間はなさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#6P#0013Fそうだな……\x01",
            "早速捜索を開始しよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -71000, 0, 250, 90)
    OP_29(0x1F, 0x1, 0x1)
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -28130, -4990, -12180, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_8_1414 end

    def Function_9_1857(): pass

    label("Function_9_1857")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0022
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(-27140, -2390, -13620, 1500)
    MoveCamera(50, 34, 0, 1500)
    OP_6E(470, 1500)
    SetCameraDistance(25000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣りをしますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "釣りをする\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1926")
    OP_E0(0x2)
    MiniGame(0x6, 0x18, 0xFFFFAF38, 0xFFFFF448, 0xFFFFC630, 0x113, 0xFFFF921E, 0xFFFFEC82, 0xFFFFD06C)

    label("loc_1926")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_9_1857 end

    SaveToFile()

Try(main)
