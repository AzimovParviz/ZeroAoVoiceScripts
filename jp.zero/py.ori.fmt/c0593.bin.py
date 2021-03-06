﻿from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0593.bin",                # FileName
        "c0593",                    # MapName
        "c0593",                    # Location
        0x0029,                     # MapIndex
        "ed7122",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0593",                  # 0
        "ボス１",                 # 1
        "ボス２",                 # 2
        "ボス３",                 # 3
        "ボス４",                 # 4
        "ボス５",                 # 5
        "ボス６",                 # 6
        "ボス７",                 # 7
        "ボス８",                 # 8
        "MapThread",              # 9
        "bc0520",                 # 10
        "bc0520",                 # 11
        "bc0520",                 # 12
        "bc0530",                 # 13
    ))

    ATBonus("ATBonus_30C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_1B27", 9,   9,   9,   9,   19,  0,   0)
    Sepith("Sepith_1B2F", 9,   9,   9,   9,   0,   19,  0)
    Sepith("Sepith_1B37", 9,   9,   9,   9,   0,   0,   19)

    MonsterBattlePostion("MonsterBattlePostion_36C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_378", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_37C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 9, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 8, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 5, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 11, 13, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_40C", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0520", "Sepith_1B27", 40, 30, 20, 10,
        (
            ("ms67600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_36C", "MonsterBattlePostion_3CC", "ed7400", "ed7403", "ATBonus_30C"),
            ("ms67600.dat", "ms67600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_36C", "MonsterBattlePostion_3CC", "ed7400", "ed7403", "ATBonus_30C"),
            ("ms67600.dat", "ms67900.dat", "ms67600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_36C", "MonsterBattlePostion_3CC", "ed7400", "ed7403", "ATBonus_30C"),
            ("ms67600.dat", "ms67600.dat", "ms67900.dat", "ms67600.dat", 0, 0, 0, 0, "MonsterBattlePostion_36C", "MonsterBattlePostion_3CC", "ed7400", "ed7403", "ATBonus_30C"),
        )
    )

    BattleInfo(
        "BattleInfo_4D4", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0520", "Sepith_1B2F", 40, 30, 20, 10,
        (
            ("ms67700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_36C", "MonsterBattlePostion_3CC", "ed7400", "ed7403", "ATBonus_30C"),
            ("ms67700.dat", "ms67700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_36C", "MonsterBattlePostion_3CC", "ed7400", "ed7403", "ATBonus_30C"),
            ("ms67700.dat", "ms67900.dat", "ms67700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_36C", "MonsterBattlePostion_3CC", "ed7400", "ed7403", "ATBonus_30C"),
            ("ms67700.dat", "ms67700.dat", "ms67900.dat", "ms67700.dat", 0, 0, 0, 0, "MonsterBattlePostion_36C", "MonsterBattlePostion_3CC", "ed7400", "ed7403", "ATBonus_30C"),
        )
    )

    BattleInfo(
        "BattleInfo_59C", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0520", "Sepith_1B37", 40, 30, 20, 10,
        (
            ("ms67800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_36C", "MonsterBattlePostion_3CC", "ed7400", "ed7403", "ATBonus_30C"),
            ("ms67800.dat", "ms67800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_36C", "MonsterBattlePostion_3CC", "ed7400", "ed7403", "ATBonus_30C"),
            ("ms67800.dat", "ms67900.dat", "ms67800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_36C", "MonsterBattlePostion_3CC", "ed7400", "ed7403", "ATBonus_30C"),
            ("ms67800.dat", "ms67800.dat", "ms67900.dat", "ms67800.dat", 0, 0, 0, 0, "MonsterBattlePostion_36C", "MonsterBattlePostion_3CC", "ed7400", "ed7403", "ATBonus_30C"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_664", 0x0002, 33, 6, 45, 0, 1, 0, 0, "bc0530", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67600.dat", "ms67600.dat", "ms67700.dat", "ms67700.dat", "ms67800.dat", "ms67800.dat", "ms67900.dat", "ms67900.dat", "MonsterBattlePostion_3EC", "MonsterBattlePostion_3CC", "ed7401", "ed7403", "ATBonus_30C"),
            (),
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
        "monster/ch67650.itc",               # 10
        "monster/ch67650.itc",               # 11
        "monster/ch67750.itc",               # 12
        "monster/ch67750.itc",               # 13
        "monster/ch67850.itc",               # 14
        "monster/ch67850.itc",               # 15
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-16720,  -13400,  0,       0x1010000,    "BattleInfo_40C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-2590,   -28620,  0,       0x1010000,    "BattleInfo_4D4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-28520,  -24620,  30,      0x1010000,    "BattleInfo_59C", 0,   20,  0xFFFF, 4,  5)

    DeclActor(-22000,  0,       -4000,   1200,    -22000,  1000,    -4000,   0x007C, 0,  6,  0x0000)
    DeclActor(0,       0,       69500,   1200,    0,       1500,    69800,   0x007C, 0,  11, 0x0000)
    DeclActor(-1000,   0,       -8750,   1200,    -1000,   1000,    -8750,   0x007C, 0,  8,  0x0000)
    DeclActor(-26000,  0,       5000,    1200,    -26000,  1000,    5000,    0x007C, 0,  9,  0x0000)
    DeclActor(-18000,  0,       5000,    1200,    -18000,  1500,    5000,    0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5

    ScpFunction((
        "Function_0_720",          # 00, 0
        "Function_1_73C",          # 01, 1
        "Function_2_759",          # 02, 2
        "Function_3_784",          # 03, 3
        "Function_4_79F",          # 04, 4
        "Function_5_BC0",          # 05, 5
        "Function_6_C10",          # 06, 6
        "Function_7_D5D",          # 07, 7
        "Function_8_E68",          # 08, 8
        "Function_9_106E",         # 09, 9
        "Function_10_1274",        # 0A, 10
        "Function_11_1744",        # 0B, 11
    ))


    def Function_0_720(): pass

    label("Function_0_720")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_73B")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_720")

    label("loc_73B")

    Return()

    # Function_0_720 end

    def Function_1_73C(): pass

    label("Function_1_73C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_758")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_73C")

    label("loc_758")

    Return()

    # Function_1_73C end

    def Function_2_759(): pass

    label("Function_2_759")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_783")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_77B")
    Sound(154, 0, 100, 0)
    Sleep(900)
    Jump("loc_77E")

    label("loc_77B")

    Sleep(30)

    label("loc_77E")

    Jump("Function_2_759")

    label("loc_783")

    Return()

    # Function_2_759 end

    def Function_3_784(): pass

    label("Function_3_784")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79E")
    Event(0, 10)

    label("loc_79E")

    Return()

    # Function_3_784 end

    def Function_4_79F(): pass

    label("Function_4_79F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_7BB")
    OP_65(0x1, 0x1)
    SetMapObjFrame(0xFF, "key_red", 0x0, 0x1)

    label("loc_7BB")

    ClearScenarioFlags(0x0, 0)
    BeginChrThread(0x10, 0, 0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 0)), scpexpr(EXPR_END)), "loc_82F")
    SetMapObjFrame(0xFF, "lgt1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lgt1a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    Jump("loc_88C")

    label("loc_82F")

    SetMapObjFrame(0xFF, "lgt1_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "lgt1a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x1, 0x1)

    label("loc_88C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 1)), scpexpr(EXPR_END)), "loc_8F7")
    SetMapObjFrame(0xFF, "lgt2_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lgt2a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari10_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari12_add", 0x0, 0x1)
    Jump("loc_954")

    label("loc_8F7")

    SetMapObjFrame(0xFF, "lgt2_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "lgt2a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari11_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari12_add", 0x1, 0x1)

    label("loc_954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96C")
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_995")

    label("loc_96C")

    ClearMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_995")
    SetScenarioFlags(0x0, 0)

    label("loc_995")

    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB8")
    OP_70(0x0, 0x0)
    Jump("loc_BBC")

    label("loc_BB8")

    OP_70(0x0, 0x1E)

    label("loc_BBC")

    Call(0, 5)
    Return()

    # Function_4_79F end

    def Function_5_BC0(): pass

    label("Function_5_BC0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BFA")
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    SetMapObjFlags(0x0, 0x4)
    Jump("loc_C0F")

    label("loc_BFA")

    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x13, 0x8)
    ClearMapObjFlags(0x0, 0x4)

    label("loc_C0F")

    Return()

    # Function_5_BC0 end

    def Function_6_C10(): pass

    label("Function_6_C10")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0C")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_C95")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
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
    SetScenarioFlags(0x112, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_D07")

    label("loc_C95")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
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
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D07")

    Jump("loc_D51")

    label("loc_D0C")

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

    label("loc_D51")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_C10 end

    def Function_7_D5D(): pass

    label("Function_7_D5D")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4A")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x2, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x2, 0x0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x2)
    OP_71(0x2, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x2, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_E4A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E66")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_E66")

    Return()

    # Function_7_D5D end

    def Function_8_E68(): pass

    label("Function_8_E68")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 0)), scpexpr(EXPR_END)), "loc_EB1")
    TalkBegin(0xFF)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでにスイッチは切られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_106D")

    label("loc_EB1")

    EventBegin(0x1)

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "スイッチがある。\x01",
            "操作しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1066")
    Fade(500)
    SetChrPos(0x0, -2050, 0, -8860, 89)
    SetChrPos(0x1, -3300, 0, -8200, 89)
    SetChrPos(0x2, -3300, 0, -9750, 89)
    SetChrPos(0x3, -4450, 0, -9040, 89)
    OP_68(-2850, 500, -8580, 0)
    MoveCamera(45, 47, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "lgt1_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_68(-14130, 500, 5840, 0)
    MoveCamera(45, 31, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    SetScenarioFlags(0xD5, 0)
    Fade(500)
    Sound(161, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FF7")
    ClearScenarioFlags(0x0, 0)

    label("loc_FF7")

    SetMapObjFrame(0xFF, "lgt1a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1060")
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_1066")

    label("loc_1060")

    ClearMapObjFlags(0x1, 0x10)

    label("loc_1066")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_106D")

    Return()

    # Function_8_E68 end

    def Function_9_106E(): pass

    label("Function_9_106E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 1)), scpexpr(EXPR_END)), "loc_10B7")
    TalkBegin(0xFF)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでにスイッチは切られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_1273")

    label("loc_10B7")

    EventBegin(0x1)

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "スイッチがある。\x01",
            "操作しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126C")
    Fade(500)
    SetChrPos(0x0, -26040, 0, 3950, 0)
    SetChrPos(0x1, -25380, 0, 2500, 0)
    SetChrPos(0x2, -27130, 0, 2500, 0)
    SetChrPos(0x3, -26280, 0, 1860, 0)
    OP_68(-26400, 500, 3350, 0)
    MoveCamera(45, 46, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "lgt2_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_68(-14130, 500, 5840, 0)
    MoveCamera(45, 31, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    SetScenarioFlags(0xD5, 1)
    Fade(500)
    Sound(161, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11FD")
    ClearScenarioFlags(0x0, 0)

    label("loc_11FD")

    SetMapObjFrame(0xFF, "lgt2a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari10_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari12_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1266")
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_126C")

    label("loc_1266")

    ClearMapObjFlags(0x1, 0x10)

    label("loc_126C")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_1273")

    Return()

    # Function_9_106E end

    def Function_10_1274(): pass

    label("Function_10_1274")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("monster/ch67950.itc", 0x1E)
    OP_68(0, 1000, 52000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x0, -600, 0, 49000, 0)
    SetChrPos(0x1, 600, 0, 49000, 0)
    SetChrPos(0x2, -600, 0, 47800, 0)
    SetChrPos(0x3, 600, 0, 47800, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)

    def lambda_133B():
        OP_98(0xFE, 0x0, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_133B)

    def lambda_1355():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1355)
    Sleep(50)

    def lambda_1369():
        OP_98(0xFE, 0x0, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1369)

    def lambda_1383():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_1383)
    Sleep(50)

    def lambda_1397():
        OP_98(0xFE, 0x0, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1397)

    def lambda_13B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_13B1)
    Sleep(50)

    def lambda_13C5():
        OP_98(0xFE, 0x0, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_13C5)

    def lambda_13DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_13DF)
    OP_68(0, 1000, 53500, 2500)
    FadeToBright(1000, 0)
    WaitChrThread(0x0, 1)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x1, 1)
    WaitChrThread(0x2, 1)
    WaitChrThread(0x3, 1)
    OP_6F(0x1)
    Fade(500)
    OP_68(0, 1000, 53500, 0)
    MoveCamera(0, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_68(0, 1000, 57500, 2000)
    MoveCamera(0, 23, 0, 2000)
    SetCameraDistance(19500, 2000)
    OP_0D()
    Sound(202, 0, 100, 0)
    SetChrPos(0x8, -1000, 0, 57500, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x9, 1000, 0, 57500, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0xA, -2400, 30, 59000, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xB, 2400, 30, 59000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xC, 0, 0, 59900, 180)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xD, 0, 0, 62300, 180)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xE, -2100, 30, 61700, 180)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xF, 2100, 30, 61700, 180)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)

    def lambda_15C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_15C6)

    def lambda_15D7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_15D7)
    Sleep(100)

    def lambda_15EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15EB)

    def lambda_15FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_15FC)
    Sleep(100)

    def lambda_1610():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1610)
    Sleep(100)

    def lambda_1624():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1624)

    def lambda_1635():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1635)
    Sleep(100)

    def lambda_1649():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1649)
    WaitChrThread(0xD, 2)
    OP_6F(0x79)
    Sleep(300)
    Battle("BattleInfo_664", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    OP_68(0, 500, 56000, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x0, 0, 0, 56000, 0)
    SetChrPos(0x1, 0, 0, 56000, 0)
    SetChrPos(0x2, 0, 0, 56000, 0)
    SetChrPos(0x3, 0, 0, 56000, 0)
    SetScenarioFlags(0xC5, 6)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_10_1274 end

    def Function_11_1744(): pass

    label("Function_11_1744")

    EventBegin(0x0)
    OP_E0(0x1)
    Fade(1000)
    OP_68(0, 700, 69500, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 0, 68500, 0)
    SetChrPos(0x102, -200, 0, 67300, 0)
    SetChrPos(0x103, -1300, 0, 67300, 0)
    SetChrPos(0x104, 900, 0, 67300, 0)
    SetChrPos(0x10A, -1300, 0, 68500, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    Fade(250)
    SetMapObjFrame(0xFF, "key_red", 0x0, 0x1)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x32E, 1)
    OP_29(0x4C, 0x1, 0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18CF")

    #C0010
    ChrTalk(
        0x101,
        (
            "#0000F#11Pずいぶん大きな鍵だけど\x01",
            "ひょっとして……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x103,
        (
            "#12P#0202Fええ、応接間のギミックを\x01",
            "解除するものでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AAD")

    label("loc_18CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1944")
    OP_29(0x4C, 0x1, 0x16)

    #C0012
    ChrTalk(
        0x101,
        "#0000F#11P２つ目の鍵か……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#12P#0202Fこれで応接間のギミックを\x01",
            "解除できそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AAD")

    label("loc_1944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A44")
    OP_29(0x4C, 0x1, 0x17)

    #C0014
    ChrTalk(
        0x101,
        (
            "#0000F#11Pまた似たような\x01",
            "鍵を見つけたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#12P#0100Fどこかで使う場所が\x01",
            "あるのかもしれないわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x10A,
        (
            "#6P#0603F──武器庫も一通り調べた。\x02\x03",

            "#0600Fいったん戻って\x01",
            "ルバーチェのビルをもう一度\x01",
            "調べてみるべきかもしれんな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AAD")

    label("loc_1A44")


    #C0017
    ChrTalk(
        0x101,
        (
            "#0005F#11Pずいぶん大きな鍵だけど\x01",
            "何に使うものなんだ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        "#12P#0101F一応、持っておきましょう。\x02",
    )

    CloseMessageWindow()

    label("loc_1AAD")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 68000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_65(0x1, 0x1)
    SetScenarioFlags(0xC5, 7)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_11_1744 end

    SaveToFile()

Try(main)
