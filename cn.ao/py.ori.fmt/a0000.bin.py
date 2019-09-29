﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "a0000.bin",                # FileName
        "a0000",                    # MapName
        "a0000",                    # Location
        0x0001,                     # MapIndex
        -1,
        0x00000000,                 # Flags
        ("a0000", "a0000_1", "a0000_2", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 45, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "a0000",                  # 0
        "Npl03",                  # 1
        "シャークマン",           # 2
        " ",                      # 3
        " ",                      # 4
        " ",                      # 5
        " ",                      # 6
        " ",                      # 7
        " ",                      # 8
        " ",                      # 9
        "bc1470",                 # 10
        "bm0113",                 # 11
        "br0000",                 # 12
        "br2000",                 # 13
        "br2000",                 # 14
        "br2000",                 # 15
        "br2000",                 # 16
        "br2000",                 # 17
        "bm2060",                 # 18
        "bm1070",                 # 19
        "bm9070",                 # 20
        "bm9099",                 # 21
        "bm9099",                 # 22
        "地名１",                 # 23
        "地名３",                 # 24
    ))

    ATBonus("ATBonus_24C", 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ATBonus("ATBonus_27C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_29C", 100, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ATBonus("ATBonus_25C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_28C", 100, 5, 0, 5, 0, 5, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0)

    Sepith("Sepith_8984", 100, 1,   2,   3,   70,  89,  99)

    MonsterBattlePostion("MonsterBattlePostion_2AC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_32C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_330", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_334", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_338", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_33C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_340", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_344", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_42C", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 14, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_44C", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 6, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_464", 9, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_468", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 0, 0, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_4AC", 0x0200, 100, 6, 45, 3, 0, 30, 0, "bc1470", "Sepith_8984", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7453", "ed7453", "ATBonus_24C"),
            (),
            (),
            (),
        )
    )

    # event battle count: 13

    BattleInfo(
        "BattleInfo_4F0", 0x0042, 50, 6, 0, 0, 1, 0, 0, "bm0113", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_32C", "ed7451", "ed7453", "ATBonus_27C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_534", 0x0000, 3, 6, 45, 3, 1, 30, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60001.dat", "ms60001.dat", "ms60001.dat", "ms60001.dat", "MonsterBattlePostion_44C", "MonsterBattlePostion_44C", "ed7453", "ed7453", "ATBonus_29C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_578", 0x0000, 3, 6, 45, 3, 3, 30, 0, "br2000", "Sepith_8984", 100, 0, 0, 0,
        (
            ("ms88300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_2AC", "ed7450", "ed7453", "ATBonus_29C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5BC", 0x0000, 3, 6, 45, 3, 3, 30, 0, "br2000", "Sepith_8984", 100, 0, 0, 0,
        (
            ("ms87000.dat", "ms87100.dat", "ms87200.dat", "ms87300.dat", "ms87400.dat", "ms87500.dat", 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7450", "ed7453", "ATBonus_29C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_600", 0x0000, 3, 6, 45, 3, 1, 30, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms00000.dat", "ms00100.dat", "ms00200.dat", "ms00300.dat", 0, 0, "ms86300.dat", 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7450", "ed7453", "ATBonus_25C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_688", 0x0000, 3, 6, 45, 3, 1, 30, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60001.dat", "ms60001.dat", "ms60001.dat", "ms60001.dat", "ms60001.dat", "ms60001.dat", "ms60001.dat", "ms60001.dat", "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7450", "ed7453", "ATBonus_24C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6CC", 0x0000, 3, 6, 45, 3, 1, 30, 0, "bm2060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03600.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, "ms86300.dat", 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7450", "ed7453", "ATBonus_24C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_710", 0x1052, 3, 6, 45, 3, 1, 30, 0, "bm1070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03500.dat", 0, 0, 0, 0, 0, "ms04200.dat", 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7450", "ed7453", "ATBonus_24C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_754", 0x0010, 3, 6, 45, 3, 1, 30, 0, "bm9070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03700.dat", 0, 0, 0, 0, 0, "ms80500.dat", 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7458", "ed7453", "ATBonus_24C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_798", 0x009A, 3, 6, 45, 3, 1, 30, 0, "bm9099", 0x00000000, 100, 0, 0, 0,
        (
            (0, 0, 0, 0, 0, "ms89000.dat", "ms86400.dat", 0, "MonsterBattlePostion_38C", "MonsterBattlePostion_38C", "ed7552", "ed7453", "ATBonus_28C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7DC", 0x009A, 3, 6, 45, 3, 1, 30, 0, "bm9099", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89100.dat", 0, 0, 0, 0, 0, "ms86500.dat", 0, "MonsterBattlePostion_3AC", "MonsterBattlePostion_3AC", "ed7459", "ed7459", "ATBonus_28C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_644", 0x0010, 3, 6, 45, 3, 1, 30, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, "ms60000.dat", 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7450", "ed7453", "ATBonus_25C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch20000.itc",                   # 00
        "chr/ch00100.itc",                   # 01
    ))

    DeclNpc(-4000,   2000,    0,       135,  261,  0x0, 0,   0,   0,   0,   14,  0,   18,  255,  0)
    DeclNpc(1830,    0,       3589,    135,  261,  0x0, 0,   0,   0,   0,   14,  0,   17,  255,  0)
    DeclNpc(0,       0,       0,       135,  328,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       135,  328,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       135,  328,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       135,  328,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       135,  328,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       135,  328,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(1000,    1000,    0,       135,  320,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(5210,    -29010,  0,       0x1010000,    "BattleInfo_4AC", 4,   0,   0xFFFF, 0,  1)

    DeclActor(2000,    0,       400000,  2000,    2000,    1000,    400000,  0x007C, 0,  5,  0x0000)
    DeclActor(2800,    0,       -10000,  2000,    2800,    1000,    -10000,  0x007C, 0,  2,  0x0000)
    DeclActor(10860,   0,       -18980,  2000,    10860,   2000,    -18980,  0x007C, 0,  3,  0x0000)

    PlaceName(10.0, 1.0, 2.0, 0x0000, 0x0000, "地名１")
    PlaceName(-10.0, 1.0, 2.0, 0x0000, 0x0000, "地名３")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 0
    ChipFrameInfo(5000, 0, [0, 1, 2, 3])                         # 1

    ScpFunction((
        "Function_0_920",          # 00, 0
        "Function_1_95E",          # 01, 1
        "Function_2_995",          # 02, 2
        "Function_3_9B3",          # 03, 3
        "Function_4_A88",          # 04, 4
        "Function_5_A9D",          # 05, 5
        "Function_6_1179",         # 06, 6
        "Function_7_1204",         # 07, 7
        "Function_8_1229",         # 08, 8
        "Function_9_1247",         # 09, 9
        "Function_10_33A5",        # 0A, 10
        "Function_11_36DC",        # 0B, 11
        "Function_12_3A22",        # 0C, 12
        "Function_13_3ACE",        # 0D, 13
        "Function_14_3B7E",        # 0E, 14
        "Function_15_3C2E",        # 0F, 15
        "Function_16_3C3F",        # 10, 16
        "Function_17_3C7E",        # 11, 17
        "Function_18_4003",        # 12, 18
        "Function_19_42AA",        # 13, 19
        "Function_20_42D2",        # 14, 20
        "Function_21_42E7",        # 15, 21
        "Function_22_4488",        # 16, 22
        "Function_23_448B",        # 17, 23
        "Function_24_448E",        # 18, 24
        "Function_25_45C4",        # 19, 25
        "Function_26_4701",        # 1A, 26
        "Function_27_4714",        # 1B, 27
        "Function_28_4E86",        # 1C, 28
        "Function_29_5542",        # 1D, 29
        "Function_30_5545",        # 1E, 30
        "Function_31_5548",        # 1F, 31
        "Function_32_554B",        # 20, 32
        "Function_33_554C",        # 21, 33
        "Function_34_554F",        # 22, 34
        "Function_35_5619",        # 23, 35
        "Function_36_56CC",        # 24, 36
        "Function_37_595E",        # 25, 37
        "Function_38_5CB4",        # 26, 38
        "Function_39_65AF",        # 27, 39
        "Function_40_6923",        # 28, 40
        "Function_41_6D13",        # 29, 41
        "Function_42_75D4",        # 2A, 42
        "Function_43_76A7",        # 2B, 43
        "Function_44_7975",        # 2C, 44
        "Function_45_7BAD",        # 2D, 45
        "Function_46_80DF",        # 2E, 46
        "Function_47_816D",        # 2F, 47
        "Function_48_8356",        # 30, 48
        "Function_49_837C",        # 31, 49
        "Function_50_84CB",        # 32, 50
        "Function_51_8579",        # 33, 51
        "Function_52_8627",        # 34, 52
        "Function_53_86D5",        # 35, 53
        "Function_54_8783",        # 36, 54
        "Function_55_8831",        # 37, 55
        "Function_56_88DF",        # 38, 56
        "Function_57_8918",        # 39, 57
    ))


    def Function_0_920(): pass

    label("Function_0_920")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_93E")
    ClearScenarioFlags(0x22, 1)
    Event(0, 4)
    Return()

    label("loc_93E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_951")
    Call(0, 5)
    SetScenarioFlags(0x20, 0)
    SetScenarioFlags(0x20, 3)

    label("loc_951")

    Event(0, 9)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFFFF0000), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_920 end

    def Function_1_95E(): pass

    label("Function_1_95E")

    OP_C3(0x0, 0x6, 0x3, 0xA, 0x0, 0x1, 11630, -1000, -18310, 5000, 3000, 0)
    LoadEffect(0x11, "eff\\\\trapdmg0.eff")
    Return()

    # Function_1_95E end

    def Function_2_995(): pass

    label("Function_2_995")


    #C0001
    ChrTalk(
        0x0,
        "ルックポイントテスト\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_2_995 end

    def Function_3_9B3(): pass

    label("Function_3_9B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_9D6")
    ClearScenarioFlags(0x2, 1)
    SetMapObjFrame(0xFF, "elevator", 0x2, "upret")
    Jump("loc_A84")

    label("loc_9D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_9FB")
    ClearScenarioFlags(0x2, 0)
    SetMapObjFrame(0xFF, "elevator", 0x2, "downret")
    Jump("loc_A84")

    label("loc_9FB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "エレベーターを上げる\x01",      # 0
            "エレベーターを下げる\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A54"),
        (1, "loc_A6B"),
        (SWITCH_DEFAULT, "loc_A84"),
    )


    label("loc_A54")

    SetMapObjFrame(0xFF, "elevator", 0x2, "up")
    SetScenarioFlags(0x2, 1)
    Jump("loc_A84")

    label("loc_A6B")

    SetMapObjFrame(0xFF, "elevator", 0x2, "down")
    SetScenarioFlags(0x2, 0)
    Jump("loc_A84")

    label("loc_A84")

    TalkEnd(0xFF)
    Return()

    # Function_3_9B3 end

    def Function_4_A88(): pass

    label("Function_4_A88")

    EventBegin(0x1)

    #C0002
    ChrTalk(
        0x0,
        "イベント\x02",
    )

    CloseMessageWindow()
    OP_B9(0x2)
    EventEnd(0x5)
    Return()

    # Function_4_A88 end

    def Function_5_A9D(): pass

    label("Function_5_A9D")

    ClearMapFlags(0x80)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_32(0x0, 0xFB, 0x0)
    OP_32(0x1, 0xFB, 0x0)
    OP_32(0x2, 0xFB, 0x0)
    OP_32(0x3, 0xFB, 0x0)
    OP_32(0x6, 0xFB, 0x0)
    OP_32(0x4, 0xFB, 0x0)
    OP_32(0x5, 0xFB, 0x0)
    OP_32(0x8, 0xFB, 0x0)
    OP_32(0x9, 0xFB, 0x0)
    AddMira(2000)
    AddSepith(0xFF, 100)
    AddItemNumber(0x3E8, 1)
    AddItemNumber(0x3E9, 1)
    AddItemNumber(0x3EA, 1)
    AddItemNumber(0x3ED, 1)
    AddItemNumber(0x1, 1)
    AddItemNumber(0x2, 1)
    AddItemNumber(0x3, 1)
    AddItemNumber(0x4, 1)
    AddItemNumber(0x5, 1)
    AddItemNumber(0x6, 1)
    AddItemNumber(0x7, 1)
    AddItemNumber(0x1F4, 10)
    AddItemNumber(0x1F5, 10)
    AddItemNumber(0x1F6, 10)
    AddItemNumber(0x1F8, 10)
    AddItemNumber(0x1F9, 10)
    AddItemNumber(0x1FB, 10)
    AddItemNumber(0x1FC, 10)
    AddItemNumber(0x20B, 10)
    AddItemNumber(0x32, 10)
    AddItemNumber(0x186, 10)
    AddItemNumber(0x187, 10)
    AddItemNumber(0x20D, 10)
    OP_42(0x0, 0x640, 0xFF)
    OP_42(0x1, 0x640, 0xFF)
    OP_42(0x2, 0x640, 0xFF)
    OP_42(0x3, 0x640, 0xFF)
    OP_42(0x8, 0x640, 0xFF)
    OP_42(0x9, 0x640, 0xFF)
    OP_42(0x7, 0x640, 0xFF)
    OP_42(0x6, 0x477, 0xFF)
    OP_42(0xA, 0x46F, 0xFF)
    OP_42(0x0, 0x5DC, 0xFF)
    OP_42(0x1, 0x5DC, 0xFF)
    OP_42(0x2, 0x5DC, 0xFF)
    OP_42(0x3, 0x5DC, 0xFF)
    OP_42(0x8, 0x5DC, 0xFF)
    OP_42(0x9, 0x5DC, 0xFF)
    OP_42(0x7, 0x5DC, 0xFF)
    OP_42(0x6, 0x478, 0xFF)
    OP_42(0x0, 0x3E8, 0xFF)
    OP_42(0x1, 0x3FC, 0xFF)
    OP_42(0x2, 0x410, 0xFF)
    OP_42(0x3, 0x424, 0xFF)
    OP_42(0x9, 0x451, 0xFF)
    OP_42(0x8, 0x44C, 0xFF)
    OP_42(0x7, 0x46A, 0xFF)
    OP_42(0x6, 0x474, 0xFF)
    AddCraft(0x0, 0x186)
    AddCraft(0x1, 0x186)
    AddCraft(0x0, 0x187)
    AddCraft(0x2, 0x187)
    AddCraft(0x0, 0x188)
    AddCraft(0x3, 0x188)
    AddCraft(0x1, 0x189)
    AddCraft(0x2, 0x189)
    AddCraft(0x1, 0x18A)
    AddCraft(0x3, 0x18A)
    AddCraft(0x2, 0x18B)
    AddCraft(0x3, 0x18B)
    AddCraft(0x0, 0x18C)
    AddCraft(0x8, 0x18C)
    AddCraft(0x0, 0x18D)
    AddCraft(0x4, 0x18D)
    AddCraft(0x1, 0x18E)
    AddCraft(0x8, 0x18E)
    AddCraft(0x1, 0x18F)
    AddCraft(0x4, 0x18F)
    AddCraft(0x2, 0x190)
    AddCraft(0x8, 0x190)
    AddCraft(0x2, 0x191)
    AddCraft(0x4, 0x191)
    AddCraft(0x3, 0x192)
    AddCraft(0x8, 0x192)
    AddCraft(0x3, 0x193)
    AddCraft(0x4, 0x193)
    AddCraft(0x8, 0x194)
    AddCraft(0x4, 0x194)
    AddCraft(0x0, 0x195)
    AddCraft(0x5, 0x195)
    AddCraft(0x0, 0x196)
    AddCraft(0x9, 0x196)
    AddCraft(0x0, 0x96)
    AddCraft(0x0, 0x97)
    AddCraft(0x0, 0x98)
    AddCraft(0x0, 0x99)
    AddCraft(0x0, 0x9A)
    AddCraft(0x0, 0x118)
    AddCraft(0x0, 0x119)
    AddCraft(0x0, 0x15E)
    AddCraft(0x0, 0x15F)
    AddCraft(0x0, 0x9B)
    AddCraft(0x0, 0x11A)
    AddCraft(0x0, 0x9F)
    AddCraft(0x1, 0xA0)
    AddCraft(0x1, 0xA1)
    AddCraft(0x1, 0xA2)
    AddCraft(0x1, 0xA3)
    AddCraft(0x1, 0xA4)
    AddCraft(0x1, 0x11D)
    AddCraft(0x1, 0x11E)
    AddCraft(0x1, 0x161)
    AddCraft(0x1, 0x162)
    AddCraft(0x1, 0xA5)
    AddCraft(0x1, 0x11F)
    AddCraft(0x2, 0xAA)
    AddCraft(0x2, 0xAB)
    AddCraft(0x2, 0xAC)
    AddCraft(0x2, 0xAD)
    AddCraft(0x2, 0xAE)
    AddCraft(0x2, 0x122)
    AddCraft(0x2, 0x123)
    AddCraft(0x2, 0x164)
    AddCraft(0x2, 0x165)
    AddCraft(0x2, 0xB1)
    AddCraft(0x2, 0x124)
    SetScenarioFlags(0x5A, 2)
    AddCraft(0x3, 0xB4)
    AddCraft(0x3, 0xB5)
    AddCraft(0x3, 0xB6)
    AddCraft(0x3, 0xB7)
    AddCraft(0x3, 0xB8)
    AddCraft(0x3, 0x127)
    AddCraft(0x3, 0x128)
    AddCraft(0x3, 0x167)
    AddCraft(0x3, 0x168)
    AddCraft(0x3, 0x129)
    AddCraft(0x4, 0xBE)
    AddCraft(0x4, 0xBF)
    AddCraft(0x4, 0xC0)
    AddCraft(0x4, 0x12C)
    AddCraft(0x4, 0x16A)
    AddCraft(0x4, 0x16B)
    AddCraft(0x4, 0xC1)
    AddCraft(0x4, 0xC2)
    AddCraft(0x4, 0x12D)
    AddCraft(0x5, 0xC8)
    AddCraft(0x5, 0xC9)
    AddCraft(0x5, 0xCA)
    AddCraft(0x5, 0xCB)
    AddCraft(0x5, 0x131)
    AddCraft(0x5, 0x16D)
    AddCraft(0x5, 0x16E)
    AddCraft(0x5, 0xCC)
    AddCraft(0x8, 0xE6)
    AddCraft(0x8, 0xE7)
    AddCraft(0x8, 0xE8)
    AddCraft(0x8, 0x140)
    AddCraft(0x8, 0x176)
    AddCraft(0x8, 0xE9)
    AddCraft(0x8, 0xEA)
    AddCraft(0x8, 0x141)
    AddCraft(0x8, 0x177)
    AddCraft(0x9, 0xF0)
    AddCraft(0x9, 0xF1)
    AddCraft(0x9, 0xF2)
    AddCraft(0x9, 0xF3)
    AddCraft(0x9, 0x145)
    AddCraft(0x9, 0x179)
    AddCraft(0x9, 0x17A)
    AddCraft(0x9, 0x146)
    AddCraft(0x7, 0xDC)
    AddCraft(0x7, 0xDD)
    AddCraft(0x7, 0xDE)
    AddCraft(0x7, 0xDF)
    AddCraft(0x7, 0xE0)
    AddCraft(0x7, 0x13B)
    AddCraft(0x7, 0x13C)
    AddCraft(0xA, 0xFA)
    AddCraft(0xA, 0xFB)
    AddCraft(0xA, 0xFC)
    AddCraft(0xA, 0xFD)
    AddCraft(0xA, 0x14A)
    AddCraft(0x6, 0xD2)
    AddCraft(0x6, 0xD3)
    AddCraft(0x6, 0xD4)
    AddCraft(0x6, 0x170)
    AddCraft(0x6, 0x171)
    SetChrChipPat(0x0, 0x6, 0x118)
    SetChrChipPat(0x1, 0x6, 0x11D)
    SetChrChipPat(0x2, 0x6, 0x122)
    SetChrChipPat(0x3, 0x6, 0x127)
    SetChrChipPat(0xA, 0x6, 0x14A)
    OP_38(0x0, 0x80, 0x2)
    OP_38(0x0, 0x81, 0x2)
    OP_38(0x0, 0x82, 0x2)
    OP_38(0x0, 0x83, 0x2)
    OP_38(0x0, 0x84, 0x2)
    OP_38(0x0, 0x85, 0x2)
    OP_38(0x0, 0x86, 0x2)
    OP_38(0x1, 0x80, 0x2)
    OP_38(0x1, 0x81, 0x2)
    OP_38(0x1, 0x82, 0x2)
    OP_38(0x1, 0x83, 0x2)
    OP_38(0x1, 0x84, 0x2)
    OP_38(0x2, 0x80, 0x2)
    OP_38(0x2, 0x81, 0x2)
    OP_38(0x2, 0x82, 0x2)
    OP_38(0x2, 0x83, 0x2)
    OP_38(0x2, 0x84, 0x2)
    OP_38(0x3, 0x80, 0x2)
    OP_38(0x3, 0x81, 0x2)
    OP_38(0x3, 0x82, 0x2)
    OP_38(0x3, 0x83, 0x2)
    OP_38(0x3, 0x84, 0x2)
    OP_38(0x3, 0x85, 0x2)
    OP_38(0x3, 0x86, 0x2)
    OP_38(0x6, 0x80, 0x2)
    OP_38(0x6, 0x81, 0x2)
    OP_38(0x6, 0x82, 0x2)
    OP_38(0x6, 0x83, 0x2)
    OP_38(0x6, 0x84, 0x2)
    OP_38(0x6, 0x85, 0x2)
    OP_38(0x6, 0x86, 0x2)
    AddItemNumber(0x6A, 1)
    AddItemNumber(0x6D, 1)
    AddItemNumber(0x70, 1)
    AddItemNumber(0x73, 1)
    AddItemNumber(0x76, 1)
    AddItemNumber(0x79, 1)
    AddItemNumber(0xDC, 1)
    AddItemNumber(0xDD, 1)
    AddItemNumber(0xDE, 1)
    AddItemNumber(0xDF, 1)
    AddItemNumber(0xE0, 1)
    AddItemNumber(0xE1, 1)
    AddItemNumber(0xE2, 1)
    AddItemNumber(0xE3, 1)
    AddItemNumber(0xE4, 1)
    AddItemNumber(0xE5, 1)
    AddItemNumber(0xE6, 1)
    AddItemNumber(0xE7, 1)
    AddItemNumber(0xE8, 1)
    AddItemNumber(0xE9, 1)
    AddItemNumber(0xEA, 1)
    AddItemNumber(0xEB, 1)
    AddItemNumber(0xEC, 1)
    AddItemNumber(0xED, 1)
    AddItemNumber(0xEE, 1)
    AddItemNumber(0xEF, 1)
    AddItemNumber(0xF0, 1)
    RemoveCraft(0x0, 0xA)
    RemoveCraft(0x0, 0xB)
    RemoveCraft(0x0, 0xC)
    RemoveCraft(0x0, 0xD)
    RemoveCraft(0x0, 0xE)
    RemoveCraft(0x0, 0xF)
    RemoveCraft(0x0, 0x11)
    RemoveCraft(0x0, 0x12)
    RemoveCraft(0x0, 0x13)
    RemoveCraft(0x0, 0x14)
    RemoveCraft(0x0, 0x15)
    RemoveCraft(0x0, 0x16)
    RemoveCraft(0x0, 0x17)
    RemoveCraft(0x0, 0x18)
    RemoveCraft(0x0, 0x19)
    RemoveCraft(0x0, 0x1A)
    RemoveCraft(0x0, 0x1B)
    RemoveCraft(0x0, 0x1C)
    RemoveCraft(0x0, 0x1D)
    RemoveCraft(0x0, 0x1E)
    RemoveCraft(0x0, 0x1F)
    RemoveCraft(0x0, 0x20)
    RemoveCraft(0x0, 0x21)
    RemoveCraft(0x0, 0x22)
    RemoveCraft(0x0, 0x23)
    RemoveCraft(0x0, 0x25)
    RemoveCraft(0x0, 0x26)
    RemoveCraft(0x0, 0x27)
    RemoveCraft(0x0, 0x28)
    RemoveCraft(0x0, 0x29)
    RemoveCraft(0x0, 0x2A)
    RemoveCraft(0x0, 0x2B)
    RemoveCraft(0x0, 0x2C)
    RemoveCraft(0x0, 0x2D)
    RemoveCraft(0x0, 0x2F)
    RemoveCraft(0x0, 0x30)
    RemoveCraft(0x0, 0x31)
    RemoveCraft(0x0, 0x32)
    RemoveCraft(0x0, 0x33)
    RemoveCraft(0x0, 0x34)
    RemoveCraft(0x0, 0x35)
    RemoveCraft(0x0, 0x36)
    RemoveCraft(0x0, 0x39)
    RemoveCraft(0x0, 0x3A)
    RemoveCraft(0x0, 0x3B)
    RemoveCraft(0x0, 0x3C)
    RemoveCraft(0x0, 0x3D)
    RemoveCraft(0x0, 0x3E)
    RemoveCraft(0x0, 0x3F)
    RemoveCraft(0x0, 0x40)
    RemoveCraft(0x0, 0x43)
    RemoveCraft(0x0, 0x44)
    RemoveCraft(0x0, 0x45)
    RemoveCraft(0x0, 0x46)
    RemoveCraft(0x0, 0x47)
    RemoveCraft(0x0, 0x48)
    RemoveCraft(0x0, 0x49)
    RemoveCraft(0x0, 0x4A)
    RemoveCraft(0x0, 0x4D)
    RemoveCraft(0x0, 0x4E)
    RemoveCraft(0x0, 0x4F)
    RemoveCraft(0x0, 0x50)
    RemoveCraft(0x0, 0x51)
    RemoveCraft(0x0, 0x52)
    RemoveCraft(0x0, 0x53)
    RemoveCraft(0x0, 0x58)
    RemoveCraft(0x0, 0x59)
    RemoveCraft(0x0, 0x5A)
    RemoveCraft(0x0, 0x60)
    RemoveCraft(0x0, 0x61)
    RemoveCraft(0x0, 0x62)
    RemoveCraft(0x0, 0x63)
    RemoveCraft(0x0, 0x64)
    RemoveCraft(0x0, 0x68)
    RemoveCraft(0x0, 0x69)
    RemoveCraft(0x0, 0x6A)
    RemoveCraft(0x0, 0x70)
    RemoveCraft(0x0, 0x71)
    RemoveCraft(0x0, 0x72)
    RemoveCraft(0x0, 0x73)
    RemoveCraft(0x0, 0x78)
    RemoveCraft(0x0, 0x79)
    RemoveCraft(0x0, 0x7A)
    RemoveCraft(0x0, 0x7B)
    RemoveCraft(0x0, 0x7C)
    RemoveCraft(0x0, 0x80)
    RemoveCraft(0x0, 0x81)
    RemoveCraft(0x0, 0x82)
    RemoveCraft(0x0, 0x83)
    RemoveCraft(0x0, 0x84)
    RemoveCraft(0x0, 0x85)
    RemoveCraft(0x0, 0x86)
    RemoveCraft(0x0, 0x87)
    RemoveCraft(0x1, 0xA)
    RemoveCraft(0x1, 0xB)
    RemoveCraft(0x1, 0xC)
    RemoveCraft(0x1, 0xD)
    RemoveCraft(0x1, 0xE)
    RemoveCraft(0x1, 0x14)
    RemoveCraft(0x1, 0x15)
    RemoveCraft(0x1, 0x16)
    RemoveCraft(0x1, 0x17)
    RemoveCraft(0x1, 0x18)
    RemoveCraft(0x1, 0x19)
    RemoveCraft(0x1, 0x1E)
    RemoveCraft(0x1, 0x1F)
    RemoveCraft(0x1, 0x20)
    RemoveCraft(0x1, 0x21)
    RemoveCraft(0x1, 0x22)
    RemoveCraft(0x1, 0x28)
    RemoveCraft(0x1, 0x29)
    RemoveCraft(0x1, 0x2A)
    RemoveCraft(0x1, 0x2B)
    RemoveCraft(0x1, 0x2C)
    RemoveCraft(0x1, 0x32)
    RemoveCraft(0x1, 0x33)
    RemoveCraft(0x1, 0x34)
    RemoveCraft(0x1, 0x3C)
    RemoveCraft(0x1, 0x48)
    RemoveCraft(0x1, 0x3E)
    RemoveCraft(0x1, 0x46)
    RemoveCraft(0x1, 0x50)
    RemoveCraft(0x1, 0x51)
    RemoveCraft(0x1, 0x52)
    RemoveCraft(0x1, 0x53)
    RemoveCraft(0x1, 0x58)
    RemoveCraft(0x1, 0x59)
    RemoveCraft(0x1, 0x5A)
    RemoveCraft(0x1, 0x60)
    RemoveCraft(0x1, 0x61)
    RemoveCraft(0x1, 0x62)
    RemoveCraft(0x1, 0x63)
    RemoveCraft(0x1, 0x64)
    RemoveCraft(0x1, 0x68)
    RemoveCraft(0x1, 0x69)
    RemoveCraft(0x1, 0x6A)
    RemoveCraft(0x1, 0x70)
    RemoveCraft(0x1, 0x71)
    RemoveCraft(0x1, 0x72)
    RemoveCraft(0x1, 0x78)
    RemoveCraft(0x1, 0x79)
    RemoveCraft(0x1, 0x7A)
    RemoveCraft(0x1, 0x73)
    RemoveCraft(0x1, 0x80)
    RemoveCraft(0x1, 0x81)
    RemoveCraft(0x1, 0x82)
    RemoveCraft(0x1, 0x83)
    RemoveCraft(0x1, 0x84)
    RemoveCraft(0x1, 0x85)
    RemoveCraft(0x2, 0x1E)
    RemoveCraft(0x2, 0x1F)
    RemoveCraft(0x2, 0x20)
    RemoveCraft(0x2, 0x21)
    RemoveCraft(0x3, 0x28)
    RemoveCraft(0x3, 0x29)
    RemoveCraft(0x3, 0x2A)
    RemoveCraft(0x3, 0x2B)
    Return()

    # Function_5_A9D end

    def Function_6_1179(): pass

    label("Function_6_1179")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1203")

    label("loc_1184")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11C5")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11BD")
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    Jump("loc_11C5")

    label("loc_11BD")

    Sleep(100)
    Jump("loc_1184")

    label("loc_11C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11FE")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F6")
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_70(0x5, 0x78)
    Jump("loc_11FE")

    label("loc_11F6")

    Sleep(1)
    Jump("loc_11C5")

    label("loc_11FE")

    Jump("Function_6_1179")

    label("loc_1203")

    Return()

    # Function_6_1179 end

    def Function_7_1204(): pass

    label("Function_7_1204")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1228")
    SetMapObjFrame(0x3, "motest06", 0x2, "play")
    Sleep(1000)
    Jump("Function_7_1204")

    label("loc_1228")

    Return()

    # Function_7_1204 end

    def Function_8_1229(): pass

    label("Function_8_1229")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1246")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    Jump("Function_8_1229")

    label("loc_1246")

    Return()

    # Function_8_1229 end

    def Function_9_1247(): pass

    label("Function_9_1247")

    SetMapFlags(0x80)

    #A0003
    AnonymousTalk(
        0x101,
        (
            "本#2R?#気#2R?#で#2R?#行#2R有#く#2R有#Ａ#2R有##2R有#。\x01",
            "012345678901234567890123456789012345678901234567890123456789\x01",
            "ううううう\x02",
        )
    )

    OP_60(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3399")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "マップ選択──━━\x01",        # 0
            "キャラ閲覧\x01",                # 1
            "戦闘テスト\x01",                # 2
            "ミニゲーム\x01",                # 3
            "ムービー\x01",                  # 4
            "クエスト関連テスト\x01",        # 5
            "徘徊テスト\x01",                # 6
            "お店テスト\x01",                # 7
            "クリアセーブメニュー\x01",      # 8
            "イベントジャンプ１\x01",        # 9
            "イベントジャンプ２\x01",        # 10
            "イベントジャンプ３\x01",        # 11
            "一般会話用フラグ管理\x01",      # 12
            "クエスト用フラグ管理\x01",      # 13
            "各種取得、リセット\x01",        # 14
            "テスト\x01",                    # 15
        )
    )

    MenuCmd(4, 0, 0x0)
    MenuEnd(0x0)
    MenuCmd(4, 0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1460"),
        (1, "loc_1468"),
        (2, "loc_1470"),
        (3, "loc_1478"),
        (4, "loc_1480"),
        (5, "loc_176A"),
        (6, "loc_1DB8"),
        (7, "loc_1DC6"),
        (8, "loc_1DD3"),
        (9, "loc_1DF3"),
        (10, "loc_1DFE"),
        (11, "loc_1E09"),
        (12, "loc_1E14"),
        (13, "loc_1E1C"),
        (14, "loc_1E24"),
        (15, "loc_1E2C"),
        (SWITCH_DEFAULT, "loc_338A"),
    )


    label("loc_1460")

    Call(1, 0)
    Jump("loc_3394")

    label("loc_1468")

    Call(0, 12)
    Jump("loc_3394")

    label("loc_1470")

    Call(0, 11)
    Jump("loc_3394")

    label("loc_1478")

    Call(0, 10)
    Jump("loc_3394")

    label("loc_1480")


    Menu(
        1,
        -1,
        -1,
        1,
        (
            "ed72_op  オープニング\x01",          # 0
            "ed72_01  列車のシーン\x01",          # 1
            "ed72_02  オルキスタワー\x01",        # 2
            "ed72_03a ＩＢＣ崩壊\x01",            # 3
            "ed72_03b ベイオウルフ号\x01",        # 4
            "ed72_04a 列車砲\x01",                # 5
            "ed72_05  キーアの儀式\x01",          # 6
            "ed72_06  アイオーン登場\x01",        # 7
            "ed72_04b アイオーン②\x01",          # 8
            "ed72_07a 《零の神域》出現\x01",      # 9
            "ed72_07b 《零の神域》突入\x01",      # 10
            "ed72_ed  エンディング \x01",         # 11
            "ed72_12  オルキスタワー\x01",        # 12
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x0)
    OP_60(0x1)
    Sleep(1000)
    OP_C9(0x0, 0x10)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_161C"),
        (1, "loc_1633"),
        (2, "loc_164A"),
        (3, "loc_1661"),
        (4, "loc_1679"),
        (5, "loc_1691"),
        (6, "loc_16A9"),
        (7, "loc_16C0"),
        (8, "loc_16D7"),
        (9, "loc_16EF"),
        (10, "loc_1707"),
        (11, "loc_171F"),
        (12, "loc_1736"),
        (SWITCH_DEFAULT, "loc_174D"),
    )


    label("loc_161C")

    PlayMovie(0x0, "ed72_op.pmf", 0x34, 0x0)
    Jump("loc_174D")

    label("loc_1633")

    PlayMovie(0x0, "ed72_01.pmf", 0x0, 0x0)
    Jump("loc_174D")

    label("loc_164A")

    PlayMovie(0x0, "ed72_02.pmf", 0x0, 0x0)
    Jump("loc_174D")

    label("loc_1661")

    PlayMovie(0x0, "ed72_03a.pmf", 0x0, 0x0)
    Jump("loc_174D")

    label("loc_1679")

    PlayMovie(0x0, "ed72_03b.pmf", 0x0, 0x0)
    Jump("loc_174D")

    label("loc_1691")

    PlayMovie(0x0, "ed72_04a.pmf", 0x0, 0x0)
    Jump("loc_174D")

    label("loc_16A9")

    PlayMovie(0x0, "ed72_05.pmf", 0x0, 0x0)
    Jump("loc_174D")

    label("loc_16C0")

    PlayMovie(0x0, "ed72_06.pmf", 0x0, 0x0)
    Jump("loc_174D")

    label("loc_16D7")

    PlayMovie(0x0, "ed72_04b.pmf", 0x0, 0x0)
    Jump("loc_174D")

    label("loc_16EF")

    PlayMovie(0x0, "ed72_07a.pmf", 0x0, 0x0)
    Jump("loc_174D")

    label("loc_1707")

    PlayMovie(0x0, "ed72_07b.pmf", 0x0, 0x0)
    Jump("loc_174D")

    label("loc_171F")

    PlayMovie(0x0, "ed72_ed.pmf", 0x0, 0x0)
    Jump("loc_174D")

    label("loc_1736")

    PlayMovie(0x0, "ed72_12.pmf", 0x0, 0x0)
    Jump("loc_174D")

    label("loc_174D")

    OP_57(0x3)
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_C9(0x1, 0x10)
    FadeToBright(10, 0)
    Jump("loc_3394")

    label("loc_176A")


    Menu(
        1,
        -1,
        -1,
        1,
        (
            "端末\x01",                                  # 0
            "報告\x01",                                  # 1
            "??? 序章メイン二つ     情報1登録\x01",      # 2
            "??? ジオフロントの探索      達成\x01",      # 3
            "??? 紛失物の捜索願い   情報1登録\x01",      # 4
            "??? 紛失物の捜索願い        達成\x01",      # 5
            "??  支援要請の補足説明 情報1登録\x01",      # 6
            "??  支援要請の補足説明      達成\x01",      # 7
            "get_note_fish\x01",                         # 8
            "DPくれ\x01",                                # 9
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_18A4"),
        (1, "loc_1C47"),
        (2, "loc_1C65"),
        (3, "loc_1C89"),
        (4, "loc_1CA5"),
        (5, "loc_1CEC"),
        (6, "loc_1CFC"),
        (7, "loc_1D0C"),
        (8, "loc_1D1C"),
        (9, "loc_1DA9"),
        (SWITCH_DEFAULT, "loc_1DB3"),
    )


    label("loc_18A4")

    OP_57(0x0)
    OP_29(0x65, 0x4, 0x2)
    OP_29(0x65, 0x1, 0x0)
    OP_29(0x65, 0x4, 0x10)
    OP_E5(0xA)
    OP_E5(0x5)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C34")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_18FD"),
        (1, "loc_190B"),
        (2, "loc_1B3C"),
        (3, "loc_1C20"),
        (SWITCH_DEFAULT, "loc_1C2F"),
    )


    label("loc_18FD")

    OP_2B(0x65, 0x66, 0x80, 0xFFFF)
    Jump("loc_1C2F")

    label("loc_190B")

    OP_E5(0x7)
    Sleep(500)
    Sound(3061, 255, 100, 0)    #voice#Fran
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_1AB3")
    OutputDebugInt(0xDE)
    SetChrName("フラン")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            "それでは達成した依頼の\x01",
            "報告を承りますね～。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A55")
    SetMapFlags(0x40000000)
    SetChrName("フラン")

    #A0005
    AnonymousTalk(
        0xFF,
        "ランクアップおめでとうございます。\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (1, "loc_19B3"),
        (SWITCH_DEFAULT, "loc_19E7"),
    )


    label("loc_19B3")


    #A0006
    AnonymousTalk(
        0xFF,
        (
            "クラス１４ｔｈ－－\x01",
            "ロイドさん、すごいです\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E7")

    label("loc_19E7")

    ClearMapFlags(0x40000000)

    #A0007
    AnonymousTalk(
        0xFF,
        (
            "特典の品もすぐに\x01",
            "そちらにお届けしますね～！\x02\x03",

            "お疲れさまでした～！\x01",
            "またよろしくお願いしますー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AAE")

    label("loc_1A55")

    SetChrName("フラン")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            "これで以上ですね～。\x02\x03",

            "では、また依頼を達成したら\x01",
            "よろしくお願いしますー。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1AAE")

    Jump("loc_1B12")

    label("loc_1AB3")

    OutputDebugInt(0x6F)
    SetChrName("フラン")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            "あれっ、報告可能な\x01",
            "依頼は無いみたいですね～。\x02\x03",

            "またよろしくお願いしますね～。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1B12")

    OP_E5(0x8)
    SetChrName("フラン")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            "テストです\x01",
            "テストです\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C2F")

    label("loc_1B3C")

    SetChrName("")
    SetMessageWindowPos(14, 308, 60, 1)

    #A0011
    AnonymousTalk(
        0xFF,
        "#5C対戦相手を選択してください。\x02",
    )


    Menu(
        2,
        128,
        64,
        1,
        (
            "ロバーツ\x01",          # 0
            "フラン\x01",            # 1
            "ミシェル\x01",          # 2
            "マリアベル\x01",        # 3
            "ヨナ\x01",              # 4
            "アバッス\x01",          # 5
            "ティオ\x01",            # 6
            "カンパネルラ\x01",      # 7
        )
    )

    MenuCmd(4, 2, 0x3)
    MenuEnd(0x0)
    OP_60(0x2)
    OP_57(0x0)
    Sleep(500)
    OP_E5(0x6)
    FadeToDark(300, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BE6"),
        (SWITCH_DEFAULT, "loc_1C0D"),
    )


    label("loc_1BE6")

    MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_1C12")

    label("loc_1C0D")

    Jump("loc_1C12")

    label("loc_1C12")

    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2F")

    label("loc_1C20")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C2F")

    label("loc_1C2F")

    Jump("loc_18C4")

    label("loc_1C34")

    OP_E5(0x6)
    OP_E5(0xB)
    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_1DB3")

    label("loc_1C47")

    OP_57(0x0)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x3)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_1DB3")

    label("loc_1C65")

    PlayBGM("ed7450", 0)
    OP_29(0x3C, 0x4, 0x2)
    OP_29(0x3C, 0x4, 0x80)
    OP_29(0x3C, 0x1, 0x0)
    OP_29(0x3D, 0x4, 0x2)
    OP_29(0x3D, 0x1, 0x0)
    Jump("loc_1DB3")

    label("loc_1C89")

    StopBGM(0x2710)
    Sleep(3000)
    PlayBGM("ed7205", 0)
    OP_29(0x3C, 0x1, 0x1)
    OP_29(0x3C, 0x4, 0x10)
    Jump("loc_1DB3")

    label("loc_1CA5")

    StopBGM(0xFA0)
    Sound(591, 0, 100, 0)
    Sleep(1000)
    Sound(591, 0, 100, 0)
    Sleep(1000)
    Sound(591, 0, 100, 0)
    Sleep(1000)
    Sound(591, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    Sound(591, 0, 100, 0)
    PlayBGM("ed7205", 0)
    OP_29(0x2, 0x4, 0x2)
    OP_29(0x2, 0x1, 0x0)
    Jump("loc_1DB3")

    label("loc_1CEC")

    OP_29(0x2, 0x1, 0x1)
    OP_29(0x2, 0x4, 0x10)
    Jump("loc_1DB3")

    label("loc_1CFC")

    OP_29(0x1, 0x4, 0x2)
    OP_29(0x1, 0x1, 0x0)
    Jump("loc_1DB3")

    label("loc_1D0C")

    OP_29(0x1, 0x1, 0x1)
    OP_29(0x1, 0x4, 0x10)
    Jump("loc_1DB3")

    label("loc_1D1C")

    Sound(3, 1, 100, 0)
    Sleep(5000)
    OP_24(0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D4D")

    #C0012
    ChrTalk(
        0x0,
        "FISH_COUNT > 0\x02",
    )

    CloseMessageWindow()

    label("loc_1D4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D75")

    #C0013
    ChrTalk(
        0x0,
        "FISH_MAXSIZE > 30\x02",
    )

    CloseMessageWindow()

    label("loc_1D75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DA4")

    #C0014
    ChrTalk(
        0x0,
        "BATTLE_NOTE_MONSCOUNT > 2\x02",
    )

    CloseMessageWindow()

    label("loc_1DA4")

    Jump("loc_1DB3")

    label("loc_1DA9")

    OP_2C(0x1, 0x5A)
    Jump("loc_1DB3")

    label("loc_1DB3")

    Jump("loc_3394")

    label("loc_1DB8")

    NewScene("r2010", 0, 0, 0)
    IdleLoop()
    Jump("loc_3394")

    label("loc_1DC6")

    OP_60(0x0)
    OP_57(0x0)
    Call(0, 21)
    Jump("loc_3394")

    label("loc_1DD3")

    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveClearMenu()
    OP_B9(0x0)
    Jump("loc_3394")

    label("loc_1DF3")

    ClearScenarioFlags(0x20, 2)
    Call(2, 0)
    Jump("loc_3394")

    label("loc_1DFE")

    ClearScenarioFlags(0x20, 2)
    Call(2, 1)
    Jump("loc_3394")

    label("loc_1E09")

    ClearScenarioFlags(0x20, 2)
    Call(2, 2)
    Jump("loc_3394")

    label("loc_1E14")

    Call(1, 94)
    Jump("loc_3394")

    label("loc_1E1C")

    Call(2, 48)
    Jump("loc_3394")

    label("loc_1E24")

    Call(0, 36)
    Jump("loc_3394")

    label("loc_1E2C")


    Menu(
        1,
        -1,
        -1,
        1,
        (
            "文字描画とか\x01",            # 0
            "スポットライト\x01",          # 1
            "LRボタン確認用\x01",          # 2
            "SEフェードアウト\x01",        # 3
            "導力車フラグ\x01",            # 4
            "導力車ジャンプ\x01",          # 5
            "メルカバジャンプ\x01",        # 6
            "パーティ選択\x01",            # 7
            "SE音質\x01",                  # 8
            "next_frame問題\x01",          # 9
            "デバッグフラグ\x01",          # 10
            "㈱絆ポイント変更\x01",        # 11
            "★前編絆＆ＧＦ変更\x01",      # 12
            "分岐チェック用\x01",          # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F64"),
        (1, "loc_21DD"),
        (2, "loc_21FB"),
        (3, "loc_2313"),
        (4, "loc_231E"),
        (5, "loc_2769"),
        (6, "loc_279B"),
        (7, "loc_27B7"),
        (8, "loc_27BC"),
        (9, "loc_2858"),
        (10, "loc_28AD"),
        (11, "loc_2931"),
        (12, "loc_2F5E"),
        (13, "loc_323D"),
        (SWITCH_DEFAULT, "loc_3378"),
    )


    label("loc_1F64")

    OP_60(0x1)

    #C0015
    ChrTalk(
        0x0,
        (
            "一行でウィンドウサイズに注目してください。\x01",
            "サイズの大きいフォント１行～２行でも、\x01",
            "従来のサイズを維持しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x0,
        "#00000Fサイズ０\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x0,
        "#00000F#1Sサイズ１\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x0,
        "#00000F#2Sサイズ２\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x0,
        "#00000F#3Sサイズ３\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x0,
        "#00000F#4Sサイズ４\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x0,
        (
            "#00000F#4Sサイズ４\x01",
            "サイズ３\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x0,
        (
            "#00000F#4Sサイズ４\x01",
            "#3Sサイズ３\x01",
            "サイズ３\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x0,
        "サイズ０\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x0,
        "#1Sサイズ１\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x0,
        "#2Sサイズ２\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x0,
        "#3Sサイズ３\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x0,
        "#4Sサイズ４\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x0,
        (
            "#4Sサイズ４！\x01",
            "サイズ３！\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x0,
        (
            "#4Sサイズ４！\x01",
            "#3Sサイズ３！\x01",
            "サイズ３！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("バイパー＆テスタメンツ")

    #A0030
    AnonymousTalk(
        0xFF,
        (
            "#2Sおおっ！！\x01",
            "おお\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_60(0x0)
    OP_57(0x0)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToDark(300, 0, -1)
    OP_0D()
    ShowSaveClearMenu()
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_B9(0x0)
    Jump("loc_3378")

    label("loc_21DD")

    OP_50(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_11(0x0, 0x0, 0x0, 0x19, 0x28, 0x0)
    Jump("loc_3378")

    label("loc_21FB")

    OP_60(0x0)
    OP_60(0x1)

    #C0031
    ChrTalk(
        0x0,
        "#00000Fおはようございます\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)

    #C0032
    ChrTalk(
        0x0,
        "#00000Fこんばんわございます\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x0,
        "#00000Fオートメッセージ１\x05\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x0,
        "#00000Fオートメッセージ２\x05\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)

    #C0035
    ChrTalk(
        0x0,
        "#00000Fオートメッセージ３\x05\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x0,
        "#00000Fオートメッセージ４\x05\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x0,
        "#00000Fこれでおしまいです\x02",
    )

    CloseMessageWindow()
    OP_CC(0x1, 0xFF, 0x0)
    Jump("loc_3378")

    label("loc_2313")

    OP_60(0x0)
    OP_60(0x1)
    Jump("loc_3378")

    label("loc_231E")

    OP_60(0x1)

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "導力車／メルカバ未入手\x01",          # 0
            "導力車で全地域移動可\x01",            # 1
            "メルカバで全地域移動可\x01",          # 2
            "車カスタム初期化\x01",                # 3
            "車カスタム全部あり\x01",              # 4
            "車カスタム①オバフェン\x01",          # 5
            "車カスタム②サイドステップ\x01",      # 6
            "車カスタム③リアスポ\x01",            # 7
            "車カスタム④バンパー\x01",            # 8
            "車カスタム⑤パトランプ\x01",          # 9
            "車カスタム⑥ホイール\x01",            # 10
            "車カスタム⑦HP回復\x01",              # 11
            "車カスタム⑧EP回復\x01",              # 12
            "車カスタム⑨CP回復\x01",              # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24B3"),
        (1, "loc_2566"),
        (2, "loc_2619"),
        (3, "loc_26D2"),
        (4, "loc_26F2"),
        (5, "loc_2712"),
        (6, "loc_271A"),
        (7, "loc_2722"),
        (8, "loc_272A"),
        (9, "loc_2732"),
        (10, "loc_273A"),
        (11, "loc_2742"),
        (12, "loc_274A"),
        (13, "loc_2752"),
        (SWITCH_DEFAULT, "loc_275A"),
    )


    label("loc_24B3")

    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x20, 5)
    ClearScenarioFlags(0x32, 0)
    ClearScenarioFlags(0x32, 1)
    ClearScenarioFlags(0x32, 2)
    ClearScenarioFlags(0x32, 3)
    ClearScenarioFlags(0x32, 4)
    ClearScenarioFlags(0x32, 5)
    ClearScenarioFlags(0x32, 6)
    ClearScenarioFlags(0x32, 7)
    ClearScenarioFlags(0x33, 0)
    ClearScenarioFlags(0x33, 1)
    ClearScenarioFlags(0x33, 2)
    ClearScenarioFlags(0x33, 3)
    ClearScenarioFlags(0x33, 4)
    ClearScenarioFlags(0x33, 5)
    ClearScenarioFlags(0x33, 6)
    ClearScenarioFlags(0x33, 7)
    ClearScenarioFlags(0x34, 0)
    ClearScenarioFlags(0x34, 1)
    ClearScenarioFlags(0x34, 2)
    ClearScenarioFlags(0x34, 3)
    ClearScenarioFlags(0x34, 4)
    ClearScenarioFlags(0x34, 5)
    ClearScenarioFlags(0x34, 6)
    ClearScenarioFlags(0x34, 7)
    ClearScenarioFlags(0x31, 6)
    ClearScenarioFlags(0x31, 4)
    ClearScenarioFlags(0x2F, 6)
    ClearScenarioFlags(0x35, 0)
    ClearScenarioFlags(0x35, 1)
    ClearScenarioFlags(0x35, 2)
    ClearScenarioFlags(0x35, 3)
    ClearScenarioFlags(0x35, 4)
    ClearScenarioFlags(0x35, 5)
    ClearScenarioFlags(0x35, 6)
    ClearScenarioFlags(0x35, 7)
    ClearScenarioFlags(0x36, 0)
    ClearScenarioFlags(0x36, 1)
    ClearScenarioFlags(0x36, 2)
    ClearScenarioFlags(0x36, 3)
    ClearScenarioFlags(0x36, 4)
    ClearScenarioFlags(0x36, 5)
    ClearScenarioFlags(0x36, 6)
    ClearScenarioFlags(0x36, 7)
    ClearScenarioFlags(0x37, 0)
    ClearScenarioFlags(0x37, 1)
    ClearScenarioFlags(0x37, 2)
    ClearScenarioFlags(0x37, 3)
    ClearScenarioFlags(0x37, 4)
    ClearScenarioFlags(0x37, 5)
    ClearScenarioFlags(0x37, 6)
    ClearScenarioFlags(0x37, 7)
    ClearScenarioFlags(0x31, 7)
    ClearScenarioFlags(0x31, 5)
    ClearScenarioFlags(0x2F, 7)
    Jump("loc_2764")

    label("loc_2566")

    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x20, 5)
    SetScenarioFlags(0x32, 0)
    SetScenarioFlags(0x32, 1)
    SetScenarioFlags(0x32, 2)
    SetScenarioFlags(0x32, 3)
    SetScenarioFlags(0x32, 4)
    SetScenarioFlags(0x32, 5)
    SetScenarioFlags(0x32, 6)
    SetScenarioFlags(0x32, 7)
    SetScenarioFlags(0x33, 0)
    SetScenarioFlags(0x33, 1)
    SetScenarioFlags(0x33, 2)
    SetScenarioFlags(0x33, 3)
    SetScenarioFlags(0x33, 4)
    SetScenarioFlags(0x33, 7)
    SetScenarioFlags(0x34, 0)
    SetScenarioFlags(0x34, 1)
    SetScenarioFlags(0x34, 2)
    SetScenarioFlags(0x34, 3)
    SetScenarioFlags(0x34, 4)
    SetScenarioFlags(0x34, 7)
    SetScenarioFlags(0x2F, 6)
    ClearScenarioFlags(0x33, 6)
    ClearScenarioFlags(0x33, 5)
    ClearScenarioFlags(0x34, 5)
    ClearScenarioFlags(0x34, 6)
    ClearScenarioFlags(0x31, 6)
    ClearScenarioFlags(0x31, 4)
    SetScenarioFlags(0x35, 0)
    SetScenarioFlags(0x35, 1)
    SetScenarioFlags(0x35, 2)
    SetScenarioFlags(0x35, 3)
    SetScenarioFlags(0x35, 4)
    SetScenarioFlags(0x35, 5)
    SetScenarioFlags(0x35, 6)
    SetScenarioFlags(0x35, 7)
    SetScenarioFlags(0x36, 0)
    SetScenarioFlags(0x36, 1)
    SetScenarioFlags(0x36, 2)
    SetScenarioFlags(0x36, 3)
    SetScenarioFlags(0x36, 4)
    SetScenarioFlags(0x36, 7)
    SetScenarioFlags(0x37, 0)
    SetScenarioFlags(0x37, 1)
    SetScenarioFlags(0x37, 2)
    SetScenarioFlags(0x37, 3)
    SetScenarioFlags(0x37, 4)
    SetScenarioFlags(0x37, 7)
    SetScenarioFlags(0x2F, 7)
    ClearScenarioFlags(0x36, 5)
    ClearScenarioFlags(0x36, 6)
    ClearScenarioFlags(0x37, 5)
    ClearScenarioFlags(0x37, 6)
    ClearScenarioFlags(0x31, 7)
    ClearScenarioFlags(0x31, 5)
    Jump("loc_2764")

    label("loc_2619")

    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x20, 5)
    SetScenarioFlags(0x32, 0)
    SetScenarioFlags(0x32, 1)
    SetScenarioFlags(0x32, 2)
    SetScenarioFlags(0x32, 3)
    SetScenarioFlags(0x32, 4)
    SetScenarioFlags(0x32, 5)
    SetScenarioFlags(0x32, 6)
    SetScenarioFlags(0x32, 7)
    SetScenarioFlags(0x33, 0)
    SetScenarioFlags(0x33, 1)
    ClearScenarioFlags(0x33, 2)
    SetScenarioFlags(0x33, 3)
    SetScenarioFlags(0x33, 4)
    SetScenarioFlags(0x33, 5)
    SetScenarioFlags(0x33, 6)
    SetScenarioFlags(0x33, 7)
    SetScenarioFlags(0x34, 0)
    SetScenarioFlags(0x34, 1)
    ClearScenarioFlags(0x34, 2)
    SetScenarioFlags(0x34, 3)
    SetScenarioFlags(0x34, 4)
    SetScenarioFlags(0x34, 5)
    SetScenarioFlags(0x34, 6)
    ClearScenarioFlags(0x34, 7)
    SetScenarioFlags(0x31, 6)
    SetScenarioFlags(0x31, 4)
    SetScenarioFlags(0x2F, 6)
    SetScenarioFlags(0x2B, 6)
    SetScenarioFlags(0x35, 0)
    SetScenarioFlags(0x35, 1)
    SetScenarioFlags(0x35, 2)
    SetScenarioFlags(0x35, 3)
    SetScenarioFlags(0x35, 4)
    SetScenarioFlags(0x35, 5)
    SetScenarioFlags(0x35, 6)
    SetScenarioFlags(0x35, 7)
    SetScenarioFlags(0x36, 0)
    SetScenarioFlags(0x36, 1)
    ClearScenarioFlags(0x36, 2)
    SetScenarioFlags(0x36, 3)
    SetScenarioFlags(0x36, 4)
    SetScenarioFlags(0x36, 5)
    SetScenarioFlags(0x36, 6)
    SetScenarioFlags(0x36, 7)
    SetScenarioFlags(0x37, 0)
    SetScenarioFlags(0x37, 1)
    ClearScenarioFlags(0x37, 2)
    SetScenarioFlags(0x37, 3)
    SetScenarioFlags(0x37, 4)
    SetScenarioFlags(0x37, 5)
    SetScenarioFlags(0x37, 6)
    ClearScenarioFlags(0x37, 7)
    SetScenarioFlags(0x31, 7)
    SetScenarioFlags(0x31, 5)
    SetScenarioFlags(0x2F, 7)
    SetScenarioFlags(0x2B, 7)
    Jump("loc_2764")

    label("loc_26D2")

    ClearScenarioFlags(0x30, 0)
    ClearScenarioFlags(0x30, 1)
    ClearScenarioFlags(0x30, 2)
    ClearScenarioFlags(0x30, 3)
    ClearScenarioFlags(0x30, 4)
    ClearScenarioFlags(0x30, 5)
    ClearScenarioFlags(0x30, 6)
    ClearScenarioFlags(0x30, 7)
    ClearScenarioFlags(0x31, 0)
    Jump("loc_2764")

    label("loc_26F2")

    SetScenarioFlags(0x30, 0)
    SetScenarioFlags(0x30, 1)
    SetScenarioFlags(0x30, 2)
    SetScenarioFlags(0x30, 3)
    SetScenarioFlags(0x30, 4)
    SetScenarioFlags(0x30, 5)
    SetScenarioFlags(0x30, 6)
    SetScenarioFlags(0x30, 7)
    SetScenarioFlags(0x31, 0)
    Jump("loc_2764")

    label("loc_2712")

    SetScenarioFlags(0x30, 0)
    Jump("loc_2764")

    label("loc_271A")

    SetScenarioFlags(0x30, 1)
    Jump("loc_2764")

    label("loc_2722")

    SetScenarioFlags(0x30, 2)
    Jump("loc_2764")

    label("loc_272A")

    SetScenarioFlags(0x30, 3)
    Jump("loc_2764")

    label("loc_2732")

    SetScenarioFlags(0x30, 4)
    Jump("loc_2764")

    label("loc_273A")

    SetScenarioFlags(0x30, 5)
    Jump("loc_2764")

    label("loc_2742")

    SetScenarioFlags(0x30, 6)
    Jump("loc_2764")

    label("loc_274A")

    SetScenarioFlags(0x30, 7)
    Jump("loc_2764")

    label("loc_2752")

    SetScenarioFlags(0x31, 0)
    Jump("loc_2764")

    label("loc_275A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2764")

    Jump("loc_3378")

    label("loc_2769")

    OP_60(0x1)
    OP_60(0x0)
    OP_57(0x0)
    ClearScenarioFlags(0x20, 5)
    MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_3378")

    label("loc_279B")

    OP_60(0x1)
    OP_60(0x0)
    OP_57(0x0)
    SetScenarioFlags(0x20, 5)
    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_3378")

    label("loc_27B7")

    Jump("loc_3378")

    label("loc_27BC")

    PlayBGM("ed7552", 0)

    label("loc_27C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2853")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "VOL100\x01",      # 0
            "VOL50\x01",       # 1
            "VOL20\x01",       # 2
            "VOL0\x01",        # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2815"),
        (1, "loc_2820"),
        (2, "loc_282B"),
        (3, "loc_2836"),
        (SWITCH_DEFAULT, "loc_2841"),
    )


    label("loc_2815")

    VolumeBGM(0x64, 0x0)
    Jump("loc_284E")

    label("loc_2820")

    VolumeBGM(0x32, 0x3E8)
    Jump("loc_284E")

    label("loc_282B")

    VolumeBGM(0x14, 0x3E8)
    Jump("loc_284E")

    label("loc_2836")

    VolumeBGM(0x0, 0x0)
    Jump("loc_284E")

    label("loc_2841")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)

    label("loc_284E")

    Jump("loc_27C0")

    label("loc_2853")

    Jump("loc_3378")

    label("loc_2858")

    EventBegin(0x0)
    OP_60(0x0)
    Sleep(1000)
    EndChrThread(0x8, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    Sleep(3000)
    Sleep(3000)
    Sleep(3000)
    Sleep(3000)
    Sleep(3000)
    Sleep(3000)
    Sleep(3000)
    Sleep(3000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_D7(0x1E)
    Sleep(3000)
    EventEnd(0x5)
    Jump("loc_3378")

    label("loc_28AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_END)), "loc_28F6")
    ClearScenarioFlags(0x20, 2)

    #C0038
    ChrTalk(
        0x0,
        "◆デバッグテキスト◆が表示されるようになりました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_292C")

    label("loc_28F6")

    SetScenarioFlags(0x20, 2)

    #C0039
    ChrTalk(
        0x0,
        "◆デバッグテキスト◆が表示されなくなりました。\x02",
    )


    label("loc_292C")

    Jump("loc_3378")

    label("loc_2931")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F4F")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "全員を０に初期化\x01",        # 0
            "全員を基準値に\x01",          # 1
            "エリィを基準値に\x01",        # 2
            "ティオを基準値に\x01",        # 3
            "ランディを基準値に\x01",      # 4
            "ノエルを基準値に\x01",        # 5
            "ワジを基準値に\x01",          # 6
            "リーシャを基準値に\x01",      # 7
            "ダドリーを基準値に\x01",      # 8
            "イリアを基準値に\x01",        # 9
            "セシルを基準値に\x01",        # 10
            "フランを基準値に\x01",        # 11
            "シュリを基準値に\x01",        # 12
            "キーアを基準値に\x01",        # 13
            "実績\x01",                    # 14
        )
    )

    MenuEnd(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2AB0"),
        (1, "loc_2B51"),
        (2, "loc_2BF4"),
        (3, "loc_2C36"),
        (4, "loc_2C78"),
        (5, "loc_2CBC"),
        (6, "loc_2CFE"),
        (7, "loc_2D3E"),
        (8, "loc_2D82"),
        (9, "loc_2DC6"),
        (10, "loc_2E08"),
        (11, "loc_2E4A"),
        (12, "loc_2E8C"),
        (13, "loc_2ECE"),
        (14, "loc_2F10"),
        (SWITCH_DEFAULT, "loc_2F32"),
    )


    label("loc_2AB0")


    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全員の絆ポイントを０に初期化しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3F")

    label("loc_2B51")


    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全員の絆ポイントを規定値に設定しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3F")

    label("loc_2BF4")


    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィの絆ポイントを規定値に設定しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3F")

    label("loc_2C36")


    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオの絆ポイントを規定値に設定しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3F")

    label("loc_2C78")


    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディの絆ポイントを規定値に設定しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3F")

    label("loc_2CBC")


    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ノエルの絆ポイントを規定値に設定しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3F")

    label("loc_2CFE")


    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ワジの絆ポイントを規定値に設定しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3F")

    label("loc_2D3E")


    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "リーシャの絆ポイントを規定値に設定しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3F")

    label("loc_2D82")


    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ダドリーの絆ポイントを規定値に設定しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3F")

    label("loc_2DC6")


    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "イリアの絆ポイントを規定値に設定しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3F")

    label("loc_2E08")


    #A0050
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セシルの絆ポイントを規定値に設定しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3F")

    label("loc_2E4A")


    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フランの絆ポイントを規定値に設定しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3F")

    label("loc_2E8C")


    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "シュリの絆ポイントを規定値に設定しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3F")

    label("loc_2ECE")


    #A0053
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キーアの絆ポイントを規定値に設定しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F3F")

    label("loc_2F10")


    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "実績入手テスト。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_E0(0x34, 0x0)
    Jump("loc_2F3F")

    label("loc_2F32")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)

    label("loc_2F3F")

    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2931")

    label("loc_2F4F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3378")

    label("loc_2F5E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_322E")
    MenuCmd(0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FA1")
    MenuCmd(1, 2, "前編エリィの絆   OFF")
    Jump("loc_2FB9")

    label("loc_2FA1")

    MenuCmd(1, 2, "前編エリィの絆   ON ")

    label("loc_2FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE0")
    MenuCmd(1, 2, "前編ティオの絆   OFF")
    Jump("loc_2FF8")

    label("loc_2FE0")

    MenuCmd(1, 2, "前編ティオの絆   ON ")

    label("loc_2FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_301F")
    MenuCmd(1, 2, "前編ランディの絆 OFF")
    Jump("loc_3037")

    label("loc_301F")

    MenuCmd(1, 2, "前編ランディの絆 ON ")

    label("loc_3037")

    MenuCmd(2, 2, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x2)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_306C"),
        (1, "loc_30F6"),
        (2, "loc_3180"),
        (SWITCH_DEFAULT, "loc_320E"),
    )


    label("loc_306C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B5")
    SetScenarioFlags(0x25, 3)

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィの前編絆フラグを「ＯＮ」に設定しました。\x07\x00\x02",
        )
    )

    Jump("loc_30F1")

    label("loc_30B5")

    ClearScenarioFlags(0x25, 3)

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィの前編絆フラグを「ＯＦＦ」に設定しました。\x07\x00\x02",
        )
    )


    label("loc_30F1")

    Jump("loc_321D")

    label("loc_30F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_313F")
    SetScenarioFlags(0x25, 4)

    #A0057
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオの前編絆フラグを「ＯＮ」に設定しました。\x07\x00\x02",
        )
    )

    Jump("loc_317B")

    label("loc_313F")

    ClearScenarioFlags(0x25, 4)

    #A0058
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオの前編絆フラグを「ＯＦＦ」に設定しました。\x07\x00\x02",
        )
    )


    label("loc_317B")

    Jump("loc_321D")

    label("loc_3180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CB")
    SetScenarioFlags(0x25, 5)

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディの前編絆フラグを「ＯＮ」に設定しました。\x07\x00\x02",
        )
    )

    Jump("loc_3209")

    label("loc_31CB")

    ClearScenarioFlags(0x25, 5)

    #A0060
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディの前編絆フラグを「ＯＦＦ」に設定しました。\x07\x00\x02",
        )
    )


    label("loc_3209")

    Jump("loc_321D")

    label("loc_320E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_321D")

    label("loc_321D")

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2F68")

    label("loc_322E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3378")

    label("loc_323D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3369")
    MenuCmd(0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3272")
    MenuCmd(1, 2, "吉田さん用   OFF")
    Jump("loc_3286")

    label("loc_3272")

    MenuCmd(1, 2, "吉田さん用   ON ")

    label("loc_3286")

    MenuCmd(2, 2, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x2)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_32AF"),
        (SWITCH_DEFAULT, "loc_3349"),
    )


    label("loc_32AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3300")
    SetScenarioFlags(0x129, 4)
    SetScenarioFlags(0x1C0, 2)
    SetScenarioFlags(0x15A, 1)
    SetScenarioFlags(0x12E, 4)
    SetScenarioFlags(0x170, 3)

    #A0061
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "吉田さん用フラグを「ＯＮ」に設定しました。\x07\x00\x02",
        )
    )

    Jump("loc_3344")

    label("loc_3300")

    ClearScenarioFlags(0x129, 4)
    ClearScenarioFlags(0x1C0, 2)
    ClearScenarioFlags(0x15A, 1)
    ClearScenarioFlags(0x12E, 4)
    ClearScenarioFlags(0x170, 3)

    #A0062
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "吉田さん用フラグを「ＯＦＦ」に設定しました。\x07\x00\x02",
        )
    )


    label("loc_3344")

    Jump("loc_3358")

    label("loc_3349")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3358")

    label("loc_3358")

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_323D")

    label("loc_3369")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3378")

    label("loc_3378")

    OP_60(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3394")

    label("loc_338A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3394")

    Jump("loc_12DB")

    label("loc_3399")

    OP_60(0x0)
    OP_57(0x0)
    OP_DD()
    ClearMapFlags(0x80)
    Return()

    # Function_9_1247 end

    def Function_10_33A5(): pass

    label("Function_10_33A5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36CE")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "パチスロ\x01",              # 0
            "釣り\x01",                  # 1
            "ルーレット\x01",            # 2
            "ポーカー\x01",              # 3
            "ブラックジャック\x01",      # 4
            "ポムっと\x01",              # 5
            "ホラーハウス\x01",          # 6
            "ダンス練習\x01",            # 7
            "導力車\x01",                # 8
            "メダル取得\x01",            # 9
            "EV_GunShoot\x01",           # 10
            "ポムっとMOVIE1\x01",        # 11
            "ポムっとMOVIE2\x01",        # 12
            "キャンセル\x01",            # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_34BD"),
        (1, "loc_34E4"),
        (2, "loc_3542"),
        (3, "loc_3569"),
        (4, "loc_3590"),
        (5, "loc_35B7"),
        (6, "loc_360B"),
        (7, "loc_3619"),
        (8, "loc_362A"),
        (9, "loc_3651"),
        (10, "loc_365F"),
        (11, "loc_3667"),
        (12, "loc_368E"),
        (SWITCH_DEFAULT, "loc_36B5"),
    )


    label("loc_34BD")

    MiniGame(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_36BF")

    label("loc_34E4")

    AddItemNumber(0x14, 1)
    AddItemNumber(0x15, 1)
    AddItemNumber(0x16, 1)
    AddItemNumber(0x17, 1)
    AddItemNumber(0x18, 1)
    AddItemNumber(0x186, 10)
    AddItemNumber(0x187, 10)
    AddItemNumber(0x188, 10)
    AddItemNumber(0x189, 10)
    AddItemNumber(0x18A, 10)
    AddItemNumber(0x18B, 10)
    MiniGame(0x6, 0x1, 0x0, 0x0, 0x0, 0x0, 0xFFFFFF38, 0x0, 0xFFFFF768)
    Jump("loc_36BF")

    label("loc_3542")

    MiniGame(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_36BF")

    label("loc_3569")

    MiniGame(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_36BF")

    label("loc_3590")

    MiniGame(0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_36BF")

    label("loc_35B7")

    SetScenarioFlags(0x27, 2)
    SetScenarioFlags(0x27, 3)
    SetScenarioFlags(0x27, 4)
    SetScenarioFlags(0x27, 5)
    SetScenarioFlags(0x27, 6)
    SetScenarioFlags(0x27, 7)
    SetScenarioFlags(0x28, 0)
    SetScenarioFlags(0x28, 1)
    SetScenarioFlags(0x2A, 0)
    SetScenarioFlags(0x2A, 1)
    SetScenarioFlags(0x2A, 2)
    SetScenarioFlags(0x2A, 3)
    SetScenarioFlags(0x2A, 4)
    SetScenarioFlags(0x2A, 5)
    SetScenarioFlags(0x2A, 6)
    MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_36BF")

    label("loc_360B")

    NewScene("t1360", 0, 0, 0)
    IdleLoop()
    Jump("loc_36BF")

    label("loc_3619")

    SetScenarioFlags(0x22, 1)
    NewScene("e3600", 0, 0, 0)
    IdleLoop()
    Jump("loc_36BF")

    label("loc_362A")

    MiniGame(0x31, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_36BF")

    label("loc_3651")

    OP_50(0x4B, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_36BF")

    label("loc_365F")

    Call(0, 49)
    Jump("loc_36BF")

    label("loc_3667")

    MiniGame(0x10, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_36BF")

    label("loc_368E")

    MiniGame(0x10, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_36BF")

    label("loc_36B5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36BF")

    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_33AF")

    label("loc_36CE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_10_33A5 end

    def Function_11_36DC(): pass

    label("Function_11_36DC")

    PlayBGM("ed7552", 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A14")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "BTL_TEST_01 テスト\x01",                  # 0
            "BTL_TEST_02 状態異常\x01",                # 1
            "BTL_TEST_03 屋内\x01",                    # 2
            "BTL_TEST_04 誰か専用(遠藤)\x01",          # 3
            "BTL_TEST_05 誰か専用(伊藤)\x01",          # 4
            "BTL_TEST_06 誰か専用(堀本)\x01",          # 5
            "BTL_TEST_07 沢山の敵テスト\x01",          # 6
            "BTL_TEST_08 カンパネルラ専用\x01",        # 7
            "BTL_TEST_09 アリアンロード専用\x01",      # 8
            "BTL_TEST_11 マリアベル専用\x01",          # 9
            "BTL_TEST_LAST ラスボス①\x01",            # 10
            "BTL_TEST_LAST ラスボス②\x01",            # 11
            "BTL_MONSSET 相手選択\x01",                # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_38A0"),
        (1, "loc_38B5"),
        (2, "loc_38CA"),
        (3, "loc_38DF"),
        (4, "loc_38F4"),
        (5, "loc_3909"),
        (6, "loc_391E"),
        (7, "loc_3933"),
        (8, "loc_3948"),
        (9, "loc_39B1"),
        (10, "loc_39C6"),
        (11, "loc_39DB"),
        (12, "loc_39F0"),
        (SWITCH_DEFAULT, "loc_3A05"),
    )


    label("loc_38A0")

    Battle("BattleInfo_4AC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3A05")

    label("loc_38B5")

    Battle("BattleInfo_4F0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3A05")

    label("loc_38CA")

    Battle("BattleInfo_534", 0x0, 0x0, 0x0, 0x28, 0xFF)
    Jump("loc_3A05")

    label("loc_38DF")

    Battle("BattleInfo_578", 0x0, 0x0, 0x100, 0x0, 0xFF)
    Jump("loc_3A05")

    label("loc_38F4")

    Battle("BattleInfo_5BC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3A05")

    label("loc_3909")

    Battle("BattleInfo_600", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3A05")

    label("loc_391E")

    Battle("BattleInfo_688", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3A05")

    label("loc_3933")

    Battle("BattleInfo_6CC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3A05")

    label("loc_3948")

    Battle("BattleInfo_710", 0x0, 0x0, 0x0, 0x40, 0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_397D")

    #C0063
    ChrTalk(
        0x0,
        "ＨＰを５０％削った\x02",
    )


    label("loc_397D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3994")

    #C0064
    ChrTalk(
        0x0,
        "勝利\x02",
    )


    label("loc_3994")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39AB")

    #C0065
    ChrTalk(
        0x0,
        "まけ\x02",
    )


    label("loc_39AB")

    CloseMessageWindow()
    Jump("loc_3A05")

    label("loc_39B1")

    Battle("BattleInfo_754", 0x30200011, 0x0, 0x0, 0x41, 0xFF)
    Jump("loc_3A05")

    label("loc_39C6")

    Battle("BattleInfo_798", 0x30200012, 0x0, 0x0, 0x1E, 0xFF)
    Jump("loc_3A05")

    label("loc_39DB")

    Battle("BattleInfo_7DC", 0x30200012, 0x0, 0x0, 0x1F, 0xFF)
    Jump("loc_3A05")

    label("loc_39F0")

    Battle("BattleInfo_644", 0x0, 0x0, 0x0, 0x1, 0xFF)
    Jump("loc_3A05")

    label("loc_3A05")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36EA")

    label("loc_3A14")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_11_36DC end

    def Function_12_3A22(): pass

    label("Function_12_3A22")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AC0")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "ＮＰＣ\x01",          # 0
            "戦闘キャラ\x01",      # 1
            "テスト\x01",          # 2
            "キャンセル\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A87"),
        (1, "loc_3A95"),
        (2, "loc_3AA3"),
        (SWITCH_DEFAULT, "loc_3AB1"),
    )


    label("loc_3A87")

    NewScene("a0002", 0, 0, 0)
    IdleLoop()
    Jump("loc_3ABB")

    label("loc_3A95")

    NewScene("a0001", 0, 0, 0)
    IdleLoop()
    Jump("loc_3ABB")

    label("loc_3AA3")

    NewScene("a0004", 0, 0, 0)
    IdleLoop()
    Jump("loc_3ABB")

    label("loc_3AB1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3ABB")

    Jump("loc_3A2C")

    label("loc_3AC0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_12_3A22 end

    def Function_13_3ACE(): pass

    label("Function_13_3ACE")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3B06"),
        (1, "loc_3B12"),
        (2, "loc_3B1E"),
        (3, "loc_3B2A"),
        (4, "loc_3B36"),
        (5, "loc_3B42"),
        (6, "loc_3B4E"),
        (SWITCH_DEFAULT, "loc_3B5A"),
    )


    label("loc_3B06")

    OP_A0(0xFE, 1450, 0x0, 0x7)
    Jump("loc_3B66")

    label("loc_3B12")

    OP_A0(0xFE, 1550, 0x0, 0x7)
    Jump("loc_3B66")

    label("loc_3B1E")

    OP_A0(0xFE, 1600, 0x0, 0x7)
    Jump("loc_3B66")

    label("loc_3B2A")

    OP_A0(0xFE, 1400, 0x0, 0x7)
    Jump("loc_3B66")

    label("loc_3B36")

    OP_A0(0xFE, 1650, 0x0, 0x7)
    Jump("loc_3B66")

    label("loc_3B42")

    OP_A0(0xFE, 1350, 0x0, 0x7)
    Jump("loc_3B66")

    label("loc_3B4E")

    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_3B66")

    label("loc_3B5A")

    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_3B66")

    label("loc_3B66")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B7D")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_3B66")

    label("loc_3B7D")

    Return()

    # Function_13_3ACE end

    def Function_14_3B7E(): pass

    label("Function_14_3B7E")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3BB6"),
        (1, "loc_3BC2"),
        (2, "loc_3BCE"),
        (3, "loc_3BDA"),
        (4, "loc_3BE6"),
        (5, "loc_3BF2"),
        (6, "loc_3BFE"),
        (SWITCH_DEFAULT, "loc_3C0A"),
    )


    label("loc_3BB6")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3C16")

    label("loc_3BC2")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3C16")

    label("loc_3BCE")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3C16")

    label("loc_3BDA")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3C16")

    label("loc_3BE6")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3C16")

    label("loc_3BF2")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3C16")

    label("loc_3BFE")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C16")

    label("loc_3C0A")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C16")

    label("loc_3C16")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C2D")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C16")

    label("loc_3C2D")

    Return()

    # Function_14_3B7E end

    def Function_15_3C2E(): pass

    label("Function_15_3C2E")

    TalkBegin(0xFF)

    #C0066
    ChrTalk(
        0x0,
        "おい\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_15_3C2E end

    def Function_16_3C3F(): pass

    label("Function_16_3C3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C7D")
    OP_9D(0xFE, 0x2BC, 0x0, 0x2AF8, 0x1F4, 0x3E8)
    OP_9D(0xFE, 0x12C0, 0x0, 0x2AF8, 0x1F4, 0x3E8)
    Jump("Function_16_3C3F")

    label("loc_3C7D")

    Return()

    # Function_16_3C3F end

    def Function_17_3C7E(): pass

    label("Function_17_3C7E")

    TalkBegin(0xFE)
    AddItemNumber(0x14, 1)

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "《海刃》シャークマン\x01",          # 0
            "《水狂》ナルセス\x01",              # 1
            "《竜宮》カグヤ\x01",                # 2
            "《銀鯱》トリトン\x01",              # 3
            "《釣皇》レイクロードⅢ世\x01",      # 4
            "キャンセル\x01",                    # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3D24"),
        (1, "loc_3D67"),
        (2, "loc_3D93"),
        (3, "loc_3DD1"),
        (4, "loc_3DFD"),
        (SWITCH_DEFAULT, "loc_3E11"),
    )


    label("loc_3D24")


    #C0067
    ChrTalk(
        0xFE,
        (
            "サドンデス（先ミス負け）、１０番勝負だがやる？\x01",
            "わしが先行\x02",
        )
    )

    Jump("loc_3E1B")

    label("loc_3D67")


    #C0068
    ChrTalk(
        0xFE,
        "値段の高い魚を釣り上げた方が勝ち。\x02",
    )

    Jump("loc_3E1B")

    label("loc_3D93")


    #C0069
    ChrTalk(
        0xFE,
        "サイズ勝負。釣った三匹の合計サイズが大きい方の勝ち。\x02",
    )

    Jump("loc_3E1B")

    label("loc_3DD1")


    #C0070
    ChrTalk(
        0xFE,
        "５種類の魚を先に釣ったほうが勝ち。\x02",
    )

    Jump("loc_3E1B")

    label("loc_3DFD")


    #C0071
    ChrTalk(
        0xFE,
        "お題釣り。\x02",
    )

    Jump("loc_3E1B")

    label("loc_3E11")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E1B")

    CloseMessageWindow()
    OP_60(0xFF)
    FadeToDark(300, 0, -1)
    OP_0D()
    ClearMapFlags(0x1)
    OP_68(3630, 0, 3760, 0)
    MoveCamera(45, 30, 0, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x0, 5680, 0, 3750, 270)
    OP_93(0xFE, 0x5A, 0x1F4)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3E9E"),
        (1, "loc_3EC5"),
        (2, "loc_3EEC"),
        (3, "loc_3F13"),
        (4, "loc_3F3A"),
        (SWITCH_DEFAULT, "loc_3F61"),
    )


    label("loc_3E9E")

    MiniGame(0x7, 0x1, 0x9, 0x1248, 0x0, 0xABE, 0xE60, 0x0, 0x1036)
    Jump("loc_3F61")

    label("loc_3EC5")

    MiniGame(0x7, 0x2, 0x9, 0x1248, 0x0, 0xABE, 0xE60, 0x0, 0x1036)
    Jump("loc_3F61")

    label("loc_3EEC")

    MiniGame(0x7, 0x4, 0x9, 0x1248, 0x0, 0xABE, 0xE60, 0x0, 0x1036)
    Jump("loc_3F61")

    label("loc_3F13")

    MiniGame(0x7, 0x3, 0x9, 0x1248, 0x0, 0xABE, 0xE60, 0x0, 0x1036)
    Jump("loc_3F61")

    label("loc_3F3A")

    MiniGame(0x7, 0x5, 0x9, 0x1248, 0x0, 0xABE, 0xE60, 0x0, 0x1036)
    Jump("loc_3F61")

    label("loc_3F61")

    FadeToDark(300, 0, -1)
    OP_0D()
    SetMapFlags(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F9D")

    #C0072
    ChrTalk(
        0x0,
        "勝ったぁ！\x02",
    )

    Jump("loc_3FFE")

    label("loc_3F9D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FBF")

    #C0073
    ChrTalk(
        0xFE,
        "勝ったぁ！\x02",
    )

    Jump("loc_3FFE")

    label("loc_3FBF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FE3")

    #C0074
    ChrTalk(
        0xFE,
        "勝負はお預け\x02",
    )

    Jump("loc_3FFE")

    label("loc_3FE3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FFE")

    #C0075
    ChrTalk(
        0xFE,
        "途中抜け\x02",
    )


    label("loc_3FFE")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_3C7E end

    def Function_18_4003(): pass

    label("Function_18_4003")

    TalkBegin(0xFE)
    PlayBGM("ed7552", 0)
    VolumeBGM(0x1E, 0x0)
    RemoveParty(0x8, 0xFF)
    AddParty(0x37, 0xFF, 0xFF)
    TurnDirection(0xFE, 0x102, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0x63)"), scpexpr(EXPR_END)), "loc_40D9")

    #C0076
    ChrTalk(
        0x101,
        (
            "#0000F#Nいや、気にしないでよ。\x02\x03",

            "手紙で色々と聞いて#4Rクロスベル#いるし……\x01",
            "それにどんなに変わったとしても#4Rクロスベル#\x01",
            "故郷#4Rクロスベル#は故郷#4Rクロスベル#だから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_40D9")


    #C0077
    ChrTalk(
        0x138,
        "#0000Fマリアベルです\x02",
    )

    CloseMessageWindow()

    label("loc_40F3")


    #C0078
    ChrTalk(
        0xFE,
        "おやエリーさま\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x0,
        "パーティ０のメッセージ\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x1,
        "パーティ１のメッセージ\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x109,
        (
            "ノエルがサポートメンバーでいればメッセージでる？\x01",
            "トゲなしウィンドウなんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "#00Fでも先生#4Rせんせい#は先生先生……\x01",
            "レナさんの死#2Rし#を乗り越えて#12Rをのりこえて#\x01",
            "遊撃士としての道を歩き始めた。\x02\x03",

            "#10F決して立ち止まることなく\x01",
            "大切なものを守り続けてきた。\x02\x03",

            "王国軍に戻った今も\x01",
            "それは変わっていないと思う。\x02\x03",

            "#00Fエステル……\x01",
            "あんたは、どうしたいの？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_18_4003 end

    def Function_19_42AA(): pass

    label("Function_19_42AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42D1")
    OP_94(0xFE, 0xFFFFD8F0, 0xFFFFD8F0, 0x2710, 0x2710, 0x157C)
    Jump("Function_19_42AA")

    label("loc_42D1")

    Return()

    # Function_19_42AA end

    def Function_20_42D2(): pass

    label("Function_20_42D2")

    OP_95(0x0, -2000, 0, 22400, 4000, 0x0)
    Return()

    # Function_20_42D2 end

    def Function_21_42E7(): pass

    label("Function_21_42E7")

    SetChrName("ショップちゃん")

    #A0083
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "どのお店？\x02",
        )
    )


    Menu(
        1,
        -1,
        -1,
        1,
        (
            "武器屋\x01",                      # 0
            "道具屋\x01",                      # 1
            "工房\x01",                        # 2
            "宿屋\x01",                        # 3
            "食材屋\x01",                      # 4
            "カジノ\x01",                      # 5
            "交換屋\x01",                      # 6
            "改造屋\x01",                      # 7
            "導力車\x01",                      # 8
            "こっそりムービーテスト\x01",      # 9
            "こっそりメニューテスト\x01",      # 10
            "工房２\x01",                      # 11
            "キャンセル\x01",                  # 12
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_60(0x1)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_43E8"),
        (1, "loc_43F0"),
        (2, "loc_43F8"),
        (3, "loc_4400"),
        (4, "loc_4408"),
        (5, "loc_4410"),
        (6, "loc_4418"),
        (7, "loc_4420"),
        (8, "loc_4428"),
        (9, "loc_4430"),
        (10, "loc_4468"),
        (11, "loc_4470"),
        (SWITCH_DEFAULT, "loc_4478"),
    )


    label("loc_43E8")

    Call(0, 22)
    Jump("loc_447D")

    label("loc_43F0")

    Call(0, 23)
    Jump("loc_447D")

    label("loc_43F8")

    Call(0, 24)
    Jump("loc_447D")

    label("loc_4400")

    Call(0, 29)
    Jump("loc_447D")

    label("loc_4408")

    Call(0, 30)
    Jump("loc_447D")

    label("loc_4410")

    Call(0, 31)
    Jump("loc_447D")

    label("loc_4418")

    Call(0, 32)
    Jump("loc_447D")

    label("loc_4420")

    Call(0, 33)
    Jump("loc_447D")

    label("loc_4428")

    Call(0, 47)
    Jump("loc_447D")

    label("loc_4430")

    OP_C9(0x0, 0x10)
    PlayMovie(0x0, "ed7_op.pmf", 0x34, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_C9(0x1, 0x10)
    FadeToBright(10, 0)
    OP_0D()
    Jump("loc_447D")

    label("loc_4468")

    Call(0, 34)
    Jump("loc_447D")

    label("loc_4470")

    Call(0, 25)
    Jump("loc_447D")

    label("loc_4478")

    Jump("loc_447D")

    label("loc_447D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_42E7 end

    def Function_22_4488(): pass

    label("Function_22_4488")

    OP_AF(0x1)
    Return()

    # Function_22_4488 end

    def Function_23_448B(): pass

    label("Function_23_448B")

    OP_AF(0x14)
    Return()

    # Function_23_448B end

    def Function_24_448E(): pass

    label("Function_24_448E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4498")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45C3")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                        # 0
            "改造?合成する\x01",                   # 1
            "マスタークオーツを購入する\x01",      # 2
            "マスタークオーツを変更する\x01",      # 3
            "やめる\x01",                          # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4541")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4541")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4562")
    Call(0, 26)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_45BE")

    label("loc_4562")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4582")
    OP_AF(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_45BE")

    label("loc_4582")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A3")
    Call(0, 28)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_45BE")

    label("loc_45A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45BE")
    OP_AF(0xFB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_45BE")

    Jump("loc_4498")

    label("loc_45C3")

    Return()

    # Function_24_448E end

    def Function_25_45C4(): pass

    label("Function_25_45C4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_45CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4700")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                        # 0
            "エニグマカバーの交換をする\x01",      # 1
            "マスタークオーツを購入する\x01",      # 2
            "マスタークオーツを装着する\x01",      # 3
            "やめる\x01",                          # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_467A")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_467A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_469B")
    Call(0, 26)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46FB")

    label("loc_469B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46BC")
    Call(0, 27)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46FB")

    label("loc_46BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46DD")
    Call(0, 28)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46FB")

    label("loc_46DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46FB")
    OP_60(0x0)
    OP_AF(0xFB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_46FB")

    Jump("loc_45CE")

    label("loc_4700")

    Return()

    # Function_25_45C4 end

    def Function_26_4701(): pass

    label("Function_26_4701")


    #C0084
    ChrTalk(
        0x0,
        "テストです。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_26_4701 end

    def Function_27_4714(): pass

    label("Function_27_4714")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_471E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E85")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_4764")
    MenuCmd(1, 0, "ブルーシェリフ　　　　購入済み")
    MenuCmd(3, 0, 0x0)
    Jump("loc_4786")

    label("loc_4764")

    MenuCmd(1, 0, "ブルーシェリフ　　　　1000ミラ")

    label("loc_4786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_47BA")
    MenuCmd(1, 0, "ピースグリーン　　　　購入済み")
    MenuCmd(3, 0, 0x1)
    Jump("loc_47DC")

    label("loc_47BA")

    MenuCmd(1, 0, "ピースグリーン　　　　1000ミラ")

    label("loc_47DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_4810")
    MenuCmd(1, 0, "ブラックキャット　　　購入済み")
    MenuCmd(3, 0, 0x2)
    Jump("loc_4832")

    label("loc_4810")

    MenuCmd(1, 0, "ブラックキャット　　　1000ミラ")

    label("loc_4832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_4866")
    MenuCmd(1, 0, "デンジャーオレンジ　　購入済み")
    MenuCmd(3, 0, 0x3)
    Jump("loc_4888")

    label("loc_4866")

    MenuCmd(1, 0, "デンジャーオレンジ　　1000ミラ")

    label("loc_4888")

    MenuCmd(1, 0, "やめる")

    #A0085
    AnonymousTalk(
        0x0,
        (
            scpstr(0x18),
            "どれに交換しますか～？\x02",
        )
    )

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_48DD")
    Sleep(1)
    Return()

    label("loc_48DD")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_499E")

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "このカバーはロイド専用です。\x01",
            "購入するとキャンプメニューの[ORBMENT]で表示される\x01",
            "戦術オーブメントのカバーが変わります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B54")

    label("loc_499E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A31")

    #A0087
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "このカバーはエリィ専用です。\x01",
            "購入するとキャンプメニューの[ORBMENT]で表示される\x01",
            "戦術オーブメントのカバーが変わります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B54")

    label("loc_4A31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AC4")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "このカバーはティオ専用です。\x01",
            "購入するとキャンプメニューの[ORBMENT]で表示される\x01",
            "戦術オーブメントのカバーが変わります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B54")

    label("loc_4AC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B54")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "このカバーはランディ専用です。\x01",
            "購入するとキャンプメニューの[ORBMENT]で表示される\x01",
            "戦術オーブメントのカバーが変わります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B54")


    #A0090
    AnonymousTalk(
        0x0,
        "はい、これでいいですか～？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【交換を頼む】\x01",      # 0
            "【やめておく】\x01",      # 1
        )
    )

    MenuEnd(0x4)
    OP_60(0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E68")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C4F")

    #C0091
    ChrTalk(
        0x0,
        (
            "あれ～、ミラが足りないみたいですよ？\x01",
            "それじゃ交換はできないですぅ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E59")

    label("loc_4C4F")


    #C0092
    ChrTalk(
        0x0,
        (
            "了解ですぅ。\x01",
            "ちょっと待っててくださいですぅ～㈱\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(71, 0, 100, 0)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0093
    ChrTalk(
        0x0,
        "はい、お待たせですぅ。\x02",
    )

    CloseMessageWindow()
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D0F")

    #A0094
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドのオーブメントのカバーを交換した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 5)
    Jump("loc_4DE7")

    label("loc_4D0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D58")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィのオーブメントのカバーを交換した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 6)
    Jump("loc_4DE7")

    label("loc_4D58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DA1")

    #A0096
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオのオーブメントのカバーを交換した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 7)
    Jump("loc_4DE7")

    label("loc_4DA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DE7")

    #A0097
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディのオーブメントのカバーを交換した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 0)

    label("loc_4DE7")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E22")
    OP_E0(0x16, 0x0)

    label("loc_4E22")


    #C0098
    ChrTalk(
        0x0,
        (
            "ふふ、またのご利用を\x01",
            "お待ちしてま～す。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_4E59")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E72")

    label("loc_4E68")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E72")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_471E")

    label("loc_4E85")

    Return()

    # Function_27_4714 end

    def Function_28_4E86(): pass

    label("Function_28_4E86")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5541")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xDD, 0x0)"), scpexpr(EXPR_END)), "loc_4ED2")
    MenuCmd(1, 0, "シールド　　　　購入済み")
    MenuCmd(3, 0, 0x0)
    Jump("loc_4EEE")

    label("loc_4ED2")

    MenuCmd(1, 0, "シールド　　　　1000ミラ")

    label("loc_4EEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE3, 0x0)"), scpexpr(EXPR_END)), "loc_4F1E")
    MenuCmd(1, 0, "カノン　　　　　購入済み")
    MenuCmd(3, 0, 0x1)
    Jump("loc_4F3A")

    label("loc_4F1E")

    MenuCmd(1, 0, "カノン　　　　　1000ミラ")

    label("loc_4F3A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xDC, 0x0)"), scpexpr(EXPR_END)), "loc_4F6A")
    MenuCmd(1, 0, "フォース　　　　購入済み")
    MenuCmd(3, 0, 0x2)
    Jump("loc_4F86")

    label("loc_4F6A")

    MenuCmd(1, 0, "フォース　　　　1000ミラ")

    label("loc_4F86")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xDE, 0x0)"), scpexpr(EXPR_END)), "loc_4FB6")
    MenuCmd(1, 0, "ピクシィ　　　　購入済み")
    MenuCmd(3, 0, 0x3)
    Jump("loc_4FD2")

    label("loc_4FB6")

    MenuCmd(1, 0, "ピクシィ　　　　1000ミラ")

    label("loc_4FD2")

    MenuCmd(1, 0, "やめる")

    #A0099
    AnonymousTalk(
        0x0,
        (
            scpstr(0x18),
            "どれを購入しますか～？\x02",
        )
    )

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5027")
    Sleep(1)
    Return()

    label("loc_5027")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50C7")

    #A0100
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "地属性のマスタークオーツです。\x01",
            "※DEF/ADF強化?戦闘開始時とピンチ時に「DEF/ADFアップ」\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51F7")

    label("loc_50C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5128")

    #A0101
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "水属性のマスタークオーツです。\x01",
            "※ATS強化?ＨＰ回復魔法の効果がアップ\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51F7")

    label("loc_5128")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5192")

    #A0102
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "火属性のマスタークオーツです。\x01",
            "※STR強化?戦闘開始時とピンチ時に「STRアップ」\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51F7")

    label("loc_5192")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51F7")

    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "風属性のマスタークオーツです。\x01",
            "※ATS強化?戦闘開始時とピンチ時に「ATSアップ」\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51F7")


    #A0104
    AnonymousTalk(
        0x0,
        "はい、これでいいですか～？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【購入する】\x01",        # 0
            "【やめておく】\x01",      # 1
        )
    )

    MenuEnd(0x4)
    OP_60(0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5524")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52F0")

    #C0105
    ChrTalk(
        0x0,
        (
            "あれ～、ミラが足りないみたいですよ？\x01",
            "それじゃ購入はできないですぅ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5515")

    label("loc_52F0")


    #C0106
    ChrTalk(
        0x0,
        (
            "了解ですぅ。\x01",
            "ちょっと待っててくださいですぅ～㈱\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(71, 0, 100, 0)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0107
    ChrTalk(
        0x0,
        "はい、お待たせですぅ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53C0")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0108
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xDD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xDD, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_54DE")

    label("loc_53C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5421")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0109
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xE3, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_54DE")

    label("loc_5421")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5482")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0110
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xDC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xDC, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_54DE")

    label("loc_5482")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54DE")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0111
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xDE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xDE, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_54DE")


    #C0112
    ChrTalk(
        0x0,
        (
            "ふふ、またのご利用を\x01",
            "お待ちしてま～す。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_5515")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_552E")

    label("loc_5524")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_552E")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_4E90")

    label("loc_5541")

    Return()

    # Function_28_4E86 end

    def Function_29_5542(): pass

    label("Function_29_5542")

    OP_AF(0x32)
    Return()

    # Function_29_5542 end

    def Function_30_5545(): pass

    label("Function_30_5545")

    OP_AF(0x12)
    Return()

    # Function_30_5545 end

    def Function_31_5548(): pass

    label("Function_31_5548")

    OP_AF(0x3E)
    Return()

    # Function_31_5548 end

    def Function_32_554B(): pass

    label("Function_32_554B")

    Return()

    # Function_32_554B end

    def Function_33_554C(): pass

    label("Function_33_554C")

    OP_AF(0xAE)
    Return()

    # Function_33_554C end

    def Function_34_554F(): pass

    label("Function_34_554F")

    MenuCmd(0, 2)
    MenuCmd(1, 2, "項目01")
    MenuCmd(1, 2, "項目02")
    MenuCmd(1, 2, "項目03")
    MenuCmd(1, 2, "項目04")
    MenuCmd(1, 2, "項目05")
    MenuCmd(1, 2, "項目06")
    MenuCmd(1, 2, "項目07")
    MenuCmd(1, 2, "項目08")
    MenuCmd(1, 2, "項目09")
    MenuCmd(1, 2, "項目10")
    MenuCmd(1, 2, "項目11")
    MenuCmd(1, 2, "項目12")
    MenuCmd(1, 2, "項目13")
    MenuCmd(1, 2, "項目14")
    MenuCmd(1, 2, "項目15")
    MenuCmd(1, 2, "項目16")
    MenuCmd(3, 2, 0x1)
    MenuCmd(3, 2, 0x8)
    MenuCmd(3, 2, 0x5)
    MenuCmd(3, 2, 0xE)
    MenuCmd(3, 2, 0xF)
    MenuCmd(3, 2, 0x9)
    MenuCmd(2, 2, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x2)
    Return()

    # Function_34_554F end

    def Function_35_5619(): pass

    label("Function_35_5619")

    EventBegin(0x1)

    #C0113
    ChrTalk(
        0x0,
        "#1001Fここなら何か釣れそうね。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0114
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣りをしますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        10,
        32,
        1,
        (
            "釣りをする\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    WaitChrThread(0x0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56BA")
    MiniGame(0x6, 0x1, 0x4B834, 0xFFFFFFBA, 0x4BB4, 0x5A, 0xFFFFFF38, 0x0, 0xFFFFF768)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_56CB")

    label("loc_56BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56CB")
    EventEnd(0x1)

    label("loc_56CB")

    Return()

    # Function_35_5619 end

    def Function_36_56CC(): pass

    label("Function_36_56CC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5950")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "基本装備\x01",                      # 0
            "魔法?クラフト\x01",                 # 1
            "捜査手帳／戦闘手帳\x01",            # 2
            "レシピ手帳／料理\x01",              # 3
            "釣り\x01",                          # 4
            "改造関係\x01",                      # 5
            "イベントアイテム\x01",              # 6
            "ＤＰセット\x01",                    # 7
            "その他\x01",                        # 8
            "ランダムテスト\x01",                # 9
            "２周目フラグを立てる\x01",          # 10
            "クリアフラグを立てる\x01",          # 11
            "「ポムっと」インストール\x01",      # 12
            "シグムント戦闘時間短縮\x01",        # 13
            "実績いくつか\x01",                  # 14
            "キャンセル\x01",                    # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5842"),
        (1, "loc_584A"),
        (2, "loc_5852"),
        (3, "loc_585A"),
        (4, "loc_5862"),
        (5, "loc_586A"),
        (6, "loc_5872"),
        (7, "loc_587A"),
        (8, "loc_5882"),
        (9, "loc_588A"),
        (10, "loc_5892"),
        (11, "loc_58AA"),
        (12, "loc_58CD"),
        (13, "loc_5906"),
        (14, "loc_591E"),
        (SWITCH_DEFAULT, "loc_5941"),
    )


    label("loc_5842")

    Call(0, 37)
    Jump("loc_594B")

    label("loc_584A")

    Call(0, 38)
    Jump("loc_594B")

    label("loc_5852")

    Call(0, 39)
    Jump("loc_594B")

    label("loc_585A")

    Call(0, 40)
    Jump("loc_594B")

    label("loc_5862")

    Call(0, 41)
    Jump("loc_594B")

    label("loc_586A")

    Call(0, 42)
    Jump("loc_594B")

    label("loc_5872")

    Call(0, 43)
    Jump("loc_594B")

    label("loc_587A")

    Call(0, 44)
    Jump("loc_594B")

    label("loc_5882")

    Call(0, 45)
    Jump("loc_594B")

    label("loc_588A")

    Call(0, 46)
    Jump("loc_594B")

    label("loc_5892")

    SetScenarioFlags(0x20, 7)

    #C0115
    ChrTalk(
        0x0,
        "２周目開始\x02",
    )

    CloseMessageWindow()
    Jump("loc_594B")

    label("loc_58AA")

    SetScenarioFlags(0x20, 1)

    #C0116
    ChrTalk(
        0x0,
        "クリアした可能性アリ\x02",
    )

    CloseMessageWindow()
    ShowSaveClearMenu()
    Jump("loc_594B")

    label("loc_58CD")

    SetScenarioFlags(0x27, 2)
    SetScenarioFlags(0x27, 3)
    OP_E4(0x3)

    #C0117
    ChrTalk(
        0x0,
        "ポムっとを端末にインストールしました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_594B")

    label("loc_5906")

    SetScenarioFlags(0x21, 3)

    #C0118
    ChrTalk(
        0x0,
        "したずら。\x02",
    )

    CloseMessageWindow()
    Jump("loc_594B")

    label("loc_591E")

    OP_E0(0x1C, 0x0)
    OP_E0(0x1D, 0x0)
    OP_E0(0x1E, 0x0)
    OP_E0(0x1F, 0x0)
    OP_E0(0x20, 0x0)
    OP_E0(0x21, 0x0)
    OP_E0(0x22, 0x0)
    OP_E0(0x23, 0x0)
    OP_E0(0x2B, 0x0)
    OP_E0(0x2C, 0x0)
    Jump("loc_594B")

    label("loc_5941")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_594B")

    Jump("loc_56D6")

    label("loc_5950")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_36_56CC end

    def Function_37_595E(): pass

    label("Function_37_595E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5968")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CA6")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "序章基本装備(レベル45)\x01",         # 0
            "１章基本装備(レベル50)\x01",         # 1
            "２章基本装備(レベル54)\x01",         # 2
            "３章基本装備(レベル57)\x01",         # 3
            "４章基本装備(レベル65)\x01",         # 4
            "断章基本装備(レベル68)\x01",         # 5
            "終章基本装備(レベル69)\x01",         # 6
            "ラスボス戦装備(レベル115)\x01",      # 7
            "ツァイト神獣化\x01",                 # 8
            "衣装変更\x01",                       # 9
            "キャンセル\x01",                     # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5AA7"),
        (1, "loc_5AE0"),
        (2, "loc_5B0D"),
        (3, "loc_5B3A"),
        (4, "loc_5B67"),
        (5, "loc_5B94"),
        (6, "loc_5BC1"),
        (7, "loc_5BEE"),
        (8, "loc_5C4B"),
        (9, "loc_5C57"),
        (SWITCH_DEFAULT, "loc_5C97"),
    )


    label("loc_5AA7")

    Call(1, 68)
    Call(1, 50)
    Call(1, 64)
    Call(1, 62)
    Call(1, 66)
    SetChrName("")

    #A0119
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "序章開始時の装備です。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5CA1")

    label("loc_5AE0")

    Call(1, 69)
    SetChrName("")

    #A0120
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "１章開始時の装備です。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5CA1")

    label("loc_5B0D")

    Call(1, 70)
    SetChrName("")

    #A0121
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "２章開始時の装備です。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5CA1")

    label("loc_5B3A")

    Call(1, 71)
    SetChrName("")

    #A0122
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "３章開始時の装備です。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5CA1")

    label("loc_5B67")

    Call(1, 72)
    SetChrName("")

    #A0123
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "４章開始時の装備です。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5CA1")

    label("loc_5B94")

    Call(1, 73)
    SetChrName("")

    #A0124
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "断章開始時の装備です。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5CA1")

    label("loc_5BC1")

    Call(1, 74)
    SetChrName("")

    #A0125
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "終章開始時の装備です。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5CA1")

    label("loc_5BEE")

    Call(1, 75)
    Call(1, 49)
    Call(1, 50)
    Call(1, 52)
    Call(1, 54)
    Call(1, 56)
    Call(1, 58)
    Call(1, 63)
    Call(1, 64)
    Call(1, 66)
    Call(1, 51)
    Call(1, 53)
    Call(1, 55)
    Call(1, 57)
    Call(1, 59)
    Call(1, 65)
    Call(1, 67)
    SetChrName("")

    #A0126
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ラスボス戦の装備です。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5CA1")

    label("loc_5C4B")

    SetScenarioFlags(0x20, 3)
    AddCraft(0x2, 0xB1)
    Jump("loc_5CA1")

    label("loc_5C57")


    #C0127
    ChrTalk(
        0x0,
        (
            "ワジを星杯騎士に変更\x01",
            "銀をリーシャに変更\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipPat(0x4, 0x1, 0x1F)
    SetChrChipPat(0x5, 0x1, 0x20)
    Jump("loc_5CA1")

    label("loc_5C97")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CA1")

    Jump("loc_5968")

    label("loc_5CA6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_37_595E end

    def Function_38_5CB4(): pass

    label("Function_38_5CB4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65A1")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "オーブメント開放最小\x01",              # 0
            "オーブメント開放ＡＬＬ１\x01",          # 1
            "オーブメント開放ＡＬＬ２\x01",          # 2
            "全員魔法無し\x01",                      # 3
            "魔法コンプ４人分\x01",                  # 4
            "全クオーツ入手\x01",                    # 5
            "クラフト初期化\x01",                    # 6
            "クラフト前編\x01",                      # 7
            "クラフトコンプ10人分\x01",              # 8
            "コンビクラフト取得\x01",                # 9
            "コンビクラフトⅡ取得\x01",              # 10
            "コンビクラフトⅢ取得\x01",              # 11
            "非装備マスタークオーツ捨てる\x01",      # 12
            "ロイド?マスターアーツ習得\x01",         # 13
            "キャンセル\x01",                        # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5E5B"),
        (1, "loc_5EA7"),
        (2, "loc_5F25"),
        (3, "loc_5F83"),
        (4, "loc_6003"),
        (5, "loc_6095"),
        (6, "loc_60CA"),
        (7, "loc_60FF"),
        (8, "loc_6154"),
        (9, "loc_61BF"),
        (10, "loc_624C"),
        (11, "loc_62BE"),
        (12, "loc_62DB"),
        (13, "loc_64A8"),
        (SWITCH_DEFAULT, "loc_6592"),
    )


    label("loc_5E5B")

    Call(1, 43)
    OP_38(0x0, 0x80, 0x2)
    OP_38(0x1, 0x80, 0x2)
    OP_38(0x2, 0x80, 0x2)
    OP_38(0x3, 0x80, 0x2)
    OP_38(0x4, 0x80, 0x2)
    OP_38(0x5, 0x80, 0x2)
    OP_38(0x8, 0x80, 0x2)
    OP_38(0x9, 0x80, 0x2)
    SetChrName("")

    #A0128
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "中央のみ開いています。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_659C")

    label("loc_5EA7")

    Call(1, 43)
    OP_38(0x0, 0x7F, 0x1)
    OP_38(0x1, 0x7F, 0x1)
    OP_38(0x2, 0x7F, 0x1)
    OP_38(0x3, 0x7F, 0x1)
    OP_38(0x4, 0x7F, 0x1)
    OP_38(0x5, 0x7F, 0x1)
    OP_38(0x8, 0x7F, 0x1)
    OP_38(0x9, 0x7F, 0x1)
    OP_38(0x0, 0x80, 0x2)
    OP_38(0x1, 0x80, 0x2)
    OP_38(0x2, 0x80, 0x2)
    OP_38(0x3, 0x80, 0x2)
    OP_38(0x4, 0x80, 0x2)
    OP_38(0x5, 0x80, 0x2)
    OP_38(0x8, 0x80, 0x2)
    OP_38(0x9, 0x80, 0x2)
    SetChrName("")

    #A0129
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメント盤を全てレベル１にしました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_659C")

    label("loc_5F25")

    Call(1, 43)
    OP_38(0x0, 0x7F, 0x2)
    OP_38(0x1, 0x7F, 0x2)
    OP_38(0x2, 0x7F, 0x2)
    OP_38(0x3, 0x7F, 0x2)
    OP_38(0x4, 0x7F, 0x2)
    OP_38(0x5, 0x7F, 0x2)
    OP_38(0x8, 0x7F, 0x2)
    OP_38(0x9, 0x7F, 0x2)
    SetChrName("")

    #A0130
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメント盤を全てレベル２にしました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_659C")

    label("loc_5F83")

    Call(1, 44)
    SetChrName("")

    #A0131
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての魔法を消去しました。\x01",
            "クオーツを装備しなおすと、\x01",
            "装備しているクオーツに合わせて再取得してしまいます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_659C")

    label("loc_6003")

    Call(1, 44)
    Call(1, 45)
    Call(1, 46)
    Call(1, 47)
    Call(1, 48)
    SetChrName("")

    #A0132
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての魔法を４人が取得しました。\x01",
            "クオーツを装備しなおすと、\x01",
            "装備しているクオーツに合わせて再取得してしまいます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_659C")

    label("loc_6095")

    Call(1, 93)
    SetChrName("")

    #A0133
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのクオーツを入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_659C")

    label("loc_60CA")

    Call(1, 49)
    SetChrName("")

    #A0134
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのクラフトを消去しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_659C")

    label("loc_60FF")

    Call(1, 49)
    Call(1, 50)
    Call(1, 52)
    Call(1, 54)
    Call(1, 56)
    Call(1, 58)
    Call(1, 60)
    Call(1, 62)
    Call(1, 63)
    Call(1, 64)
    Call(1, 66)
    SetChrName("")

    #A0135
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クラフト第１段階を入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_659C")

    label("loc_6154")

    Call(1, 49)
    Call(1, 50)
    Call(1, 51)
    Call(1, 52)
    Call(1, 53)
    Call(1, 54)
    Call(1, 55)
    Call(1, 56)
    Call(1, 57)
    Call(1, 58)
    Call(1, 59)
    Call(1, 60)
    Call(1, 61)
    Call(1, 62)
    Call(1, 63)
    Call(1, 64)
    Call(1, 65)
    Call(1, 66)
    Call(1, 67)
    SetChrName("")

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのクラフトを入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_659C")

    label("loc_61BF")

    AddCraft(0x0, 0x186)
    AddCraft(0x1, 0x186)
    AddCraft(0x0, 0x187)
    AddCraft(0x2, 0x187)
    AddCraft(0x0, 0x188)
    AddCraft(0x3, 0x188)
    AddCraft(0x1, 0x189)
    AddCraft(0x2, 0x189)
    AddCraft(0x1, 0x18A)
    AddCraft(0x3, 0x18A)
    AddCraft(0x2, 0x18B)
    AddCraft(0x3, 0x18B)
    AddCraft(0x0, 0x18C)
    AddCraft(0x8, 0x18C)
    AddCraft(0x0, 0x18D)
    AddCraft(0x4, 0x18D)
    AddCraft(0x1, 0x18E)
    AddCraft(0x8, 0x18E)
    AddCraft(0x1, 0x18F)
    AddCraft(0x4, 0x18F)
    AddCraft(0x2, 0x190)
    AddCraft(0x8, 0x190)
    AddCraft(0x2, 0x191)
    AddCraft(0x4, 0x191)
    AddCraft(0x3, 0x192)
    AddCraft(0x8, 0x192)
    AddCraft(0x3, 0x193)
    AddCraft(0x4, 0x193)
    AddCraft(0x8, 0x194)
    AddCraft(0x4, 0x194)
    AddCraft(0x0, 0x195)
    AddCraft(0x5, 0x195)
    AddCraft(0x0, 0x196)
    AddCraft(0x9, 0x196)
    Jump("loc_659C")

    label("loc_624C")

    AddCraft(0x0, 0x19A)
    AddCraft(0x1, 0x19A)
    AddCraft(0x0, 0x19B)
    AddCraft(0x2, 0x19B)
    AddCraft(0x0, 0x19C)
    AddCraft(0x3, 0x19C)
    AddCraft(0x0, 0x1A0)
    AddCraft(0x8, 0x1A0)
    AddCraft(0x0, 0x1A1)
    AddCraft(0x4, 0x1A1)
    AddCraft(0x0, 0x1A9)
    AddCraft(0x5, 0x1A9)
    AddCraft(0x0, 0x1AA)
    AddCraft(0x9, 0x1AA)
    SetChrName("")

    #A0137
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのコンビクラフト２を入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_659C")

    label("loc_62BE")

    AddCraft(0x0, 0x1AE)
    AddCraft(0x1, 0x1AE)
    AddCraft(0x0, 0x1AF)
    AddCraft(0x2, 0x1AF)
    AddCraft(0x0, 0x1B0)
    AddCraft(0x3, 0x1B0)
    Jump("loc_659C")

    label("loc_62DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xDC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62F1")
    SubItemNumber(0xDC, 1)

    label("loc_62F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xDD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6307")
    SubItemNumber(0xDD, 1)

    label("loc_6307")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xDE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_631D")
    SubItemNumber(0xDE, 1)

    label("loc_631D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xDF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6333")
    SubItemNumber(0xDF, 1)

    label("loc_6333")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6349")
    SubItemNumber(0xE0, 1)

    label("loc_6349")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_635F")
    SubItemNumber(0xE1, 1)

    label("loc_635F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6375")
    SubItemNumber(0xE2, 1)

    label("loc_6375")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_638B")
    SubItemNumber(0xE3, 1)

    label("loc_638B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63A1")
    SubItemNumber(0xE4, 1)

    label("loc_63A1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63B7")
    SubItemNumber(0xE5, 1)

    label("loc_63B7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE6, 0x0)"), scpexpr(EXPR_END)), "loc_63C7")
    SubItemNumber(0xE6, 1)

    label("loc_63C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63DD")
    SubItemNumber(0xE7, 1)

    label("loc_63DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63F3")
    SubItemNumber(0xE8, 1)

    label("loc_63F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6409")
    SubItemNumber(0xE9, 1)

    label("loc_6409")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xEA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_641F")
    SubItemNumber(0xEA, 1)

    label("loc_641F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xEB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6435")
    SubItemNumber(0xEB, 1)

    label("loc_6435")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xEC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_644B")
    SubItemNumber(0xEC, 1)

    label("loc_644B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xED, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6461")
    SubItemNumber(0xED, 1)

    label("loc_6461")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xEE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6477")
    SubItemNumber(0xEE, 1)

    label("loc_6477")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xEF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_648D")
    SubItemNumber(0xEF, 1)

    label("loc_648D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xF0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64A3")
    SubItemNumber(0xF0, 1)

    label("loc_64A3")

    Jump("loc_659C")

    label("loc_64A8")


    Menu(
        2,
        -1,
        -1,
        1,
        (
            "防壁のルーン\x01",      # 0
            "慈愛のルーン\x01",      # 1
            "勝利のルーン\x01",      # 2
            "暴風のルーン\x01",      # 3
            "刹那のルーン\x01",      # 4
            "震天のルーン\x01",      # 5
            "幻影のルーン\x01",      # 6
            "キャンセル\x01",        # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_654E"),
        (1, "loc_6557"),
        (2, "loc_6560"),
        (3, "loc_6569"),
        (4, "loc_6572"),
        (5, "loc_657B"),
        (6, "loc_6584"),
        (SWITCH_DEFAULT, "loc_658D"),
    )


    label("loc_654E")

    RemoveCraft(0x0, 0x12)
    Jump("loc_658D")

    label("loc_6557")

    RemoveCraft(0x0, 0x1C)
    Jump("loc_658D")

    label("loc_6560")

    RemoveCraft(0x0, 0x26)
    Jump("loc_658D")

    label("loc_6569")

    RemoveCraft(0x0, 0x30)
    Jump("loc_658D")

    label("loc_6572")

    RemoveCraft(0x0, 0x3A)
    Jump("loc_658D")

    label("loc_657B")

    RemoveCraft(0x0, 0x44)
    Jump("loc_658D")

    label("loc_6584")

    RemoveCraft(0x0, 0x4E)
    Jump("loc_658D")

    label("loc_658D")

    Jump("loc_659C")

    label("loc_6592")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_659C")

    Jump("loc_5CBE")

    label("loc_65A1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_38_5CB4 end

    def Function_39_65AF(): pass

    label("Function_39_65AF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6915")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "捜査手帳情報初期化\x01",          # 0
            "捜査手帳ＡＬＬコンプ\x01",        # 1
            "捜査手帳メインコンプ\x01",        # 2
            "捜査手帳サブコンプ\x01",          # 3
            "捜査手帳サブ受付のみ\x01",        # 4
            "捜査手帳サブ失敗\x01",            # 5
            "戦闘手帳情報初期化\x01",          # 6
            "戦闘手帳コンプ(全魔獣)\x01",      # 7
            "キャンセル\x01",                  # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_66B9"),
        (1, "loc_66ED"),
        (2, "loc_672B"),
        (3, "loc_6772"),
        (4, "loc_67B7"),
        (5, "loc_67FB"),
        (6, "loc_6844"),
        (7, "loc_68A2"),
        (SWITCH_DEFAULT, "loc_6906"),
    )


    label("loc_66B9")

    Call(1, 76)
    Call(1, 77)
    SetChrName("")

    #A0138
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "捜査手帳を初期化しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6910")

    label("loc_66ED")

    Call(1, 78)
    Call(1, 79)
    SetChrName("")

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "捜査手帳を全てコンプリートしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6910")

    label("loc_672B")

    Call(1, 78)
    SetChrName("")

    #A0140
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "捜査手帳のメインクエストをコンプリートしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6910")

    label("loc_6772")

    Call(1, 79)
    SetChrName("")

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "捜査手帳のサブクエストをコンプリートしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6910")

    label("loc_67B7")

    Call(1, 77)
    Call(1, 80)
    SetChrName("")

    #A0142
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "捜査手帳のサブクエストを受付だけしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6910")

    label("loc_67FB")

    Call(1, 77)
    Call(1, 80)
    Call(1, 81)
    SetChrName("")

    #A0143
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "捜査手帳のサブクエストを全て失敗にしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6910")

    label("loc_6844")

    SetChrName("")

    #A0144
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "戦闘手帳の初期化は、\x01",
            "[F5]メニューの6ページの MonsNote を使用してください。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6910")

    label("loc_68A2")

    SetChrName("")

    #A0145
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "戦闘手帳のコンプリートは、\x01",
            "[F5]メニューの6ページの MonsNote を使用してください。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6910")

    label("loc_6906")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6910")

    Jump("loc_65B9")

    label("loc_6915")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_39_65AF end

    def Function_40_6923(): pass

    label("Function_40_6923")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_692D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D05")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "レシピ情報初期化\x01",                    # 0
            "レシピ全てコンプリート\x01",              # 1
            "レシピ成功料理のみコンプリート\x01",      # 2
            "レシピ大成功のみコンプリート\x01",        # 3
            "レシピ予想外のみコンプリート\x01",        # 4
            "食材いっぱい入手(50個)\x01",              # 5
            "全料理アイテム入手(10個)\x01",            # 6
            "全予想外料理アイテム入手(1個)\x01",       # 7
            "レシピ入手、残り１個\x01",                # 8
            "キャンセル\x01",                          # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6A77"),
        (1, "loc_6AAC"),
        (2, "loc_6AF7"),
        (3, "loc_6B3E"),
        (4, "loc_6B87"),
        (5, "loc_6BD0"),
        (6, "loc_6C08"),
        (7, "loc_6C40"),
        (8, "loc_6C77"),
        (SWITCH_DEFAULT, "loc_6CF6"),
    )


    label("loc_6A77")

    OP_B2(0x0)
    SetChrName("")

    #A0146
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レシピ手帳を全て消去しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D00")

    label("loc_6AAC")

    Call(1, 82)
    Call(1, 83)
    Call(1, 84)
    SetChrName("")

    #A0147
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レシピ手帳の全ての料理をコンプリートしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D00")

    label("loc_6AF7")

    Call(1, 82)
    SetChrName("")

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レシピ手帳の「成功料理」をコンプリートしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D00")

    label("loc_6B3E")

    Call(1, 83)
    SetChrName("")

    #A0149
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レシピ手帳の「大成功料理」をコンプリートしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D00")

    label("loc_6B87")

    Call(1, 84)
    SetChrName("")

    #A0150
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レシピ手帳の「予想外料理」をコンプリートしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D00")

    label("loc_6BD0")

    Call(1, 85)
    SetChrName("")

    #A0151
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての食材を 50ずつ入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D00")

    label("loc_6C08")

    Call(1, 86)
    SetChrName("")

    #A0152
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての料理を 50ずつ入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D00")

    label("loc_6C40")

    Call(1, 87)
    SetChrName("")

    #A0153
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "予想外料理を 1ずつ入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D00")

    label("loc_6C77")

    OP_B2(0x1)
    OP_B2(0x3)
    OP_B2(0x4)
    OP_B2(0x5)
    OP_B2(0x6)
    OP_B2(0x7)
    OP_B2(0x8)
    OP_B2(0x9)
    OP_B2(0xA)
    OP_B2(0xB)
    OP_B2(0xC)
    OP_B2(0xD)
    OP_B2(0xE)
    OP_B2(0xF)
    OP_B2(0x10)
    OP_B2(0x11)
    OP_B2(0x12)
    OP_B2(0x13)
    OP_B2(0x14)
    OP_B2(0x15)
    OP_B2(0x16)
    OP_B2(0x17)
    OP_B2(0x18)
    SetChrName("")

    #A0154
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "チャンホイ以外のレシピを入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D00")

    label("loc_6CF6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D00")

    Jump("loc_692D")

    label("loc_6D05")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_40_6923 end

    def Function_41_6D13(): pass

    label("Function_41_6D13")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75C6")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "釣り情報初期化\x01",                # 0
            "釣り情報コンプ(全魚)\x01",          # 1
            "釣り竿全部入手\x01",                # 2
            "釣りエサ全部入手\x01",              # 3
            "釣り魚全部入手\x01",                # 4
            "釣り魚個別入手①手帳記載\x01",      # 5
            "釣り魚個別入手②手帳記載\x01",      # 6
            "釣り魚全破棄\x01",                  # 7
            "ゲームフィッシュ取得\x01",          # 8
            "４天皇倒す\x01",                    # 9
            "レイクロード倒す\x01",              # 10
            "キャンセル\x01",                    # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6E52"),
        (1, "loc_6EB0"),
        (2, "loc_6F14"),
        (3, "loc_6F57"),
        (4, "loc_6FF6"),
        (5, "loc_7096"),
        (6, "loc_7294"),
        (7, "loc_74C9"),
        (8, "loc_7569"),
        (9, "loc_759E"),
        (10, "loc_75AF"),
        (SWITCH_DEFAULT, "loc_75B7"),
    )


    label("loc_6E52")

    SetChrName("")

    #A0155
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣り手帳の初期化は、\x01",
            "[F5]メニューの6ページの FishNote を使用してください。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_75C1")

    label("loc_6EB0")

    SetChrName("")

    #A0156
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣り手帳のコンプリートは、\x01",
            "[F5]メニューの6ページの FishNote を使用してください。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_75C1")

    label("loc_6F14")

    AddItemNumber(0x32, 1)
    AddItemNumber(0x33, 1)
    AddItemNumber(0x34, 1)
    AddItemNumber(0x35, 1)
    AddItemNumber(0x37, 1)
    SetChrName("")

    #A0157
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての釣竿を入手した。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_75C1")

    label("loc_6F57")

    AddItemNumber(0x186, 10)
    AddItemNumber(0x187, 10)
    AddItemNumber(0x188, 10)
    AddItemNumber(0x189, 10)
    AddItemNumber(0x18A, 10)
    AddItemNumber(0x18B, 10)
    AddItemNumber(0x18C, 10)
    AddItemNumber(0x18D, 10)
    AddItemNumber(0x15E, 10)
    AddItemNumber(0x162, 10)
    AddItemNumber(0x165, 10)
    AddItemNumber(0x167, 10)
    AddItemNumber(0x168, 10)
    AddItemNumber(0x169, 10)
    AddItemNumber(0x16C, 10)
    AddItemNumber(0x16D, 10)
    SetChrName("")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのエサを入手した。\x01",
            "エサとして使用できる魚も入手します。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_75C1")

    label("loc_6FF6")

    AddItemNumber(0x15E, 10)
    AddItemNumber(0x15F, 10)
    AddItemNumber(0x160, 10)
    AddItemNumber(0x161, 10)
    AddItemNumber(0x162, 10)
    AddItemNumber(0x163, 10)
    AddItemNumber(0x164, 10)
    AddItemNumber(0x165, 10)
    AddItemNumber(0x166, 10)
    AddItemNumber(0x167, 10)
    AddItemNumber(0x168, 10)
    AddItemNumber(0x169, 10)
    AddItemNumber(0x16A, 10)
    AddItemNumber(0x16B, 10)
    AddItemNumber(0x16C, 10)
    AddItemNumber(0x16D, 10)
    AddItemNumber(0x16E, 10)
    AddItemNumber(0x16F, 10)
    AddItemNumber(0x170, 10)
    AddItemNumber(0x171, 10)
    AddItemNumber(0x172, 10)
    AddItemNumber(0x173, 10)
    AddItemNumber(0x174, 10)
    AddItemNumber(0x175, 10)
    SetChrName("")

    #A0159
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての魚を入手した。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_75C1")

    label("loc_7096")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_728F")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "ファイタ\x01",            # 0
            "スノーシュラブ\x01",      # 1
            "エーゼル\x01",            # 2
            "カサギン\x01",            # 3
            "アルモリカブナ\x01",      # 4
            "トタス\x01",              # 5
            "オロショ\x01",            # 6
            "ロック\x01",              # 7
            "レインボウ\x01",          # 8
            "ピラーニャ\x01",          # 9
            "カルプ\x01",              # 10
            "グラトンバス\x01",        # 11
            "トラード\x01",            # 12
            "グラディエタ\x01",        # 13
            "レイニー\x01",            # 14
        )
    )

    MenuEnd(0x4)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_71B8"),
        (1, "loc_71C5"),
        (2, "loc_71D2"),
        (3, "loc_71DF"),
        (4, "loc_71EC"),
        (5, "loc_71F9"),
        (6, "loc_7206"),
        (7, "loc_7213"),
        (8, "loc_7220"),
        (9, "loc_722D"),
        (10, "loc_723A"),
        (11, "loc_7247"),
        (12, "loc_7254"),
        (13, "loc_7261"),
        (14, "loc_726E"),
        (SWITCH_DEFAULT, "loc_727B"),
    )


    label("loc_71B8")

    AddItemNumber(0x15E, 1)
    OP_E4(0x2, 0x0)
    Jump("loc_728A")

    label("loc_71C5")

    AddItemNumber(0x15F, 1)
    OP_E4(0x2, 0x1)
    Jump("loc_728A")

    label("loc_71D2")

    AddItemNumber(0x160, 1)
    OP_E4(0x2, 0x2)
    Jump("loc_728A")

    label("loc_71DF")

    AddItemNumber(0x161, 1)
    OP_E4(0x2, 0x3)
    Jump("loc_728A")

    label("loc_71EC")

    AddItemNumber(0x162, 1)
    OP_E4(0x2, 0x4)
    Jump("loc_728A")

    label("loc_71F9")

    AddItemNumber(0x163, 1)
    OP_E4(0x2, 0x5)
    Jump("loc_728A")

    label("loc_7206")

    AddItemNumber(0x164, 1)
    OP_E4(0x2, 0x6)
    Jump("loc_728A")

    label("loc_7213")

    AddItemNumber(0x165, 1)
    OP_E4(0x2, 0x7)
    Jump("loc_728A")

    label("loc_7220")

    AddItemNumber(0x166, 1)
    OP_E4(0x2, 0x8)
    Jump("loc_728A")

    label("loc_722D")

    AddItemNumber(0x167, 1)
    OP_E4(0x2, 0x9)
    Jump("loc_728A")

    label("loc_723A")

    AddItemNumber(0x168, 1)
    OP_E4(0x2, 0xA)
    Jump("loc_728A")

    label("loc_7247")

    AddItemNumber(0x169, 1)
    OP_E4(0x2, 0xB)
    Jump("loc_728A")

    label("loc_7254")

    AddItemNumber(0x16A, 1)
    OP_E4(0x2, 0xC)
    Jump("loc_728A")

    label("loc_7261")

    AddItemNumber(0x16B, 1)
    OP_E4(0x2, 0xD)
    Jump("loc_728A")

    label("loc_726E")

    AddItemNumber(0x16C, 1)
    OP_E4(0x2, 0xE)
    Jump("loc_728A")

    label("loc_727B")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_728A")

    label("loc_728A")

    Jump("loc_70A0")

    label("loc_728F")

    Jump("loc_75C1")

    label("loc_7294")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_729E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74C4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "サンショ\x01",              # 0
            "サモーナ\x01",              # 1
            "アローナ\x01",              # 2
            "イール\x01",                # 3
            "アダマンタス\x01",          # 4
            "クインシザー\x01",          # 5
            "パルルク\x01",              # 6
            "タイタン\x01",              # 7
            "ゴルドサモーナ\x01",        # 8
            "オオザンショ\x01",          # 9
            "ノーブルカルプ\x01",        # 10
            "エメロド\x01",              # 11
            "ティガロック\x01",          # 12
            "クリムゾンイータ\x01",      # 13
            "ブルドラゴン\x01",          # 14
            "ギガルーク\x01",            # 15
        )
    )

    MenuEnd(0x4)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_73E5"),
        (1, "loc_73F2"),
        (2, "loc_73FF"),
        (3, "loc_740C"),
        (4, "loc_7419"),
        (5, "loc_7426"),
        (6, "loc_7433"),
        (7, "loc_7440"),
        (8, "loc_744D"),
        (9, "loc_745A"),
        (10, "loc_7467"),
        (11, "loc_7474"),
        (12, "loc_7481"),
        (13, "loc_748E"),
        (14, "loc_749B"),
        (15, "loc_74A8"),
        (SWITCH_DEFAULT, "loc_74B5"),
    )


    label("loc_73E5")

    AddItemNumber(0x16D, 1)
    OP_E4(0x2, 0xF)
    Jump("loc_74BF")

    label("loc_73F2")

    AddItemNumber(0x16E, 1)
    OP_E4(0x2, 0x10)
    Jump("loc_74BF")

    label("loc_73FF")

    AddItemNumber(0x16F, 1)
    OP_E4(0x2, 0x11)
    Jump("loc_74BF")

    label("loc_740C")

    AddItemNumber(0x170, 1)
    OP_E4(0x2, 0x12)
    Jump("loc_74BF")

    label("loc_7419")

    AddItemNumber(0x171, 1)
    OP_E4(0x2, 0x13)
    Jump("loc_74BF")

    label("loc_7426")

    AddItemNumber(0x172, 1)
    OP_E4(0x2, 0x14)
    Jump("loc_74BF")

    label("loc_7433")

    AddItemNumber(0x173, 1)
    OP_E4(0x2, 0x15)
    Jump("loc_74BF")

    label("loc_7440")

    AddItemNumber(0x174, 1)
    OP_E4(0x2, 0x16)
    Jump("loc_74BF")

    label("loc_744D")

    AddItemNumber(0x175, 1)
    OP_E4(0x2, 0x17)
    Jump("loc_74BF")

    label("loc_745A")

    AddItemNumber(0x176, 1)
    OP_E4(0x2, 0x18)
    Jump("loc_74BF")

    label("loc_7467")

    AddItemNumber(0x177, 1)
    OP_E4(0x2, 0x19)
    Jump("loc_74BF")

    label("loc_7474")

    AddItemNumber(0x178, 1)
    OP_E4(0x2, 0x1A)
    Jump("loc_74BF")

    label("loc_7481")

    AddItemNumber(0x179, 1)
    OP_E4(0x2, 0x1B)
    Jump("loc_74BF")

    label("loc_748E")

    AddItemNumber(0x17A, 1)
    OP_E4(0x2, 0x1C)
    Jump("loc_74BF")

    label("loc_749B")

    AddItemNumber(0x17B, 1)
    OP_E4(0x2, 0x1D)
    Jump("loc_74BF")

    label("loc_74A8")

    AddItemNumber(0x17C, 1)
    OP_E4(0x2, 0x1E)
    Jump("loc_74BF")

    label("loc_74B5")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_74BF")

    Jump("loc_729E")

    label("loc_74C4")

    Jump("loc_75C1")

    label("loc_74C9")

    SubItemNumber(0x15E, 1)
    SubItemNumber(0x15F, 1)
    SubItemNumber(0x160, 1)
    SubItemNumber(0x161, 1)
    SubItemNumber(0x162, 1)
    SubItemNumber(0x163, 1)
    SubItemNumber(0x164, 1)
    SubItemNumber(0x165, 1)
    SubItemNumber(0x166, 1)
    SubItemNumber(0x167, 1)
    SubItemNumber(0x168, 1)
    SubItemNumber(0x169, 1)
    SubItemNumber(0x16A, 1)
    SubItemNumber(0x16B, 1)
    SubItemNumber(0x16C, 1)
    SubItemNumber(0x16D, 1)
    SubItemNumber(0x16E, 1)
    SubItemNumber(0x16F, 1)
    SubItemNumber(0x170, 1)
    SubItemNumber(0x171, 1)
    SubItemNumber(0x172, 1)
    SubItemNumber(0x173, 1)
    SubItemNumber(0x174, 1)
    SubItemNumber(0x175, 1)
    SubItemNumber(0x176, 1)
    SubItemNumber(0x177, 1)
    SubItemNumber(0x178, 1)
    SubItemNumber(0x179, 1)
    SubItemNumber(0x17A, 1)
    SubItemNumber(0x17B, 1)
    SubItemNumber(0x17C, 1)
    Jump("loc_75C1")

    label("loc_7569")

    AddItemNumber(0x169, 1)
    OP_E4(0x2, 0xB)
    AddItemNumber(0x165, 1)
    OP_E4(0x2, 0x7)
    AddItemNumber(0x162, 1)
    OP_E4(0x2, 0x4)
    AddItemNumber(0x167, 1)
    OP_E4(0x2, 0x9)
    AddItemNumber(0x16F, 1)
    OP_E4(0x2, 0x11)
    AddItemNumber(0x173, 1)
    OP_E4(0x2, 0x15)
    Jump("loc_75C1")

    label("loc_759E")

    SetScenarioFlags(0x1C0, 3)
    SetScenarioFlags(0x1C0, 4)
    SetScenarioFlags(0x1C0, 5)
    SetScenarioFlags(0x1C0, 6)
    Jump("loc_75C1")

    label("loc_75AF")

    SetScenarioFlags(0x191, 1)
    Jump("loc_75C1")

    label("loc_75B7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_75C1")

    Jump("loc_6D1D")

    label("loc_75C6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_41_6D13 end

    def Function_42_75D4(): pass

    label("Function_42_75D4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_75DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7699")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Ｕマテリアル\x01",          # 0
            "デヴァインクロス\x01",      # 1
            "ゼムリアストーン\x01",      # 2
            "Ｔマテリアル\x01",          # 3
            "キャンセル\x01",            # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7662"),
        (1, "loc_766C"),
        (2, "loc_7676"),
        (3, "loc_7680"),
        (SWITCH_DEFAULT, "loc_768A"),
    )


    label("loc_7662")

    AddItemNumber(0x38E, 10)
    Jump("loc_7694")

    label("loc_766C")

    AddItemNumber(0x395, 10)
    Jump("loc_7694")

    label("loc_7676")

    AddItemNumber(0x396, 10)
    Jump("loc_7694")

    label("loc_7680")

    AddItemNumber(0x397, 10)
    Jump("loc_7694")

    label("loc_768A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7694")

    Jump("loc_75DE")

    label("loc_7699")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_42_75D4 end

    def Function_43_76A7(): pass

    label("Function_43_76A7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_76B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7967")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "研究棟認証カード\x01",            # 0
            "自室家具一式\x01",                # 1
            "小説全巻\x01",                    # 2
            "小説?１巻抜き\x01",               # 3
            "クロスベルタイムズ全巻\x01",      # 4
            "自治州の地図\x01",                # 5
            "クロスベル市の地図\x01",          # 6
            "街区ジャンプＯＮ\x01",            # 7
            "街区ジャンプＯＦＦ\x01",          # 8
            "GAMESTART_ON\x01",                # 9
            "キャンセル\x01",                  # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_77BA"),
        (1, "loc_77C4"),
        (2, "loc_77F1"),
        (3, "loc_783C"),
        (4, "loc_7887"),
        (5, "loc_78C8"),
        (6, "loc_78D2"),
        (7, "loc_78FA"),
        (8, "loc_7905"),
        (9, "loc_7910"),
        (SWITCH_DEFAULT, "loc_7918"),
    )


    label("loc_77BA")

    AddItemNumber(0x335, 1)
    Jump("loc_7922")

    label("loc_77C4")

    AddItemNumber(0x350, 1)
    AddItemNumber(0x351, 1)
    AddItemNumber(0x352, 1)
    AddItemNumber(0x353, 1)
    AddItemNumber(0x354, 1)
    AddItemNumber(0x355, 1)
    AddItemNumber(0x356, 1)
    AddItemNumber(0x357, 1)
    Jump("loc_7922")

    label("loc_77F1")

    AddItemNumber(0x2C6, 1)
    AddItemNumber(0x2C7, 1)
    AddItemNumber(0x2C8, 1)
    AddItemNumber(0x2C9, 1)
    AddItemNumber(0x2CA, 1)
    AddItemNumber(0x2CB, 1)
    AddItemNumber(0x2CC, 1)
    AddItemNumber(0x2CD, 1)
    AddItemNumber(0x2CE, 1)
    AddItemNumber(0x2CF, 1)
    AddItemNumber(0x2D0, 1)
    AddItemNumber(0x2D1, 1)
    AddItemNumber(0x2D2, 1)
    AddItemNumber(0x2D3, 1)
    Jump("loc_7922")

    label("loc_783C")

    SubItemNumber(0x2C6, 99)
    AddItemNumber(0x2C7, 1)
    AddItemNumber(0x2C8, 1)
    AddItemNumber(0x2C9, 1)
    AddItemNumber(0x2CA, 1)
    AddItemNumber(0x2CB, 1)
    AddItemNumber(0x2CC, 1)
    AddItemNumber(0x2CD, 1)
    AddItemNumber(0x2CE, 1)
    AddItemNumber(0x2CF, 1)
    AddItemNumber(0x2D0, 1)
    AddItemNumber(0x2D1, 1)
    AddItemNumber(0x2D2, 1)
    AddItemNumber(0x2D3, 1)
    Jump("loc_7922")

    label("loc_7887")

    AddItemNumber(0x2E1, 1)
    AddItemNumber(0x2E2, 1)
    AddItemNumber(0x2E3, 1)
    AddItemNumber(0x2E4, 1)
    AddItemNumber(0x2E5, 1)
    AddItemNumber(0x2E6, 1)
    AddItemNumber(0x2E7, 1)
    AddItemNumber(0x2E8, 1)
    AddItemNumber(0x2E9, 1)
    AddItemNumber(0x2EA, 1)
    AddItemNumber(0x2EB, 1)
    AddItemNumber(0x2EC, 1)
    Jump("loc_7922")

    label("loc_78C8")

    AddItemNumber(0x5, 1)
    Jump("loc_7922")

    label("loc_78D2")

    SetChrName("")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そんな物はないです。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7922")

    label("loc_78FA")

    OP_C9(0x0, 0x1000)
    Jump("loc_7922")

    label("loc_7905")

    OP_C9(0x1, 0x1000)
    Jump("loc_7922")

    label("loc_7910")

    SetScenarioFlags(0x20, 0)
    Jump("loc_7922")

    label("loc_7918")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7922")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7962")
    SetChrName("")

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アイテムを入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7962")

    Jump("loc_76B1")

    label("loc_7967")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_43_76A7 end

    def Function_44_7975(): pass

    label("Function_44_7975")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_797F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B9F")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "ＤＰ　０\x01",          # 0
            "ＤＰ　１５\x01",        # 1
            "ＤＰ　３０\x01",        # 2
            "ＤＰ　５５\x01",        # 3
            "ＤＰ　７０\x01",        # 4
            "ＤＰ　９０\x01",        # 5
            "ＤＰ　１１０\x01",      # 6
            "ＤＰ　１３０\x01",      # 7
            "ＤＰ　１５０\x01",      # 8
            "ＤＰ　１９５\x01",      # 9
            "ＤＰ　２２４\x01",      # 10
            "ＤＰ　２６５\x01",      # 11
            "ＤＰ　２９４\x01",      # 12
            "ＤＰ　３２４\x01",      # 13
            "ＤＰ　３８０\x01",      # 14
            "キャンセル\x01",        # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7ABE"),
        (1, "loc_7ACC"),
        (2, "loc_7ADA"),
        (3, "loc_7AE8"),
        (4, "loc_7AF6"),
        (5, "loc_7B04"),
        (6, "loc_7B12"),
        (7, "loc_7B20"),
        (8, "loc_7B2E"),
        (9, "loc_7B3C"),
        (10, "loc_7B4A"),
        (11, "loc_7B58"),
        (12, "loc_7B66"),
        (13, "loc_7B74"),
        (14, "loc_7B82"),
        (SWITCH_DEFAULT, "loc_7B90"),
    )


    label("loc_7ABE")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B9A")

    label("loc_7ACC")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B9A")

    label("loc_7ADA")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B9A")

    label("loc_7AE8")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x37), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B9A")

    label("loc_7AF6")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B9A")

    label("loc_7B04")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B9A")

    label("loc_7B12")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B9A")

    label("loc_7B20")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B9A")

    label("loc_7B2E")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B9A")

    label("loc_7B3C")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B9A")

    label("loc_7B4A")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B9A")

    label("loc_7B58")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x109), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B9A")

    label("loc_7B66")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x126), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B9A")

    label("loc_7B74")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x144), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B9A")

    label("loc_7B82")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x17C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B9A")

    label("loc_7B90")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7B9A")

    Jump("loc_797F")

    label("loc_7B9F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_44_7975 end

    def Function_45_7BAD(): pass

    label("Function_45_7BAD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7BB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80D1")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "全アイテム消去\x01",          # 0
            "基本アイテム入手\x01",        # 1
            "全装備品入手\x01",            # 2
            "全アクセサリ入手\x01",        # 3
            "全消費アイテム入手\x01",      # 4
            "セピス大量入手\x01",          # 5
            "セピスを０に\x01",            # 6
            "クオーツ大量入手\x01",        # 7
            "全員瀕死\x01",                # 8
            "実績全部初期化\x01",          # 9
            "実績全部入手\x01",            # 10
            "クロスベル全部\x01",          # 11
            "エニグマカバー\x01",          # 12
            "キャンセル\x01",              # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7CF0"),
        (1, "loc_7D2B"),
        (2, "loc_7DAB"),
        (3, "loc_7DEE"),
        (4, "loc_7E27"),
        (5, "loc_7E6A"),
        (6, "loc_7EA4"),
        (7, "loc_7ED8"),
        (8, "loc_7F0D"),
        (9, "loc_7F63"),
        (11, "loc_7F8D"),
        (12, "loc_8021"),
        (SWITCH_DEFAULT, "loc_80C2"),
    )


    label("loc_7CF0")

    SubItemNumber(0x270F, 99)
    SetChrName("")

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての所持アイテムを削除しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_80CC")

    label("loc_7D2B")

    AddItemNumber(0x1, 1)
    AddItemNumber(0x2, 1)
    AddItemNumber(0x3, 1)
    AddItemNumber(0x4, 1)
    AddItemNumber(0x5, 1)
    AddItemNumber(0x1F4, 10)
    AddItemNumber(0x1F5, 10)
    AddItemNumber(0x1F6, 10)
    AddItemNumber(0x1F8, 10)
    AddItemNumber(0x1F9, 10)
    AddItemNumber(0x1FB, 10)
    AddItemNumber(0x1FC, 10)
    AddItemNumber(0x20B, 10)
    AddItemNumber(0x32, 10)
    AddItemNumber(0x186, 10)
    AddItemNumber(0x187, 10)
    SetChrName("")

    #A0163
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "基本アイテムを入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_80CC")

    label("loc_7DAB")

    Call(1, 88)
    Call(1, 89)
    Call(1, 90)
    SetChrName("")

    #A0164
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての装備品(武器防具)を入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_80CC")

    label("loc_7DEE")

    Call(1, 91)
    SetChrName("")

    #A0165
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのアクセサリーを入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_80CC")

    label("loc_7E27")

    Call(1, 92)
    SetChrName("")

    #A0166
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての消費アイテム(薬、道具)を入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_80CC")

    label("loc_7E6A")

    AddSepith(0xFF, 5000)
    SetChrName("")

    #A0167
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのセピスを大量に入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_80CC")

    label("loc_7EA4")

    SubSepith(0xFF, 9999)
    SetChrName("")

    #A0168
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのセピスを消去しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_80CC")

    label("loc_7ED8")

    Call(1, 93)
    SetChrName("")

    #A0169
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのクオーツを入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_80CC")

    label("loc_7F0D")

    OP_32(0x0, 0x2, 0x1)
    OP_32(0x1, 0x2, 0x1)
    OP_32(0x2, 0x2, 0x1)
    OP_32(0x3, 0x2, 0x1)
    OP_32(0x4, 0x2, 0x1)
    OP_32(0x5, 0x2, 0x1)
    OP_32(0x8, 0x2, 0x1)
    OP_32(0x9, 0x2, 0x1)
    SetChrName("")

    #A0170
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全員のＨＰを１にしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_80CC")

    label("loc_7F63")

    SetChrName("")

    #A0171
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "実績を初期化しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_80CC")

    label("loc_7F8D")

    SetScenarioFlags(0xF8, 0)
    SetScenarioFlags(0xF8, 1)
    SetScenarioFlags(0xF8, 2)
    SetScenarioFlags(0xF8, 3)
    SetScenarioFlags(0xF8, 4)
    SetScenarioFlags(0xF8, 5)
    SetScenarioFlags(0xF8, 6)
    SetScenarioFlags(0xF8, 7)
    SetScenarioFlags(0xF9, 0)
    SetScenarioFlags(0xF9, 1)
    SetScenarioFlags(0xF9, 2)
    SetScenarioFlags(0xF9, 3)
    SetScenarioFlags(0xF9, 4)
    SetScenarioFlags(0xF9, 5)
    SetScenarioFlags(0xF9, 6)
    SetScenarioFlags(0xF9, 7)
    SetScenarioFlags(0xFA, 0)
    SetScenarioFlags(0xFA, 1)
    SetScenarioFlags(0xFA, 2)
    SetScenarioFlags(0xFA, 3)
    SetScenarioFlags(0xFA, 4)
    SetScenarioFlags(0xFA, 5)
    SetScenarioFlags(0xFA, 6)
    SetScenarioFlags(0xFA, 7)
    SetScenarioFlags(0xFB, 0)
    SetScenarioFlags(0xFB, 1)
    SetScenarioFlags(0xFB, 2)
    SetScenarioFlags(0xFB, 3)
    SetScenarioFlags(0xFB, 4)
    SetScenarioFlags(0xFB, 5)
    SetScenarioFlags(0xFB, 6)
    SetScenarioFlags(0xFB, 7)
    SetChrName("")

    #A0172
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベルジャンプ使用できます。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_80CC")

    label("loc_8021")

    OP_60(0x2)

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期\x01",            # 0
            "前編分購入\x01",      # 1
            "後編分購入\x01",      # 2
            "キャンセル\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8072"),
        (1, "loc_8095"),
        (2, "loc_80A6"),
        (SWITCH_DEFAULT, "loc_80BD"),
    )


    label("loc_8072")

    ClearScenarioFlags(0xF0, 5)
    ClearScenarioFlags(0xF0, 6)
    ClearScenarioFlags(0xF0, 7)
    ClearScenarioFlags(0xF1, 0)
    ClearScenarioFlags(0x2E, 0)
    ClearScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0x2E, 4)
    ClearScenarioFlags(0x2F, 0)
    Jump("loc_80BD")

    label("loc_8095")

    SetScenarioFlags(0xF0, 5)
    SetScenarioFlags(0xF0, 6)
    SetScenarioFlags(0xF0, 7)
    SetScenarioFlags(0xF1, 0)
    Jump("loc_80BD")

    label("loc_80A6")

    SetScenarioFlags(0x2E, 0)
    SetScenarioFlags(0x2E, 1)
    SetScenarioFlags(0x2E, 2)
    SetScenarioFlags(0x2E, 3)
    SetScenarioFlags(0x2E, 4)
    SetScenarioFlags(0x2F, 0)
    Jump("loc_80BD")

    label("loc_80BD")

    Jump("loc_80CC")

    label("loc_80C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_80CC")

    Jump("loc_7BB7")

    label("loc_80D1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_45_7BAD end

    def Function_46_80DF(): pass

    label("Function_46_80DF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_80E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_815F")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "波音ループ再生\x01",      # 0
            "波音停止\x01",            # 1
            "キャンセル\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_813D"),
        (1, "loc_8148"),
        (SWITCH_DEFAULT, "loc_8150"),
    )


    label("loc_813D")

    Sound(479, 1, 100, 0)
    Jump("loc_815A")

    label("loc_8148")

    OP_24(0x1DF)
    Jump("loc_815A")

    label("loc_8150")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_815A")

    Jump("loc_80E9")

    label("loc_815F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_46_80DF end

    def Function_47_816D(): pass

    label("Function_47_816D")

    EventBegin(0x0)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF4080FF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_6E(1000, 0)
    SetCameraDistance(8000, 0)
    OP_68(5000, 500, -5000, 0)
    MoveCamera(45, 15, 0, 0)
    SetChrPos(0x0, 5000, 0, -5000, 240)
    OP_78(0x0, 0x0)
    BeginChrThread(0x0, 1, 0, 48)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_81D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_832C")

    Menu(
        2,
        16,
        64,
        1,
        (
            "初期\x01",              # 0
            "テクスチャ１\x01",      # 1
            "テクスチャ２\x01",      # 2
            "テクスチャ３\x01",      # 3
            "テクスチャ４\x01",      # 4
            "キャンセル\x01",        # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_825A"),
        (1, "loc_8281"),
        (2, "loc_82A8"),
        (3, "loc_82CF"),
        (4, "loc_82F6"),
        (SWITCH_DEFAULT, "loc_831D"),
    )


    label("loc_825A")

    MiniGame(0x2D, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_8327")

    label("loc_8281")

    MiniGame(0x2D, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_8327")

    label("loc_82A8")

    MiniGame(0x2D, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_8327")

    label("loc_82CF")

    MiniGame(0x2D, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_8327")

    label("loc_82F6")

    MiniGame(0x2D, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_8327")

    label("loc_831D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8327")

    Jump("loc_81D3")

    label("loc_832C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    SetChrPos(0x0, 0, 0, 0, 0)
    EndChrThread(0x0, 0xFF)
    EventEnd(0x5)
    SetMapFlags(0x80)
    Return()

    # Function_47_816D end

    def Function_48_8356(): pass

    label("Function_48_8356")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_837B")
    OP_93(0x0, 0xF0, 0xA)
    OP_93(0x0, 0x168, 0xA)
    OP_93(0x0, 0x78, 0xA)
    Jump("Function_48_8356")

    label("loc_837B")

    Return()

    # Function_48_8356 end

    def Function_49_837C(): pass

    label("Function_49_837C")

    OP_60(0x0)
    OP_60(0x1)
    OP_60(0x2)
    OP_57(0x0)
    ClearParty()
    AddParty(0x1, 0xFF, 0xFF)
    SetChrPos(0x0, 22000, 0, -4000, 0)
    ClearMapFlags(0x80)
    ClearMapFlags(0x1)
    MoveCamera(0, 15, 0, 0)
    OP_68(22000, 1000, 0, 0)
    SetCameraDistance(7000, 0)
    OP_6E(1000, 0)
    OP_1C(0x0, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1C(0x0, 0x2, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1C(0x0, 0x3, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_37()
    SetChrPos(0xA, 20000, 0, 0, 0)
    SetChrPos(0xB, 22000, 0, 0, 0)
    SetChrPos(0xC, 24000, 0, 0, 0)
    SetChrPos(0xD, 21000, 0, 1500, 0)
    SetChrPos(0xE, 23000, 0, 1500, 0)
    SetChrPos(0xF, 22000, 0, 3000, 0)
    OP_70(0x1, 0xA)
    OP_70(0x2, 0xA)
    OP_70(0x3, 0xA)
    OP_70(0x4, 0xA)
    OP_70(0x5, 0xA)
    OP_70(0x6, 0xA)
    OP_78(0x1, 0xA)
    OP_78(0x2, 0xB)
    OP_78(0x3, 0xC)
    OP_78(0x4, 0xD)
    OP_78(0x5, 0xE)
    OP_78(0x6, 0xF)
    BeginChrThread(0xA, 0, 0, 50)
    BeginChrThread(0xB, 0, 0, 51)
    BeginChrThread(0xC, 0, 0, 52)
    BeginChrThread(0xD, 0, 0, 53)
    BeginChrThread(0xE, 0, 0, 54)
    BeginChrThread(0xF, 0, 0, 55)
    BeginChrThread(0xF, 1, 0, 56)

    label("loc_84B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_84CA")
    Sleep(1000)
    Jump("loc_84B7")

    label("loc_84CA")

    Return()

    # Function_49_837C end

    def Function_50_84CB(): pass

    label("Function_50_84CB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8578")
    OP_1C(0x0, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8511")
    SetMapObjFrame(0x1, "npc", 0x0, 0x1)
    SetMapObjFrame(0x1, "enemy", 0x1, 0x1)
    Jump("loc_8529")

    label("loc_8511")

    SetMapObjFrame(0x1, "npc", 0x1, 0x1)
    SetMapObjFrame(0x1, "enemy", 0x0, 0x1)

    label("loc_8529")

    SetMapObjFlags(0x1, 0x2)
    SetMapObjFlags(0x1, 0x800000)
    ClearMapObjFlags(0x1, 0x80000000)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x1)
    OP_70(0x1, 0x0)
    Sleep(2000)
    ClearMapObjFlags(0x1, 0x2)
    ClearMapObjFlags(0x1, 0x800000)
    OP_71(0x1, 0xFFFF, 0xA, 0x0, 0x0)
    OP_79(0x1)
    OP_70(0x1, 0xA)
    Call(0, 57)
    Jump("Function_50_84CB")

    label("loc_8578")

    Return()

    # Function_50_84CB end

    def Function_51_8579(): pass

    label("Function_51_8579")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8626")
    OP_1C(0x0, 0x2, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_85BF")
    SetMapObjFrame(0x2, "npc", 0x0, 0x1)
    SetMapObjFrame(0x2, "enemy", 0x1, 0x1)
    Jump("loc_85D7")

    label("loc_85BF")

    SetMapObjFrame(0x2, "npc", 0x1, 0x1)
    SetMapObjFrame(0x2, "enemy", 0x0, 0x1)

    label("loc_85D7")

    SetMapObjFlags(0x2, 0x2)
    SetMapObjFlags(0x2, 0x800000)
    ClearMapObjFlags(0x2, 0x80000000)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x2)
    OP_70(0x2, 0x0)
    Sleep(4000)
    ClearMapObjFlags(0x2, 0x2)
    ClearMapObjFlags(0x2, 0x800000)
    OP_71(0x2, 0xFFFF, 0xA, 0x0, 0x0)
    OP_79(0x2)
    OP_70(0x2, 0xA)
    Call(0, 57)
    Jump("Function_51_8579")

    label("loc_8626")

    Return()

    # Function_51_8579 end

    def Function_52_8627(): pass

    label("Function_52_8627")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_86D4")
    OP_1C(0x0, 0x3, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_866D")
    SetMapObjFrame(0x3, "npc", 0x0, 0x1)
    SetMapObjFrame(0x3, "enemy", 0x1, 0x1)
    Jump("loc_8685")

    label("loc_866D")

    SetMapObjFrame(0x3, "npc", 0x1, 0x1)
    SetMapObjFrame(0x3, "enemy", 0x0, 0x1)

    label("loc_8685")

    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x3, 0x800000)
    ClearMapObjFlags(0x3, 0x80000000)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x3)
    OP_70(0x3, 0x0)
    Sleep(3000)
    ClearMapObjFlags(0x3, 0x2)
    ClearMapObjFlags(0x3, 0x800000)
    OP_71(0x3, 0xFFFF, 0xA, 0x0, 0x0)
    OP_79(0x3)
    OP_70(0x3, 0xA)
    Call(0, 57)
    Jump("Function_52_8627")

    label("loc_86D4")

    Return()

    # Function_52_8627 end

    def Function_53_86D5(): pass

    label("Function_53_86D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8782")
    OP_1C(0x0, 0x4, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_871B")
    SetMapObjFrame(0x4, "npc", 0x0, 0x1)
    SetMapObjFrame(0x4, "enemy", 0x1, 0x1)
    Jump("loc_8733")

    label("loc_871B")

    SetMapObjFrame(0x4, "npc", 0x1, 0x1)
    SetMapObjFrame(0x4, "enemy", 0x0, 0x1)

    label("loc_8733")

    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x4, 0x800000)
    ClearMapObjFlags(0x4, 0x80000000)
    OP_71(0x4, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x4)
    OP_70(0x4, 0x0)
    Sleep(2000)
    ClearMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x4, 0x800000)
    OP_71(0x4, 0xFFFF, 0xA, 0x0, 0x0)
    OP_79(0x4)
    OP_70(0x4, 0xA)
    Call(0, 57)
    Jump("Function_53_86D5")

    label("loc_8782")

    Return()

    # Function_53_86D5 end

    def Function_54_8783(): pass

    label("Function_54_8783")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8830")
    OP_1C(0x0, 0x5, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_87C9")
    SetMapObjFrame(0x5, "npc", 0x0, 0x1)
    SetMapObjFrame(0x5, "enemy", 0x1, 0x1)
    Jump("loc_87E1")

    label("loc_87C9")

    SetMapObjFrame(0x5, "npc", 0x1, 0x1)
    SetMapObjFrame(0x5, "enemy", 0x0, 0x1)

    label("loc_87E1")

    SetMapObjFlags(0x5, 0x2)
    SetMapObjFlags(0x5, 0x800000)
    ClearMapObjFlags(0x5, 0x80000000)
    OP_71(0x5, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x5)
    OP_70(0x5, 0x0)
    Sleep(2000)
    ClearMapObjFlags(0x5, 0x2)
    ClearMapObjFlags(0x5, 0x800000)
    OP_71(0x5, 0xFFFF, 0xA, 0x0, 0x0)
    OP_79(0x5)
    OP_70(0x5, 0xA)
    Call(0, 57)
    Jump("Function_54_8783")

    label("loc_8830")

    Return()

    # Function_54_8783 end

    def Function_55_8831(): pass

    label("Function_55_8831")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_88DE")
    OP_1C(0x0, 0x6, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8877")
    SetMapObjFrame(0x6, "npc", 0x0, 0x1)
    SetMapObjFrame(0x6, "enemy", 0x1, 0x1)
    Jump("loc_888F")

    label("loc_8877")

    SetMapObjFrame(0x6, "npc", 0x1, 0x1)
    SetMapObjFrame(0x6, "enemy", 0x0, 0x1)

    label("loc_888F")

    SetMapObjFlags(0x6, 0x2)
    SetMapObjFlags(0x6, 0x800000)
    ClearMapObjFlags(0x6, 0x80000000)
    OP_71(0x6, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x6)
    OP_70(0x6, 0x0)
    Sleep(2000)
    ClearMapObjFlags(0x6, 0x2)
    ClearMapObjFlags(0x6, 0x800000)
    OP_71(0x6, 0xFFFF, 0xA, 0x0, 0x0)
    OP_79(0x6)
    OP_70(0x6, 0xA)
    Call(0, 57)
    Jump("Function_55_8831")

    label("loc_88DE")

    Return()

    # Function_55_8831 end

    def Function_56_88DF(): pass

    label("Function_56_88DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8917")
    OP_96(0xFE, 0x4E20, 0x0, 0xF64, 0x3E8, 0x0)
    OP_96(0xFE, 0x5DC0, 0x0, 0xF46, 0x3E8, 0x0)
    Jump("Function_56_88DF")

    label("loc_8917")

    Return()

    # Function_56_88DF end

    def Function_57_8918(): pass

    label("Function_57_8918")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_893B")
    Sleep(1000)
    Jump("loc_8983")

    label("loc_893B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8952")
    Sleep(2000)
    Jump("loc_8983")

    label("loc_8952")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8969")
    Sleep(3000)
    Jump("loc_8983")

    label("loc_8969")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8980")
    Sleep(4000)
    Jump("loc_8983")

    label("loc_8980")

    Sleep(5000)

    label("loc_8983")

    Return()

    # Function_57_8918 end

    SaveToFile()

Try(main)
