#!/usr/bin/perl
#The file /usr/src/linux/drivers/sbus/char/sunkeymap.map contains
#the default type 4/5 mappings
#This converter can be found at ftp://ftp.dementia.org/pub/linux/pc2sun.pl
print "! Translated from PC keytable to Sun Type 4/5 by pc2sun,\n";
print "!\n";
print "! Copyright 1996 Derrick J Brashear.\n";
print "!\n";
print "! Permission to use, copy, modify, and distribute this software\n";
print "! and its documentation for any purpose and without fee is\n";
print "! hereby granted, provided that the above copyright notice\n";
print "! and this permission notice appear in all copies and that\n";
print "! the above copyright notice appear in any keytables so\n";
print "! translated by this software, and that the author's name\n";
print "! not be used in advertising or publicity pertaining to\n";
print "! distribution of the software without specific, written prior\n";
print "! permission.\n";
print "! The author makes no representations about the suitability of\n";
print "! this software for any purpose.  It is provided \"as is\" without\n";
print "! express or implied warranty.\n";
while (<>) {
s/ 0 / _FIX0_ /;
s/ 1 / _29_ /;
s/ 2 / _30_ /;
s/ 3 / _31_ /;
s/ 4 / _32_ /;
s/ 5 / _33_ /;
s/ 6 / _34_ /;
s/ 7 / _35_ /;
s/ 8 / _36_ /;
s/ 9 / _37_ /;
s/ 10 / _38_ /;
s/ 11 / _39_ /;
s/ 12 / _40_ /;
s/ 13 / _41_ /;
s/ 14 / _43_ /;
s/ 15 / _53_ /;
s/ 16 / _54_ /;
s/ 17 / _55_ /;
s/ 18 / _56_ /;
s/ 19 / _57_ /;
s/ 20 / _58_ /;
s/ 21 / _59_ /;
s/ 22 / _60_ /;
s/ 23 / _61_ /;
s/ 24 / _62_ /;
s/ 25 / _63_ /;
s/ 26 / _64_ /;
s/ 27 / _65_ /;
s/ 28 / _89_ /;
s/ 29 / _76_ /;
s/ 30 / _77_ /;
s/ 31 / _78_ /;
s/ 32 / _79_ /;
s/ 33 / _80_ /;
s/ 34 / _81_ /;
s/ 35 / _82_ /;
s/ 36 / _83_ /;
s/ 37 / _84_ /;
s/ 38 / _85_ /;
s/ 39 / _86_ /;
s/ 40 / _87_ /;
s/ 41 / _42_ /;
s/ 42 / _99_ /;
s/ 43 / _88_ /;
s/ 44 / _100_ /;
s/ 45 / _101_ /;
s/ 46 / _102_ /;
s/ 47 / _103_ /;
s/ 48 / _104_ /;
s/ 49 / _105_ /;
s/ 50 / _106_ /;
s/ 51 / _107_ /;
s/ 52 / _108_ /;
s/ 53 / _109_ /;
s/ 54 / _110_ /;
s/ 55 / _47_ /;
s/ 56 / _19_ /;
s/ 57 / _121_ /;
s/ 58 / _119_ /;
s/ 59 / _5_ /;
s/ 60 / _6_ /;
s/ 61 / _8_ /;
s/ 62 / _10_ /;
s/ 63 / _12_ /;
s/ 64 / _14_ /;
s/ 65 / _16_ /;
s/ 66 / _17_ /;
s/ 67 / _18_ /;
s/ 68 / _7_ /;
s/ 69 / _98_ /;
s/ 70 / _23_ /;
s/ 71 / _68_ /;
s/ 72 / _69_ /;
s/ 73 / _70_ /;
s/ 74 / _71_ /;
s/ 75 / _91_ /;
s/ 76 / _92_ /;
s/ 77 / _93_ /;
s/ 78 / _125_ /;
s/ 79 / _112_ /;
s/ 80 / _113_ /;
s/ 81 / _114_ /;
s/ 82 / _94_ /;
s/ 83 / _50_ /;
# 84 is Last_Console on PCs
s/ 84 / _FIX84_ /;
# unused on PCs
s/ 85 / _FIX85_ /;
# 86 is less/greater on PCs
s/ 86 / _FIX86_ /;
s/ 87 / _9_ /;
s/ 88 / _11_ /;
# unused on PCs
s/ 89 / _FIX89_ /;
# unused on PCs
s/ 90 / _FIX90_ /;
# unused on PCs
s/ 91 / _FIX91_ /;
# unused on PCs
s/ 92 / _FIX92_ /;
# unused on PCs
s/ 93 / _FIX93_ /;
# unused on PCs
s/ 94 / _FIX94_ /;
# unused on PCs
s/ 95 / _FIX95_ /;
s/ 96 / _90_ /;
# 97 is the second Control on PCs
s/ 97 / _FIX97_ /;
s/ 98 / _46_ /;
# 99 is control-Backslash on PCs
s/ 99 / _FIX99_ /;
s/ 100 / _13_ /;
# 101 is break on PCs
s/ 101 / _FIX101_ /;
s/ 102 / _52_ /;
s/ 103 / _20_ /;
s/ 104 / _96_ /;
s/ 105 / _24_ /;
s/ 106 / _28_ /;
s/ 107 / _74_ /;
s/ 108 / _27_ /;
s/ 109 / _123_ /;
s/ 110 / _44_ /;
# 111 is remove on PCs
s/ 111 / _FIX111_ /;
# 112 is Macro on PCs
s/ 112 / _FIX112_ /;
# 113 is F13 on PCs
s/ 113 / _FIX113_ /;
# 114 is F14 on PCs
s/ 114 / _FIX114_ /;
s/ 115 / _118_ /;
# 116 is do on PCs
s/ 116 / _FIX116_ /;
# 117 is F17 on PCs
s/ 117 / _FIX117_ /;
# 118 is keypad minus/plus on PCs
s/ 118 / _FIX118_ /;
s/ 119 / _21_ /;
# unused on PCs
s/ 120 / _FIX120_ /;
# unused on PCs
s/ 121 / _FIX121_ /;
# unused on PCs
s/ 122 / _FIX122_ /;
# unused on PCs
s/ 123 / _FIX123_ /;
# unused on PCs
s/ 124 / _FIX124_ /;
# unused on PCs
s/ 125 / _FIX125_ /;
# unused on PCs
s/ 126 / _FIX126_ /;
# unused on PCs
s/ 127 / _FIX127_ /;
s/_1_/1/;
s/_2_/2/;
s/_3_/3/;
s/_4_/4/;
s/_5_/5/;
s/_6_/6/;
s/_7_/7/;
s/_8_/8/;
s/_9_/9/;
s/_10_/10/;
s/_11_/11/;
s/_12_/12/;
s/_13_/13/;
s/_14_/14/;
s/_15_/15/;
s/_16_/16/;
s/_17_/17/;
s/_18_/18/;
s/_19_/19/;
s/_20_/20/;
s/_21_/21/;
s/_22_/22/;
s/_23_/23/;
s/_24_/24/;
s/_25_/25/;
s/_26_/26/;
s/_27_/27/;
s/_28_/28/;
s/_29_/29/;
s/_30_/30/;
s/_31_/31/;
s/_32_/32/;
s/_33_/33/;
s/_34_/34/;
s/_35_/35/;
s/_36_/36/;
s/_37_/37/;
s/_38_/38/;
s/_39_/39/;
s/_40_/40/;
s/_41_/41/;
s/_42_/42/;
s/_43_/43/;
s/_44_/44/;
s/_45_/45/;
s/_46_/46/;
s/_47_/47/;
s/_48_/48/;
s/_49_/49/;
s/_50_/50/;
s/_51_/51/;
s/_52_/52/;
s/_53_/53/;
s/_54_/54/;
s/_55_/55/;
s/_56_/56/;
s/_57_/57/;
s/_58_/58/;
s/_59_/59/;
s/_60_/60/;
s/_61_/61/;
s/_62_/62/;
s/_63_/63/;
s/_64_/64/;
s/_65_/65/;
s/_66_/66/;
s/_67_/67/;
s/_68_/68/;
s/_69_/69/;
s/_70_/70/;
s/_71_/71/;
s/_72_/72/;
s/_73_/73/;
s/_74_/74/;
s/_75_/75/;
s/_76_/76/;
s/_77_/77/;
s/_78_/78/;
s/_79_/79/;
s/_80_/80/;
s/_81_/81/;
s/_82_/82/;
s/_83_/83/;
s/_84_/84/;
s/_85_/85/;
s/_86_/86/;
s/_87_/87/;
s/_88_/88/;
s/_89_/89/;
s/_90_/90/;
s/_91_/91/;
s/_92_/92/;
s/_93_/93/;
s/_94_/94/;
s/_95_/95/;
s/_96_/96/;
s/_97_/97/;
s/_98_/98/;
s/_99_/99/;
s/_100_/100/;
s/_101_/101/;
s/_102_/102/;
s/_103_/103/;
s/_104_/104/;
s/_105_/105/;
s/_106_/106/;
s/_107_/107/;
s/_108_/108/;
s/_109_/109/;
s/_110_/110/;
s/_111_/111/;
s/_112_/112/;
s/_113_/113/;
s/_114_/114/;
s/_115_/115/;
s/_116_/116/;
s/_117_/117/;
s/_118_/118/;
s/_119_/119/;
s/_120_/120/;
s/_121_/121/;
s/_122_/122/;
s/_123_/123/;
s/_124_/124/;
s/_125_/125/;
s/_126_/126/;
s/_127_/127/;
  if (! m/ _FIX[0-9]+_ /) {
    print;
    if ( m/^keymaps / ) {
	print "keycode  45 = equal\n";
	print "keycode  66 = Delete           Delete\n";
        print "\tcontrol keycode  66 = BackSpace\n";
	print "keycode  67 = Compose\n";
        print "\talt     keycode  67 = Meta_Delete\n";
	print "keycode 111 = Linefeed\n";
    }
  }
}
