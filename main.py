# Import of tk
import tkinter as tk
import tkinter

window = tkinter.Tk()
window.geometry("800x600")
window.title("Basic Incremental")
window.update()

# Logo
window.iconphoto(False, (tk.PhotoImage(file="LogoProgramu.png")))
# Definition of Ores
money = 0
upgraded = 1
upgradecost = 15 * upgraded * (1.5 * upgraded)
upgradecolor = "red"
level = 1
xp = 0
xprequire = 100
xpupgrade = 1
xpmoneyrequire = xpupgrade * 20 * (1.2 * xpupgrade)
upgradexpcolor = "red"
boulders = 0


# Definition of Events
# Mine
def mined():
    global money
    global upgradecost
    global upgradecolor
    global xp
    global level
    global xprequire
    global xpupgrade
    global xpmoneyrequire
    global upgradexpcolor
    money = money + (1 * (upgraded * upgraded))
    xp = xp + (1 * xpupgrade)
    if upgradecost <= money:
        upgradecolor = "green"
    else:
        upgradecolor = "red"
    if xprequire <= xp:
        level = level + 1
        xprequire = xprequire * 2
    if xpmoneyrequire <= money:
        upgradexpcolor = "green"
    else:
        upgradexpcolor = "red"
    MoneyCounter.config(text="Money" + ":" + str(money))
    UpgradeCounter.config(text="Upgraded" + ":" + str(upgraded))
    UpgradecostCounter.config(text="Upgrade Cost " + ":" + str(upgradecost))
    LevelCounter.config(text="Level" + ":" + str(level))
    LevelprogressCounter.config(text="Level Progress:" + str(xp) + "/" + str(xprequire))
    upgrademoney.config(
        text="Upgrade Money Gain",
        width=20,
        height=5,
        bg=upgradecolor,
        fg="black",
        command=upgradegainmoney
    )
    UpgradeXpCounter.config(text="XP Level Upgrade" + ":" + str(xpupgrade))
    round(xpmoneyrequire, 1)
    UpgradeXpCostCounter.config(text="XP Upgrade Cost" + ":" + str(xpmoneyrequire))
    UpgradeButton.config(
        text="Upgrade XP Gain",
        width=20,
        height=5,
        bg=upgradexpcolor,
        fg="black",
        command=upgradexpgain)


# MONEY UPGRADE
def upgradegainmoney():
    global money
    global upgradecost
    global upgraded
    global upgradecolor
    global upgradexpcolor
    upgradecost = 15 * upgraded * (1.5 * upgraded)
    if upgradecost <= money:
        money = money - upgradecost
        upgraded = upgraded + 1
        upgradecost = 15 * upgraded * (1.5 * upgraded)
    if upgradecost <= money:
        upgradecolor = "green"
    else:
        upgradecolor = "red"
    if xpmoneyrequire <= money:
        upgradexpcolor = "green"
    else:
        upgradexpcolor = "red"
    MoneyCounter.config(text="Money" + ":" + str(money))
    UpgradeCounter.config(text="Upgraded" + ":" + str(upgraded))
    UpgradecostCounter.config(text="Upgrade Cost " + ":" + str(upgradecost))
    upgrademoney.config(
        text="Upgrade Money Gain",
        width=20,
        height=5,
        bg=upgradecolor,
        fg="black",
        command=upgradegainmoney
    )
    UpgradeButton.config(
        text="Upgrade XP Gain",
        width=20,
        height=5,
        bg=upgradexpcolor,
        fg="black",
        command=upgradexpgain
    )


# xp money
def upgradexpgain():
    global money
    global xp
    global xpupgrade
    global xpmoneyrequire
    global upgradecolor
    global upgradexpcolor
    xpmoneyrequire = xpupgrade * 20 * (1.5 * xpupgrade)
    round(xpmoneyrequire, 1)
    if xpmoneyrequire <= money:
        money = money - xpmoneyrequire
        xpupgrade = xpupgrade + 1
        xpmoneyrequire = xpupgrade * 20 * (1.5 * xpupgrade)
        round(xpmoneyrequire, 1)
    if xpmoneyrequire <= money:
        upgradexpcolor = "green"
    else:
        upgradexpcolor = "red"
    if upgradecost <= money:
        upgradecolor = "green"
    else:
        upgradecolor = "red"
    MoneyCounter.config(text="Money" + ":" + str(money))
    UpgradeXpCounter.config(text="XP Level Upgrade" + ":" + str(xpupgrade))
    round(xpmoneyrequire, 1)
    UpgradeXpCostCounter.config(text="XP Upgrade Cost" + ":" + str(xpmoneyrequire))
    UpgradeButton.config(
        text="Upgrade XP Gain",
        width=20,
        height=5,
        bg=upgradexpcolor,
        fg="black",
        command=upgradexpgain
    )
    upgrademoney.config(
        text="Upgrade Money Gain",
        width=20,
        height=5,
        bg=upgradecolor,
        fg="black",
        command=upgradegainmoney
    )


