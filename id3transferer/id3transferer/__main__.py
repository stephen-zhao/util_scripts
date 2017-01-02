import argparse
from Transferer import InfoTransferer
from getInfoStrategies import *
from setInfoStrategies import *

DEF_GET_STRAT = "f"
DEF_SET_STRAT = "at"

argsParser = argparse.ArgumentParser(
    description="Transfers info between filename and id3 tags")

argsParser.add_argument(
    "file", dest="file",
    help="the sound file to edit")
argsParser.add_argument(
    "-i", "--in", dest="get_strat",
    choices=GetInfoStrategy.getStratListAbbr(),
    help="the strategy used to get info for the transfer")
argsParser.add_argument(
    "-o", "--out", dest="set_strat",
    choices=SetInfoStrategy.getStratListAbbr(),
    help="the strategy used to for where the info gets transfered to")

args = argsParser.parse_args()

if args.get_strat:
    get_strat = GetInfoStrategy.createStrategy(args.get_strat)
else:
    get_strat = GetInfoStrategy.createStrategy(DEF_GET_STRAT)

if args.set_strat:
    set_strat = SetInfoStrategy.createStrategy(args.set_strat)
else:
    set_strat = SetInfoStrategy.createStrategy(DEF_SET_STRAT)

T = InfoTransferer(get_strat, set_strat)

InfoTransferer.transfer(args.file)
