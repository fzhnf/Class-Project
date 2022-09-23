input_text = input(">Masukkan singkatan emoji = ")
singkatan = input_text.split(" ")
singkatan_dict = {
    "TL"    : "😄",
    "TSGG"  : "🤣",
    "YKWIM" : "😏",
    "KGT"   : "😱",
    "HOAN"  : "🥱",
    "OKS"   : "👍",
    "MTB"   : "👏",
    "OTK"   : "🧠",
    "GBLK"  : "🙅",
    "IMS"   : "🦸",
    "SLMT"  : "🥳",
    "SMS"   : "🥺",
}

output = " "
for emoji in singkatan:
    try:
        output += singkatan_dict.get(emoji)
        print(output)
    except TypeError:
        print("Input singkatan salah, Silahkan Masukkan lagi")
