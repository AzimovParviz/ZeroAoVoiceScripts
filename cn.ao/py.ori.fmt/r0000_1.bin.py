﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r0000_1.bin",                # FileName
        "r0000",                    # MapName
        "r0000",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [100, 0, 0, 0, 83952996, 83952897, 5, 1, 1380, 1281, 1281, 1281, 84215045, 5, 83887460, 1280, 512, 5, 0, 2, 0, 0, 0],
    )

    BuildStringList((
        "r0000_1",                # 0
    ))

    ChipFrameInfo(356, 0)                                        # 0

    ScpFunction((
        "Function_0_164",          # 00, 0
        "Function_1_1F6",          # 01, 1
        "Function_2_248",          # 02, 2
        "Function_3_CF6",          # 03, 3
        "Function_4_1465",         # 04, 4
        "Function_5_184E",         # 05, 5
        "Function_6_1B93",         # 06, 6
        "Function_7_1BD0",         # 07, 7
    ))


    def Function_0_164(): pass

    label("Function_0_164")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "发现了物品。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D, 7)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AB")
    Call(1, 5)
    Jump("loc_1F5")

    label("loc_1AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D, 6)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3")
    Call(1, 4)
    Jump("loc_1F5")

    label("loc_1D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D, 5)), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F2")
    Call(1, 3)
    Jump("loc_1F5")

    label("loc_1F2")

    Call(1, 2)

    label("loc_1F5")

    Return()

    # Function_0_164 end

    def Function_1_1F6(): pass

    label("Function_1_1F6")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_220")
    Call(1, 5)
    Jump("loc_247")

    label("loc_220")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_244")
    Call(1, 4)
    Jump("loc_247")

    label("loc_244")

    Call(1, 3)

    label("loc_247")

    Return()

    # Function_1_1F6 end

    def Function_2_248(): pass

    label("Function_2_248")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F0")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_2A7"),
        (1, "loc_2F3"),
        (2, "loc_33F"),
        (3, "loc_38B"),
        (4, "loc_3D7"),
        (5, "loc_423"),
        (6, "loc_46F"),
        (7, "loc_4BB"),
        (8, "loc_507"),
        (9, "loc_553"),
        (SWITCH_DEFAULT, "loc_59F"),
    )


    label("loc_2A7")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '解毒药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('解毒药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_5EB")

    label("loc_2F3")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '软化膏'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('软化膏', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_5EB")

    label("loc_33F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '绝缘胶带'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('绝缘胶带', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_5EB")

    label("loc_38B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '解冻暖炉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('解冻暖炉', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_5EB")

    label("loc_3D7")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '舒缓凝胶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('舒缓凝胶', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_5EB")

    label("loc_423")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '冷却喷雾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('冷却喷雾', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_5EB")

    label("loc_46F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '眼药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('眼药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_5EB")

    label("loc_4BB")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '提神薄荷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('提神薄荷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_5EB")

    label("loc_507")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '苏醒药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('苏醒药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_5EB")

    label("loc_553")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '镇静剂'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('镇静剂', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_5EB")

    label("loc_59F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('回复药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_5EB")

    label("loc_5EB")

    Jump("loc_CF5")

    label("loc_5F0")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6C0"),
        (18, "loc_6C0"),
        (25, "loc_6C0"),
        (1, "loc_71C"),
        (19, "loc_71C"),
        (26, "loc_71C"),
        (2, "loc_778"),
        (20, "loc_778"),
        (27, "loc_778"),
        (3, "loc_7D4"),
        (21, "loc_7D4"),
        (28, "loc_7D4"),
        (4, "loc_830"),
        (22, "loc_830"),
        (29, "loc_830"),
        (5, "loc_88C"),
        (23, "loc_88C"),
        (30, "loc_88C"),
        (6, "loc_8E8"),
        (24, "loc_8E8"),
        (31, "loc_8E8"),
        (7, "loc_944"),
        (8, "loc_993"),
        (9, "loc_9E2"),
        (10, "loc_A31"),
        (11, "loc_A80"),
        (12, "loc_ACF"),
        (13, "loc_B1E"),
        (14, "loc_B6D"),
        (15, "loc_BBC"),
        (16, "loc_C0B"),
        (17, "loc_C5A"),
        (SWITCH_DEFAULT, "loc_CA9"),
    )


    label("loc_6C0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片\x07\x00",
            "捡到了10个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x0, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_71C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I水之耀晶片\x07\x00",
            "捡到了10个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x1, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_778")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58I火之耀晶片\x07\x00",
            "捡到了10个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x2, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_7D4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I风之耀晶片\x07\x00",
            "捡到了10个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x3, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_830")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0017
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I时之耀晶片\x07\x00",
            "捡到了10个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x4, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_88C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0018
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61I空之耀晶片\x07\x00",
            "捡到了10个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x5, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_8E8")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0019
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I幻之耀晶片\x07\x00",
            "捡到了10个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x6, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_944")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '鲑鱼卵'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('鲑鱼卵', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_993")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0021
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '熬炼丸子'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('熬炼丸子', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_9E2")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0022
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '红虫'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('红虫', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_A31")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0023
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '蚯蚓'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('蚯蚓', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_A80")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0024
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽兽肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽兽肉', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_ACF")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0025
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽鱼肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽鱼肉', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_B1E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0026
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽之壳'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽之壳', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_B6D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0027
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽之卵'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽之卵', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_BBC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0028
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽羽翼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽羽翼', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_C0B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0029
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽之种'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽之种', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_C5A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0030
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽明胶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽明胶', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_CA9")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0031
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('回复药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CF5")

    label("loc_CF5")

    Return()

    # Function_2_248 end

    def Function_3_CF6(): pass

    label("Function_3_CF6")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_D90"),
        (1, "loc_DDC"),
        (2, "loc_E28"),
        (3, "loc_E74"),
        (4, "loc_EC0"),
        (5, "loc_F0C"),
        (6, "loc_F58"),
        (7, "loc_FA4"),
        (8, "loc_FF0"),
        (9, "loc_103C"),
        (10, "loc_1088"),
        (11, "loc_10D4"),
        (12, "loc_1120"),
        (13, "loc_116C"),
        (14, "loc_11B8"),
        (15, "loc_1204"),
        (16, "loc_1250"),
        (17, "loc_129C"),
        (18, "loc_12E8"),
        (19, "loc_1334"),
        (20, "loc_1380"),
        (21, "loc_13CC"),
        (22, "loc_1418"),
        (SWITCH_DEFAULT, "loc_1464"),
    )


    label("loc_D90")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0032
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＨＰ１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_DDC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0033
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＥＰ１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_E28")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0034
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '攻击１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('攻击１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_E74")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0035
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('防御１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_EC0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '精神１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('精神１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_F0C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0037
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔防１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔防１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_F58")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0038
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('命中１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_FA4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0039
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('回避１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_FF0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0040
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '移动１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('移动１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_103C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0041
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '行动力１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('行动力１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_1088")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0042
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '妨害１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('妨害１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_10D4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0043
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '省ＥＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('省ＥＰ１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_1120")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0044
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '银胸针'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('银胸针', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_116C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0045
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '珊瑚戒指'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('珊瑚戒指', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_11B8")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0046
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '英雄戒指'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('英雄戒指', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_1204")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0047
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '夜光眼镜'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('夜光眼镜', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_1250")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0048
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '凉爽项链'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('凉爽项链', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_129C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0049
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '打火机'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('打火机', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_12E8")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0050
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '幻彩围巾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('幻彩围巾', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_1334")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0051
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '叮当耳环'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('叮当耳环', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_1380")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0052
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '钢手镯'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('钢手镯', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_13CC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0053
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '花之瓶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('花之瓶', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_1418")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0054
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '神圣之链'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('神圣之链', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1464")

    label("loc_1464")

    Return()

    # Function_3_CF6 end

    def Function_4_1465(): pass

    label("Function_4_1465")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_14BD"),
        (1, "loc_1509"),
        (2, "loc_1555"),
        (3, "loc_15A1"),
        (4, "loc_15ED"),
        (5, "loc_1639"),
        (6, "loc_1685"),
        (7, "loc_16D1"),
        (8, "loc_171D"),
        (9, "loc_1769"),
        (10, "loc_17B5"),
        (11, "loc_1801"),
        (SWITCH_DEFAULT, "loc_184D"),
    )


    label("loc_14BD")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0055
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＨＰ２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_184D")

    label("loc_1509")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0056
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＥＰ２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_184D")

    label("loc_1555")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0057
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '攻击２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('攻击２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_184D")

    label("loc_15A1")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0058
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('防御２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_184D")

    label("loc_15ED")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0059
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '精神２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('精神２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_184D")

    label("loc_1639")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0060
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔防２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔防２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_184D")

    label("loc_1685")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0061
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('命中２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_184D")

    label("loc_16D1")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0062
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('回避２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_184D")

    label("loc_171D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0063
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '移动２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('移动２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_184D")

    label("loc_1769")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0064
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '行动力２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('行动力２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_184D")

    label("loc_17B5")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0065
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '妨害２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('妨害２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_184D")

    label("loc_1801")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0066
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '省ＥＰ２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('省ＥＰ２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_184D")

    label("loc_184D")

    Return()

    # Function_4_1465 end

    def Function_5_184E(): pass

    label("Function_5_184E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_189A"),
        (1, "loc_18E6"),
        (2, "loc_1932"),
        (3, "loc_197E"),
        (4, "loc_19CA"),
        (5, "loc_1A16"),
        (6, "loc_1A62"),
        (7, "loc_1AAE"),
        (8, "loc_1AFA"),
        (9, "loc_1B46"),
        (SWITCH_DEFAULT, "loc_1B92"),
    )


    label("loc_189A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0067
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＨＰ３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1B92")

    label("loc_18E6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0068
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＥＰ３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1B92")

    label("loc_1932")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0069
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '攻击３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('攻击３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1B92")

    label("loc_197E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0070
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('防御３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1B92")

    label("loc_19CA")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0071
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '精神３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('精神３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1B92")

    label("loc_1A16")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0072
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔防３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔防３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1B92")

    label("loc_1A62")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0073
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('命中３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1B92")

    label("loc_1AAE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0074
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('回避３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1B92")

    label("loc_1AFA")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0075
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '行动力３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('行动力３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1B92")

    label("loc_1B46")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0076
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '省ＥＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('省ＥＰ３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1B92")

    label("loc_1B92")

    Return()

    # Function_5_184E end

    def Function_6_1B93(): pass

    label("Function_6_1B93")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    TalkBegin(0xFF)
    SetChrName("")

    #A0077
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "发现了物品。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 7)
    TalkEnd(0xFF)
    ClearMapFlags(0x80)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1B93 end

    def Function_7_1BD0(): pass

    label("Function_7_1BD0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_202B")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1C3B"),
        (1, "loc_1C8A"),
        (2, "loc_1CD9"),
        (3, "loc_1D28"),
        (4, "loc_1D77"),
        (5, "loc_1DC6"),
        (6, "loc_1E12"),
        (7, "loc_1E5E"),
        (8, "loc_1EAA"),
        (9, "loc_1EF6"),
        (10, "loc_1F42"),
        (11, "loc_1F8E"),
        (SWITCH_DEFAULT, "loc_1FDA"),
    )


    label("loc_1C3B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0078
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '鲑鱼卵'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('鲑鱼卵', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2026")

    label("loc_1C8A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0079
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '熬炼丸子'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('熬炼丸子', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2026")

    label("loc_1CD9")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0080
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '红虫'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('红虫', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2026")

    label("loc_1D28")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0081
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '蚯蚓'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('蚯蚓', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2026")

    label("loc_1D77")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0082
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '熬炼丸子ＤＸ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('熬炼丸子ＤＸ', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2026")

    label("loc_1DC6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0083
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽兽肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽兽肉', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2026")

    label("loc_1E12")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0084
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽鱼肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽鱼肉', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2026")

    label("loc_1E5E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0085
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽之壳'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽之壳', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2026")

    label("loc_1EAA")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0086
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽之卵'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽之卵', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2026")

    label("loc_1EF6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0087
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽羽翼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽羽翼', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2026")

    label("loc_1F42")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0088
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽之种'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽之种', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2026")

    label("loc_1F8E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0089
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽明胶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽明胶', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2026")

    label("loc_1FDA")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0090
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽兽肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽兽肉', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2026")

    label("loc_2026")

    Jump("loc_282D")

    label("loc_202B")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_20C5"),
        (1, "loc_2114"),
        (2, "loc_2163"),
        (3, "loc_21B2"),
        (4, "loc_2201"),
        (5, "loc_2250"),
        (6, "loc_229F"),
        (7, "loc_22EE"),
        (8, "loc_233D"),
        (9, "loc_238C"),
        (10, "loc_23DB"),
        (11, "loc_242A"),
        (12, "loc_2479"),
        (13, "loc_24C8"),
        (14, "loc_2517"),
        (15, "loc_2566"),
        (16, "loc_25B5"),
        (17, "loc_2604"),
        (18, "loc_2653"),
        (19, "loc_26A2"),
        (20, "loc_26F1"),
        (21, "loc_2740"),
        (22, "loc_278F"),
        (SWITCH_DEFAULT, "loc_27DE"),
    )


    label("loc_20C5")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0091
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '发芽糙米'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('发芽糙米', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_2114")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0092
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '五谷味噌'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('五谷味噌', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_2163")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0093
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '百药精酒'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('百药精酒', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_21B2")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0094
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '朝摘香叶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了5个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('朝摘香叶', 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_2201")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0095
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '清绿香草'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了5个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('清绿香草', 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_2250")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0096
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '胡椒粒'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了8个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('胡椒粒', 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_229F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0097
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '热辣椒'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了8个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('热辣椒', 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_22EE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0098
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '香油'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了8个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('香油', 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_233D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0099
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '蜂蜜糖浆'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了8个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('蜂蜜糖浆', 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_238C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0100
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '粗碎岩盐'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了8个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('粗碎岩盐', 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_23DB")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0101
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '新磨小麦粉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了8个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('新磨小麦粉', 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_242A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0102
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '新鲜牛奶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了4个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('新鲜牛奶', 4)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_2479")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0103
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '新鲜奶酪'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了4个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('新鲜奶酪', 4)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_24C8")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0104
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '新鲜鸡蛋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了4个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('新鲜鸡蛋', 4)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_2517")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0105
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '铃铛草莓'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了3个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('铃铛草莓', 3)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_2566")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0106
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '黑暗菇'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了3个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('黑暗菇', 3)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_25B5")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0107
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '七彩豆'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了3个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('七彩豆', 3)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_2604")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0108
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '国王马铃薯'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了5个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('国王马铃薯', 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_2653")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0109
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '万能青葱'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了5个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('万能青葱', 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_26A2")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0110
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '迷你胡萝卜'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了5个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('迷你胡萝卜', 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_26F1")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0111
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '苦西红柿'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('苦西红柿', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_2740")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0112
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '雪花里脊肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('雪花里脊肉', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_278F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0113
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '新鲜白肉鱼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('新鲜白肉鱼', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_27DE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0114
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '新鲜白肉鱼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "捡到了2个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('新鲜白肉鱼', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_282D")

    label("loc_282D")

    Return()

    # Function_7_1BD0 end

    SaveToFile()

Try(main)
