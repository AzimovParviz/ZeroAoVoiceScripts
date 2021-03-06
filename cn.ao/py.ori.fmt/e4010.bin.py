﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e4010.bin",                # FileName
        "e4010",                    # MapName
        "e4010",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4010",                  # 0
        "金发青年",               # 1
        "黑发军人",               # 2
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(216, 0)                                        # 0

    ScpFunction((
        "Function_0_D8",           # 00, 0
        "Function_1_E8",           # 01, 1
        "Function_2_E9",           # 02, 2
    ))


    def Function_0_D8(): pass

    label("Function_0_D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_E7")

    Return()

    # Function_0_D8 end

    def Function_1_E8(): pass

    label("Function_1_E8")

    Return()

    # Function_1_E8 end

    def Function_2_E9(): pass

    label("Function_2_E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11102.itc", 0x1E)
    LoadChrToIndex("chr/ch11300.itc", 0x1F)
    LoadChrToIndex("apl/ch51205.itc", 0x20)
    CreatePortrait(0, 16, 20, 528, 84, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis503.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07300.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07200.itp")
    SetChrPos(0x0, -7000, 0, 2000, 0)
    SetChrPos(0x1, -7000, 0, 2000, 0)
    SetChrPos(0x2, -7000, 0, 2000, 0)
    SetChrPos(0x3, -7000, 0, 2000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 50, 7100, 180)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -7500, 0, -3000, 90)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(500)
    Sound(103, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("青年的声音")

    #A0001
    AnonymousTalk(
        0xFF,
        "──你还没睡啊？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0x5)
    OP_68(-6000, 1000, -3000, 0)
    MoveCamera(309, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    PlayBGM("ed7515", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_68(0, 1000, 5900, 8000)
    MoveCamera(315, 21, 0, 8000)
    SetCameraDistance(18500, 8000)

    def lambda_2D0():
        OP_95(0xFE, -4000, 0, -3000, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2D0)

    def lambda_2EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2EA)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    WaitChrThread(0x9, 1)

    def lambda_315():
        OP_95(0xFE, 0, 0, 4300, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_315)
    Sound(104, 0, 100, 0)
    OP_71(0x3, 0x5, 0x0, 0x0, 0x0)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x8, 500)
    OP_6F(0x79)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0002
    AnonymousTalk(
        0x9,
        (
            "明天一大早就要出发，\x01",
            "你差不多也该去休息了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0003
    ChrTalk(
        0x8,
        (
            "#11P#07208F#30W啊……嗯……\x02\x03",

            "#07203F我准备把这些报告也\x01",
            "过目一遍。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "#6P#07303F士官学校吗……\x02\x03",

            "#07302F真没想到，你居然会如此\x01",
            "兢兢业业地尽自己的职责。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "#11P#07204F呵呵，但说到底，\x01",
            "我也只是个挂名理事而已。\x02\x03",

            "#07200F那些孩子如今正在努力，\x01",
            "我也得做点事情才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            "#6P#07304F呵……也好。\x02\x03",

            "#07300F对了，那件传闻\x01",
            "似乎是真的。\x02\x03",

            "凯恩大公的手下\x01",
            "正在暗中安排。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#11P#07206F凯恩大公吗……\x01",
            "我倒也早就料到一二了。\x02\x03",

            "#07200F已经掌握到大致规模了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "#6P#07303F不，目前尚未查明。\x02\x03",

            "#07300F就连情报局也未能\x01",
            "掌握那方面的消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#11P#07209F哈哈，虽说是咎由自取，\x01",
            "但宰相阁下还真是天降横祸呢。\x02\x03",

            "#07202F呵呵，对方说不定还打算\x01",
            "把我也一并解决掉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        (
            "#6P#07306F……这玩笑可不好笑。\x02\x03",

            "#07301F看来还是应该从第七师团派遣\x01",
            "一些增援，加强你的护卫力度为好吧？\x02\x03",

            "如果现在呼叫，应该还来得及。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#11P#07204F不，没那个必要。\x02\x03",

            "若宰相阁下那样做，倒是无可厚非，\x01",
            "但我如果做出那种安排，至今为止\x01",
            "好不容易才塑造起来的形象就要全毁了。\x02\x03",

            "#07202F而且──\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(400)
    Sound(822, 0, 100, 0)
    OP_63(0x8, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    SetCameraDistance(18200, 400)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(800)

    #C0012
    ChrTalk(
        0x8,
        (
            "#11P#07209F不是有你在我身边嘛⊥\x02\x03",

            "#07212F只要能靠在你的臂弯，\x01",
            "被你用心保护，就已经足够啦！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    OP_63(0x8, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)
    OP_93(0x9, 0xB4, 0x1F4)

    #C0013
    ChrTalk(
        0x9,
        "#11P#07303F好了，我也得早点睡了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(100)

    #C0014
    ChrTalk(
        0x8,
        (
            "#11P#07206F抱歉，我好像太得意忘形了。\x02\x03",

            "#07200F不管怎么说，我想趁着明天，\x01",
            "和公主殿下好好谈谈。\x02\x03",

            "那方面的事情安排好了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    #C0015
    ChrTalk(
        0x9,
        (
            "#6P#07304F没问题，我已经和准校取得了联系。\x02\x03",

            "#07302F明天的午餐会结束之后，\x01",
            "会在傍晚时分安排你们见面。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#11P#07202F是吗……\x01",
            "呵呵，已经有一年没见了呢。\x02\x03",

            "#07206F要是艾丝蒂尔他们还留在克洛斯贝尔，\x01",
            "我们就可以开个同学会了。\x02\x03",

            "#07208F雪拉最近好像也很忙，\x01",
            "没有出差的时间呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        "#6P#07303F……是啊。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#11P#07204F算了，就让我好好\x01",
            "享受一下这个最高级的\x01",
            "旅游胜地吧。\x02\x03",

            "#07212F对了，你不必担心，\x01",
            "我并不打算去打扰你和\x01",
            "准校的幽会哦⊥\x02\x03",

            "#07209F不然的话，你们干脆就去那个\x01",
            "传闻中的主题公园约会吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        (
            "#6P#07306F不用你多管闲事，白痴。\x02\x03",

            "#07303F话说回来，你今天的胡言乱语\x01",
            "好像比平时更加严重啊。\x02\x03",

            "#07301F……该不会是在\x01",
            "打什么坏主意吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#11P#07211F（惊）……\x02\x03",

            "#07209F哈哈哈，真讨厌，\x01",
            "怎么可能会有那种事嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "#6P#07308F（……明天干脆在他的\x01",
            "  脖子上套根绳子吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0022
    AnonymousTalk(
        0x8,
        (
            "说起来……这恐怕会是我\x01",
            "最后一次外出游玩了吧。\x02\x03",

            "之后不仅要调查宰相阁下的目的，\x01",
            "同时还要观察整个大陆的动向……\x02\x03",

            "免不了要像以往一样让你受累，\x01",
            "一切都拜托了哦，我的好友。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0023
    ChrTalk(
        0x9,
        "#6P#07304F哼，这还用说。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18700, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("e430B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_E9 end

    SaveToFile()

Try(main)