# Reset layer 1 - Collapse


def collapse():
    global money
    global level
    global xprequire
    global xpupgrade
    global upgraded
    global upgradecolor
    global upgradexpcolor
    global xpmoneyrequire
    global upgradecost
    global xp
    global boulders
    if 30 <= level:
        money = 0
        upgraded = 1
        xpupgrade = 1
        xp = 0
        boulders = boulders + (level - 29) * 2.5
        xprequire = 100
        upgradecost = 22.5
        xpmoneyrequire = 30.0
        level = 1
    if xpmoneyrequire <= money:
        upgradexpcolor = "green"
    else:
        upgradexpcolor = "red"
    if upgradecost <= money:
        upgradecolor = "green"
    else:
        upgradecolor = "red"
    UpgradeCounter.config(text="Upgraded" + ":" + str(upgraded))
    UpgradecostCounter.config(text="Upgrade Cost " + ":" + str(upgradecost))
    LevelCounter.config(text="Level" + ":" + str(level))
    LevelprogressCounter.config(text="Level Progress:" + str(xp) + "/" + str(xprequire))
    MoneyCounter.config(text="Money" + ":" + str(money))
    UpgradeXpCounter.config(text="XP Level Upgrade" + ":" + str(xpupgrade))
    round(xpmoneyrequire, 1)
    UpgradeXpCostCounter.config(text="XP Upgrade Cost" + ":" + str(xpmoneyrequire))
    UpgradeButton.config(
        text="Upgrade XP Gain",
        width=20,
        height=5,
        bg=upgradexpcolor,
        fg="black",
        command=upgradexpgain
    )
    upgrademoney.config(
        text="Upgrade Money Gain",
        width=20,
        height=5,
        bg=upgradecolor,
        fg="black",
        command=upgradegainmoney
    )
    boulderamount.config(text="Boulders :" + " " + str(boulders))


while True:
    # variables used in realtime
    upgradecost = 15 * upgraded * (1.5 * upgraded)
    xpmoneyrequire = xpupgrade * 20 * (1.5 * xpupgrade)
    round(xpmoneyrequire, 1)
    if upgradecost <= money:
        upgradecolor = "green"
    else:
        upgradecolor = "red"
    # definition of buttons and labels
    MoneyCounter = tk.Label(text="Money" + ":" + str(money))
    LevelCounter = tk.Label(text="Level" + ":" + str(level))
    LevelprogressCounter = tk.Label(text="Level Progress:" + str(xp) + "/" + str(xprequire))
    UpgradeCounter = tk.Label(text="Upgraded" + ":" + str(upgraded))
    UpgradecostCounter = tk.Label(text="Upgrade Cost " + ":" + str(upgradecost))
    button = tk.Button(
        text="Mine",
        width=50,
        height=10,
        bg="gray",
        fg="white",
        command=mined
    )
    upgrademoney = tk.Button(
        text="Upgrade Money Gain",
        width=20,
        height=5,
        bg=upgradecolor,
        fg="black",
        command=upgradegainmoney
    )
    UpgradeXpCounter = tk.Label(text="XP Level Upgrade" + ":" + str(xpupgrade))
    round(xpmoneyrequire, 1)
    UpgradeXpCostCounter = tk.Label(text="XP Upgrade Cost" + ":" + str(xpmoneyrequire))
    UpgradeButton = tk.Button(
        text="Upgrade XP Gain",
        width=20,
        height=5,
        bg=upgradexpcolor,
        fg="black",
        command=upgradexpgain
    )
    CollapseButton = tk.Button(
        text="Collapse",
        width=20,
        height=5,
        bg="orange",
        fg="black",
        command=collapse
    )
    LevelRequirementCollapse = tk.Label(text="Requires Level 30")
    boulderamount = tk.Label(text="Boulders :" + " " + str(boulders))
    splitbasic = tk.Label(text="------------------------------------------------------Basic------------------------------------------------------")
    splitcollapse = tk.Label(text="------------------------------------------------------Collapse------------------------------------------------------")
    window.iconphoto(False, (tk.PhotoImage(file="LogoProgramu.png")))

    # displaying buttons and text
    MoneyCounter.pack()
    LevelCounter.pack()
    LevelprogressCounter.pack()
    boulderamount.pack()
    splitbasic.pack()
    button.place(x=10, y=110)
    upgrademoney.place(x=400, y=110)
    UpgradeCounter.place(x=440, y=200)
    UpgradecostCounter.place(x=420, y=220)
    UpgradeButton.place(x=600, y=110)
    UpgradeXpCounter.place(x=625, y=200)
    UpgradeXpCostCounter.place(x=620, y=220)
    CollapseButton.place(x=10, y=300)
    LevelRequirementCollapse.place(x=35, y=390)
    splitcollapse.place(x=100, y=275)
    window.mainloop()
